
# coding=utf-8

import sys
import os
import string

if len(sys.argv)<2:
	print("usage: %s input_file !"%(sys.argv[0]));
	sys.exit(0)

in_file=sys.argv[1];
fp_in=open(in_file);
lines=fp_in.readlines()

fp_log = open("dict_check.log",'w');


th_rat=0.01
map_fs={};
map_num={};  # 记录每个发音对应的次数
map_num_rat={};  # 记录每个发音所占比例

for line in lines:
	if line[-1] == '\n':
		line = line[:-1]
	if line[-1] == '\r':
		line = line[:-1]
	#print(line);

	spls=line.split('\t');
	word=spls[0]	
	py=spls[1]	
	pys=py.split(' ');

	vec_char = [];
	for c in word:
		vec_char.append(c);

	vec_py = [];
	lef_py = "";
	for py in pys:
		if py == "?":
			lef_py = "";
			#lef_py = "? ";
			continue; 
		if py == ".":
			lef_py = "";
			continue; 

		py=py.replace("\"","");

		py="%s%s"%(lef_py,py);
		vec_py.append(py);
		lef_py = "";
	
	if len(vec_char) != len(vec_py):
		print("%s\n%s\t%s"%(line,vec_char,vec_py))
		continue;

	for ii in range(len(vec_char)):
		if map_fs.has_key(vec_char[ii]):  ## map 中 有这个字母

			is_count = map_fs[vec_char[ii]].count(vec_py[ii]); 
			if is_count == 0:   # 没有相应发音
				map_fs[vec_char[ii]].append(vec_py[ii]);
				map_num[vec_char[ii]].append(1);
			else:   # 有字母  有发音
				idx = map_fs[vec_char[ii]].index(vec_py[ii]); 
				map_num[vec_char[ii]][idx] = map_num[vec_char[ii]][idx] + 1;
		else:   #  没有字母
			vec_py_temp = [];
			vec_py_temp.append(vec_py[ii]);
			map_fs[vec_char[ii]] = vec_py_temp;
			map_num[vec_char[ii]] = [1];
			
			

for key in map_num.keys():
	all_num = 0;
	map_num_rat[key] = [];
	for num in map_num[key]:
		all_num = all_num + num;
	for num in map_num[key]:
		rat = float(num)/float(all_num);
		map_num_rat[key].append(rat);
	
	
## 第一遍统计 单个字母的发音情况	
for key in map_fs.keys():
	if len(map_fs[key]) != len(map_num[key]):
		print("map_fs.size != map_num.size");
	print("%s\t%s\t%s\t%s"%(key,map_fs[key],map_num[key],map_num_rat[key]));
	


####  处理一遍文件
print("###################################################");
for line in lines:
	if line[-1] == '\n':
		line = line[:-1]
	if line[-1] == '\r':
		line = line[:-1]

	spls=line.split('\t');
	word=spls[0]	
	py=spls[1]	
	pys=py.split(' ');

	vec_char = [];  ## 字母序列
	vec_py = [];
	for c in word:
		vec_char.append(c);

	for py in pys:
		if py in ["?","."]:
			continue; 

		py=py.replace("\"","");
		vec_py.append(py);
	
	if len(vec_char) != len(vec_py):
		#print (vec_char)
		#print (vec_py)
		continue;

	for ii in range(len(vec_char)):
		if map_fs.has_key(vec_char[ii]):  ## map 中 有这个字母

			is_count = map_fs[vec_char[ii]].count(vec_py[ii]); 
			if is_count == 0:   # 没有相应发音
				print("%s not in map_key"%(vec_py[ii]));
			else:   # 有字母  有发音
				idx = map_fs[vec_char[ii]].index(vec_py[ii]); 
				if map_num_rat[vec_char[ii]][idx] < th_rat:
					print ("%s -> %s\t%s"%(vec_char[ii],vec_py[ii],line))
					
		else:   #  没有字母
			print("%s not in map_key"%(vec_char[ii]));



fp_in.close();
fp_log.close();

