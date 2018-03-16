在服务器安装hadoop、spark，并配置好环境变量，在服务器访问pyspark时，需要在~/.bashrc中添加环境变量  
`export SPARK_HOME=/usr/local/xypf/hadoop-2.7`  
`export PATH="/home/pccs/anaconda2/bin:/usr/local/xypf/spark-2.0.2-bin-hadoop2.7/python:$PATH"`  
`export PYTHONPATH=$SPARK_HOME/python/:$SPARK_HOME/python/lib/py4j-0.10.3-src.zip`  

同时需要在本地的pycharm客户端配置环境变量  
`Run->Edit Configurations->Environment variables`中添加两个环境变量  
`SPARK_HOME /usr/local/xypf/hadoop-2.7`  
`PYTHONPATH /usr/local/xypf/hadoop-2.7/PYTHON/:/usr/local/xypf/hadoop-2.7/python/lib/py4j-0.10.3-src.zip`  
[参考博客](https://www.cnblogs.com/felixzh/p/4973952.html)
