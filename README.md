# Bihar Election Race Predictor

A machine learning-based web application that predicts election outcomes for constituencies in Bihar, India. The predictor uses historical polling data and electoral information to forecast which party will win a given constituency.
###  Local Host : http://127.0.0.1:5000/

## Features

- **Interactive Web Interface**: User-friendly form to input election parameters
- **Prediction Engine**: ML model that predicts election outcomes based on:
  - Poll percentage
  - Total votes
  - Total electors
  - Political party
  - District
  - Constituency type (General)
  
- **Instant Results**: Get real-time predictions with detailed information:
  - Predicted outcome (Safe Seat or Competitive Race)
  - Winning party
  - District information
  - Constituency type

## Getting Started

### Prerequisites
- Python 3.7+
- Flask
- Machine Learning libraries (scikit-learn, pandas, numpy)

### Installation

1. Clone the repository
```bash
git clone https://github.com/pawanpal481/Bihar-Election-Predictor.git
cd Bihar-Election-Predictor
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

## Usage

1. Enter the **Poll %** - Percentage from recent polls
2. Enter the **Total Votes** - Expected total votes to be cast
3. Enter the **Total Electors** - Total eligible voters in the constituency
4. Select the **Party** - Choose from available political parties
5. Select the **District** - Choose the district (e.g., Araria, Khagaria)
6. Select the **Constituency Type** - Choose between General or other categories
7. Click **Predict** - Get instant prediction results

## Application Structure

```
Bihar-Election-Predictor/
├── app.py                 # Flask application
├── model.pkl              # Trained ML model
├── templates/
│   ├── index.html         # Main input form
│   └── result.html        # Prediction results page
├── static/
│   └── style.css          # Styling
└── requirements.txt       # Python dependencies
```

## Model

The prediction model is trained on historical Bihar election data and uses machine learning algorithms to identify patterns and relationships between input features and election outcomes.

## Results

The application provides predictions in the following format:
- **Prediction**: Safe Seat or Competitive Race
- **Party**: Predicted winning party
- **District**: Constituency district
- **Constituency Type**: Type of constituency

## 📸 Screenshots

### Input Form

The main interface allows users to input various parameters including poll percentage, total votes, electors, and other electoral data.

<p align="center">
  <img src=""C:\Users\pawan\OneDrive\Pictures\Screenshots\Screenshot 2026-05-07 140806.png"" width="900">
</p>

---

### Prediction Results

After clicking predict, the application displays the predicted outcome with party affiliation, district, and constituency type information.

<p align="center">
  <img src=""C:\Users\pawan\OneDrive\Pictures\Screenshots\Screenshot 2026-05-07 140712.png"" width="900">
</p>
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Pawan Pal** - [GitHub Profile](https://github.com/pawanpal481)

## Contact

For questions or suggestions, please open an issue in the repository.

---

**Note**: This predictor is for educational and informational purposes. Actual election outcomes may vary based on numerous factors not captured by the model.
