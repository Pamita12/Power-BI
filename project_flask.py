from flask import Flask, render_template
import sqlite3
import pathlib

base_path = pathlib.Path(__file__).parent
db_name = "student_health_data.db"
db_path = base_path / db_name

app = Flask(__name__)

@app.route("/")
def info_project():
    return render_template("info_project.html") 

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/data")
def data_page():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    students = cursor.execute("SELECT * FROM student_health").fetchall()
    con.close()

    return render_template("data_table.html", students=students)


if __name__=="__main__":
    app.run(debug=True)