from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    
    # name = request.args.get("name")
    lname = request.args.get("lname")
    fname = request.args.get("fname")
    # if not name:
    #     return jsonify({"error": "Name parameter is required"}), 400
    # response = {"data": f"Hello, {name}!"}
    # return jsonify(response)
    # Check if both first name and last name are provided
    if not fname and not lname:
        return jsonify({"error": "First name and last name are required"}), 400
    elif not fname and lname:
    # Check if only last name is provided
        return jsonify({"data": f"Hello Mr {lname}!"})
    # Check if only first name is provided
    elif fname and not lname:
        return jsonify({"data": f"Hello, {fname}!"})
    # If both names are provided
    else:
        return jsonify({"data": f"Is your name {fname} {lname}?"})