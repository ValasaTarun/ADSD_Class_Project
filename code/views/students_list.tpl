<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Students List</title>
</head>
<body>
    <h2> Students </h2>
    <hr/>
    <hr>
      <button><a href="/students/add">Add</a></button>
    <hr/>
    <table>
      <thead>
        <tr>
          <th>Student id</th>
          <th>Student Name</th>
          <th>Course Name</th>
          <th>Code</th>
        </tr>
      </thead>
    % for item in students_list:
      <tr>
        <td>{{str(item['Student id'])}}</td>
        <td>{{str(item['Student Name'])}}</td>
        <td>{{str(item['Course Name'])}}</td>
        <td>{{str(item['Code'])}}</td>
        <td><a href="/update_student/{{str(item['Student id'])}}">update</a></td>
        <td><a href="/delete_student/{{str(item['Student id'])}}">delete</a></td>
      </tr>
    % end
    </table>
    <hr/>
</body>
</html>