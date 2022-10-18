from pickletools import string1
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

    sql = "INSERT INTO add_product_order (order_id, product_name, product_quantity) VALUES ( %s, %s, %s )"
    order_id = int(input("""Enter your order id:"""))
    order_id = str(order_id)
    product_name = input("""Enter product name:""")
    product_quantity = int(input("""Enter product quantity:"""))
    val = (order_id, product_name, product_quantity)
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    select_query = "select order_id, product_name, product_quantity from add_product_order where order_id = " + order_id
    mycursor.execute(select_query)
    records = mycursor.fetchone()
    print(records)
   


    #print(mycursor.rowcount, "record inserted.")

def show_order():
    mycursor.execute("SELECT * FROM ")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)     


#function to show all orders/tables
def show_orders():
    mycursor.execute("SHOW TABLES")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)     


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