"""
Concerned with storing
"""

books =[]


def add_book(name,author):
    books.append({'name' : name, 'author': author, 'read': False})

# This is considered bad practise because you should not modify anything while looping because it can affect other elements
# def delete_name(name):
#      for book in books:
#          if book['name'] == name:
#              books.remove(book)
#
# So create one new list and add all the rest


def delete_book(name):
    # new_book_list=[]
    # for book in books:
    #     if book['name'] !=name:
    #         new_book_list.append(book)
#     not working I don't know why
    global books
    books_new=[ book  for book in books if book['name'] !=name  ]

def read_book(name):
    for book in books:
        if book['name'] == name:
            book['read']= True


def get_all_books():
    return books