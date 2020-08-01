from flask import Blueprint, jsonify, g
from database import Session
from .model import Article
from utils import return_500_if_errors

blueprint = Blueprint('bleprint', __name__)

@blueprint.route("/add", methods=["POST"])
def add():
    new_model = Article(title="ggg!", length=55)
    g.session.add(new_model)
    g.session.commit()
    return "saved"