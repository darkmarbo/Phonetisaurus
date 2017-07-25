#!/bin/sh


in_file=$1

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib:/usr/local/lib/fst

dos2unix ${in_file}
sed -i 's/   / /g;s/  / /g'  ${in_file}

phonetisaurus-align --input=$in_file --ofile=${in_file}.pts

python /home/yanfa/shaozhiming/tools/dict_check/dict_check.py ${in_file}.pts ${in_file} > ${in_file}.pts.err 


