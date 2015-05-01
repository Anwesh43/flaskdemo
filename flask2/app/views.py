from app import app
from flask import render_template
from app import Post
@app.route('/')
def index():
    return "Hello World";

@app.route('/dogs')
def getDogs():
    dogs = ["Labrador Retriever","Beagle","German Shepherd Dog","Poodle","Bulldog","Rottweiler"];
    return ",".join(dogs);

@app.route('/fruits')
def getFruits():
    fruits = ["apple","pear","pineapple","jackfruit"];
    return ','.join(fruits);

@app.route('/properPage')
def getProperPage():
    user = {"name":"Brit","age":"22","id":"1"};
    return render_template('index.html',headerText="index",title="Proper",user=user);

@app.route('/checkifier')
def getChecker():
    return render_template('checker.html',headerText="Checker",user = {"name":"Anwesh","age":23});

@app.route('/post')
def getPosts():
    post1 = Post.Post('Anwesh',22);
    post2 = Post.Post('Broto',23);
    post3 = Post.Post('Groto',24);
    post4 = Post.Post('Hrito',25);
    post5 = Post.Post('Lrito',26);
    posts = [post1,post2,post3,post4,post5];
    return render_template('posts.html',headerText="Posts",posts=posts);



