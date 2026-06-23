import pymysql as mysql
import streamlit as st
try:
    db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
    smt=db.cursor()
    id=st.text_input("Enter Id you want to delete:",placeholder="Use Only Number like 100,200,...")
    if st.button("Search"):
        smt.execute(f"select * from employees where employeeid={id}")
        record=smt.fetchone()
        if record:
            st.session_state.Record=record
            st.success("Record found....")
        else:
            st.error("Record not found...")
    db.close()
except Exception as e:
    st.error(e)
if 'Record' in st.session_state:
    en=st.text_input("Enter New Employee Name:",value=f"{st.session_state.Record['employeename']}")
    dob=st.text_input("Enter New Employee DOB:",value=f"{st.session_state.Record['dob']}")
    gender=st.text_input("Enter New Employee Gender:",value=f"{st.session_state.Record['gender']}")
    city=st.text_input("Enter New Employee City:",value=f"{st.session_state.Record['city']}")
    salary=st.text_input("Enter New Employee Salary:",value=f"{st.session_state.Record['salary']}")
    mobileno=st.text_input("Enter New Employee Mobile No:",value=f"{st.session_state.Record['mobileno']}")
    ans=st.radio("Do you want to delete above record?",options=['Yes','No'])
    if ans.lower()=='no':
        st.warning("Record not deleted...")
    elif ans.lower()=='yes':
        if st.button("Delete"):
            try:
                db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
                smt=db.cursor()
                q=f"DELETE FROM employees WHERE employeeid = {st.session_state.Record['employeeid']}"
                smt.execute(q)
                db.commit()
                st.success("Record Deleted successfully....")
                db.close()
            except Exception as e:
                st.error(e)