import json
from sas7bdat import SAS7BDAT



def return_table():
	with SAS7BDAT('C:\Python27\Projects\Kaman\output\segment_all_txn.sas7bdat') as f:
		df = f.to_data_frame()

	return df.to_json(orient='records')
