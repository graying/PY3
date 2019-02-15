from main_app import Post, db

# create database
db.create_all()

# insert data
db.session.add(Post("GOOD", "I AM GOOD"))
db.session.add(Post("WELL", "I AM LLLL"))
db.session.add(Post("EVIL", "Y're EVIL"))

# commit database
db.session.commit()
