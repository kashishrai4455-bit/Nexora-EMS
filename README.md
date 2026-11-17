# 🏢 NEXORA TECHNOLOGIES
## Employee Management System (EMS)

### 📌 Project Overview
Nexora Technologies Employee Management System is a web-based application developed using Python, Streamlit, and MySQL.

This application helps organizations efficiently manage employee records, personal details, and salary information. It provides separate login access for Admin and Employee users with role-based functionalities.

### ✨ Features

**1. Admin Login**
- Secure login system for administrators.
- Access to all employee management operations.
- Admin can manage employee records.

**2. Employee Login**
- Separate login for employees.
- Employees can view employee records.
- Search employee details by ID.
- Search employees by salary range.

**3. Employee Management**
- ➕ Add New Employee Records
- 👥 View All Employee Records
- ✏️ Update Employee Details
- 🗑️ Delete Employee Records
- 🔍 Search Employee By ID
- 💰 Search Employee By Salary

**4. User Interface**
- Interactive Streamlit web interface.
- Custom background image.
- Login popup dialog.
- Role-based navigation menu.
- Profile image display.
- Logout functionality.

### 🛠️ Technologies Used

- **Python** – Backend Programming
- **Streamlit** – Web Application Framework
- **MySQL** – Database Management
- **PyMySQL** – MySQL Database Connectivity
- **Streamlit Option Menu** – Navigation Menu
- **HTML & CSS** – UI Styling

### 📂 Project Structure

```text
Nexora-Employee-Management-System/
│
├── app.py
├── Employee_management.py
├── README.md
├── backgroundtwo.avif
└── employeeone.png
```

*Note: Replace `app.py` with the actual name of your main Python file if it is different.*

### ⚙️ Installation & Setup

**Step 1: Clone the Repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Navigate to Project Folder**

```bash
cd Nexora-Employee-Management-System
```

**Step 3: Install Required Libraries**

```bash
pip install streamlit
pip install pymysql
pip install streamlit-option-menu
```

**Step 4: Setup MySQL Database**

- Install and start MySQL Server.
- Create a database named `pythonpractice`.
- Create the required `userss` and `employees` tables.
- Add the required user login records and employee records.

The application expects the following database fields:

**userss table:**
- user_id
- user_pswd
- user_name
- image

**employees table:**
- employeeid
- employeename
- dob
- gender
- city
- salary
- mobileno

**Step 5: Configure Database Connection**

Update the MySQL connection details in the Python files according to your local MySQL configuration.

Do not upload real database passwords or sensitive credentials to GitHub.

### ▶️ How to Run the Project

Run the following command in the VS Code terminal:

```bash
streamlit run app.py
```

The application will open in your web browser.

### 🔐 User Roles

| Admin | Employee |
|---|---|
| Add Employee | View Employees |
| View Employees | Search By ID |
| Update Employee | Search By Salary |
| Delete Employee | Home Page |
| Search By ID | |
| Search By Salary | |

### 🎯 Project Objective

The main objective of this project is to simplify employee record management by providing an easy-to-use web application with database connectivity and role-based access.

### 👩‍💻 Developer

**Developed by: Kashish Rai**

**Project Name:** Nexora Technologies – Employee Management System

---

⭐ If you find this project useful, don't forget to give it a star on GitHub!