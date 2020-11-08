from flask import Flask
from kafka import KafkaProducer
from kafka import KafkaConsumer
app = Flask(__name__)
topicName = 'First_Topic'
bootstrap_servers = ['localhost:9092']
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
consumer = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers=bootstrap_servers)
@app.route('/producer')
def produce():
    producer.send(topicName, b'Hello from kafka...')
    print("message sent")
    return "Producer page"

@app.route('/consumer')
def consume():
    for msg in consumer:
        print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))

@app.route('/monitoring')
def metric():
    return( {"producer_metrics":producer.metrics(), "consumer_metrics":consumer.metrics() })
    


if __name__ == '__main__':
    app.run(debug=True)

