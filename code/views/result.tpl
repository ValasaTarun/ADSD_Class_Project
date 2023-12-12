<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Search Result</title>
</head>
<body>
    <h2 class="text-center">Search Result</h2>
    <br>
    % if results:
    <hr>
    <table class="table">
        <thead>
          <tr>
            <th>Course Name</th>
            <th>Course Information</th>
            <th>Professor Name</th>
            <th>Class Timings</th>
            <th>Student Name</th>
          </tr>
        </thead>
      % for item in results:
        <tr>
          <td>{{str(item['Course_Name'])}}</td>
          <td>{{str(item['Info'])}}</td>
          <td>{{str(item['Professor Name'])}}</td>
          <td>{{str(item['Class Timings'])}}</td>
          <td>{{str(item['Student_Name'])}}</td>
        </tr>
      % end
      </table>
     % end

     % if len(results) == 0:
        <h3 class="text-center">No Results</h3>
     % end
     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
</body>
</html>