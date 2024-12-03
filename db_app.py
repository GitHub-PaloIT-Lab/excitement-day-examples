from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_restx import Api, Resource, fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


api = Api(app, version='1.0', title='User API',
         description='A simple User API with a SQL Injection vulnerability')


ns = api.namespace('users', description='User operations')


user_model = api.model('User', {
   'id': fields.Integer(readOnly=True, description='The user unique identifier'),
   'name': fields.String(required=True, description='The user name')
})


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50))


def insert_example_users():
   if User.query.count() == 0:
       # Only insert if the table is empty to avoid duplicate entries on reload
       db.session.add(User(id=1, name="John Doe"))
       db.session.add(User(id=2, name="Jane Smith"))
       db.session.add(User(id=3, name="Alice Johnson"))
       db.session.commit()


@app.before_request
def create_tables_and_insert_initial_data():
   db.create_all()
   insert_example_users()


@ns.route('/<string:id>')
@ns.response(404, 'User not found')
@ns.param('id', 'The user identifier')
class UserResource(Resource):
   @ns.doc('get_user')
   @ns.marshal_with(user_model)
   def get(self, id):
       """Fetch a user given its identifier"""


       try:
           # Use parameterized query to prevent SQL injection
           query = text("SELECT * FROM user WHERE id = :id")

           # Execute the safe query with parameter
           result = db.session.execute(query, {'id': id})
           user = result.fetchall()

           if user:
               return user
           else:
               api.abort(404)
       except Exception as e:
           # Handle the exception here
           print(f"An error occurred: {str(e)}")
           api.abort(500, f"An error occurred: {str(e)}")


# Serve the OpenAPI spec at /api-spec
@app.route('/api-spec')
def api_spec():
   return jsonify(api.__schema__)


if __name__ == '__main__':
   with app.app_context():
       db.create_all()
   app.run(debug=True, port=4000)
