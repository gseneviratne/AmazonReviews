from confluent_kafka import Consumer, Producer
import random
import json
from googletrans import Translator

translator = Translator()

# Configurazione del consumatore Kafka
consumer_config = {
    'bootstrap.servers': 'kafka-server:9092',  # Indirizzo del broker Kafka
    'group.id': 'my-group',  # Gruppo di consumatori
    'auto.offset.reset': 'earliest'  # Inizio dalla prima posizione disponibile nel topic
}

# Configurazione del produttore Kafka
producer_config = {
    'bootstrap.servers': 'kafka-server:9092'  # Indirizzo del broker Kafka
}


def simulate_DetectAI():
    probabilita_10_percento = 0.10
    probabilita_30_percento = 0.30

    numero_random = random.random()  # Genera un numero casuale tra 0 e 1

    if numero_random < probabilita_10_percento:
        return random.uniform(0, 59)  # Restituisce un numero casuale tra 0 e 59
    elif numero_random < probabilita_10_percento + probabilita_30_percento:
        return random.uniform(60, 79)  # Restituisce un numero casuale tra 60 e 79
    else:
        return random.uniform(80, 100)  # Restituisce un numero casuale tra 80 e 100 (incluso)

# Crea un consumatore Kafka
consumer = Consumer(consumer_config)

# Sottoscrivi al topic "reviews"
consumer.subscribe(['reviews'])

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
            username = json.loads(msg.value())["utente"]
            num_stelle =  json.loads(msg.value())["valutazione"]
            date =  json.loads(msg.value())["data"]
            if review != "":
                translatedReview = translator.translate(review, dest='en')
        except json.JSONDecodeError as e:
            print(f"Errore durante il parsing del JSON: {e}")
            continue
        
        # Esegui le operazioni desiderate sui dati (aggiungi campo1 e campo2)
        processed_data = {
            "recensione": translatedReview.text,
            "utente": username,
            "valutazione": num_stelle,
            "data": date,
            "perplexity_per_line": simulate_DetectAI(),
        }

        # Invia il messaggio elaborato al topic "detectedreviews"
        producer.produce("detectedreviews", key=msg.key(), value=json.dumps(processed_data))

        # Attendere finché il messaggio viene inviato con successo
        producer.flush()

# Chiudi il consumatore Kafka in modo sicuro alla fine
consumer.close()

    

