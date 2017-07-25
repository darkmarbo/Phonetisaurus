

按照README 中的步骤安装 open-fst 



wget http://www.openfst.org/twiki/pub/FST/FstDownload/openfst-1.6.2.tar.gz
    tar -xvzf openfst-1.6.2.tar.gz
    cd openfst-1.6.1
    sudo ./configure --enable-static --enable-shared --enable-far --enable-ngram-fsts
    sudo make -j 12
    sudo make install
 
    echo 'export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib:/usr/local/lib/fst' >> ~/.bashrc
    source ~/.bashrc

git clone https://github.com/AdolfVonKleist/Phonetisaurus.git
    cd Phonetisaurus/src
    ./configure
    sudo make -j 12 
    sudo make install


运行  phonetisaurus-align   时: 
	version `GLIBCXX_3.4.18' not found
	http://blog.csdn.net/rznice/article/details/51090966


安装 open-fst 需要:
autoconf-2.69.tar.gz

automake-1.14.tar.gz

gcc-4.8.2.tar.bz2
	http://www.linuxidc.com/Linux/2015-01/112595.htm
	http://blog.csdn.net/zr1076311296/article/details/51334538


