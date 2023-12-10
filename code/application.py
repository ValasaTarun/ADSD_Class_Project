from bottle import route, post, run, template, redirect, request
import database

@route("/")
def get_index():
     return template("home.tpl")

@route("/courses")
def get_courses():
    items = database.get_courses()
    return template("courses_list.tpl", courses_list=items , )

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
    print(result)
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
    return template("students_list.tpl", students_list=items , )


run(host='localhost', port=8080)