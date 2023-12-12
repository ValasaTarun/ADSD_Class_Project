<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Course Details</title>
</head>
<body>
    <form action="/course/update" method="post">
        <input type="hidden" name="id" value="{{str(item['id'])}}"/>
        <p>Name : <input name="Name" value="{{item['Course Name']}}"/></p>
        <label for="cars">Choose a Professor:</label>
        <select name="Profid" id="">
            % for prof in professors_list:
                <option value="{{str(prof['id'])}}" {{!'selected="selected"' if str(item['Profid']) == str(prof['id']) else ""}}>{{str(prof['Professor Name']) + ' ' + str(prof['Class Timings'])}}</option>
            % end
        </select>
        <p>Code : <input type="text" name="Code" value="{{item['Code']}}"></p>
        <p>Information : <input type="text" name="Info" value="{{item['Information']}}"></p>
        <p>
            <button type="submit">Submit</button>
        </p>
    </form>
</body>
</html>