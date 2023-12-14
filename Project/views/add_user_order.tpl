<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add User and Order</title>
</head>
<body>
    <h1>Add User and Order</h1>
    <form method="post" action="/add">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <br>
        <label for="product">Product:</label>
        <input type="text" name="product" required>
        <br>
        <input type="submit" value="Add">
    </form>
    <br>
    <a href="/list">Back to List</a>
</body>
</html>
