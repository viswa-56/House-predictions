from flask import Flask, request, jsonify,render_template
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/')
def hello():
    return "ello!!!!!!"

@app.route('/#')
def about():
    return render_template("about.html")
@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']  # Location should remain as a string
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({
        'estimated_price': util.get_estimated_prices(location, total_sqft, bhk, bath)
    })

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__ == "__main__":
    print("Starting python flask server for house price predictions...")
    util.load_saved_artifacts()
    app.run(debug=True, port=8000)
