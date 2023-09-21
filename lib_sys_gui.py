import crud, loginop, registerop, userop
import dearpygui.dearpygui as dpg
from lib_sys import books, login, register
from datetime import datetime

book_data = books("None", "None", "None", "None")
login_data = login("None", "None", "None")
register_data = register("None", "None", "None")

# operations
crudObject = crud.CRUD("books")
loginObject = loginop.LOGIN("members")
registerObject = registerop.REGISTRATION("members")
useropObject = userop.USEROP("books")
inventoryObject = userop.USEROP("inventory")
borrowObject = userop.USEROP("borrowed_by")
returnObject = userop.USEROP("borrowed_by")

def loginClicked(sender, app_data):
    login_data.set_name(dpg.get_value("input_name"))
    login_data.set_password(dpg.get_value("input_password"))
    login_data.set_member_type(dpg.get_value("radio_member_type"))

    clause = (' WHERE Member_Name = "' + login_data.get_name() +'" AND Password = "'+ login_data.get_password() +'" AND Member_Type = "'+ login_data.get_member_type() +'"')
    is_connected = loginObject.login_verfication(clause)

    extract_id = loginObject.extract_member_id(clause)
    login_data.set_id(extract_id)

    if is_connected == "success": # membership is verified
        dpg.delete_item("login_portal_window")
        user_interface("all_data", "none")

def logoutClicked(sender, app_data):
    if sender == "user_logout":
        delete_user_table_item()
        show_portal()

def registerClicked(sender, app_data):
    register_data.set_name(dpg.get_value("input_name"))
    register_data.set_password(dpg.get_value("input_password"))
    register_data.set_member_type(dpg.get_value("radio_member_type"))

    registerdata = (register_data.get_name(), register_data.get_password(), register_data.get_member_type())
    registerObject.register(registerdata)

def userReturnClicked(sender, app_data, type):
    try:
        book_data.set_title(dpg.get_value("user_return_book"))
        clause = (' WHERE Inventory.Title = "' + book_data.get_title() + '"')

        bookdata = inventoryObject.readSingleData(clause, 'return')
        if bookdata[3] == 'No':
            useropObject.updateAvailability('Yes', book_data.get_title())
            # inventoryObject.deleteInventorySingleData(book_data.get_title(), 'inventory')

            book_data.set_book_id(bookdata[0])
            returnObject.deleteSingleInventoryData(str(book_data.get_book_id()))
            returnObject.refreshReturnedSingleData(str(book_data.get_book_id()))

            # refresh data and interface
            dpg.delete_item("user_inventory")
            dpg.delete_item("user_books")
            create_inventory_table()
            create_user_table()
            update_user_inventory_table("all_data", clause)
            update_user_books_table("all_data", clause)
    except TypeError as e:
        print('Try again.')

def userBorrowClicked(sender, app_data, type):
    try:
        book_data.set_title(dpg.get_value("user_borrow_book"))
        clause = (' WHERE Title = "' + book_data.get_title() + '"')

        bookdata = useropObject.readSingleData(clause, 'borrow')

        if bookdata[3] == 'Yes':
            useropObject.updateAvailability('No', book_data.get_title())

            book_data.set_book_id(bookdata[0])
            book_data.set_title(bookdata[1])
            book_data.set_author(bookdata[2])
            bookdata = (book_data.get_book_id(), book_data.get_title(), book_data.get_author())

            borrowObject.setBorrowDate(book_data.get_book_id())
            inventoryObject.insertBorrowedBook(bookdata)

            # refresh data and interface
            dpg.delete_item("user_inventory")
            dpg.delete_item("user_books")
            clause = (' WHERE Title = "' + book_data.get_title() + '"')
            create_inventory_table()
            create_user_table()
            update_user_inventory_table("all_data", clause)
            update_user_books_table("all_data", clause)

        elif bookdata[3] == 'Yes':
            print("The book is not available.")
    except TypeError as e:
        print("Try Again.")

def userSearchClicked(sender, app_data):
    try:
        book_data.set_title(dpg.get_value("user_search_book"))
        clause = (' WHERE Title = "' + book_data.get_title() + '"')
        dpg.delete_item("user_books")
        create_user_table()
        update_user_books_table('single_data', clause)
    except TypeError as e:
        print("Try again.")

def userViewAllClicked(sender, app_data):
    try:
        delete_user_table_item()
        user_interface("all_data", "None")
    except TypeError as e:
        print("Try again.")
def update_user_books_table(status, clause):
    if status == "all_data":
        data = useropObject.readData()
        for i in range(len(data)):
            with dpg.table_row(parent="user_books_table"):
                for j in range(0, 4):
                    dpg.add_text(data[i][j])

    if status == "single_data":
        data = useropObject.readSingleData(clause, 'search')
        with dpg.table_row(parent="user_books_table"):
            for j in range(0, 4):
                dpg.add_text(data[j])

