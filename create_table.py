import connect_db  # import the other file *Connection Object

print(connect_db.myConnection)  # check if connect is OK

try:
    # create a cursor
    cursorObject = connect_db.myConnection.cursor()
    # SQL query string
    # ID, Skin, Hair, Chest Items, Pants
    # sqlQuery = "CREATE TABLE Books(Book_ID INTEGER PRIMARY KEY AUTO_INCREMENT, Title varchar (50), Author varchar (50), Available varchar (50))"
    # sqlQuery = "CREATE TABLE Members(Member_ID int PRIMARY KEY AUTO_INCREMENT, Member_Name varchar (50), Password varchar (50), Member_Type varchar(11))"
    sqlQuery = "CREATE TABLE Borrowed_By(Borrowed_By_ID int NOT NULL AUTO_INCREMENT, Book_ID_FK int NOT NULL, Issue DATE, Due_Date DATE, Return_Date DATE, PRIMARY KEY (Borrowed_By_ID), FOREIGN KEY (Book_ID_FK) REFERENCES Books(Book_ID))"
    # sqlQuery = "CREATE TABLE Inventory(Inventory_ID int NOT NULL AUTO_INCREMENT, Inv_Book_ID_FK int NOT NULL, Title varchar (50), Author varchar (50), Available varchar (50), PRIMARY KEY (Inventory_ID), FOREIGN KEY (Inv_Book_ID_FK) REFERENCES Books(Book_ID))"
    # sqlQuery = "CREATE TABLE Returned_By(Returned_By_ID int NOT NULL AUTO_INCREMENT, Borrowed_By_ID_FK int NOT NULL, Returned_Date, PRIMARY KEY (Returned_By_ID), FOREIGN KEY (Borrowed_By_ID_FK) REFERENCES Borrowed_By(Borrowed_By_ID))"


    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    ##Check if we are successful in making the table
    sqlQuery = "DESCRIBE Borrowed_By"
    cursorObject.execute(sqlQuery)
    rows = cursorObject.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    connect_db.myConnection.close()