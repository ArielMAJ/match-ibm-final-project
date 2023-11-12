"""
Define the REST verbs relative to the index page.
"""

from flask import make_response, render_template
from flask_restful import Resource


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
