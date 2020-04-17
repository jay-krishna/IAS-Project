import math
from random import random

def PredictTemperature(n_emp):
	mu=50
	temp0=25

	val_temp=(temp0-(-1*(n_emp-mu)**3)/5000)+random()/4
	if(val_temp>55):
		val_temp=random()+54.0
	if(val_temp<7):
		val_temp=random()+6.0
	
	return round(val_temp,2)