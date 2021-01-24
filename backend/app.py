from flask import Flask, jsonify, request
from flask_cors import CORS
import data_process as dp
from constants import *
    
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def func():
    # Process form submission data
    requests = request.get_json()
    print(requests)
    
    # Load data
    database = open("ev_database.csv", "r")
    data = dp.clean_data(database)
    
    # Load search query
    search = []
    for specification, query in requests:
        search.append([specification, query])

    # Get random search data, then send
    search_data = dp.search_data(data, search)
    # search_data = dp.search_data(data, [[BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]]])
    random_search_data = dp.get_data_from_model(data, dp.get_random_cars_from_search_data(search_data, 5)) # Get 5 random
    return jsonify(random_search_data)
    # return jsonify("Hello World")
    
if __name__ == "__main__":
    app.run(debug=True)