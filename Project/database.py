import dataset

db = dataset.connect('sqlite:///example.db')

def setup_database():
    try:
        db["users"].drop()
        db["orders"].drop()
    except:
        pass
    
    users_table = db["users"]
    orders_table = db["orders"]

    users_data = [
        {"username": "user1", "email": "user1@example.com"},
        {"username": "user2", "email": "user2@example.com"}
    ]

    orders_data = [
        {"product": "Laptop", "user_id": 1},
        {"product": "Mobile", "user_id": 2},
    ]

    users_table.insert_many(users_data, ensure=None)
    orders_table.insert_many(orders_data, ensure=None)



def get_users_and_orders():
    query = """
    SELECT users.id as user_id, users.username, users.email, orders.id as order_id, orders.product
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
    """
    result = db.query(query)
    rows = [dict(row) for row in result]
    
    return rows
    
def get_user_and_order_by_ids(user_id, order_id):
    query = f"""
    SELECT users.id as user_id, users.username, users.email, orders.id as order_id, orders.product
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
    WHERE users.id = {user_id} AND orders.id = {order_id}
    """
    result = db.query(query)
    user_order = None
    for row in result:
        user_order = dict(row)
        break
    return user_order

def add_user(username, email):
    return db["users"].insert({"username": username, "email": email})

def add_order(product, user_id):
    return db["orders"].insert({"product": product, "user_id": user_id})

def delete_user(user_id):
    db["users"].delete(id=user_id)

def delete_order(order_id):
    db["orders"].delete(id=order_id)

def update_user(user_id, username, email):
    db["users"].update({"id": user_id, "username": username, "email": email}, ['id'])

def update_order(order_id, product):
    db["orders"].update({"id": order_id, "product": product}, ['id'])


def search_users_and_orders(keyword):
    query = f"""
    SELECT users.id as user_id, users.username, users.email, orders.id as order_id, orders.product
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
    WHERE users.username LIKE '%{keyword}%' OR orders.product LIKE '%{keyword}%'
    """
    result = db.query(query)
    return [dict(row) for row in result]

