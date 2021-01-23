from flask import Flask, jsonify, request
from flask_cors import CORS
import data_process as data_process
from constants import *
    
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def func():
    # Process form submission data
    requests = request.get_json()
    #print(requests)
    
    # Load data
    database = open("ev_database.csv", "r")
    data = data_process.clean_data(database)
    
    # Load search query
    search = []
    for specification, query in requests:
        search.append([specification, query])

    search_data = data_process.search_data(data, search)
    return jsonify(search_data)
    
if __name__ == "__main__":
    app.run(debug=True)