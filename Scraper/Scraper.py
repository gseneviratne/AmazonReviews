#PROGETTO TECHNOLOGIES FOR ADVANCED PROGRAMMING 
#SCRAPER PYTHON SCRIPT

import requests
from bs4 import BeautifulSoup
import json
import time
import socket


def leggi_file_e_crea_array(nome_file):
    try:
        with open(nome_file, 'r') as file:
            array_links = file.read().splitlines()
            return array_links
    except FileNotFoundError:
        print(f"File '{nome_file}' non trovato.")
        return []

def get_amazon_reviews():
        

        while True:
            #Leggo il codice HTML dato dall'URL in input
            response = requests.get(product_url) 
            html_content = response.text

            #BeautifulSoup analizzerà il codice HTML
            soup = BeautifulSoup(html_content, 'html.parser') 
            #Trovo il "tag div" "padre" da cui poi estrapolo i vari div figli
            divs = soup.find_all('div', {'class' : 'a-section review aok-relative'})
            #print(divs)

             # Se la lista dei div è vuota, esco dal ciclo
            if divs != []:
                break



        for div in divs:
            #estrapolo nome,stelle e recensione
            
            span = div.find("span", class_="a-profile-name")
            username = span.text if span else ''

            span = div.find("span", class_="a-icon-alt")
            star = span.text if span else ''

            span = div.find("span", class_="a-size-base a-color-secondary review-date")
            date = span.text if span else ''

            span = div.find("span", class_="a-size-base review-text review-text-content")
            review = span.text if span else ''


            num_stelle = star.split(',')[0]
            print("Recensione-------")
            print(username)
            print("⭐" * int(num_stelle))
            print(date)
            print(review)
            print("-----------------")

            recensione_dict = {
                "utente": username,
                "valutazione": num_stelle,
                "data": date,
                "recensione": review
            }

            recensione_json = json.dumps(recensione_dict)

            #print("lastreview: " + review)
            send_review_to_server(recensione_json)


def send_review_to_server(data):
    # URL del server a cui inviare 
    connected = False
    while not connected:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("logstash", 5002))
                # Invio del JSON a Logstash
                s.sendall(data.encode('utf-8'))
                # Chiudere la connessione
                s.close()
                print("Json inviato")
                connected = True
        except requests.exceptions.RequestException as e:
            print("Errore durante l'invio della recensione al server:", str(e))
        except Exception as e:
            print("Errore imprevisto:", str(e))

if __name__ == '__main__':
    #Definisco l'URL del prodotto Amazon da cui estrarre le recensioni direttamente dal file txt creato
    nome_file = 'reviewlinkAmazon.txt'
    array_links = leggi_file_e_crea_array(nome_file)

    #product_url = array_links[1]
    #get_amazon_reviews()

    for i in range(len(array_links)):
        product_url = array_links[i]
        print("PRODOTTO N* " , i)
        get_amazon_reviews()
        time.sleep(0)  # Pausa di 1 secondo tra un elemento e l'altro