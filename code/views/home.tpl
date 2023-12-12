<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
</head>
<body>
    <h2> Home Page </h2>
    <button>
        <a href="/professors">Professors</a>
    </button>
    <br>
    <button>
        <a href="/courses">Courses</a>
    </button>
    <br>
    <button>
        <a href="/students">Students</a>
    </button>
    <br>
    <hr>
    <form action="/search">
        <label for="">Search in </label>
        <select name="type" id="">
            <option value="Professor">Professor</option>
            <option value="Course">Course</option>
            <option value="Student">Student</option>
        </select>
    </form>
</body>
</html>