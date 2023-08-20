class DBPersistance:
    def getAuthors():
        conn = db.open(connstr)
        row = conn.exec("SELECT * FROM authors")
        authors = []
        for row in rows:
            author = { "id" : row[0], "firstName" : row[1], "lastName" : row[2]}
            author = Author(row[0], row[1], row[2])
            authors.append(author)
        return authors
    

class Author:
    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
    
    def fullName(self):
        return f"{self.firstName} {self.lastName}"
    
    def logic2():
        pass
    
class App:
    def printAuthors(self):
        authors = DBPersistance.getAuthors()
        for author in authors:
            print(author.fullName())
    
    def createAuthor(self, firstName, lastName):
        newAuthor = Author(0, firstName, lastName)