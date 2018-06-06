在win下配置好spark运行的必要条件后，想要在jupyter notebook上而不是shell里运行pyspark。只需要在windows环境变量中为pyspark在jupyter notebook中
启动设置两个变量。

1、新建系统变量PYSPARK_DRIVER_PYTHON，值设为jupyter；

2、新建系统变量PYSPARK_DRIVER_PYTHON_OPTS，值设为notebook。

重启电脑，在shell中cd到spark安装目录，运行.\bin\pyspark 将会打开jupyter notebook。
[pyspark详细的安装及配置方法](https://www.cnblogs.com/zhw-080/archive/2016/08/05/5740580.html)
