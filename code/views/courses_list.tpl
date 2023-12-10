<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Courses List</title>
</head>
<body>
    <h2> Courses </h2>
    <hr/>
    <table>
      <thead>
        <tr>
          <th>S No</th>
          <th>Course Name</th>
          <th>Professor Name</th>
          <th>Class Timings</th>
          <th>Code</th>
          <th>Information</th>
        </tr>
      </thead>
    % for item in courses_list:
      <tr>
        <td>{{str(item['id'])}}</td>
        <td>{{str(item['Course Name'])}}</td>
        <td>{{str(item['Professor Name'])}}</td>
        <td>{{str(item['Class Timings'])}}</td>
        <td>{{str(item['Code'])}}</td>
        <td>{{str(item['Information'])}}</td>
        <td><a href="/update/{{str(item['id'])}}">update</a></td>
        <td><a href="/delete/{{str(item['id'])}}">delete</a></td>
      </tr>
    % end
    </table>
    <hr/>
</body>
</html>