def set_action_vars(choice):

	shotgun = None
	no_huddle = None
	qb_dropback = None
	play_type = None
	run_location = None
	run_gap = None
	pass_length = None
	pass_location = None

	if choice == 0:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "left" 
		run_gap = "guard" 
	elif choice == 1:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "left" 
		run_gap = "guard" 
	elif choice == 2:
		shotgun = False
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "left" 
		run_gap = "guard" 
	elif choice == 3:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "left" 
		run_gap = "guard" 
	elif choice == 4:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "left" 
		run_gap = "guard" 
	elif choice == 5:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "left" 
		run_gap = "guard" 
	elif choice == 6:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "left" 
		run_gap = "guard" 
	elif choice == 7:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "left" 
		run_gap = "guard" 
	elif choice == 8:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "left" 
		run_gap = "tackle" 
	elif choice == 9:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "left" 
		run_gap = "tackle" 
	elif choice == 10:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "left" 
		run_gap = "tackle" 
	elif choice == 11:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "left" 
		run_gap = "tackle" 
	elif choice == 12:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "left" 
		run_gap = "tackle" 
	elif choice == 13:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "left" 
		run_gap = "tackle" 
	elif choice == 14:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "left" 
		run_gap = "tackle" 
	elif choice == 15:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "left" 
		run_gap = "tackle" 
		pass_length = None												
	elif choice == 16:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "middle" 
		run_gap = None 
	elif choice == 17:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "middle" 
		run_gap = None 
	elif choice == 18:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "middle" 
		run_gap = None 
	elif choice == 19:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "middle" 
		run_gap = None 
	elif choice == 20:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "middle" 
		run_gap = None 
	elif choice == 21:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "middle" 
		run_gap = None 
	elif choice == 22:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "middle" 
		run_gap = None 
	elif choice == 23:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "middle" 
		run_gap = None 
	elif choice == 24:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "right" 
		run_gap = "guard" 
	elif choice == 25:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "right" 
		run_gap = "guard" 
	elif choice == 26:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "right" 
		run_gap = "guard" 
	elif choice == 27:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "right" 
		run_gap = "guard" 
	elif choice == 28:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "right" 
		run_gap = "guard" 
	elif choice == 29:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "right" 
		run_gap = "guard" 
	elif choice == 30:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "right" 
		run_gap = "guard" 
	elif choice == 31:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "right" 
		run_gap = "guard" 
	elif choice == 32:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "right" 
		run_gap = "tackle" 
	elif choice == 33:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "run" 
		run_location = "right" 
		run_gap = "tackle" 
	elif choice == 34:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "right" 
		run_gap = "tackle" 
	elif choice == 35:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "right" 
		run_gap = "tackle" 
	elif choice == 36:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "run" 
		run_location = "right" 
		run_gap = "tackle" 
	elif choice == 37:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "right" 
		run_gap = "tackle" 
	elif choice == 38:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "run" 
		run_location = "right" 
		run_gap = "tackle" 
	elif choice == 39:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "run" 
		run_location = "right" 
		run_gap = "tackle" 
		pass_length = None													
	elif choice == 40:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "short"
	elif choice == 41:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "short"
	elif choice == 42:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "short"
	elif choice == 43:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "short"
	elif choice == 44:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "short"
	elif choice == 45:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "short"
	elif choice == 46:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "short"
	elif choice == 47:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "short"
	elif choice == 48:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "deep"
	elif choice == 49:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "deep"
	elif choice == 50:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "deep"
	elif choice == 51:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "deep"
	elif choice == 52:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "deep"
	elif choice == 53:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "deep"
	elif choice == 54:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "deep"
	elif choice == 55:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "left" 
		pass_length = "deep"
	elif choice == 56:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "short"
	elif choice == 57:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "short"
	elif choice == 58:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "short"
	elif choice == 59:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "short"
	elif choice == 60:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "short"
	elif choice == 61:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "short"
	elif choice == 62:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "short"
	elif choice == 63:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "short"
	elif choice == 64:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "deep"
	elif choice == 65:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "deep"
	elif choice == 66:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "deep"
	elif choice == 67:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "deep"
	elif choice == 68:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "deep"
	elif choice == 69:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "deep"
	elif choice == 70:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "deep"
	elif choice == 71:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "middle" 
		pass_length = "deep"
	elif choice == 72:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "short"
	elif choice == 73:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "right"
		pass_length = "short"
	elif choice == 74:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "short"
	elif choice == 75:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "short"
	elif choice == 76:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "short"
	elif choice == 77:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "short"
	elif choice == 78:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "short"
	elif choice == 79:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "short"
	elif choice == 80:
		shotgun = False 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "deep"
	elif choice == 81:
		shotgun = True 
		no_huddle = False 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "deep"
	elif choice == 82:
		shotgun = False 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "deep"
	elif choice == 83:
		shotgun = False 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "deep"
	elif choice == 84:
		shotgun = True 
		no_huddle = True 
		qb_dropback = False 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "deep"
	elif choice == 85:
		shotgun = False 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "deep"
	elif choice == 86:
		shotgun = True 
		no_huddle = False 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "deep"
	elif choice == 87:
		shotgun = True 
		no_huddle = True 
		qb_dropback = True 
		play_type = "pass" 
		pass_location = "right" 
		pass_length = "deep"
	if choice == 88:
		play_type = "punt"
	if choice == 88:
		play_type = "field goal"

	return (shotgun, no_huddle, qb_dropback, play_type, run_location, run_gap, pass_location, pass_length)





