import connect_db
import pymysql

print(connect_db.myConnection)

class LOGIN:
    def __init__(self, table):
        self.cursorObject = connect_db.myConnection.cursor()
        self.table = table

    def login_verfication(self, clause):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT * FROM ' + self.table + ' ' + clause)  # DB query
                row = cur.fetchall()  # get name and password data
                if row:
                    return "success"
                else:
                    return "failed"

        except Exception as e:
            print("Exeception occured:{}".format(e))

    def extract_member_id(self, clause):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT * FROM ' + self.table + ' ' + clause)  # DB query
                row = cur.fetchall()  # get name and password data
                for i in row:
                    return i
        except Exception as e:
            print("Exeception occured:{}".format(e))

    # utility functions
    def set_Table(self, table):
        self.table = table

    def recon(self):
        self.cursorObject = connect_db.myConnection.cursor()

    def closeConn(self):
        self.cursorObject.close()