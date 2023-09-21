import connect_db
from datetime import datetime, timedelta, date
from lib_sys import borrowed_by, books
import pymysql

print(connect_db.myConnection)

borrowed_by_data = borrowed_by("None", "None", "None")
book_data = books("None", "None", "None", "None")

class USEROP:
    def __init__(self, table):
        self.cursorObject = connect_db.myConnection.cursor()
        self.table = table

    def readData(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT * FROM ' + self.table)
                rows = cur.fetchall()
                return rows
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def readSingleData(self, clause, type):
        self.recon()
        if type == 'borrow':
            try:
                with self.cursorObject as cur:
                    cur.execute('SELECT * FROM ' + self.table + ' ' + clause)
                    rows = cur.fetchall()
                    for row in rows:
                        return row
            except Exception as e:
                print("Exeception occured:{}".format(e))

        elif type == 'return':
            try:
                with self.cursorObject as cur:
                    cur.execute('SELECT Books.Book_ID, Books.Title, Books.Author, Books.Available FROM ' + self.table + ' LEFT JOIN Books ON Books.Book_ID = Inventory.Inv_Book_ID_FK'+ clause)
                    rows = cur.fetchall()
                    for row in rows:
                        return row
            except Exception as e:
                print("Exeception occured:{}".format(e))

        elif type == 'search':
            try:
                with self.cursorObject as cur:
                    cur.execute('SELECT * FROM ' + self.table + ' ' + clause)
                    rows = cur.fetchall()
                    for row in rows:
                        return row
            except Exception as e:
                print("Exeception occured:{}".format(e))

    def readInventoryData(self):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT Inventory.Inventory_ID, Inventory.Title, Inventory.Author, Borrowed_By.Issue, Borrowed_By.Due_Date, Borrowed_By.Return_Date FROM ' + self.table + ' LEFT JOIN Borrowed_By ON Inventory.Inv_Book_ID_FK = Borrowed_By.Book_ID_FK')
                rows = cur.fetchall()
                return rows
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def readSingleInventoryData(self, clause):
        self.recon()
        try:
            with self.cursorObject as cur:
                cur.execute('SELECT Inventory.Inventory_ID, Inventory.Title, Inventory.Author, Borrowed_By.Issue, Borrowed_By.Due_Date, Borrowed_By.Return_Date FROM ' + self.table + ' LEFT JOIN Borrowed_By ON Inventory.Inv_Book_ID_FK = Borrowed_By.Book_ID_FK')
                rows = cur.fetchall()
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def updateAvailability(self, status, title):
        self.recon()
        try:
            updatequery = ("UPDATE " + self.table + " SET Available = '" + status + "' WHERE Title = '" + title + "'")
            self.cursorObject.execute(updatequery)
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def insertBorrowedBook(self, data):
        self.recon()
        try:
            with self.cursorObject as cur:
                book_data.set_book_id(data[0])
                book_data.set_title(data[1])
                book_data.set_author(data[2])
                cur.execute('INSERT INTO ' + self.table + '(Inv_Book_ID_FK, Title, Author) VALUES (%s, %s, %s)', data)
                cur.close()
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def deleteInventorySingleData(self, data, type):
        self.recon()
        if type == 'borrowed_by':
            try:
                deletequery = "DELETE FROM " + self.table + " WHERE Book_ID_FK = '" + data + "'"
                self.cursorObject.execute(deletequery)
            except Exception as e:
                print("Exeception occured:{}".format(e))

        if type == 'inventory':
            try:
                deletequery = "DELETE FROM " + self.table + " WHERE Title = '" + data + "'"
                self.cursorObject.execute(deletequery)
            except Exception as e:
                print("Exeception occured:{}".format(e))

    def setBorrowDate(self, book_id):
        self.recon()
        try:
            with self.cursorObject as cur:
                issuedate = datetime.today().strftime('%Y-%m-%d')
                duedate = date.today() + timedelta(days=7)

                borrowed_by_data.set_issue(issuedate)
                borrowed_by_data.set_duedate(duedate)
                cur.execute('INSERT INTO ' + self.table + '(Book_ID_FK, Issue, Due_Date, Return_Date) VALUES (%s, "' +issuedate+ '", "' +str(duedate)+ '", "0000-00-00")', book_id)
                cur.close()
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def deleteSingleBorrowedData(self, book_id):
        self.recon()
        try:
            deletequery = "DELETE FROM " + self.table + " WHERE Book_ID_FK = '" + book_id + "'"
            self.cursorObject.execute(deletequery)
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def deleteSingleInventoryData(self, book_id):
        self.recon()
        try:
            deletequery = "DELETE FROM " + self.table + " WHERE Book_ID_FK = '" + book_id + "' AND Return_Date = '0000-00-00'"
            self.cursorObject.execute(deletequery)
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def refreshReturnedSingleData(self, book_id):
        self.recon()
        try:
            with self.cursorObject as cur:
                returned_date = datetime.today().strftime('%Y-%m-%d')
                issue = borrowed_by_data.get_issue()
                duedate = borrowed_by_data.get_duedate()
                cur.execute('INSERT INTO ' + self.table + '(Book_ID_FK, Issue, Due_Date, Return_Date) VALUES (%s, "' +issue+ '", "' +duedate+ '", "' +returned_date+ '")', book_id)
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