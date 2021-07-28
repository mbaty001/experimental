from flask import jsonify, Flask, make_response, abort
import json
import sqlite3

from flask.globals import request

app = Flask(__name__)

DB_FILE = "cloud-native.db"

@app.errorhandler(404)
def resource_not_found(error):
    return make_response(jsonify({'error': 'Resource not found!'}), 404)

@app.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(409)
def duplicate_entry(error):
    return make_response(jsonify({'error': 'Duplicate entry'}), 409)

@app.route("/api/v1/info")
def home_index():
    conn = sqlite3.connect(DB_FILE)
    print ("DB file {} opened successfully".format(DB_FILE))
    api_list = []
    cursor = conn.execute("SELECT buildtime, version, methods, links from apirelease")
    for row in cursor:
        a_dict = {}
        a_dict['version'] = row[0]
        a_dict['buildtime'] = row[1]
        a_dict['methods'] = row[2]
        a_dict['links'] = row[3]
        api_list.append(a_dict)
    conn.close()

    return jsonify({'api_version': api_list}), 200

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return list_users()

@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return list_users(user_id)

def list_users(user_id=None):
    conn = sqlite3.connect(DB_FILE)
    print ("DB file {} opened successfully".format(DB_FILE))
    user_list = []
    if user_id:
        cursor = conn.execute("SELECT * from users where id=?", (user_id,))
    else:
        cursor = conn.execute("SELECT username, full_name, email, password, id from users")

    for row in cursor:
        a_dict = {}
        a_dict['username'] = row[0]
        a_dict['name'] = row[1]
        a_dict['email'] = row[2]
        a_dict['password'] = row[3]
        a_dict['id'] = row[4]
        user_list.append(a_dict)
    conn.close()

    return jsonify({'user_list': user_list})

def add_user(new_user):
    conn = sqlite3.connect(DB_FILE)
    print ("DB file {} opened successfully".format(DB_FILE))
    ret = "None"

    cursor = conn.cursor()
    cursor.execute("SELECT * from users where username=? or email=?",
                   (new_user['username'], new_user['email']))
    data = cursor.fetchall()
    if len(data) != 0:
        abort(409)
    else:
        cursor.execute("INSERT INTO users (username, email, password, full_name) values(?, ?, ?, ?)",
        (new_user['username'], new_user['email'], new_user['password'], new_user['name']))
        conn.commit()

        ret = "Success"
    conn.close()
    return ret

def del_user(del_user): 
    conn = sqlite3.connect(DB_FILE) 
    print ("DB file {} opened successfully".format(DB_FILE))
    ret = "None"

    cursor=conn.cursor() 
    cursor.execute("SELECT * from users where username=? ", (del_user,)) 
    data = cursor.fetchall() 

    if len(data) == 0: 
        abort(404) 
    else: 
        cursor.execute("delete from users where username==?", (del_user,)) 
        conn.commit() 
        ret = "Success" 
    return ret

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or\
       not 'username' in request.json or\
       not 'email' in request.json or\
       not 'password' in request.json:
       abort(400)
    user = {
        'username': request.json['username'],
        'email': request.json['email'],
        'name': request.json['name'],
        'password': request.json['password']
    }
    return jsonify({'status': add_user(user)}), 201

@app.route('/api/v1/users', methods=['DELETE'])
def delete_user():
    if not request.json or\
       not 'username' in request.json:
       abort(400)
    user = request.json['username']
    return jsonify({'status': del_user(user)}), 200

if __name__ == "__main__": 
     app.run(host='0.0.0.0', port=5000, debug=True)