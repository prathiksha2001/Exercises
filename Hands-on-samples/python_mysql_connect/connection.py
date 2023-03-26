import mysql.connector

# connect() will open a connection to a MySQL server and return a MySQLConnection object.
conn = mysql.connector.connect(host="localhost", user = "root" , password="Admin@2022", database = "book")

if(conn.is_connected()):
    print("connected successfully")

mycursor = conn.cursor()
mycursor.execute("SELECT * FROM books")

# mycursor.execute("CREATE TABLE books")

##### show databases 

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

## create book table
mycursor.execute("CREATE TABLE books(book_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, author_id INT NOT NULL)")

## create author table 
#mycursor.execute("CREATE TABLE authors(author_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL)")

## add foreign key constraint in books table

#mycursor.execute("ALTER TABLE books ADD CONSTRAINT FOREIGN KEY(author_id) REFERENCES authors(author_id)")

# add column in authors table
#mycursor.execute("ALTER TABLE authors ADD COLUMN age INT")


### insert values into author table
# sql_formula = "INSERT INTO authors(name,age) VALUES(%s, %s)"
# author_name = [("William Shakespeare", "60"),
#                 ("Ruskin Bond", "48"),
#                 ("Ashwin Sanghi", "34"),
#                 ("Amish Tripathi", "45"),
#                 ("Shobha Nihalani", "39"),
#                 ("Anita Nair", "40"),
#                  ]

# mycursor.executemany(sql_formula, author_name)
# conn.commit()

### insert values into books table

# sql_cmd = "INSERT INTO books(name,author_id) VALUES(%s,%s)"

# book_details = [
#                 ("The Silent Monument",5),
#                 ("The Room on the Roof",2),
#                 ("Romeo and Juliet",1),
#                 ("Unresolved – A psychological thriller",5),
#                 ("Sita - Warrior of Mithila",4),
#                 ("Mistress",6),
#                 ("Dharma: Decoding the Epics for a Meaningful Life",4),
#                 ("the NINE trilogy",5),
#                 ("Lessons in Forgetting",6),
#                 ("Raavan: Enemy of Aryavarta",4),
#                 ("Angry River",5),
#                 ("Count to Ten",3),
#                 ("Hamlet",1),
#                 ("The Blue Jade",5),
#                 ("How To Live Your Life",2),
#                 ("The Krishna Key",3),
#                 ("A Midsummer Night's Dream",1),
#                 ("Cherry tree",2),
#                 ("The Better Man",6),
#                 ("Private India",3),
#                 ("Julius Caesar",1),
#                 ("Trikon – a medical sci-fi thriller",5),
#                 ("The Blue Umberlla",2),                
#                 ]
# mycursor.executemany(sql_cmd, book_details)
# conn.commit()


## view book name and author
# mycursor.execute("SELECT b.name, a.name FROM books b JOIN authors a ON b.author_id = a.author_id")

# for bname, aname in mycursor:
#     print(bname + " - " + aname)

## view book name and author in alphabetical order
# mycursor.execute("SELECT b.name, a.name FROM books b JOIN authors a ON b.author_id = a.author_id ORDER BY b.name")

# for bname, aname in mycursor:
#     print(bname + " - " + aname)

## show the author with their book_count
# mycursor.execute("SELECT a.name, COUNT(*) AS book_count FROM books b 
#                   JOIN authors a ON b.author_id = a.author_id GROUP BY a.author_id")
# for aname, count in mycursor:
#     print(aname +" - " + str(count))

## show the author with their book_count
mycursor.execute("SELECT a.name FROM books b JOIN authors a ON b.author_id = a.author_id GROUP BY a.author_id ORDER BY COUNT(*) DESC LIMIT 1")

for aname in mycursor:
    print(aname)

