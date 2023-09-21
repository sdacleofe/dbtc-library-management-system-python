# Library Management System using Python

## Objectives
Create a system that uses OOP for the structure and Dearpygui for the GUI. The system should be relevant and must use a Database

## Abstract
We plan to create a Library Management System (LMS) that manages and stores books information electronically. The LMS contains several entries of books with the addition of genre, ratings, and other information details about the entry. The purpose is to organize and catalog the books from the system according to its title, year released, author, and much more. 

## Scope and Limitation
### Scope:  Areas covered by the system
The system allows the admin to add entries of any published books in the library as well as its details, display and list all records of books and its information from the system, edit its information, and delete some entries. Aside from the CRUD functionalities, the system also has a search bar which allows the admin to look up for the specific book entry by title or record they are looking for. It also displays the total number of book records created in the system.

### Limitation: Areas where the system meets its limit
The system is strictly for administrator use only.

### Screenshots
Actual GUI (all active GUI should be shown).
![](/lms.gif)


## Analysis
The Library Management System uses a database in order to have a collection of books and its information from the system. 
Using the python programming language, there are several requirements needed to complete this project. 
### Database: Library
- In python, there is a library called pymysql. Importing that library can create a new database using python.
- Connect the python program to the mysql database to use the newly created database in the succeeding and create the following requirements. 
- Create a cursor object is used to make the connection for executing SQL queries.

- After connecting to the database and creating the cursor object, execute a sql query string to create a table within the connected database. The table shall consist of relevant details about books. Execute sql query to insert dataset/s from the table.
- It is appropriate to use error handling and check if the program is successful in making the following SQL queries.
Functions

### Develop CRUD functionalities using the same library, pymysql together with OOP. 
- CREATE -  Create a default function that will call the cursor object and table. Create a class and define a function called createRow to execute a parameter that will allow the system to insert a new book record to the table.
- 
- READ - there are several functions within the Read Functionality. There is the readData which displays all book records, readNextBookID will display the next book_id after the last existing book_id, readSingleData will filter a book record depending on the condition, readCountNumber will display the number of existing rows or records from the table.
  
- UPDATE - In this function, it allows the administrator to edit the details of a book_id that is entered.
  
- DELETE - The function allows the administrator to delete a specific existing record from the table. Then, it will reset the auto increment number after deleting a table row of the record.
  
### Object-Oriented Programming (OOP)
- library.py is created to structure the program and use the objects of a book.
### GUI
- To create a GUI interface in python, it is necessary to have a library that supports GUI. For this application, dearpygui is imported.
- import the previous (CRUD) functionalities created as well as the database in order to utilize them to the GUI interface.
- Using the dearpygui framework, The library can have a GUI interface that can create multiple windows. Each window is separated by functionality. 
	- There is Create functionality in the window “Insert Book” to add new book into the database
	- Update Functionality is in the window “Update Book” will use the book_id to locate the book record the administrator wishes to edit.
	- Read Functionality is shown in the window named “Books”, located below, displays all of the existing book records from the database.
	- Delete Functionality will use the book_id to delete a specific book record.
	- The application also has a Search function that uses book_id to display the specific book record the administrator wishes to find.
	- There is also a Book Information which displays the total number of existing books in the database.

##  Acknowledgments
I want to thank my professor in the course of Application Development & Emerging Technologies for teaching us how to develop applications using procedural and object-oriented programming (OOP) paradigms in Python. Also, I want to express my gratitude to my partner, Mari, in this project for making this documentation possible.

**This project was made on Feb 10, 2023**