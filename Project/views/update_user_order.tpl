<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update User and Order</title>
</head>
<body>
    <h1>Update User and Order</h1>
    
    <form action="/update" method="post">
        <input type="hidden" name="user_id" value="{{ user_order['user_id'] }}">
        <label for="username">Username:</label>
        <input type="text" name="username" value="{{ user_order['username'] }}" required>
        
        <label for="email">Email:</label>
        <input type="email" name="email" value="{{ user_order['email'] }}" required>
        
        <label for="order_id">Order ID:</label>
        <input type="text" name="order_id" value="{{ user_order['order_id'] }}" readonly>
        
        <label for="product">Product:</label>
        <input type="text" name="product" value="{{ user_order['product'] }}" required>
        
        <input type="submit" value="Update">
    </form>
    
    <br>
    <a href="/list">Back to List</a>
</body>
</html>
