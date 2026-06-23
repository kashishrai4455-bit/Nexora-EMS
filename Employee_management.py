import pymysql as mysql
import streamlit as st

#insert record
def addEmployee():
    try:
        db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice')
        smt=db.cursor()
        col1, col2 = st.columns([1,4])
        with col1:
            st.image("employeeone.png", width=170)
        with col2:
            st.title("NEXORA TECHNOLOGIES")
        st.title("➕ Insert Employee Record")
        eid=st.text_input('Enter Employee Id:',placeholder="Use Only Numbers like 100,200,...")
        en=st.text_input('Enter Employee Name:',placeholder="Use Only Characters like Abhir, Rahul,...")
        dob=st.text_input('Enter Date Of Birth:',help="Use Date Format like 1990/01/01")
        gender=st.radio('Enter Employee Gender:',options=['Male','Female','Other'])
        ec=st.text_input('Enter Employee City:',placeholder="Use Only Characters like Delhi, Mumbai,...")
        salary=int(st.number_input('Enter Employee salary',min_value=20000,max_value=1000000,step=1000))
        mobile=st.text_input('Enter mobile number:',placeholder="Use Only Numbers like 9876543210")
        q=f"insert into employees values ({eid},'{en}','{dob}','{gender}','{ec}',{salary},'{mobile}')"
        if st.button('submit', key="submit_btn"):
            smt.execute(q)
            st.success('Employee created successfully....')
            db.commit()
            db.close()
    except Exception as e:
        st.error(e)

#search record
def searchById():
    try:
        db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
        smt=db.cursor()
        col1, col2 = st.columns([1,4])
        with col1:
            st.image("employeeone.png", width=170)
        with col2:
            st.title("NEXORA TECHNOLOGIES")
        st.title("🔍 Search Employee Record")
        id=st.text_input("Enter Employee Id you want to search:",placeholder="Use Only Numbers Like 100,200,.....")
        if(st.button('Search', key="search_btn")):
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

#update record
def updateEmployee():
    try:
        db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
        smt=db.cursor()
        col1, col2 = st.columns([1,4])
        with col1:
            st.image("employeeone.png", width=170)
        with col2:
            st.title("NEXORA TECHNOLOGIES")
        st.title("✏️ Edit Employee Record")
        id=st.text_input("Enter Id you want to Edit:",placeholder="Use Only Number like 100,200,...")
        if st.button("Search", key="search_edit_btn"):
            q=f"select * from employees where employeeid={id}"
            smt.execute(q)
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
 
        if st.button("Edit", key="edit_btn"):
            try:
                db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
                smt=db.cursor()
                q=f"update employees set employeename='{en}',dob='{dob}',gender='{gender}',city='{city}',salary='{salary}',mobileno='{mobileno}' where employeeid={st.session_state.Record['employeeid']}"
                smt.execute(q)
                db.commit()
                st.success("Record updated successfully....")
                db.close()
            except Exception as e:
                st.error(e)

#delete record
def deleteEmployee():
    try:
        db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
        smt=db.cursor()
        col1, col2 = st.columns([1,4])
        with col1:
            st.image("employeeone.png", width=170)
        with col2:
            st.title("NEXORA TECHNOLOGIES")
        st.title("🗑️ Delete Employee Record")
        id=st.text_input("Enter Id you want to delete:",placeholder="Use Only Number like 100,200,...")
        if st.button("Search", key="search_delete_btn"):
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
            if st.button("Delete", key="delete_btn"):
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

#show all records
def showAllEmployees():
    try:
        db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
        smt=db.cursor()
        col1, col2 = st.columns([1,4])
        with col1:
            st.image("employeeone.png", width=170)
        with col2:
            st.title("NEXORA TECHNOLOGIES")
        st.title("👥 Display All Employee Records")
        smt.execute('Select employeeid as "Employee ID",employeename as "Employee Name",dob as "Date of Birth",gender as "Gender",city as "City",salary as "Salary",mobileno as "Mobile No." from employees')
        records=smt.fetchall()
        st.dataframe(records)
        db.close()
    except Exception as e:
        st.error(e)

#search By salary
def searchBySalary():
    try:
        db=mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
        smt=db.cursor()
        col1, col2 = st.columns([1,4])
        with col1:
            st.image("employeeone.png", width=170)
        with col2:
            st.title("NEXORA TECHNOLOGIES")
        st.title("💰 Search Employee Record")
        salary_range=st.slider("Select salary Range",10000,1500000,(20000,1000000),step=500)
        smt.execute(f"Select * from employees where salary between {salary_range[0]} and {salary_range[1]}")
        records=smt.fetchall()
        if records:
            st.dataframe(records)
        else:
            st.error("Record Not Found...")
        db.close()
    except Exception as e:
        st.error(e)

#Home page
def home():
    # st.markdown("""
    #  # 🏢 NEXORA TECHNOLOGIES

    #  ### Employee Management System

    #  Efficiently manage employee records, salary details, and workforce information.
    #  """)
    st.markdown("""
        <div style="
        background: rgba(255,255,255,0.08);
        padding:25px;
        border-radius:20px;
        backdrop-filter: blur(15px);
        border:1px solid rgba(255,255,255,0.15);
        ">
        <h1>🏢 NEXORA TECHNOLOGIES</h1>
        <h3>Employee Management System</h3>
        <p>Efficiently manage employee records, salary details, and workforce information.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    ### Features

    ✅ Add New Employees

    ✅ Search Employees
            
    ✅ Search Employees By Salary
            
    ✅ Update Employee Details

    ✅ Delete Employees

    ✅ View All Employees
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.info("📦 Employee Management")

    with col2:
        st.info("📊 Salary Tracking")

    st.markdown("""
    ### About

    This application helps manage employee records efficiently using
    Python, Streamlit, and MySQL.
   """)

    st.markdown("---")
    st.caption("Developed by Kashish Rai")

