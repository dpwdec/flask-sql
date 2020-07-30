from flask import Flask
from database import Base, db
from articles.model import Article
from articles.controller import blueprint as articles_controller

Base.metadata.create_all(db)

app = Flask(__name__)
app.register_blueprint(articles_controller, url_prefix="/articles")

if __name__ == "__main__":
    app.run(debug=True)
