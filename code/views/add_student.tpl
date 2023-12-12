<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Student</title>
</head>
<body>
    <form action="/add_student" method="post">
        <p>Student Name : <input type="text" name="Name"></p>
        <label >Choose a Course:</label>
        <select name="Courseid" id="">
        % for item in courses_list:
            <option value="{{str(item['id'])}}">{{str(item['Course Name']) + ' ' + str(item['Code'])}}</option>
            % end
        </select>
        <p><button type="submit">Submit</button></p>
    </form>
</body>
</html>