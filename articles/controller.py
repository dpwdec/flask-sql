from flask import Blueprint, jsonify, g
from database import Session
from .model import Article
from utils import return_500_if_errors
import random
import string

blueprint = Blueprint('bleprint', __name__)

@blueprint.route("/add", methods=["GET"])
def add():
    new_model = Article(title=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]), length=55)
    g.session.add(new_model)
    g.session.commit()
    return "saved"