import connect_db
import pymysql

print(connect_db.myConnection)

class REGISTRATION:
    def __init__(self, table):
        self.cursorObject = connect_db.myConnection.cursor()
        self.table = table

    def register(self, data):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('INSERT INTO ' + self.table + '(Member_Name, Password, Member_Type) VALUES(%s, %s, %s)', data)
                cur.close()
        except Exception as e:
            print("Exeception occured:{}".format(e))

    # utility functions
    def set_Table(self, table):
        self.table = table

    def recon(self):
        self.cursorObject = connect_db.myConnection.cursor()

    def closeConn(self):
        self.cursorObject.close()