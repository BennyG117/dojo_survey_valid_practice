from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class User:
    DB = 'dojo_survey_schema_valid'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#if the following remains true to the end then the data is valid
    @staticmethod
    def validate_dojo(new_dojo):
        is_valid = True
        if len(new_dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if (new_dojo['location']) == 'Tucson':
            flash("Choose a different location.")
            is_valid = False
        if (new_dojo['language']) == 'Java':
            flash("should probably be C#.")
            is_valid = False
        if len(new_dojo['comment']) < 1:
            flash("Language must be at least 1 character.")
            is_valid = False
        return is_valid

    # method to save & add new Dojo (return dojo id)
    @classmethod
    def save_submission(cls, data):
        query = """INSERT INTO dojos (name, location, language, comment)
        VALUES (%(name)s, %(location)s, %(language)s, %(comment)s) ;
        """

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    #method to get one dojo
    @classmethod
    def get_one(cls, data):
        query = """SELECT * 
        FROM dojos
        WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        singleDojo = cls(results[0])
        
        return singleDojo
    

