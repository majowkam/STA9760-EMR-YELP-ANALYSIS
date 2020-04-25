import 


from src import opcv, es
import sys
import os
from datetime import datetime as dt

temp_path = "app//_temp//"
temp_json = dt.now().strftime('%Y%m%d.%M%S') + '_temp.json'

def main(): 
	print('hello matt')


if __name__ == "__main__":
	args   = sys.argv[1:]
	apitoken = os.environ['APIKEY']
	main()