# Market Value Predictor ⚽

A machine learning-powered web application that predicts football player market values based on various player attributes and statistics.

## 🌟 Features

- **Machine Learning Model**: Random Forest regression model trained on player data
- **FastAPI Backend**: High-performance REST API for predictions
- **Streamlit Frontend**: Interactive web interface for easy data input
- **Real-time Predictions**: Instant market value estimations based on player attributes

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nortcele7/Market-Value_Predictor.git
   cd Market-Value_Predictor
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

4. **Install required packages**
   ```bash
   pip install fastapi uvicorn streamlit requests pandas joblib scikit-learn
   ```

## 💻 Usage

### Starting the Backend API

1. Open a terminal and navigate to the project directory
2. Activate your virtual environment
3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

### Starting the Frontend

1. Open a **new terminal** and navigate to the project directory
2. Activate your virtual environment
3. Run the Streamlit app:
   ```bash
   streamlit run frontend.py
   ```
   The web interface will open automatically in your browser at `http://localhost:8501`

## 📊 Input Features

The model considers the following player attributes:

- **Age**: Player's age
- **Position**: Playing position (ST, CM, CDM, CAM, RW, LW, RB, LB, RM, LM, CB)
- **League**: Current league (Premier League, La Liga, Bundesliga, Serie A, Ligue 1, etc.)
- **Contract Until**: Contract expiration year
- **Squad Size**: Size of the player's squad
- **Foreign Players in Squad**: Number of foreign players in the squad
- **Performance Metrics**:
  - Goals
  - Assists
  - Yellow Cards
  - Red Cards
  - Substitutions On/Off
  - Minutes Played

## 🗂️ Project Structure

```
Market_Value_Predictor/
│
├── main.py              # FastAPI backend server
├── frontend.py          # Streamlit web interface
├── rf_model.joblib      # Trained Random Forest model
├── players.csv          # Training dataset
├── test.ipynb           # Jupyter notebook for testing
└── README.md            # Project documentation
```

## 🔧 API Endpoints

### `GET /`
Returns a welcome message

### `POST /predict`
Predicts player market value

**Request Body:**
```json
{
  "age": 25,
  "position": "ST",
  "league": "Premier League",
  "contract_until": 2027,
  "squad_size": 25,
  "foreigners_in_squad": 15,
  "goals": 20,
  "assists": 10,
  "yellow_cards": 3,
  "red_cards": 0,
  "substitutions_on": 5,
  "substitutions_off": 10,
  "minutes_played": 2500
}
```

**Response:**
```json
{
  "predicted_market_value": "€45.2M"
}
```

## 🤖 Model Information

- **Algorithm**: Random Forest Regressor
- **Training Data**: Historical player statistics from `players.csv`
- **Model File**: `rf_model.joblib`

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shreyam Regmi @Nortcele7**
- GitHub: [@Nortcele7](https://github.com/Nortcele7)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## ⭐ Show your support

Give a ⭐️ if this project helped you!

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: Make sure both the FastAPI backend and Streamlit frontend are running simultaneously for the application to work properly.
