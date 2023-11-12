"""
Define the REST verbs relative to the FinancialGoal route.
"""

import math
from http import HTTPStatus

from flask import jsonify, make_response
from flask_restful import Resource, request


class FinancialGoalResource(Resource):
    """Verbs relative to the FinancialGoal route"""

    @staticmethod
    def post():
        """Returns the amount of months to reach the financial goal"""
        if request.json is None:
            return make_response(
                jsonify(
                    {
                        "months": None,
                        "message": "Request should include a JSON in the body.",
                    }
                ),
                HTTPStatus.BAD_REQUEST,
            )
        if request.json["monthly_savings"] <= 0:
            return make_response(
                {"months": None, "message": "Monthly savings should be positive."},
                HTTPStatus.BAD_REQUEST,
            )
        if request.json["goal"] <= 0:
            return make_response(
                {"months": None, "message": "Goal should be positive."},
                HTTPStatus.BAD_REQUEST,
            )

        months: int = math.ceil(request.json["goal"] / request.json["monthly_savings"])
        return make_response(
            {
                "months": months,
                "message": f"It will take {months} months to reach your goal.",
            },
            HTTPStatus.OK,
        )
