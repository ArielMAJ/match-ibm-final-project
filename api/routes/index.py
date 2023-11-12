"""
Defines the blueprint for the index page.
"""
from flask import Blueprint
from flask_restful import Api
from resources import IndexResource

INDEX_BLUEPRINT = Blueprint("index", __name__)
Api(INDEX_BLUEPRINT).add_resource(IndexResource, "/")
