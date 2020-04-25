import sys

def main(dsname,s3bucket): 
	import os
	fpath = 'temp'
	os.mkdir(fpath)
	try:
		get_kaggle(dsname,fpath)
	except Exception as e:
		print(e,'Could not get Kaggle data',sep='\n')
	try:
		to_s3(s3bucket,fpath)
	except Exception as e:
		print(e,'Could not upload to s3',sep='\n')
	for f in os.listdir(fpath):
		os.remove(f)
	os.rmdir(fpath)
	print('all done matt')

def get_kaggle(dsname,fpath):
	import kaggle.api as k
	k.authenticate()
	k.dataset_download_files(dsname,path='temp/',unzip=True)

def to_s3(bucket,fpath):
	import boto3
	import os
	s3 = boto3.client('s3')
	for f in os.listdir(fpath):
		s3.upload_file(f,bucket,f)

if __name__ == "__main__":
	args   = sys.argv[1:]
	main(args[0],args[1])
