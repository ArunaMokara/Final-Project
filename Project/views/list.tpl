<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User and Orders</title>
</head>
<body>
    <h1>User and Orders</h1>
    
    <form action="/list" method="get">
        <label for="search">Search:</label>
        <input type="text" name="search" value="{{ search_keyword }}">
        <input type="submit" value="Search">
    </form>

    <table border="1">
        <thead>
            <tr>
                <th>User ID</th>
                <th>Username</th>
                <th>Email</th>
                <th>Order ID</th>
                <th>Product</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            % for row in user_order_list:
                <tr>
                    <td>{{ row['user_id'] }}</td>
                    <td>{{ row['username'] }}</td>
                    <td>{{ row['email'] }}</td>
                    <td>{{ row['order_id'] }}</td>
                    <td>{{ row['product'] }}</td>
                    <td>
                        <a href="/update/{{ row['user_id'] }}/{{ row['order_id'] }}">Update</a>
                        <a href="/delete/{{ row['user_id'] }}/{{ row['order_id'] }}">Delete</a>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
    
    <br>
    <a href="/add">Add User and Order</a>
</body>
</html>
