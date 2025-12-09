from pydantic import BaseModel, computed_field

from datetime import date

from fastapi import FastAPI
from fastapi.responses import JSONResponse

import pandas as pd

import joblib

# Loading Model

model = joblib.load("rf_model.joblib")

today = date.today()

current_year = today.year



league = {
    "Premier League": 5,
    "La Liga": 5,
    "Bundesliga": 5,
    "Serie A": 5,
    "Ligue 1": 5,

    "Primeira Liga": 4,
    "Pro League": 4,   # Belgium
    "Süper Lig": 4,
    "Eredivisie": 4,
    "Super League": 4,  # Swiss Super League
    "Premiership": 4,   # Scottish Premiership
    "Championship": 4,  # England 2nd tier
    "La Liga 2": 4,
    "2. Bundesliga": 4,
    "Major League Soccer": 4,

    "Serie B": 3,
    "Primera División": 3,  # Chile / Uruguay context
    "Liga Profesional de Fútbol": 3,  # Argentina
    "První liga": 3,  # Czech 1st league
    "Hrvatska nogometna liga": 3,  # Croatia
    "Eliteserien": 3,  # Norway
    "Nemzeti Bajnokság I": 3,  # Hungary
    "K League 1": 3,
    "Ligue 2": 3,
    "Superliga": 3,  # Danish Superliga
    "A-League Men": 3,
    "Liga 1": 3,  # Romania
    "Ekstraklasa": 3,  # Poland
    "1. Division": 3,  # Denmark second tier
    "División Profesional": 3,  # Paraguay / Bolivia
    "División de Fútbol Profesional": 3,  # Bolivia
    "Série A": 3,  # Brazil Série A

    "Allsvenskan": 2,  # Sweden
    "Liga I": 2,
    "Veikkausliiga": 2,  # Finland
    "Premyer Liqa": 2,  # Azerbaijan
    "League One": 2,
    "3. Liga": 2,
    "Liga 1": 2,  # If this refers to Indonesia; adjust if needed

    "League Two": 1,
    "Premier Division": 1  # Various smaller leagues
}

class Player(BaseModel):
    preferred_foot: str  
    weak_foot: int
    skill_moves: int
    international_reputation: int
    overall_rating: int
    potential: int
    height_cm: float
    weight_kg: float
    age: int
    club_contract_valid_until: int    
    club_position: str
    league_name: str
    club_rating: int

    @computed_field
    @property
    def bmi(self) -> float:
        height_m = self.height_cm/100
        bmi = self.weight_kg/(height_m**2)

        return bmi

    @computed_field
    @property
    def league_strength(self) -> float:
        league_strength = league[self.league_name]

        return league_strength

    @computed_field
    @property
    def contract_length(self)->float:
        contract_length = self.club_contract_valid_until - current_year
        return contract_length
    
    @computed_field
    @property
    def pref_foot_encoded(self) -> int:
        # Right = 1, Left = 0
        return 1 if self.preferred_foot.lower() == "right" else 0
    
    @computed_field
    @property
    def age_group_encoded(self) -> float:
        if self.age<23:
            return 0
        if self.age>=23 and self.age<30:
            return 1
        if self.age>=30 and self.age<35:
            return 2
        if self.age>=35:
            return 3
        
    @computed_field
    @property
    def position_encoded(self) -> dict:
        positions = ["ST", "CM", "CDM", "CAM", "RW", "LW", "RB", "LB", "RM", "LM", "CB"]
        return {f"pos_{pos}": 1 if self.club_position.upper() == pos else 0 for pos in positions}

app = FastAPI()


@app.post("/predict")
def predict_value(player: Player):
    input_dict = {
        "weak_foot": player.weak_foot,
        "skill_moves": player.skill_moves,
        "international_reputation": player.international_reputation,
        "overall_rating": player.overall_rating,
        "potential": player.potential,
        "club_rating": player.club_rating,
        "bmi": player.bmi,
        "league_strengh": player.league_strength,
        "contract_length": player.contract_length,
        "pref_foot": player.pref_foot_encoded,
        "age_group_encoded": player.age_group_encoded,
        "pos_CAM": player.position_encoded["pos_CAM"],
        "pos_CB": player.position_encoded["pos_CB"],
        "pos_CDM": player.position_encoded["pos_CDM"],
        "pos_CM": player.position_encoded["pos_CM"],
        "pos_LB": player.position_encoded["pos_LB"],
        "pos_LM": player.position_encoded["pos_LM"],
        "pos_LW": player.position_encoded["pos_LW"],
        "pos_RB": player.position_encoded["pos_RB"],
        "pos_RM": player.position_encoded["pos_RM"],
        "pos_RW": player.position_encoded["pos_RW"],
        "pos_ST": player.position_encoded["pos_ST"]
    }


    input_df = pd.DataFrame([input_dict])

    # Since we are training our random forest regressor model in a specific column order so we are reordering it
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(input_df)

    return JSONResponse(status_code = 201, content={"Prediction": prediction[0]})

