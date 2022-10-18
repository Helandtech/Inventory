from genericpath import exists
from pickletools import string1
from select import select
import mysql.connector as mysql

mydb = mysql.connect (host = "localhost", database= "orderinventory", user= "root", password="Casa98" , port = "330" )




mycursor = mydb.cursor()






def create_order():
    sql = "INSERT INTO create_order (user_id) VALUES (%s)"
    username = []
    user = int(input("Enter your phone number to place an order: "))
    user = str(user)
    username.append(user)
    val = (username)
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    select_query = "select * from create_order where user_id= " + user
    mycursor.execute(select_query)
    records = mycursor.fetchone()
    print("Order created with id",records[0])


def add_product_order():

    sql = "INSERT INTO add_product_order (product_name, product_quantity, product_id) VALUES ( %s, %s, %s )"
    product_name = input("""Enter product name:""")

    product_quantity = int(input("""Enter product quantity:"""))
    product_id = int(input("""Enter your order id to add products:"""))
    val = ( product_name, product_quantity,product_id)
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    select_query = "select product_name, product_quantity,product_id from add_product_order where product_id = " + str(product_id)+" ORDER BY ID DESC LIMIT 1"
    mycursor.execute(select_query)
    records = mycursor.fetchmany()
    for row in records:
     print(row[1],row[0], "added to order",row[2] )




def show_order():
    product_id = str(input("""Enter order id:"""))
    select_query = "select * from add_product_order where product_id = " + product_id
    
    mycursor.execute(select_query)
    myresult = mycursor.fetchall()

    #select_sum = "select sum(product_quantity) AS 'TOTAL' from  add_product_order where product_id=" + product_id
    query = "select product_quantity from add_product_order where product_id=" + product_id
    mycursor.execute(query)
    data_sum = mycursor.fetchall()
    data_sum = sum(list(map(sum, list(data_sum))))
   
    print("Order " +   product_id + " " + "DRAFT",data_sum)
    for x in myresult:
        print(x[1], x[2], x[4])     


#function to show all orders/tables
def show_orders():
    mycursor.execute("SELECT product_id,product_name,product_quantity,status FROM add_product_order order by product_id asc")
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Order ", x[0], x[3])
        print(x[1], x[2], x[3])          


option = input("Enter what action to take "
                        "\n 1 - CREATE_ORDER "
                        "\n 2 - ADD_PRODUCT_ORDER "
                        "\n 3 - SHOW_ORDER "
                        "\n 4 - SHOW_ORDERS "
                        "\n Choose function here: ")
                    
if option == "1" :
    create_order()

elif option == "2":
    add_product_order()

elif option == "3":
    show_order()

elif option == "4":
    show_orders()

else:
    print("Invalid option")