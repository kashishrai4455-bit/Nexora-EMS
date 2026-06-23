import pymysql as mysql
import streamlit as st
try:
  db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
  smt=db.cursor()
  st.title("Search Employee Record")
  st.image('employee.png',width=300)
  salary_range=st.slider("Select salary Range",10000,1500000,(20000,1000000),step=500)
  # if st.button("Search"):
  smt.execute(f"Select * from employees where salary between {salary_range[0]} and {salary_range[1]}")
  records=smt.fetchall()
  if records:
    st.dataframe(records)
  else:
    st.error("Record Not Found...")
  db.close()
except Exception as e:
 st.error(e)