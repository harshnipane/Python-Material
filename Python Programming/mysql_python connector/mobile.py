import mysql.connector

rec = []

for i in range(3):
    nm = input("enter name")
    mno = input("enter mobile no")
    rec.append([nm,mno])

cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()

cur.execute("""CREATE TABLE mobile_details( 
            name varchar(10), 
            mobile varchar(10));""")
cnx.commit()
cnx.close()


cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')

cur = cnx.cursor()
for name,mobile in rec:
    query = "insert into mobile_details values(" +\
                repr(name) + ","+\
                repr(mobile)+");"
    print(query)
    cur.execute(query)

cnx.commit()
cnx.close()


cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
cur.execute("select * from mobile_details")

for row in cur:
    print(row)

print("______________________________________________________________________")    

cur.execute("select name from mobile_details where mobile regexp '^98'")

for row in cur:
    print(row)

print("______________________________________________________________________")        


cur.execute("select name from mobile_details where mobile regexp '0{3,}'")

for row in cur:
    print(row)
cnx.close()





