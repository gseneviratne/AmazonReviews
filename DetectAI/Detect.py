from model import GPT2PPL
from confluent_kafka import Consumer, Producer
import json
model = GPT2PPL()

# Configurazione del consumatore Kafka
consumer_config = {
    'bootstrap.servers': 'kafkaServer:9092',  # Indirizzo del broker Kafka
    'group.id': 'my-group',  # Gruppo di consumatori
    'auto.offset.reset': 'earliest'  # Inizio dalla prima posizione disponibile nel topic
}

# Configurazione del produttore Kafka
producer_config = {
    'bootstrap.servers': 'kafkaServer:9092'  # Indirizzo del broker Kafka
}

# Crea un produttore Kafka
producer = Producer(producer_config)

while True:
    # Leggi un messaggio dalla coda Kafka
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print('Error: %s' % msg.error())
    else:
        # Estrai il campo "recensione" dal messaggio JSON
        try:
            review = json.loads(msg.value())["recensione"]
        except json.JSONDecodeError as e:
            print(f"Errore durante il parsing del JSON: {e}")
            continue

        model(reviews)

        # Esegui le operazioni desiderate sui dati (aggiungi campo1 e campo2)
        processed_data = {
            "recensione": review,
            "campo1": "valore1",
            "campo2": "valore2"
        }

        # Invia il messaggio elaborato al topic "detectedreviews"
        producer.produce("detectedreviews", key=msg.key(), value=json.dumps(processed_data))

        # Attendere finché il messaggio viene inviato con successo
        producer.flush()

# Chiudi il consumatore Kafka in modo sicuro alla fine
consumer.close()

    

