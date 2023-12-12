<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Student Details</title>
</head>
<body>
    <h2>
        Update Student
    </h2>
    <hr>
    <form action="/student/update" method="post">
        <input type="hidden" name="id" value="{{str(item['Student id'])}}"/>
        <p>Name : <input name="Name" value="{{item['Student Name']}}"/></p>
        <label for="cars">Choose Course:</label>
        <select name="Courseid" id="">
            % for course in courses_list:
                <option value="{{str(course['id'])}}" {{!'selected="selected"' if str(item['Courseid']) == str(course['id']) else ""}}>{{str(course['Course Name']) + ' ' + str(course['Code'])}}</option>
            % end
        </select>
        <p>
            <button type="submit">Submit</button>
        </p>
    </form>
</body>
</html>