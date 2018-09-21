from mongoengine import Document, StringField, IntField

class Review(Document):
    author = StringField()
    song = StringField()
    artist = StringField()
    content = StringField()
