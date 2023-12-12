<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Course</title>
</head>
<body>
    <h2>
        Add Course
    </h2>
    <hr>
    <form action="/add_course" method="post">
        <p>Course Name : <input type="text" name="Name"></p>
        <label for="cars">Choose a Professor:</label>
        <select name="Profid" id="">
        % for item in professors_list:
            <option value="{{str(item['id'])}}">{{str(item['Professor Name']) + ' ' + str(item['Class Timings'])}}</option>
            % end
        </select>
        <p>Code : <input type="text" name="Code"></p>
        <p>Information : <input type="text" name="Info"></p>
        <p><button type="submit">Submit</button></p>
    </form>
</body>
</html>