from flask import Blueprint, jsonify
from database import session
from .model import Article

blueprint = Blueprint('bleprint', __name__)

@blueprint.route("/add")
def add():
    new_model = Article(title="A lovely day out", length=55)
    session.add(new_model)
    session.commit()
    return "saved"