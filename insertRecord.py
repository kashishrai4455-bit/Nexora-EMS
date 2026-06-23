import streamlit as st
import pymysql as mysql
try:
  db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice')
  smt=db.cursor()
  st.title("Insert Employee Record")
  st.image('employee.png',width=300)
  eid=st.text_input('Enter Employee Id:',placeholder="Use Only Numbers like 100,200,...")
  en=st.text_input('Enter Employee Name:',placeholder="Use Only Characters like Abhir, Rahul,...")
  dob=st.text_input('Enter Date Of Birth:',help="Use Date Format like 1990/01/01")
  gender=st.radio('Enter Employee Gender:',options=['Male','Female','Other'])
  ec=st.text_input('Enter Employee City:',placeholder="Use Only Characters like Delhi, Mumbai,...")
  salary=int(st.number_input('Enter Employee salary',min_value=20000,max_value=1000000,step=1000))
  mobile=st.text_input('Enter mobile number:',placeholder="Use Only Numbers like 9876543210")
  q=f"insert into employees values ({eid},'{en}','{dob}','{gender}','{ec}',{salary},'{mobile}')"
  if st.button('submit'):
    smt.execute(q)
    st.success('Employee created successfully....')
  db.commit()
  db.close()
except Exception as e:
 st.error(e)

