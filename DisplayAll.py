import streamlit as st
import pymysql as mysql
try:
  db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
  smt=db.cursor()
  st.title("Display All Employee Records")
  st.image('employee.png',width=300)
  smt.execute('Select employeeid as "Employee ID",employeename as "Employee Name",dob as "Date of Birth",gender as "Gender",city as "City",salary as "Salary",mobileno as "Mobile No." from employees')
  records=smt.fetchall()
  st.dataframe(records)
  db.close()
except Exception as e:
 st.error(e)
