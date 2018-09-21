from mongoengine import Document, StringField, IntField

class User(Document):
    name = StringField()
    email = StringField()
    user_name = StringField()
    password = StringField()
