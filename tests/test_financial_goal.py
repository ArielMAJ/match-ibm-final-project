"""Test `plant` endpoints"""

import json
import logging
from http import HTTPStatus

import pytest

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "goal,monthly_savings,result,status_code",
    [
        (4, 2, 2, HTTPStatus.OK),
        (8, 7, 2, HTTPStatus.OK),
        (100, 10, 10, HTTPStatus.OK),
        (100, 11, 10, HTTPStatus.OK),
        (100, 9, 12, HTTPStatus.OK),
        (100, 10.0, 10, HTTPStatus.OK),
        (100.5, 10, 11, HTTPStatus.OK),
        (100.5, 10.5, 10, HTTPStatus.OK),
        (100, 10.5, 10, HTTPStatus.OK),
        ("4", 2, 2, HTTPStatus.OK),
        ("8", 7, 2, HTTPStatus.OK),
        ("100", 10, 10, HTTPStatus.OK),
        ("100", 11, 10, HTTPStatus.OK),
        ("100", 9, 12, HTTPStatus.OK),
        ("100.5", 10, 11, HTTPStatus.OK),
        ("100.5", 10.5, 10, HTTPStatus.OK),
        ("100", 10.5, 10, HTTPStatus.OK),
        (4, "2", 2, HTTPStatus.OK),
        (8, "7", 2, HTTPStatus.OK),
        (100, "10", 10, HTTPStatus.OK),
        (100, "11", 10, HTTPStatus.OK),
        (100, "9", 12, HTTPStatus.OK),
        (100.5, "10", 11, HTTPStatus.OK),
        (100.5, "10.5", 10, HTTPStatus.OK),
        (100, "10.5", 10, HTTPStatus.OK),
        ("4", "2", 2, HTTPStatus.OK),
        ("8", "7", 2, HTTPStatus.OK),
        ("100", "10", 10, HTTPStatus.OK),
        ("100", "11", 10, HTTPStatus.OK),
        ("100", "9", 12, HTTPStatus.OK),
        ("100.5", "10", 11, HTTPStatus.OK),
        ("100.5", "10.5", 10, HTTPStatus.OK),
        ("100", "10.5", 10, HTTPStatus.OK),
        (100, 0, None, HTTPStatus.BAD_REQUEST),
        (100, -1, None, HTTPStatus.BAD_REQUEST),
        (0, 10, None, HTTPStatus.BAD_REQUEST),
        (-1, 10, None, HTTPStatus.BAD_REQUEST),
        (None, 10, None, HTTPStatus.BAD_REQUEST),
        (100, None, None, HTTPStatus.BAD_REQUEST),
        (None, None, None, HTTPStatus.BAD_REQUEST),
        ("", 10, None, HTTPStatus.BAD_REQUEST),
        (100, "", None, HTTPStatus.BAD_REQUEST),
        ("", "", None, HTTPStatus.BAD_REQUEST),
        ("", None, None, HTTPStatus.BAD_REQUEST),
        (None, "", None, HTTPStatus.BAD_REQUEST),
        (None, "A", None, HTTPStatus.BAD_REQUEST),
        ("A", None, None, HTTPStatus.BAD_REQUEST),
        ("A", "A", None, HTTPStatus.BAD_REQUEST),
        ("A", 10, None, HTTPStatus.BAD_REQUEST),
        (100, "A", None, HTTPStatus.BAD_REQUEST),
    ],
)
def test_financial_goal(test_client, goal, monthly_savings, result, status_code):
    response = test_client.post(
        "/",
        content_type="application/json",
        data=json.dumps({"goal": goal, "monthly_savings": monthly_savings}),
    )

    assert response.status_code == status_code

    response_json = json.loads(response.data.decode("utf-8"))
    assert response_json["months"] == result
