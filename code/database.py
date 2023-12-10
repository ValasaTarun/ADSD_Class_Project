import sqlite3

connection = sqlite3.connect("Class-Project.db")

def get_courses(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select C.id, C.Name as Course_Name , P.Name as Professor_Name , P.Class_Time, C.Code,C.Information   from courses C join Professors P on P.id = C.Taught_by")
    else:
        rows = cursor.execute(f"select C.id, C.Name as Course_Name , P.Name as Professor_Name , P.Class_Time, C.Code ,C.Information  from courses C join Professors P on P.id = C.Taught_by where C.id = {id};")
    rows = list(rows)
    rows = [ {'id' : row[0], 'Course Name': row[1],'Professor Name': row[2],'Class Timings': row[3],'Code': row[4],'Information':row[5]} for row in rows ]
    return rows

def get_professors(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select id, Name, Class_Time from professors")
    else:
        rows = cursor.execute(f"select id, Name, Class_Time from professors where id = {id}")
    rows = list(rows)
    print(rows , 'from get prof')
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
        rows = cursor.execute("select S.id as Student_id , C.Name as Course_Name , S.Name as Student_Name,  C.Code from courses C inner join Students S on C.id = S.Course_Enrolled")
    else:
        rows = cursor.execute(f"select S.id as Student_id  , C.Name as Course_Name , S.Name as Student_Name , C.Code from courses C inner join Students S on C.id = S.Course_Enrolled where S.id = {id}")
    rows = list(rows)
    rows = [ {'Student id' : row[0], 'Course Name': row[1],'Student Name': row[2] , 'Code': row[3]} for row in rows ]
    return rows


    
