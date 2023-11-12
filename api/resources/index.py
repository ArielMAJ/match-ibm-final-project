"""
Define the REST verbs relative to the index page.
"""

from flask import make_response, render_template
from flask_restful import Resource, request


class IndexResource(Resource):
    """Verbs relative to the index page"""

    @staticmethod
    def get():
        """Returns the index page"""
        return make_response(
            render_template("index.html"),
            200,
            {"Content-Type": "text/html; charset=utf-8"},
        )

    @staticmethod
    def post():
        """Returns the index page with data"""
        return make_response(
            render_template("index.html", message=request.json.pop("message")),
            200,
            {"Content-Type": "text/html; charset=utf-8"},
        )
