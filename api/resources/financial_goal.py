"""
Define the REST verbs relative to the FinancialGoal route.
"""

import math
from http import HTTPStatus

from flask import Request, Response, jsonify, make_response, render_template
from flask_restful import Resource, request


class FinancialGoalResource(Resource):
    """Verbs relative to the FinancialGoal route"""

    @staticmethod
    def post():
        """Returns the amount of months to reach the financial goal"""
        response = FinancialGoalResource.get_response(request)
        if request.is_json:
            return response

        return make_response(
            render_template("index.html", message=response.json.pop("message")),
            HTTPStatus.OK,
            {"Content-Type": "text/html; charset=utf-8"},
        )

    @staticmethod
    def get_response(request: Request) -> Response:
        """Returns the response for the POST request"""
        data = request.json if request.is_json else request.form
        if not data:
            return make_response(
                jsonify(
                    {
                        "months": None,
                        "message": "É esperado submissão de formulário ou um JSON.",
                    }
                ),
                HTTPStatus.BAD_REQUEST,
            )

        if not (goal := data.get("goal")):
            return make_response(
                {"months": None, "message": 'Incluir "Meta Financeira".'},
                HTTPStatus.BAD_REQUEST,
            )

        if not (monthly_savings := data.get("monthly_savings", None)):
            return make_response(
                {
                    "months": None,
                    "message": 'Incluir "Economia Mensal".',
                },
                HTTPStatus.BAD_REQUEST,
            )
        try:
            monthly_savings = float(monthly_savings)
            goal = float(goal)
        except ValueError:
            return make_response(
                {
                    "months": None,
                    "message": "Economia Mensal e Meta Financeira devem ser números.",
                },
                HTTPStatus.BAD_REQUEST,
            )
        if monthly_savings <= 0:
            return make_response(
                {
                    "months": None,
                    "message": "Economia Mensal deve ser um valor numérico positivo.",
                },
                HTTPStatus.BAD_REQUEST,
            )
        if goal <= 0:
            return make_response(
                {
                    "months": None,
                    "message": '"Meta Financeira" deve ser um valor numérico positivo.',
                },
                HTTPStatus.BAD_REQUEST,
            )

        months: int = FinancialGoalResource.caculate_months(goal, monthly_savings)

        return make_response(
            jsonify(
                {
                    "months": months,
                    "message": (
                        f"Levará {months} meses para atingir sua Meta Financeira."
                    ),
                }
            ),
            HTTPStatus.OK,
        )

    @staticmethod
    def caculate_months(goal: int | float, monthly_savings: int | float) -> int:
        return math.ceil(goal / monthly_savings)
