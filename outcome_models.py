
import pandas as pd
from statsmodels.genmod.bayes_mixed_glm import PoissonBayesMixedGLM
from statsmodels.genmod.bayes_mixed_glm import BinomialBayesMixedGLM


nfl_2019 = pd.read_csv("./nfl_pbp_2019.csv")

filter_cols = ["qb_kneel", "qb_spike", "qb_scramble"]

select_cols = ["play_id", "game_id", "touchdown", "yards_gained", "turnover", "posteam", "defteam", "yardline_100", 
	"half_seconds_remaining", "play_type", "shotgun", "no_huddle", "qb_dropback",
	"pass_length", "pass_location", "run_location", "run_gap", "field_goal_result",
	"opp_fg_prob", "opp_td_prob", "fumble_forced", "fumble_not_forced", "fumble_lost", "penalty"]

nfl_rush_2019 = nfl_2019[nfl_2019["play_type"] == "rush"]

# first, fit rush outcome models

# 1 - touchdown
rush_penalty_mod = BinomialBayesMixedGLM.from_formula(
	'penalty ~ shotgun + no_huddle + qb_dropback + run_location + run_gap',
	['0 + rusher_id', '0 + def_id'],
	data = nfl_rush_2019
)

rush_penalty_result = rush_penalty_mod.fit_vb


# 2 - rushing yards
rush_yard_mod = PoissonBayesMixedGLM.from_formula(
	'yards_gained ~ shotgun + no_huddle + qb_dropback + run_location + run_gap',
	['0 + rusher_id', '0 + def_id'],
	data = nfl_rush_2019
)

rush_yard_result = rush_yard_mod.fit_vb()


# 3 - rushing turnovers (fumbles)
rush_turnover_mod = BinomialBayesMixedGLM.from_formula(
	'turnover ~ shotgun + no_huddle + qb_dropback + run_location + run_gap',
	['0 + rusher_id', '0 + def_id'],
	data = nfl_rush_2019
)

rush_turnover_result = rush_turnover_mod.fit_vb()

# 4 - penalty (holding)
rush_penalty_mod = BinomialBayesMixedGLM.from_formula(
	'penalty ~ shotgun + no_huddle + qb_dropback + run_location + run_gap',
	['0 + rusher_id', '0 + def_id'],
	data = nfl_rush_2019
)

rush_penalty_result = rush_penalty_mod.fit_vb

# 5 - seconds used
rush_seconds_mod = PoissonBayesMixedGLM.from_formula(
	'seconds_used ~ shotgun + no_huddle + qb_dropback + run_location + run_gap',
	['0 + rusher_id', '0 + def_id'],
	data = nfl_rush_2019
)

def create_rush_df(rb_id, def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap):
	pred_df = {
		'rb_id': rb_id,
		'def_id': def_id,
		'shotgun': shotgun,
		'no_huddle': no_huddle,
		'qb_dropback': qb_dropback,
		'run_location': run_location,
		'run_gap': run_gap
	}

def predict_rush_yards(rb_id, def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap):
	rush_df = create_rush_df(rb_id, def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
	rush_yards_pred = rush_yard_result.predict(rush_df)
	return rush_yards_pred

def predict_rush_turnover(rb_id, def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap):
	rush_df = create_rush_df(rb_id, def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
	rush_turnover_pred = rush_turnover_result.predict(rush_df)
	return rush_turnover_pred

def predict_rush_penalty(rb_id, def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap):
	rush_df = create_rush_df(rb_id, def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
	rush_penalty_pred = rush_penalty_result.predict(rush_df)
	return rush_penalty_pred

def predict_rush_seconds(rb_id, def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap):
	rush_df = create_rush_df(rb_id, def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
	rush_seconds_pred = rush_seconds_result.predict(rush_df)
	return rush_seconds_pred

