import numpy as np
# import mysql.connector
# import mysql
import sqlite3
# import _mysql_connector



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
