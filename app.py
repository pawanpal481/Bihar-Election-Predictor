from flask import Flask, request, jsonify, render_template
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load model
model = pickle.load(open('election_race_model.pkl', 'rb'))

# Party Mapping
party_mapping = {
    0: "BJP",
    1: "RJD",
    2: "INC",
    3: "JD(U)",
    4: "LJP",
    5: "CPI(ML)",
    6: "CPI",
    7: "CPM",
    8: "BSP",
    9: "HAM(S)",
    10: "RLSP",
    11: "AIMIM",
    12: "Independent",
    13: "Others"
}

# District Mapping
district_mapping = {
    1: "Araria",
    2: "Arwal",
    3: "Aurangabad",
    4: "Banka",
    5: "Begusarai",
    6: "Bhagalpur",
    7: "Bhojpur",
    8: "Buxar",
    9: "Darbhanga",
    10: "East Champaran",
    11: "Gaya",
    12: "Gopalganj",
    13: "Jamui",
    14: "Jehanabad",
    15: "Kaimur",
    16: "Katihar",
    17: "Khagaria",
    18: "Kishanganj",
    19: "Lakhisarai",
    20: "Madhepura",
    21: "Madhubani",
    22: "Munger",
    23: "Muzaffarpur",
    24: "Nalanda",
    25: "Nawada",
    26: "Patna",
    27: "Purnia",
    28: "Rohtas",
    29: "Saharsa",
    30: "Samastipur",
    31: "Saran",
    32: "Sheikhpura",
    33: "Sheohar",
    34: "Sitamarhi",
    35: "Siwan",
    36: "Supaul",
    37: "Vaishali",
    38: "West Champaran"
}

# Constituency Type Mapping
type_mapping = {
    0: "General",
    1: "SC",
    2: "ST"
}

# Home Route
@app.route('/')
def home():
    return render_template(
        "index.html",
        parties=party_mapping,
        districts=district_mapping,
        types=type_mapping
    )

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        poll = float(request.form['poll'])
        total_votes = int(request.form['total_votes'])
        total_electors = int(request.form['total_electors'])
        party = int(request.form['party'])
        district = int(request.form['district'])
        ac_type = int(request.form['type'])

        features = [
            poll,
            total_votes,
            total_electors,
            party,
            district,
            ac_type
        ]

        prediction = model.predict([features])[0]

        result = "Tight Race" if prediction == 1 else "Safe Seat"

        return render_template(
            "result.html",
            result=result,
            party=party_mapping.get(party),
            district=district_mapping.get(district),
            ac_type=type_mapping.get(ac_type)
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)