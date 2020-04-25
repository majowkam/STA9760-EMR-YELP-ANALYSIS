docker-compose up -d
docker-compose run pyth python kaggle-to-s3.py
docker-compose down
