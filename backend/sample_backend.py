from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import random
import string

app = Flask(__name__) 
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}


@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd["id"] = randomID()
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp 

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   userToDelete = findUser(id)
   if request.method == 'DELETE':
      users['users_list'].remove(userToDelete)
      resp = jsonify(success=True)
      resp.status_code = 204 #optionally, you can always set a response code. 
      # 200 is the default code for a normal respo
      return resp
   elif userToDelete == {}:
      resp = jsonify(success=False)
      resp.status_code = 404
   return jsonify(success=False)
   
def findUser(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users

def randomID():
   id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(6)])
   return id 