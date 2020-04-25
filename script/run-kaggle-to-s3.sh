docker-compose up -d
docker-compose run pyth2 python kaggle-to-s3.py yelp-dataset/yelp-dataset mm-sta9760-yelpdataset
docker-compose down
