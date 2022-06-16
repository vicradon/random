from kafka import KafkaConsumer

consumer = KafkaConsumer('input_topic')

for msg in consumer:
    print (msg)