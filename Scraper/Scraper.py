#PROGETTO TECHNOLOGIES FOR ADVANCED PROGRAMMING 
#SCRAPER PYTHON SCRIPT

import requests
from bs4 import BeautifulSoup
import json
import time

#Creo una variabile che sarà una lista vuota
global data

def leggi_file_e_crea_array(nome_file):
    try:
        with open(nome_file, 'r') as file:
            array_links = file.read().splitlines()
            return array_links
    except FileNotFoundError:
        print(f"File '{nome_file}' non trovato.")
        return []

def get_amazon_reviews():
        #Leggo il codice HTML dato dall'URL in input
        response = requests.get(product_url) 
        html_content = response.text

        #BeautifulSoup analizzerà il codice HTML
        soup = BeautifulSoup(html_content, 'html.parser') 

        #Trovo il "tag div" "padre" da cui poi estrapolo i vari div figli
        divs = soup.find_all('div', {'class' : 'a-section review aok-relative'})

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

            data.append({"utente": username})
            data.append({"valutazione": star})
            data.append({"data": date})
            data.append({"recensione": review})

if __name__ == '__main__':
    #Definisco l'URL del prodotto Amazon da cui estrarre le recensioni direttamente dal file txt creato
    nome_file = 'reviewlinkAmazon.txt'
    array_links = leggi_file_e_crea_array(nome_file)

    data = []

    #product_url = array_links[1]
    #get_amazon_reviews()

    for i in range(len(array_links)):
        product_url = array_links[i]
        print("PRODOTTO N* " , i)
        get_amazon_reviews()
        time.sleep(1)  # Pausa di 1 secondo tra un elemento e l'altro
        with open("data.json" , "w") as file:
            json.dump(data,file)