import configparser

from mongoengine import Document, CASCADE, connect
from mongoengine.fields import StringField, ListField, ReferenceField

config = configparser.ConfigParser()
config.read('config.ini')
mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')

connect(host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@pasichniuk.qpmb3z9.mongodb.net/{db_name}?retryWrites=true&w=majority", ssl=True)


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()
   
    
class Quote(Document):
    tags = ListField()
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()

