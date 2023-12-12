from bottle import route, post, run, template, redirect, request
import database

@route("/")
def get_index():
     return template("home.tpl")

@route("/courses")
def get_courses():
    items = database.get_courses()
    return template("courses_list.tpl", courses_list=items  )

@route("/courses/add")
def add_courses():
    items = database.get_professors()
    # print('------------------------')
    # print(items)
    # print('------------------------')
    return template("add_courses.tpl",professors_list = items[1:])

@post("/add_course")
def add_course():
    Name = request.forms.get("Name")
    Prof_id = request.forms.get("Profid")
    Code = request.forms.get("Code")
    Info = request.forms.get("Info")
    database.add_course(Name,Prof_id,Code,Info)
    redirect("/courses")


@route("/update_course/<id>")
def update_prof(id):
    result = database.get_courses(id)
    items = database.get_professors()
    # print(result)
    return template("update_course.tpl",item = result[0],professors_list = items[1:])

@post("/course/update")
def update_prof():
    id_ = request.forms.get("id")
    Name = request.forms.get("Name")
    Prof_id = request.forms.get("Profid")
    Code = request.forms.get("Code")
    Info = request.forms.get("Info")
    items = database.update_course(id_,Name,Prof_id,Code,Info)
    redirect("/courses")

@route("/delete_course/<id>")
def delete_course(id):
    database.delete_course(id)
    redirect("/courses")


@route("/professors")
def get_professors():
    items = database.get_professors()
    return template("professors_list.tpl", professors_list=items[1:] , )

@route("/professors/add")
def add_professor():
    return template("add_professor.tpl")

@post("/add_prof")
def add_professor():
    Name = request.forms.get("Name")
    Class_Time = request.forms.get("Class_Time")
    items = database.add_professor(Name,Class_Time)
    redirect("/professors")


@route("/update_prof/<id>")
def update_prof(id):
    result = database.get_professors(id)
    # print(result)
    return template("update_professor.tpl",item = result[0])

@post("/professors/update")
def update_prof():
    id_ = request.forms.get("id")
    Name = request.forms.get("Name")
    Class_Time = request.forms.get("Class_Time")
    database.update_prof(id_,Name,Class_Time)
    redirect("/professors")

@route("/delete_prof/<id>")
def delete_prof(id):
    database.delete_prof(id)
    redirect("/professors")

@route("/students")
def get_students():
    items = database.get_students()
    return template("students_list.tpl", students_list=items)

@route("/students/add")
def add_student():
    items = database.get_courses()
    return template("add_student.tpl",courses_list = items)

@post("/add_student")
def add_student():
    Name = request.forms.get("Name")
    Courseid = request.forms.get("Courseid")
    items = database.add_student(Name,Courseid)
    redirect("/students")


@route("/update_student/<id>")
def update_student(id):
    result = database.get_students(id)
    items = database.get_courses()
    # print(result)
    return template("update_student.tpl",item = result[0],courses_list = items)
    

@post("/student/update")
def update_student():
    id_ = request.forms.get("id")
    Name = request.forms.get("Name")
    Courseid = request.forms.get("Courseid")
    database.update_student(id_,Name,Courseid)
    redirect("/students")

@route("/delete_student/<id>")
def delete_student(id):
    database.delete_student(id)
    redirect("/students")

@post("/search")
def search():
    search_string = request.forms.get("value")
    type_ = request.forms.get("type")
    database.master_join(search_string,type_)

run(host='localhost', port=8080)

