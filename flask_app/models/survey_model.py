from flask_app.config.mysqlconnection import connectToMySQL

#add class, def __init__, add

class User:
    DB = 'dojo_survey_schema_valid'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']