# Python连接Hive的方法
1. 在使用Python连接hive之前，需要将hive安装路径下的lib/py中的文件拷贝到python安装路径中的site-packages下，否则引入对应的包会报错，这个是使用hive提供的Python接口来调用hive客户端。
2. 启动hive 的thrift  
确保以下服务开启：`hive --service hiveserver`
默认端口是10000，如果10000端口被占用，可以使用`hive --service hiveserver -p 10008`把端口改成10008，python代码中也要相应的更改。

3. Python中的连接代码
```python
from hive_service import ThriftHive
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def ReadHiveTest(sql):
    try:
        tSocket = TSocket.TSocket('localhost',10008)
        tTransport = TTransport.TBufferedTransport(tSocket)
        protocol = TBinaryProtocol.TBinaryProtocol(tTransport)
        client = ThriftHive.Client(protocol)
        tTransport.open()
        client.execute(sql)
        return client.fetchAll()
    except Thrift.TException, tx:
        print '%s' % (tx.message)
    finally:
        tTransport.close()

if __name__ == '__main__':
    showDatabasesSql = 'show databases'
    showTablesSql = 'show tables'
    selectSql = 'SELECT * FROM 07_jn_mysql_2'
    result = ReadHiveTest(selectSql)
    for r in result:
        print r
```
