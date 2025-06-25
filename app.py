# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {"usage": "/dict?=<word>"}
    # Since this is a website with front-end, we don't need to send the usage instructions
    return jsonify(response)


@app.get("/dict")
def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    # word = request.args.get("word")
    words = request.args.getlist("word")
    if not words:
        return jsonify({"status":"error","data": "No word provided"}), 400
    response = {"words": []}
    for word in words:
        definition = match_exact(word)
        if definition:
            response["words"].append({"word": word, "definition": definition})
        definition = match_like(word)
        if definition:
            response["words"].append({"word": word, "definition": definition})
        else:
            response["words"].append({"word": word, "definition": "No matches found"})
    return response
    # definition = match_exact(word)
    # if definition:
    #     return jsonify({"status": "success", "data": definition, "word": word})
    # else:
    #     definition = match_like(word)
    #     if definition:
    #         return jsonify({"status": "success", "data": definition, "word": word})
    #     else:
    #         return jsonify({"status": "error", "data": "No matches found"}), 404


if __name__ == "__main__":
    app.run()
