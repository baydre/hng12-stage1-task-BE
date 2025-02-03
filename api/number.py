"""
"""
from flask import Blueprint, request, jsonify
from api.helper import is_prime, is_perfect,is_armstrong, sum_of_digits, fetch_fun_fact

# Create blueprint for number API
number_api = Blueprint('number', __name__)

# Flask API route
@number_api.route("/api/classify-number", methods=["GET"])
def classify_number():
    number = request.args.get("number")

    # Validate input
    if number is None or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)

    # Compute properties
    prime = is_prime(number)
    perfect = is_perfect(number)
    armstrong = is_armstrong(number)
    digit_sum = sum_of_digits(number)
    parity = "even" if number % 2 == 0 else "odd"

    # Determine properties list
    properties = ["armstrong"] if armstrong else []
    properties.append(parity)

    # Fetch fun fact
    fun_fact = fetch_fun_fact(number)

    # Return JSON response
    return jsonify({
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }), 200