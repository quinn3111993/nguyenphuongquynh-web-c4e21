import mongoengine

#mongodb://<admin>:<c4e123456>@ds157762.mlab.com:57762/c4e21-blog

host = "ds157762.mlab.com"
port = 57762
db_name = "c4e21-blog"
user_name = "admin"
password = "c4e123456"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())