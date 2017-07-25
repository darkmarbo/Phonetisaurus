
# coding=utf-8

import sys
import os
import string

if len(sys.argv)<3:
	print("usage: %s in_pro in_old !"%(sys.argv[0]));
	sys.exit(0)

in_file=sys.argv[1];
fp_in=open(in_file);
lines=fp_in.readlines()

fp_in_old=open(sys.argv[2]);
lines_old=fp_in_old.readlines()

fp_log = open("dict_check.log",'w');


th_rat=0.01
th_count=20
map_fs={};
map_num={};  # 记录每个发音对应的次数
map_num_rat={};  # 记录每个发音所占比例

for line in lines:
	line = line.replace("\r","");
	while(len(line) > 0 and line[-1] == ' '):
		line = line[:-1]
	if line[-1] == '\n':
		line = line[:-1]
	if line[-1] == '\r':
		line = line[:-1]

	spls=line.split(' ');
	for sp in spls:

		sps = sp.split("}");
		if len(sps)<2 or sps[0] == "" or sps[1] == "":
			continue;
		word = sps[0];
		py = sps[1];

		if py == ".|?" or py == "?|.":
			continue;
		py = py.replace(".|","");
		py = py.replace("?|","");
		py = py.replace("|.","");
		py = py.replace("|?","");

		if map_fs.has_key(word):  ## 有字母
			is_count = map_fs[word].count(py); 
			if is_count == 0:   # 没发音
				map_fs[word].append(py);
				map_num[word].append(1);
			else:   # 有字母  有发音
				idx = map_fs[word].index(py); 
				map_num[word][idx] = map_num[word][idx] + 1;
		else:   #  没有字母
			vec_py_temp = [];
			vec_py_temp.append(py);
			map_fs[word] = vec_py_temp;
			map_num[word] = [1];
			
			

for key in map_num.keys():
	all_num = 0;
	map_num_rat[key] = [];
	for num in map_num[key]:
		all_num = all_num + num;
	for num in map_num[key]:
		rat = float(num)/float(all_num);
		map_num_rat[key].append(rat);
	
	
### 第一遍统计 单个字母的发音情况	
for key in map_fs.keys():
	#if len(map_fs[key]) != len(map_num[key]):
		#print("map_fs.size != map_num.size");
	print("%s\t"%(key)),
	for ii in range(len(map_fs[key])):
		print("%s:%s"%(map_fs[key][ii],map_num[key][ii])),
		
	print("");
	#print("%s\t%s\t%s"%(key, map_fs[key], map_num[key]));
	#print("%s\t%s\t%s\t%s"%(key, map_fs[key], map_num[key], map_num_rat[key]));
	



#####  处理一遍文件
print("###################################################");
line_num=-1;
for line in lines:
	line_num = line_num + 1;
	line = line.replace("\r","");
	while(len(line) > 0 and line[-1] == ' '):
		line = line[:-1]
	if line[-1] == '\n':
		line = line[:-1]
	if line[-1] == '\r':
		line = line[:-1]

	spls=line.split(' ');
	for sp in spls:

		sps = sp.split("}");
		if len(sps)<2 or sps[0] == "" or sps[1] == "":
			continue;
		word = sps[0];
		py = sps[1];

		if py == ".|?" or py == "?|.":
			continue;
		py = py.replace(".|","");
		py = py.replace("?|","");
		py = py.replace("|.","");
		py = py.replace("|?","");

		if map_fs.has_key(word):  ## map 中 有这个字母

			is_count = map_fs[word].count(py); 
			if is_count == 0:   # 没有相应发音
				print("%s not in map_key"%(py));
			else:   # 有字母  有发音
				idx = map_fs[word].index(py); 
				if map_num_rat[word][idx] < th_rat or\
					map_num[word][idx] < th_count:
					print ("%s -> %s\t%s"%(word, py, lines_old[line_num])),
					
		else:   #  没有字母
			print("%s not in map_key"%(word));



fp_in.close();
fp_log.close();

