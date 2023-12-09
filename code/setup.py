import sqlite3

connection = sqlite3.connect("Class-Project.db")

cursor = connection.cursor()

try:
    #because of the relations, drop the dependent table first
    cursor.execute("drop table Students")
    cursor.execute("drop table Courses")
    cursor.execute("drop table Professors")
except:
    pass

cursor.execute("CREATE TABLE Professors ( id INTEGER PRIMARY KEY ASC , Name varchar(255), Class_Time varchar(255))")
cursor.execute("CREATE TABLE Courses ( id INTEGER PRIMARY KEY ASC , Name varchar(255), Taught_by INTEGER NOT NULL, Code varchar(255), Information varchar(255), FOREIGN KEY (Taught_by) REFERENCES Professors(id))")
cursor.execute("CREATE TABLE Students ( id INTEGER PRIMARY KEY ASC , Name varchar(255), Course_Enrolled INTEGER NOT NULL, FOREIGN KEY (Course_Enrolled) REFERENCES Courses(id))")

professors_list = ['Gregory Deloizer' , 'Augustine Samba' , 'Xinyu Li' , 'Maha Allouzi','TBA']
class_timings = ['MW 5:30 to 6:45 PM' , 'TTR 2:15 to 3:30 PM' , 'TTR 3:45 to 5:00 PM' , 'MW 8:30 to 9:45 PM', 'NONE']

professors_list = [[professors_list[4] , class_timings[4]],[professors_list[0] , class_timings[0]] , [professors_list[0] , class_timings[3]] , [professors_list[1] , class_timings[1]] , [professors_list[2] , class_timings[2]] , [professors_list[3] , class_timings[0]] ]
for item in professors_list:
    print(item[0] , item[1])

for item in professors_list:
    query = f"insert into Professors ('Name','Class_Time') values ('{item[0]}' , '{item[1]}')"
    print(query)
    cursor.execute(query)


courses_list = [ ['ADSD' , 2, 'CS 63005','Advanced Database Systems Design'] ,['ADSD' ,3,  'CS 63006','Advanced Database Systems Design'] , ['ADD' ,4, 'CS 53305','Advanced Digital Design'] , ['IS' ,6, 'CS 57205','Information Security'] , ['DAA' ,5, 'CS 56101','Design and Analysis of Algorithms'] ]

for item in courses_list:
    query = f"insert into Courses ('Name','Taught_by','Code','Information') values ('{item[0]}' , {item[1]} , '{item[2]}' ,'{item[3]}')"
    print(query)
    cursor.execute(query)


students_list = [['John Doe' , 1] , ['Jane Doe' , 2] , ['Robert Jane' , 2] , ['Mike Hector' , 1] , ['Bear Ross',3] , ['Vincent Jacobs',4] , ['Branson Solis',5]]
for item in students_list:
    query = f"insert into Students ('Name','Course_Enrolled') values ('{item[0]}' , {item[1]})"
    print(query)
    cursor.execute(query)

connection.commit()
connection.close()
print("-----------------------------------------------------------------")