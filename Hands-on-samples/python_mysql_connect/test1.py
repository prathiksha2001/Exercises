import mysql.connector
import even

print(even.sayHello())
# con = mysql.connector.connect(host="localhost",user="root" ,password="Admin@2022", database = "python")
# if(con.is_connected()):
#     print("Connection Successful")

# cursor = con.cursor()

# # mycursor.execute("SELECT * FROM books")
# # myresult = mycursor.fetchall()
# # print(myresult)
# # for x in myresult:
# #   print(x)
# # mycursor.execute("DESC actor")
# # result = mycursor.fetchall()
# # for x in result:
# #     print(x)

# # ---------CREATING DATABASE-------------
# # cursor.execute("CREATE DATABASE python")

# # ---------CHECK IF DATABASE EXIST-------------
# cursor.execute("SHOW DATABASES")
# result = cursor.fetchall()
# print(result)
# print('\n') 
# #-----------CREATE TABLE---------------
# # cursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")
# #-----------Check if Table Exists---------------
# # cursor.execute("DESC customers")
# # res = cursor.fetchall()
# # for row in res:
# #     print(row)

# #-----------ADD PRIMARY KEY----------------
# # cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# #-----------DROP TABLE ------------------
# # cursor.execute("DROP TABLE customers")
# # print(cursor)
# # cursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL , address VARCHAR(255) )")


# # ------------INSERT VALUES INTO TABLE-----------------
# # query = "INSERT INTO customers(name, address) VALUES (%s, %s)"
# # values = [("suji", "France"),("prathi", "France")]
# # cursor.executemany(query,values)
# # con.commit()
# # print(str(cursor.rowcount) + ' rows inserted')
# # print(cursor.lastrowid)

# #--------------SELECT STATEMENT--------------------
# # cursor.execute("SELECT * FROM customers")
# # for row in cursor.fetchall():
# #     print(row)

# print("\n")

# #-----------SELECT STATEMENT--------------------

# # cursor.execute("SELECT name FROM customers")
# # for row in cursor.fetchall():
# #     print(row)
# # print('\n')
# # cursor.execute("SELECT name FROM customers WHERE name LIKE '%e%' and 1 = 1")
# # for row in cursor.fetchall():
# #     print(row)

# # sql = "SELECT * FROM customers WHERE address = %s"
# # adr = ("Orange island", )
# # cursor.execute(sql,adr)
# # for row in cursor.fetchall():
# #     print(row)

# #-----------------ORDER BY--------------------------
# # cursor.execute("SELECT * FROM customers ORDER BY address DESC")
# # for row in cursor.fetchall():
# #     print(row)

# #-----------------DELETE FROM----------------------------

# # cursor.execute("DELETE FROM customers WHERE id = 6")
# # con.commit()

# #-------------------PREVENT SQL INJECTION------------------
# # query = "DELETE FROM customers WHERE name = %s" 
# # key = ('Hoenn',)
# # cursor.execute(query,key)
# # con.commit()

# #-----------------UPDATE-------------------------------
# # cursor.execute("UPDATE customers SET address='Idly' WHERE address='India'")
# # con.commit()

# #-----------------LIMIT---------------------------------
# cursor.execute("SELECT * FROM customers LIMIT 2 OFFSET 2")
# for row in cursor.fetchall():
#     print(row)