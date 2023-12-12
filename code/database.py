import sqlite3

connection = sqlite3.connect("Class-Project.db")

def get_courses(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select C.id, C.Name as Course_Name , P.Name as Professor_Name , P.Class_Time, C.Code,C.Information , P.id as Profid   from courses C join Professors P on P.id = C.Taught_by")
    else:
        rows = cursor.execute(f"select C.id, C.Name as Course_Name , P.Name as Professor_Name , P.Class_Time, C.Code ,C.Information,P.id as Profid  from courses C join Professors P on P.id = C.Taught_by where C.id = {id};")
    rows = list(rows)
    rows = [ {'id' : row[0], 'Course Name': row[1],'Professor Name': row[2],'Class Timings': row[3],'Code': row[4],'Information':row[5],'Profid':row[6]} for row in rows ]
    return rows

def add_course(Name , Prof_id , Code , Information):
    cursor = connection.cursor()
    query = f"insert into Courses ('Name','Taught_by','Code','Information') values ('{Name}' , {Prof_id} , '{Code}' ,'{Information}')"
    cursor.execute(query)
    connection.commit()

def update_course(id,Name, Prof_id, Code,Info):
    cursor = connection.cursor()
    statement = f"update courses set Name='{Name}' ,Taught_by = '{Prof_id}',Code = '{Code}',Information = '{Info}'  where id={id}"
    cursor.execute(statement)
    connection.commit()

def delete_course(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from courses where id={id}")
    connection.commit()


def get_professors(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select id, Name, Class_Time from professors")
    else:
        rows = cursor.execute(f"select id, Name, Class_Time from professors where id = {id}")
    rows = list(rows)
    # print(rows , 'from get prof')
    rows = [ {'id' : row[0], 'Professor Name': row[1],'Class Timings': row[2]} for row in rows ]
    return rows



def add_professor(Name , Class_Time):
    cursor = connection.cursor()
    query = f"insert into Professors ('Name','Class_Time') values ('{Name}' , '{Class_Time}')"
    cursor.execute(query)
    connection.commit()

def update_prof(id, Name, Class_Time):
    cursor = connection.cursor()
    statement = f"update Professors set Name='{Name}' ,Class_Time = '{Class_Time}'  where id={id}"
    cursor.execute(statement)
    connection.commit()

def delete_prof(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from Professors where id={id}")
    connection.commit()

def get_students(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select S.id as Student_id , C.Name as Course_Name , S.Name as Student_Name,  C.Code,C.id as Courseid from courses C inner join Students S on C.id = S.Course_Enrolled")
    else:
        rows = cursor.execute(f"select S.id as Student_id  , C.Name as Course_Name , S.Name as Student_Name , C.Code,C.id as Courseid from courses C inner join Students S on C.id = S.Course_Enrolled where S.id = {id}")
    rows = list(rows)
    rows = [ {'Student id' : row[0], 'Course Name': row[1],'Student Name': row[2] , 'Code': row[3],'Courseid':row[4]} for row in rows ]
    return rows

def add_student(Name , Course_id):
    cursor = connection.cursor()
    query = f"insert into Students ('Name','Course_Enrolled') values ('{Name}' , {Course_id})"
    cursor.execute(query)
    connection.commit()

def update_student(id,Name, Course_id):
    cursor = connection.cursor()
    statement = f"update Students set Name='{Name}' ,Course_Enrolled = '{Course_id}'  where id={id}"
    cursor.execute(statement)
    connection.commit()

def delete_student(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from Students where id={id}")
    connection.commit()

def master_join(search_string , type_):
    print(search_string,type_)
    result_from = ''
    if 'P' in type_:
        cursor = connection.cursor()
        statement = f"select C.Name as Course_Name ,P.Name as Professor_Name ,P.Class_Time,C.Information ,S.Name as Student_Name,S.id as Student_id from courses C inner join Professors P on P.id = C.Taught_by inner join Students S on C.id = S.Course_Enrolled where P.id in (select id from Professors where Name like '%{search_string}%')"
        rows = cursor.execute(statement)
        result_from = 'Professor'
    if 'S' in type_:
        cursor = connection.cursor()
        statement = f"select C.Name as Course_Name ,P.Name as Professor_Name ,P.Class_Time,C.Information ,S.Name as Student_Name,S.id as Student_id from courses C inner join Professors P on P.id = C.Taught_by inner join Students S on C.id = S.Course_Enrolled where S.id in (select id from students where Name like '%{search_string}%')"
        rows = cursor.execute(statement)
        result_from = 'Student'

    if 'C' in type_:
        cursor = connection.cursor()
        statement = f"select C.Name as Course_Name ,P.Name as Professor_Name ,P.Class_Time,C.Information ,S.Name as Student_Name,S.id as Student_id from courses C inner join Professors P on P.id = C.Taught_by inner join Students S on C.id = S.Course_Enrolled where C.id in (select id from courses where Name like '%{search_string}%')"
        rows = cursor.execute(statement)
        result_from = 'Course'

    print('results from :',result_from)
    rows = list(rows)
    rows = [ {'Course_Name' : row[0], 'Professor Name': row[1],'Class Timings': row[2],'Info':row[3],'Student_Name':row[4] } for row in rows ]
    return rows
     
