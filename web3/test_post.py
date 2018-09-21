import mlab
from post import Post

#1. Connect
mlab.connect()

#2. Create data
# p = Post(title='C4E21', author='Quinn', content='Sap den project roi', likes=15)
# print(p.title)
# print(p.content)
# print(p.author)
# print(p.likes)

#3. Write data
# p.save()

def test_load_data():
    #2. Load all documents
    all_posts = Post.objects()

    #3. Print all documents
    for post in all_posts:
        print(post.title)
        print(post.content)
        print(post.author)
        print('----------')

def delete_one_data(post_id):
    #1. Get document
    post = Post.objects().with_id(post_id)

    #2. Delete document
    if post is None:
        print('Post not found')
    else:
        post.delete()

def update_one(post_id, new_title):
    #1. Get document
    post = Post.objects().with_id(post_id)

    #2. Update
    if post is None:
        print('Post not found')
    else:
        #Slug
        post.update(set__title=new_title)

update_one('5b9cd22ff4fba09861ab7003', 'New new title')