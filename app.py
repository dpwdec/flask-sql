from flask import Flask, g
from database import Base, db, Session
from articles.model import Article
from articles.controller import blueprint as articles_controller

Base.metadata.create_all(db)

app = Flask(__name__)
app.register_blueprint(articles_controller, url_prefix="/articles")

@app.before_request
def before():
    g.session = Session()

@app.after_request
def after(response):
    g.session.close()
    return response

if __name__ == "__main__":
    app.run(debug=True)