def update_user_inventory_table(status, clause):
    if status == "all_data":
        data = inventoryObject.readInventoryData()
        for i in range(len(data)):
            with dpg.table_row(parent="user_inventory_table"):
                for j in range(0, 6):
                    dpg.add_text(data[i][j])


def create_user_table():
    with dpg.window(tag="user_books", label="List of Books", width=985, height=200, pos=(0,0)):
        with dpg.table(tag="user_books_table", header_row=True):
            # data format : (Book_ID, Title, Author, Available, Actions)
            dpg.add_table_column(label="Book ID")
            dpg.add_table_column(label="Title")
            dpg.add_table_column(label="Author")
            dpg.add_table_column(label="Available")

def create_inventory_table():
    with dpg.window(tag="user_inventory", label="User Inventory", width=740, height=200, pos=(0, 338)):
        with dpg.table(tag="user_inventory_table", header_row=True):
            # data format : (Book_ID, Title, Author, Available, Actions)
            dpg.add_table_column(label="Inventory ID")
            dpg.add_table_column(label="Title")
            dpg.add_table_column(label="Author")
            dpg.add_table_column(label="Issued")
            dpg.add_table_column(label="Due Date")
            dpg.add_table_column(label="Returned Date")

def delete_user_table_item():
    dpg.delete_item("user_books")
    dpg.delete_item("user_borrow_feature")
    dpg.delete_item("user_return_feature")
    dpg.delete_item("user_search_feature")
    dpg.delete_item("user_account_feature")
    dpg.delete_item("user_inventory")

def hide_admin_window():
    dpg.delete_item("admin_db_account")
    dpg.delete_item("admin_db_create")
    dpg.delete_item("admin_db_update")
    dpg.delete_item("admin_db_delete")
    dpg.delete_item("admin_db_table")

# GUI INTERFACE

# Default Setup
dpg.create_context()
dpg.create_viewport(title='Library Management', width=1000, height=580)

# LOGIN AND REGISTRATION INTERFACE

# USER INTERFACE
def show_portal():
    with dpg.window(tag="login_portal_window", label="Library Portal", width=220, height=220, pos=(380, 150)):
        dpg.add_text("Name: ")
        dpg.add_input_text(label="", tag="input_name", width=200)
        #
        #
        dpg.add_text("Password: ")
        dpg.add_input_text(label="", tag="input_password", width=200)
        #
        #
        dpg.add_radio_button(label="member_type", tag="radio_member_type", items=['student', 'librarian'],default_value="student", horizontal=True)
        #
        #
        dpg.add_text("", tag="portal_msg")
        dpg.add_button(label="Login", callback=loginClicked, width=200)
        dpg.add_button(label="Register", callback=registerClicked, width=200)

show_portal()

def user_interface(status, data):
    with dpg.window(tag="user_borrow_feature", label="Borrow Feature", width=244, height=130, pos=(0, 205)):
        dpg.add_text("")
        dpg.add_input_text(default_value="", tag="user_borrow_book", width=227)
        #
        #
        dpg.add_button(label="Borrow Book", width=227, callback=userBorrowClicked)
        dpg.add_text("")
        popupError()

    with dpg.window(tag="user_return_feature", label="Return Feature", width=244, height=130, pos=(248, 205)):
        dpg.add_text("")
        dpg.add_input_text(default_value="", tag="user_return_book", width=227)
        #
        #
        dpg.add_button(label="Return Book", width=227, callback=userReturnClicked)
        dpg.add_text("")

    with dpg.window(tag="user_search_feature", label="Search Feature", width=244, height=130, pos=(496, 205)):
        dpg.add_text("")
        dpg.add_input_text(default_value="", tag="user_search_book", width=227)
        #
        #
        dpg.add_button(label="Search Book", width=227, callback=userSearchClicked)
        dpg.add_button(label="View All", width=227, callback=userViewAllClicked)

    with dpg.window(tag="user_account_feature", label="User Account", width=241, height=333, pos=(742, 205)):
        dpg.add_text("Name: " + login_data.get_name())
        dpg.add_text("No. Books Borrowed: ")
        dpg.add_text("Max Books Limit: ")
        dpg.add_button(label="Logout", tag="user_logout", callback=logoutClicked)

    user_books_interface(status, data)
    user_inventory_interface("all_data", "None")

def user_inventory_interface(status, data):
    create_inventory_table()
    update_user_inventory_table(status, data)

def user_books_interface(status, data):
    create_user_table()
    update_user_books_table(status, data)


def popupError():
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal_id"):
        dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal_id", show=False))

# ADMIN INTERFACE

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()