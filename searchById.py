import streamlit as st
import pymysql as mysql
try:
  db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
  smt=db.cursor()
  st.title("Search Employee Record")
  st.image('employee.png',width=300)
  id=st.text_input("Enter Employee Id you want to search:",placeholder="Use Only Numbers Like 100,200,.....")
  if(st.button('Search')):
      smt.execute(f"Select * from employees where employeeid={id}")
      record=smt.fetchone()
      if(record):
        st.text_input("Employee ID",value=f"{record['employeeid']}")
        st.text_input("Employee Name",value=f"{record['employeename']}")
        st.text_input("Date of Birth",value=f"{record['dob']}")
        st.text_input("Gender",value=f"{record['gender']}")
        st.text_input("City",value=f"{record['city']}")
        st.text_input("Salary",value=f"{record['salary']}")
        st.text_input("Mobile No.",value=f"{record['mobileno']}")
      else:
        st.error("Employee Not Found...")
  db.close()
except Exception as e:
  st.error(e)