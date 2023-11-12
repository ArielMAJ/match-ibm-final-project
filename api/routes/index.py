"""
Defines the blueprint for the index page.
"""
from api.resources import IndexResource
from flask import Blueprint
from flask_restful import Api

INDEX_BLUEPRINT = Blueprint("index", __name__)
Api(INDEX_BLUEPRINT).add_resource(IndexResource, "/")
