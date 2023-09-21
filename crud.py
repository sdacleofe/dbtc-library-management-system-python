import connect_db
import pymysql

print(connect_db.myConnection)

class CRUD:
    def __init__(self, table):
        self.cursorObject = connect_db.myConnection.cursor()
        self.table = table

    def createRows(self, data):
        self.recon()
        try:
            with self.cursorObject as cur:
                # data format : (Book_ID, Title, Author, Available)
                cur.executemany('INSERT INTO ' + self.table + ' VALUES(%s, %s, %s, %s)', data)
                cur.close()
                for data in data:
                    print('new book data inserted : {}'.format(data[1]))
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def createRow(self, data):
        self.recon()
        try:
            with self.cursorObject as cur:
                # data format : (Book_ID, Title, Author, Available)
                cur.executemany('INSERT INTO ' + self.table + ' VALUES(%s, %s, %s, %s)',
                            (int(data[0]), data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
                cur.close()
                print('new book data inserted : {}'.format(data[1]))
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def readData(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT * FROM ' + self.table)  # DB query
                rows = cur.fetchall()  # get all data
                return rows
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def readSingleData(self, clause):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT * FROM ' + self.table + ' ' + clause)  # DB query
                rows = cur.fetchall()  # get all data
                for row in rows:
                    return row
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def updateData(self, data, id):
        self.recon()
        try:
            # data format : (Book_ID, Title, Author, Price, Available, Status, Issue, Due_Date, Return_Date)
            updatequery = "UPDATE " + self.table + " SET Title='" + data[
                    1] + "', Author='" + data[2] + "', Price='" + data[3] + "', Available='" + data[4] +  "', Status='" + data[5] + "', Issue='" + data[6] + "', Due_Date='" + data[7] + "', Return_Date='" + data[8] + "' WHERE Book_ID = " + id
            self.cursorObject.execute(updatequery)
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def deleteData(self, data):
        self.recon()
        try:
            deletequery = "delete from " + self.table + " where Book_ID = " + data
            self.cursorObject.execute(deletequery)
        except Exception as e:
            print("Exeception occured:{}".format(e))

    # utility functions
    def set_Table(self, table):
        self.table = table

    def recon(self):
        self.cursorObject = connect_db.myConnection.cursor()

    def closeConn(self):
        self.cursorObject.close()