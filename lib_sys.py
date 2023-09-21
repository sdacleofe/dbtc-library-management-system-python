class books:
    book_id = ''
    title = ''
    author = ''
    available  = ''

    def __init__(self, book_id, title, author, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def get_book_id(self):
        return int(self.book_id)

    def get_title(self):
        return str(self.title)

    def get_author(self):
        return str(self.author)

    def get_available(self):
        return str(self.available)

    def set_book_id(self, book_id):
        self.book_id = book_id

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_available(self, available):
        self.available = available

# object
book_data = books("0", "Reject Marcos-Duterte", "Filipinos", "10")

# data format : (book_id, title, author, price, available, status, issue, due_date, return_date)

print("parameterized constructor")
print("book_id: " + book_data.book_id)
print("title: " + book_data.title)
print("author: " + book_data.author)
print("available: " + book_data.available)

class login:
    id = ''
    name = ''
    password = ''
    member_type = ''

    def __init__(self, name, password, member_type):
        self.name = name
        self.password = password
        self.member_type = member_type

    def get_id(self):
        return str(self.id)

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return str(self.name)

    def set_name(self, name):
        self.name = name

    def get_password(self):
        return str(self.password)

    def set_password(self, password):
        self.password = password

    def get_member_type(self):
        return str(self.member_type)

    def set_member_type(self, member_type):
        self.member_type = member_type

class register:
    name = ''
    password = ''
    member_type = ''

    def __init__(self, name, password, member_type):
        self.name = name
        self.password = password
        self.member_type = member_type

    def get_name(self):
        return str(self.name)

    def set_name(self, name):
        self.name = name

    def get_password(self):
        return str(self.password)

    def set_password(self, password):
        self.password = password

    def get_member_type(self):
        return str(self.member_type)

    def set_member_type(self, member_type):
        self.member_type = member_type

class borrowed_by:
    issue = ''
    duedate = ''
    returndate = ''

    def __init__(self, issue, duedate, returndate):
        self.issue = issue
        self.duedate = duedate
        self.returndate = returndate

    def get_issue(self):
        return str(self.issue)

    def set_issue(self, issue):
        self.issue = issue

    def get_duedate(self):
        return str(self.duedate)

    def set_duedate(self, duedate):
        self.duedate = duedate

    def get_returndate(self):
        return str(self.returndate)

    def set_returndate(self, returndate):
        self.returndate = returndate

