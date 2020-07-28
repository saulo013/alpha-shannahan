import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time

# import set_action_vars
import set_action_vars.py

style.use("ggplot")

HM_EPISODES = 25000

# just to keep this example simple, constant turnover reward of -4
TD_REWARD = 7
FG_REWARD = 3
TO_REWARD = -4

class DriveEnv(gym.Env):

	metadata = {"render.modes":["human"]}

	def __init__(self):
		super(DriveEnv, self).__init__()

		# 88 distinct actions defined by shotgun / no_huddle / qb_dropback / run or pass / horizontal direction / run gap / pass length
		self.action_space = spaces.Discrete(88)

		# observation space: field position, down, to_go, turnover, touchdown
		self.observation_space = spaces.Tuple(
			(
				spaces.Discrete(),
				spaces.Discrete(),
				spaces.Discrete(1800), # seconds left in half
				spaces.Discrete(100), # yards to endzone
				spaces.Discrete(99), # yards to first down
				spaces.Discrete(4) # down
			)
		)

		# randomly select offense team
		self.offense_team_id = np.random.randint(0, 32)

		# randomly select starting drive time
		self.half_seconds = np.random.randint(0, 1800)

		# randomly sample yardline with ball
		self.yards_to_endzone = np.random.randint(0, 100)
		self.yards_to_first = np.min(10, self.yards_to_endzone)

		# initialize drive state
		self.down = 1
		self.done = False

		# reset rewards
		self.reward = 0

	def reset(self):
		# randomly select starting drive time
		self.half_seconds = np.random.randint(0, 1800)

		# randomly sample yardline with ball
		self.yards_to_endzone = np.random.randint(0, 100)
		self.yards_to_first = np.min(10, self.yards_to_endzone)

		# initialize drive state
		self.down = 1
		self.done = False

		# reset rewards
		reward = 0 

	def step(self, action):
		
		# check to make sure action is in action space
		assert self.action_space.contains(action)

		# set play call given action
		shotgun, no_huddle, qb_dropback, play_type, run_location, run_gap, pass_location, pass_length = set_action_vars(action)


		if play_type == "run":
			touchdown = predict_touchdown(self.rb_id, self.def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
			yards_gained = predict_run_yards(self.rb_id, self.def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
			turnover = predict_run_turnover(self.rb_id, self.def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
			penalty = predict_run_penalty(self.rb_id, self.def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
			seconds_used = predict_run_seconds(self.rb_id, self.def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
		elif play_type == "pass"
			# not handling scrambles, don't know what passing route would have been
			# predict touchdowns first, (yards to endzone acts as cap on yards_gained near endzone)
			touchdown = predict_touchdown(self.qb_id, self.wr_id, self.def_id, shotgun, no_huddle, qb_dropback, pass_location, pass_length)
			yards_gained = predict_pass_yards(self.qb_id, self.wr_id, self.def_id, shotgun, no_huddle, qb_dropback, pass_location, pass_length)
			turnover = predict_pass_turnover(self.qb_id, self.wr_id, self.def_id, shotgun, no_huddle, qb_dropback, pass_location, pass_length)
			penalty = predict_pass_penalty(self.qb_id, self.wr_id, self.def_id, shotgun, no_huddle, qb_dropback, run_location, run_gap)
			seconds_used = predict_pass_seconds(self.qb_id, self.wr_id, self.def_id, shotgun, no_huddle, qb_dropback, pass_location, pass_length)
		elif play_type == "field goal":
			fg_success = predict_fg_success(self.k_id, self.def_id, self.yards_to_endzone)
		# punt
		else:
			reward = 0
			done = True

		# for now, just modeling holding probability, back up 5 yards
		if penalty == 1:
			yards_to_endzone += 5
			yards_to_first += 5
		else:
			# take time off the clock
			self.half_seconds -= seconds_used

			# if first down, reset downs and increment yards to first down
			# otherwise, increase down
			if yards_gained >= self.yards_to_first:
				self.down = 1
				self.yards_to_first = np.min(10, self.yards_to_endzone)
			else:
				self.down += 1

			# if safety, reward is -2
			if yards_to_endzone - yards_gained >= 100:
				done = True
				reward = -2

			# if touchdown, reward is 7
			if touchdown >= 1:
				done = True
				reward = 7

			# if field goal, reward is 3
			if fg_success == 1:
				done = True
				reward = 3

			# if turnover on downs, reward is -2
			if down > 4:
				done = True
				reward = -2

			# if turnover, reward is -2
			if turnover == 1:
				done = True
				reward = -2

		observation = np.array([self.half_seconds, self.yards_to_endzone, self.yards_to_first, self.down]).astype(np.float32)

		return observation, reward, done, info











