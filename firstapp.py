#import flask
from flask import Flask

#create an instance(app)
app=Flask(__name__)

#Route(End point defined as start '@')
@app.route("/")

# method function
def sample():
    return "<center><h1>Welcome S16 Students To learn Flask</h1></center>"

if __name__ == '__main__':
    app.run()