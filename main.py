from flask import Flask, request, render_template
from random import randint

from models.user import User
app = Flask(__name__, static_url_path='/static')
state_list = []

user = User()
active_user = None
print(user)

@app.route("/")
def show_items():
    return f"""
        <img src = "/static/images/university.jpg" />

        <form action="/add_item" method="POST">
          <div>
             <label for="new_item">Please enter name of student</label>
             <input name="name" id="new_item"  />
          </div>
          <div>
             <label for="new_item">Please enter language of studying</label>
             <input name="language" id="new_item" />
          </div>
            <button>Send my choice</button>
        </form>
            <form action = "/show_students" method="POST">
            <button>Check students list</button>

        </form>
    """

@app.route("/show_students", methods = ["POST"])
def show_students():

    students = [str(students.name) for students in state_list]
    return render_template('list_of_students.html', students=students)

@app.route("/chose_value", methods=['POST', 'GET'])
def chose_value():
    our_student = []
    select = request.form.get('students')
    for temp in state_list:
        global active_user
        if temp.name == str(select):
            active_user = temp
    return render_template('student_print.html', student=active_user)

@app.route("/menu_change_course", methods=['POST', 'GET'])
def menu_change_course():
    global active_user
    return render_template('change_course.html', our_student=active_user)

@app.route("/change_course", methods=['POST', 'GET'])
def change_course():
    global active_user
    course = str(request.form.get('course'))
    for user_temp in state_list:
        if user_temp == active_user:
            user_temp.chose_course(course)
    return show_items()
#ccccccccccccccc

@app.route("/menu_autorization", methods=['POST', 'GET'])
def menu_autorization():

    return render_template('password_check.html')

@app.route("/check_autorization", methods=['POST', 'GET'])
def check_autorization():
    password = str(request.form.get('password'))
    if password == "I love Liza Sladkowskaya":
        return render_template('change_grade.html')
    else:
        return f"""Incorrected password { password }
        <form action = "/show_students" method="POST">
            <button type="submit" class="btn btn-default">Home page</button>
        </form>
"""

@app.route("/change_grade", methods=['POST', 'GET'])
def change_grade():
    global active_user
    grade = int(request.form.get('grade'))
    for user_temp in state_list:
        if user_temp == active_user:
            user_temp.set_grade(grade)
    return show_items()


@app.route("/add_item", methods=["POST"])
def add_item():
    user_input = False
    name = ""
    language = ""
    try:
        name = str(request.form.get('name'))
        language = str(request.form.get('language'))

        user_input = True
    except ValueError:
       pass
    user_temp = User(name=name, language=language)

    state_list.append(user_temp)
    return f"""
        <h3>Updated list: {state_list}</h3>
        </br>
        <h4>New item {name}</h4>
        <h4>New item {language}</h4>

        </br>
        <a href="/">Return to the HOME page</a>

    """


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)

"""
HTTP Status Codes

Informational responses (100 – 199)
Successful responses (200 – 299)

200 OK
201 Created
202 Accepted

Redirection messages (300 – 399)

301 Moved Permanently

Client error responses (400 – 499)

400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed
408 Request Timeout
429 Too Many Requests

Server error responses (500 – 599)

500 Internal Server Error
501 Not Implemented
"""