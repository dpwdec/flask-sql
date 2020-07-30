from flask import Blueprint, jsonify, g
from database import Session
from .model import Article

blueprint = Blueprint('bleprint', __name__)

@blueprint.route("/add")
def add():
    new_model = Article(title="goodbye", length=55)
    g.session.add(new_model)
    g.session.commit()
    return "saved"