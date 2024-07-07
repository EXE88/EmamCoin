from flask import Flask , jsonify , request
import sqlite3

#setup
app = Flask(__name__)
connection = sqlite3.connect('database.sqlite3')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, coin INTEGER NOT NULL);")
connection.commit()
cursor.close()
connection.close()

#little shorcut for createing new connection 
def new_connection():
  connection = sqlite3.connect('database.sqlite3')
  cursor = connection.cursor()
  return connection , cursor

#user create route
@app.route('/user/create/<string:username>', methods=['POST'])
def create_user(username):
    connection , cursor = new_connection()
    try:
        cursor.execute(f"INSERT INTO Users(username, coin) VALUES('{username}', 0)")
        connection.commit()
        return jsonify({'info': "user created successfully!"}), 200
    except sqlite3.Error as error:
        return jsonify({'error': str(error)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/user/coin/add/<string:username>/<int:value>' , methods=['POST'])
def add_coin(username,value):
    connection , cursor = new_connection()
    try:
        user_id = cursor.execute(f"""
                                 SELECT user_id 
                                 FROM Users 
                                 WHERE username="{username}"
                                 """)
        user_id = user_id.fetchone()
        if user_id is not None:
            cursor.execute(f"UPDATE Users SET coin = coin+{value} WHERE user_id={user_id[0]}")
            connection.commit()
            return jsonify({"info":"user coins updated successfully!"}) , 200
        return jsonify({"error":"user not found!"}) , 404
    except sqlite3.Error as error:
        return jsonify({"error":error}) , 500
    finally:
        cursor.close()
        connection.close()

@app.route('/user/coin/get/<string:username>' , methods=['GET'])
def get_coin_count(username):
    connection , cursor = new_connection()
    try:
        coin_count = cursor.execute(f'SELECT coin FROM Users WHERE username="{username}"').fetchone()
        if coin_count is not None:
            return jsonify({'data':coin_count}) , 200
        return jsonify({"error":"user not found"}) , 404
    except sqlite3.Error as  error:
        return jsonify({"error":error}) , 500
    finally:
        cursor.close()
        connection.close()


    
#run app
if __name__=="__main__":
    app.run()