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
        if not (monthly_savings := request.json.pop("monthly_savings", None)):
            return make_response(
                {
                    "months": None,
                    "message": "Request should include the monthly savings.",
                },
                HTTPStatus.BAD_REQUEST,
            )
        if not (goal := request.json.pop("goal")):
            return make_response(
                {"months": None, "message": "Request should include the goal."},
                HTTPStatus.BAD_REQUEST,
            )
        try:
            monthly_savings = float(monthly_savings)
            goal = float(goal)
        except ValueError:
            return make_response(
                {
                    "months": None,
                    "message": "Monthly savings and goal should be numbers.",
                },
                HTTPStatus.BAD_REQUEST,
            )
        if monthly_savings <= 0:
            return make_response(
                {"months": None, "message": "Monthly savings should be positive."},
                HTTPStatus.BAD_REQUEST,
            )
        if goal <= 0:
            return make_response(
                {"months": None, "message": "Goal should be positive."},
                HTTPStatus.BAD_REQUEST,
            )

        months: int = math.ceil(goal / monthly_savings)
        return make_response(
            {
                "months": months,
                "message": f"It will take {months} months to reach your goal.",
            },
            HTTPStatus.OK,
        )
