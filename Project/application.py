from bottle import route, post, run, template, redirect, request
import database

database.setup_database()

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    keyword = request.query.get('search', '')
    if keyword:
        rows = database.search_users_and_orders(keyword)
    else:
        rows = database.get_users_and_orders()
    return template("list.tpl", user_order_list=rows, search_keyword=keyword)

@route("/add")
def get_add():
    return template("add_user_order.tpl")

@post("/add")
def post_add():
    username = request.forms.get("username")
    email = request.forms.get("email")
    product = request.forms.get("product")
    user_id = database.add_user(username, email)
    database.add_order(product, user_id)
    rows = database.get_users_and_orders()
    return template("list.tpl", user_order_list=rows, search_keyword='')
    

@route("/delete/<user_id:int>/<order_id:int>")
def get_delete(user_id, order_id):
    database.delete_user(user_id)
    database.delete_order(order_id)
    redirect("/list")

@route("/update/<user_id:int>/<order_id:int>")
def get_update(user_id, order_id):
    user_order = database.get_user_and_order_by_ids(user_id, order_id)
    return template("update_user_order.tpl", user_order=user_order)

@post("/update")
def post_update():
    user_id = request.forms.get("user_id")
    username = request.forms.get("username")
    email = request.forms.get("email")
    order_id = request.forms.get("order_id")
    product = request.forms.get("product")

    database.update_user(user_id, username, email)
    database.update_order(order_id, product)
    
    redirect("/list")

if __name__ == '__main__':
    run(host='localhost', port=8080)
