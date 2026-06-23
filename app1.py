import streamlit as st
import pymysql as mysql
import Employee_management as employee
from streamlit_option_menu import option_menu
import base64
st.set_page_config(page_title="Nexora Technologies EMS",page_icon="🏢",layout="wide")
st.markdown("""
<style>

/* Login Dialog */
div[data-testid="stDialog"] div[role="dialog"]{
    background: rgba(255,255,255,0.5) !important;
    backdrop-filter: blur(30px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 20px !important;
}

/* Input boxes */
.stTextInput input{
    background: rgba(255,255,255,0.15) !important;
    color: white !important;
}

/* Labels */
label{
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("backgroundtwo.avif")

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/avif;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)


@st.dialog('Login Page')
def login():
    user=st.text_input("Username")
    pwd=st.text_input("Password",type="password")

    if st.button("🔐 Login"):
        try:
           db = mysql.connect(host='localhost',port=3306,user='root',password='1234',database='pythonpractice',cursorclass=mysql.cursors.DictCursor)
           smt=db.cursor()
           q=f"Select * from userss where user_id='{user}' and user_pswd='{pwd}'"
           smt.execute(q)
           record=smt.fetchone()

           if record :
             st.session_state.username=record['user_name']
             st.session_state.user_id=record['user_id']
             st.session_state.image=record['image']
             st.session_state.logged_in=True
             st.rerun()
           else:
             st.error('Invalid Login')
        except Exception as e:
           st.error(e)
        finally:
           db.close() 
# initialize
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# login popup
if not st.session_state.logged_in:
    login()
    st.stop()

# top profile
col1,col2,col3 = st.columns([1,6,1])

with col1:
    st.image(st.session_state.image,width=90)

with col2:
    st.header(f"Hello, {st.session_state.username}!")

with col3:
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

# role based menu
if st.session_state.user_id == "admin":

    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "Home",
            "Insert Employee",
            "View Employee",
            "Update Employee",
            "Delete Employee",
            "Search By ID",
            "Search By Salary"
        ],
        icons=["house", "plus", "eye", "pencil", "trash", "search", "cash-stack"],
        menu_icon="cast",
        orientation="horizontal",
        styles={
            "container": {
                "padding": "5px",
                "background-color": "rgba(255,255,255,0.08)",
                "border-radius": "15px"
                },
            "nav-link": {
                "font-size": "18px",
                "text-align": "center",
                "margin": "5px",
                "--hover-color": "#3b82f6",
                },
            "nav-link-selected": {
               "background": "linear-gradient(45deg,#2563eb,#7c3aed)",
               "color": "white",
               },
        }
    )
    if selected=="Home":
       employee.home()

    elif selected=="Insert Employee":
        employee.addEmployee()

    elif selected=="View Employee":
        employee.showAllEmployees()

    elif selected=="Update Employee":
        employee.updateEmployee()

    elif selected=="Delete Employee":
        employee.deleteEmployee()

    elif selected=="Search By ID":
        employee.searchById()

    elif selected=="Search By Salary":
        employee.searchBySalary()
elif st.session_state.user_id == "employee":

    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "Home",
            "View Employee",
            "Search By ID",
            "Search By Salary"
        ],
        icons=["house", "eye", "search", "cash-stack"],
        menu_icon="cast",
        orientation="horizontal",
        styles={
            "container": {
                "padding": "5px",
                "background-color": "rgba(255,255,255,0.08)",
                "border-radius": "15px"
                },
            "nav-link": {
                "font-size": "18px",
                "text-align": "center",
                "margin": "5px",
                "--hover-color": "#3b82f6",
                },
            "nav-link-selected": {
               "background": "linear-gradient(45deg,#2563eb,#7c3aed)",
               "color": "white",
               },
        }
    )  

    if selected=="Home":
       employee.home()

    elif selected=="View Employee":
        employee.showAllEmployees()

    elif selected=="Search By ID":
        employee.searchById()

    elif selected=="Search By Salary":
        employee.searchBySalary()

