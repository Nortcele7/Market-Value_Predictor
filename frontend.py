import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Market Value Predictor")
st.markdown("Enter the related information: ")

# Input

number_list = [1,2,3,4,5]

contract_years = [2026,2027,2028,2029,2030]

position = [
    "ST",   # Striker
    "CM",   # Central Midfielder
    "CDM",  # Central Defensive Midfielder
    "CAM",  # Central Attacking Midfielder
    "RW",   # Right Winger
    "LW",   # Left Winger
    "RB",   # Right Back
    "LB",   # Left Back
    "RM",   # Right Midfielder
    "LM",   # Left Midfielder
    "CB"    # Center Back
]

league = [
    "Premier League",
    "La Liga",
    "Bundesliga",
    "Serie A",
    "Ligue 1",
    "Primeira Liga",
    "Pro League",
    "Süper Lig",
    "Eredivisie",
    "Super League",
    "Premiership",
    "Championship",
    "La Liga 2",
    "2. Bundesliga",
    "Major League Soccer",
    "Serie B",
    "Primera División",
    "Liga Profesional de Fútbol",
    "První liga",
    "Hrvatska nogometna liga",
    "Eliteserien",
    "Nemzeti Bajnokság I",
    "K League 1",
    "Ligue 2",
    "Superliga",
    "A-League Men",
    "Liga 1",
    "Ekstraklasa",
    "1. Division",
    "División Profesional",
    "División de Fútbol Profesional",
    "Série A",
    "Allsvenskan",
    "Liga I",
    "Veikkausliiga",
    "Premyer Liqa",
    "League One",
    "3. Liga",
    "Liga 1",
    "League Two",
    "Premier Division"
]



preferred_foot = st.selectbox("Enter preferred foot", ["Right", "Left"])

weak_foot = st.selectbox("Select Weak Foot Ability", number_list)

skill_moves = st.selectbox("Select Skill Moves rating ", number_list)

international_reputation = st.selectbox("Select Internationl Reputation rating ", number_list)

overall_rating = st.number_input("Select Overall Rating (0-100): ", min_value=0, max_value=100, value=85)

potential = st.number_input("Select Potential Rating (0-100): ", min_value=0, max_value=100, value=85)

weight = st.number_input("Weight(kg)", min_value=1.0, value=65.0)

height = st.number_input("Height(cm)", min_value=5, max_value=250, value=170)

age = st.number_input("Age", min_value=1, value=18)

club_contract_valid_until = st.selectbox("Select contract expiry year: ", contract_years)

club_position = st.selectbox("Select Position: ", position)

league_name = st.selectbox("Select League: ", league)

club_rating = st.number_input("Select Club Rating (0-90): ", min_value=0, max_value=90, value=85)

if st.button("Predict Market Value"):
    input_data = {
        "preferred_foot": preferred_foot,
        "weak_foot": weak_foot,
        "skill_moves": skill_moves,
        "international_reputation": international_reputation,
        "overall_rating": overall_rating,
        "potential": potential,
        "height_cm": height,
        "weight_kg": weight,
        "age": age,
        "club_contract_valid_until": club_contract_valid_until,
        "club_position": club_position,
        "league_name": league_name,
        "club_rating": club_rating
    }

    response = requests.post(API_URL, json=input_data)

    if response.status_code == 201:
        result = response.json()
        st.success(f"Predicted Market Value: {result["Prediction"]}")