<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Home Page</title>
</head>
<body>
    <h2 class="text-center"> Home Page </h2>

    <div class="text-center">

        <a class="btn btn-primary mt-2" href="/professors">Professors</a>
        <br>
            <a class="btn btn-primary mt-2" href="/courses">Courses</a>
        <br>
            <a class="btn btn-primary mt-2"href="/students">Students</a>
    </div>
       
    
    <br>
    <hr>
    <div class="container text-center">
        <form action="/search" method="post">
            <label for="">Search : </label>
            <input type="text" name="value" id="" required>
            <br><br>
            <label for="">Search in </label>
            <select name="type" id="">
                <option value="Professor">Professor</option>
                <option value="Course">Course</option>
                <option value="Student">Student</option>
            </select>
            <br><br>
            <p>
                <button type="submit">Submit</button>
            </p>
        </form>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>