import json
import subprocess
from sas7bdat import SAS7BDAT
import pandas as pd


def return_mvp(objective):
	print "Objective: " + objective
	CMD = '"C:\Program Files\SASHome\SASFoundation\9.4\sas.exe" C:\Python27\Projects\Kaman\code\generate_mvp_recs_driver.sas -config "C:\Program Files\SASHome\SASFoundation\9.4\\nls\en\sasv9.cfg" -set objective ' + objective
	print CMD
	subprocess.call(CMD, shell=True)
	
	#with SAS7BDAT('D:\Kaman\output\mvp_recommendations.sas7bdat') as f:
	#	df = f.to_data_frame()

	df = pd.read_csv('mvp_rec.csv')
	return df.to_json(orient='records')
