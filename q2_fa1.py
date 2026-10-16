class Publication:
    title:str
    author:str
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def get_title():
        return title
    def get_author():
        return author
    def set_title(self,title):
        self.title = title
    def set_author(author):
        self.author = author
    def display_info():
        print(f"Title: ",{self.title},"Author: ",{self.author})

class Book(Publication):
    number_of_pages:int
    def __init__(self,title,author,number_pages):
        
    def get_number_of_pages():
        
    def set_number_of_pages(number_pages):


class Magazine(Publication):
    issue_number:int
    def __init__(title,author,issue_number):

    def get_issue_number():

    def set_issue_number(issue_number):


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van DOngen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
book1.display_info()

print("\nBook Information:")
book1.display_info()








print("Publication title: ",publication1.get_title())
print("Publication author: ",publication1.get_author())
