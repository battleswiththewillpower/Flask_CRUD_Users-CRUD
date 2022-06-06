# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# Naming convenction to use for mutiple projects. just change the string name to the proper scema
DATABASE = 'user_dashboard_schema'

# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.email= data['email']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def create(cls, data:dict):
        #query the string
        query = "INSERT INTO users (name, email, description) VALUES (%(name)s, %(email)s, %(description)s);"
        #contact the database
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id

    #want to be able to update whichever user we select by id thro the DB since each id is unique to the user
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    #edit the user and update the information
    @classmethod
    def update(cls, data):
        # query = "UPDATE users SET name=%(name)s, email=%(email)s, description=%(description)s, updated_at=NOW() WHERE id = %(id)s;"
        # make sure theres no spaces inbetwwen each comma
        query = "UPDATE users SET name=%(name)s,email=%(email)s,description=%(description)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # checking to make sure there arent any errors
        if results:
        # Create an empty list to append our instances of friends
            users = []
            # Iterate over the db results and create instances of friends with cls.
            for user in results:
                users.append( cls(user) )
            return users
        return False