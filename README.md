# STA9760-EMR-YELP-ANALYSIS

The analysis in Analysis.ipynb (link below) was performed after using script/kaggle-to-s3.py to use the Kaggle API to download the yelp dataset and upload it to an S3 bucket.  This script can be used for any Kaggle dataset to upload to any S3 bucket.

Once the data was available in S3, an EMR cluster was configured and launched with a PySpark notebook connected to it.  The configurations for the EMR cluster and PySpark notebook can be seen below.  PySpark was the main tool used to analyze the data.

## [Analysis](Analysis.ipynb)

## Kaggle to S3

The below environment variables will need to be set before running:
* KAGGLE_USERNAME=Your Kaggle Username
* KAGGLE_KEY=Your Kaggle API Key
* AWS_ACCESS_KEY_ID=Your AWS CLI Key ID
* AWS_SECRET_ACCESS_KEY= Your AWS CLI Secret Key
* AWS_SESSION_TOKEN= Your AWS CLI Session Token

Usage
```
docker-compose up
docker-compose run pyth2 python kaggle-to-s3.py KAGGLE-DATASET S3-BUCKET
```

## S3 Bucket Data
https://mm-sta9760-yelpdataset.s3.amazonaws.com/yelp_academic_dataset_business.json
![bucket](/assets/s3.png)


## Cluster Configuration
![cluster](/assets/cluster.PNG)

## Notebook Configuration
![notebook](/assets/notebook.PNG)
