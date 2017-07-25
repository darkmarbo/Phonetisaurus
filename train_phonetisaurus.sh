#!/bin/bash

path=$(dirname -- $(readlink -f -- "$0"))
cd $path/$1

model_dir=$path/$1/model/phonetisaurus
tmp_dir=$path/$1/model/phonetisaurus/tmp

mkdir -p $model_dir
rm -rf $tmp_dir
mkdir -p $tmp_dir

# 0. preparation
perl $path/../util/format_4train.pl -i $path/$1/lexicon/core/train.lex -o $model_dir/train.bsf
perl $path/../util/format_4train.pl -i $path/$1/lexicon/core/test.lex -o $model_dir/test.bsf

# 1. Dictionary Alignment
phonetisaurus-align --input=$model_dir/train.bsf --ofile=$tmp_dir/train.corpus

## 2. Joint-Sequence N-gram model
#ngramsymbols < $tmp_dir/train.corpus > $tmp_dir/train.syms
#farcompilestrings --symbols=$tmp_dir/train.syms --keep_symbols=1 $tmp_dir/train.corpus > $tmp_dir/train.far
#ngramcount --order=7 $tmp_dir/train.far > $tmp_dir/train.cnts
#ngrammake  --method=kneser_ney $tmp_dir/train.cnts > $tmp_dir/train.mod
#ngramprint --ARPA $tmp_dir/train.mod > $tmp_dir/train.arpa
#
## 3. Converting the model
#phonetisaurus-arpa2fst --input=$tmp_dir/train.arpa --prefix="$model_dir/latest_model"
#
## 4. testing
#python $path/eval_phonetisaurus.py --modelfile $model_dir/latest_model.fst --testfile $model_dir/train.bsf --prefix "$model_dir/train" > $model_dir/train.log
#python $path/eval_phonetisaurus.py --modelfile $model_dir/latest_model.fst --testfile $model_dir/test.bsf --prefix "$model_dir/test" > $model_dir/test.log
#
##rm -rf $tmp_dir
#
#cd $path

echo
echo " --> done"
echo
