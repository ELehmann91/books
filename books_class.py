class Authors:
    '''
    creates an object that stores authors number and returns it as one string
    '''
    def __init__(self, authors):
        self.authors = []
        for author in authors:
        	self.authors.append(author)
        
    def __repr__(self):
        return ' / '.join([a for a in self.authors])
        

class Books:
    '''
    creates an object that stores different properies of books and lets you add autors 
    '''
    def __init__(self,book_name, isbn,no_pages):
        self.book_name = book_name
        self.authors = []
        self.isbn = isbn
        self.no_pages = no_pages

    def add_author(self,author):
        self.authors.append(Authors(author))
            
    def __eq__(self, other):
        return self.no_pages == other.no_pages
    
    def __gt__(self, other):
        return self.no_pages > other.no_pages
    
    def __str__(self):
        output = []
        for element in vars(self).items():
            output.append(element[0]+': '+ str(element[1]))
        str_all_items = '\n'.join(output)
        return str_all_items

