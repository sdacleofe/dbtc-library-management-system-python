import pymysql

hostname = 'localhost' #this can be server IP or just localhost if you are refering to yourown server
username = 'root'
password = ''
database = 'lib_db'

myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database, autocommit=True )
#print(myConnection) #erase this after
#myConnection.close() #erase this after