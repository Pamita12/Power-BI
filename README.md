# README FILE FOR THE STUDENT HEALTH DATA WEBSITE

## Contents
1. [Project Name](#project-name)
2. [Project Description](#project-description)
3. [Prerequisites and Packages/Libraries](#prerequisites-and-packageslibraries)
4. [Getting Started](#getting-started)
5. [Installation and Configuration Instructions](#installation-and-configuration-instructions)
6. [Running the project_flask Application](#running-the-project_flask-application)
7. [Project/Code Structure](#projectcode-structure)
8. [App Routes](#app-routes)
9. [License](#license)
10. [References](#references)
    
## 1. Project Name
- **Project_flask.py**
  
## 2. Project Description
- The `project_flask.py` application allows users to view student health data stored in an SQLite database, `student_health_data.db`. The app provides a simple interface to navigate between the project information, about page, and the data table.
- The data was sourced from Kaggle: [Student-Health-Data](https://www.kaggle.com/datasets/ziya07/student-health-data).
  
## 3. Prerequisites and Packages/Libraries
- Python 3.12.7
- Flask and `render_template` from flask
- SQLite3
- Pathlib
  
## 4. Getting Started
- Develop Python codes:
  - SQL Database and Table using `sqlite3`
  - `project_flask` website
- Develop HTML codes and save in a folder named `template`:
  - Homepage
  - About page
  - Data page
  - Group Information
    
## 5. Installation and Configuration Instructions
- Use the virtual environment (myspace) created in Visual Studio Code.
- Install and import the required packages:
  - `pip install flask` and import `Flask`, `render_template`
  - Import `sqlite3`, `pathlib`
- Setup the database: Ensure you have the `student_health_data.db` SQLite database in the project directory. If not, create and populate it accordingly.
- Define codes for the `project_flask` for the website:
  - `app_routes` for the four HTML files (homepage, about, data_table, group_info)
  - Path to call the database `student_health_data.db`
  - `app.run` to run the code
    
## 6. Running the project_flask Application
    1. Start the `project_flask` app by executing the code for the application:
      ```bash
      # Serving Flask app 'project_flask'
      # Debug mode: on
      WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
      # Running on http://127.0.0.1:5000
      Press CTRL+C to quit
      # Restarting with stat
      # Debugger is active!
      # Debugger PIN: 696-082-221
      ```
    2. Access the application:
      - Open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
      - This opens the `project_flask` website
      
## 7. Project/Code Structure
    1. `project_flask.py`: The main Flask application file.
    2. `templates/`: Directory containing HTML files.
       - `homepage.html`: The project information page.
       - `about.html`: The about page is the information about the dataset, describing the functions of each variable.
       - `data_table.html`: The page displaying the sample of 100 observations in the student health data.
       - `group_info.html`: Names and IDs of group 10 members
     
## 8. App Routes
    1. `/`: Displays the project information page.
    2. `/about`: Displays the about page.
    3. `/data`: Connects to the SQLite database, retrieves student health data, and displays it in a table.
    4. `/group_info`: Displays the names of the group 10 members
   
## 9. License
The `flask_project` is the final group project for the Introduction to Python Programming (DAB 111) course under the St. Clair Data Analytics for Business Program.

## 10. References
  - Flask documentation: [Flask Docs](https://flask.palletsprojects.com/)
  - SQLite documentation: [SQLite Docs](https://www.sqlite.org/docs.html)
  - HTML documentation: [HTML Docs](https://www.w3schools.com/html/)
  - Dataset Source: [Kaggle - Student Health Data](https://www.kaggle.com/datasets/ziya07/student-health-data)
  - Lecture notes
