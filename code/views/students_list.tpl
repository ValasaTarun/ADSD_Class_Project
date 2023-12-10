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
    <table>
      <thead>
        <tr>
          <th>Student id</th>
          <th>Course Name</th>
          <th>Student Name</th>
          <th>Code</th>
        </tr>
      </thead>
    % for item in students_list:
      <tr>
        <td>{{str(item['Student id'])}}</td>
        <td>{{str(item['Course Name'])}}</td>
        <td>{{str(item['Student Name'])}}</td>
        <td>{{str(item['Code'])}}</td>
        <td><a href="/update/{{str(item['Student id'])}}">update</a></td>
        <td><a href="/delete/{{str(item['Student id'])}}">delete</a></td>
      </tr>
    % end
    </table>
    <hr/>
</body>
</html>