from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers': '172.23.224.190:9092',
    'group.id': 'product-service',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)
consumer.subscribe(['my-topic'])

print("Waiting for messages...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Error: {}".format(msg.error()))
    else:
        print("Received message: {}".format(msg.value().decode('utf-8')))

