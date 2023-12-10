<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professors List</title>
</head>
<body>
    <h2> Professors </h2>
    <hr>
    <button><a href="/professors/add">Add</a></button>
    <hr/>
    <table>
      <thead>
        <tr>
          <th>S No</th>
          <th>Professor Name</th>
          <th>Class Timings</th>
        </tr>
      </thead>
    % for item in professors_list:
      <tr>
        <td>{{str(item['id'])}}</td>
        <td>{{str(item['Professor Name'])}}</td>
        <td>{{str(item['Class Timings'])}}</td>
        <td><a href="/update_prof/{{str(item['id'])}}">update</a></td>
        <td><a href="/delete_prof/{{str(item['id'])}}">delete</a></td>
      </tr>
    % end
    </table>
    <hr/>
</body>
</html>