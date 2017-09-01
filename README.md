## pyspeex-wx
 把从微信服务端下载的高清录音文件 \*.speex文件解码为\*.wav文件

### 环境：
1. MAC OS /Linux ubuntu
2. Gcc
3. python 3.6

### Quick Start：
- 安装speex，下载speex源码
  
  http://downloads.us.xiph.org/releases/speex/speex-1.2.0.tar.gz
    
  解压speex-1.2.0.tar.gz

    cd speex-1.2.0

    ./configure 

   sudo make && make install 


- 编译动态库
    
     cd declib
 
    - linux系统:  
     
     make -f makefile-linux  
    
    - mac系统:
      
    make -f makefile-mac    

- 测试
    
    .decode("pathto/a.speex", "pathto/a-test.wav");
    
 ## 问题
   > 1、mac环境编译 fatal error: malloc.h: No such file or directory
   修改为malloc/malloc.h
    
    
    
        


## 参考
[guoguo11/JSpeex-util](https://github.com/guoguo11/JSpeex-util)

## 说明
>本项目的目的为学习测试用，若有侵权行为，请联系作者

