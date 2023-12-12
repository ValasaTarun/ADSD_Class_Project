<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Professor Details</title>
</head>
<body><h2>
        Update Professor
    </h2>
    <hr>
    <form action="/professors/update" method="post">
        <input type="hidden" name="id" value="{{str(item['id'])}}"/>
        <p>Name : <input name="Name" value="{{item['Professor Name']}}"/></p>
        <p>Class Timings : <input name="Class_Time" value="{{item['Class Timings']}}"/></p>
        <p>
            <button type="submit">Submit</button>
        </p>
    </form>
</body>
</html>