from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')


for line in open("ip_addresses_with_countries.txt"):
    ip_address, country = line.split(",")
    producer.send('ip_addresses', b"{ip_address}:{'country': country}")
    


