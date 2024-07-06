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
@app.route('/user/create/<string:username>/', methods=['POST'])
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
    
#run app
if __name__=="__main__":
    app.run()