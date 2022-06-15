import numpy as np
# import mysql.connector
# import mysql
import sqlite3
from js import console
# import _mysql_connector

conn = sqlite3.connect('arise_database.db')

def shuffle_array(*args):
    pyscript.write('output','hello')
    # result_place = Element('output').element
    # result_place.write((float(Element('name').value).element) * float((Element('lastName').value).element))
    
def testing(*args, **kwargs):

    result_place = Element('output')
    result_place.write((float(Element('name').element.value)) * float((Element('lastName').element.value)))
           
def arrayList(*args):
    arr = [1,2,3,4,5]
    
    
    # pyscript.write('output2',arr[1])
    for i in arr:
        pyscript.write('output2',i)
    
def loginPage():
    #return render(request, 'accounts/login.html')
 
        username = Element('username').element.value
        password = Element('password').element.value

def create_database(*args, **kwargs):
    """
    This function is for 
    creating database
    """
    try:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS admin_login (id INT AUTO_INCREMENT PRIMARY KEY,\
                username VARCHAR(250), password_admin VARCHAR(250),status_admin VARCHAR(250))")

        console.log('databse has been created') 
    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")
def insert_adminLogin(*args, **kwargs):
    """
    This function is for 
    inserting data to admin database
    """ 
    conn.execute(
        """INSERT INTO admin_login (id,username,password_admin,status_admin) VALUES('3','joey','genesis@11','approved') """)
    console.log('Item is inserted')
    
def fetch_data_admin(*args, **kwargs):
    """
    This function is for fetching
    data from admin
    """
    user_login_list = conn.execute('SELECT * from admin_login')
    # user_login_list = conn.execute('SELECT name from sqlite_master where type= "table"')
    # 'SELECT name from sqlite_master where type= "table"'
    
    # for row in user_login_list:
    #     # print(row[0],row[1],row[2])
    #     a = row[0]
    #     pyscript.write('output2',a)
    pyscript.write('output2',user_login_list.fetchall())
        
    # pyscript.write('output2','i am legend')
# create_database()   
# mydb = mysql.connector.connect(
#     host="192.46.225.247",
#     user="joeysabusido",
#     password="Genesis@11",
#     database="ldglobal",
#     )
# cursor = mydb.cursor()

# def showColumns():
#     query ='SHOW COLUMNS FROM ldglobal.payroll_computation;'
#     cursor.execute(query)
#     myresult = cursor.fetchall()

#     for i in myresult:
#         pyscript.write('output',i[0])
