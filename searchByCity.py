import streamlit as st
import pymysql as mysql
try:
  db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
  smt=db.cursor()
  st.title("Search Employee Record")
  st.image('employee.png',width=300)
  city=tuple(st.text_input("Enter city:").split(','))
  if(st.button('Search')):
    smt.execute(f"Select employeeid as 'Employee ID',employeename as 'Employee Name',dob as 'Date of Birth',gender as 'Gender',city as 'City',salary as 'Salary',mobileno as 'Mobile No.' from employees where city in {city}")
    records=smt.fetchall()
    if(len(records)>0):
      st.dataframe(records)
    else:
      st.error("Record Not Found...")
  db.close()
except Exception as e:
  st.error(e)