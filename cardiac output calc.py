#Let's do some bio, nerds

def cardiacCalc(userBPM_I):
	userBPM_S = str(userBPM_I)
	CO = 75*userBPM_I
	print("Heartrate: " + userBPM_S + " BPM")
	print("Cardiac output: " + (str(CO)) + " mL/min")
	print("")
	print("At this rate, your heart will pump...")
	print((str(CO*60)) + " mL of blood per hour")
	print((str(CO*60*24)) + " mL of blood per day")
	print((str(CO*60*24*365)) + " mL of blood per year")
	print((str(CO*60*24*365*75)) + "mL of blood in the average human lifespan")