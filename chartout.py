import json
import subprocess
from sas7bdat import SAS7BDAT



def return_chart(segmentid, level):
	seg = segmentid.split('.')
	lev = level.split('.')
	CMD = '"C:\Program Files\SASHome\SASFoundation\9.4\sas.exe" C:\Python27\Projects\Kaman\code\lookup_rates_driver.sas -config "C:\Program Files\SASHome\SASFoundation\9.4\\nls\en\sasv9.cfg" -set segmentid ' + seg[0] + ' -set level ' +lev[0]
	print CMD
	subprocess.call(CMD, shell=True)
	
	with SAS7BDAT('C:\Python27\Projects\Kaman\output\\binned_txn.sas7bdat') as f:
		df = f.to_data_frame()

	return df.to_json(orient='records')
