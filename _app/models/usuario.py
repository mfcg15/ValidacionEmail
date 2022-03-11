from _app.config.connection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.correo = data['correo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios (correo,created_at,updated_at) VALUES (%(correo)s,NOW(),NOW());"
        return connectToMySQL('esquema_validacion').query_db( query, data)

    @staticmethod
    def validate_user(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['correo']):
            flash("Email is not valid!")
            is_valid = False
        return is_valid
    
    @staticmethod
    def is_exists_email(correo):
        is_valid = True
        if  correo == 1:
            flash("Email already exists!")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT id,correo, date_format(created_at,'%e/%m/%y %l:%i %p') as fecha FROM usuarios"
        results = connectToMySQL('esquema_validacion').query_db(query)
        usuario = []
        for i in results:
            usuario.append(i)
        return usuario
    
    @classmethod
    def search_email(cls, data):
        query = "SELECT correo FROM usuarios where correo = %(correo)s"
        result = connectToMySQL('esquema_validacion').query_db(query,data)
        return len(result)
    
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM usuarios where id =  %(id)s;"
        return connectToMySQL('esquema_validacion').query_db(query,data)
    

