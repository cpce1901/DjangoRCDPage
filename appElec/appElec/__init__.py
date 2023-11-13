import pymysql
from . import mqtt

pymysql.install_as_MySQLdb()
mqtt.client.loop_start()
