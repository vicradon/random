from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

try:
    for i in range(100):
        print()
        producer.send('input_topic', b"hi there")
except:
    print("an exception occured")