# Kafka-Monitoring

## steps
python3 -m venv venv \
source venv/bin/activate \
pip install -r requirements.txt \
start zookeeper and broker on your machine \
export FLASK_APP=main.py \
flask run 


## producer
127.0.0.1:5000/producer 

## consumer
127.0.0.1:5000/consumer 

## monitoring
127.0.0.1:5000/monitoring 
