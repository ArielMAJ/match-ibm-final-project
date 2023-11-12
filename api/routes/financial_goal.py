"""
Defines the blueprint for the FinancialGoal route.
"""
from api.resources import FinancialGoalResource
from flask import Blueprint
from flask_restful import Api

FINANCIAL_GOAL_BLUEPRINT = Blueprint("financial_goal", __name__)
Api(FINANCIAL_GOAL_BLUEPRINT).add_resource(FinancialGoalResource, "/goal/")
