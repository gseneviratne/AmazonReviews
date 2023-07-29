#PROGETTO TECHNOLOGIES FOR ADVANCED PROGRAMMING 
#SCRAPER PYTHON SCRIPT - CORRADO TRGILIA X8100881

#Descrizione dello script: Web Scraping delle recensioni di un prodotto su Amazon

#Importa le librerie necessarie (come  Beautiful Soup)
import requests
from bs4 import BeautifulSoup
import json

#Definisco l'URL del prodotto Amazon da cui estrarre le recensioni

#KingdomCome Deliverance - not work 


#The Witcher 3 - work


#Kingdom Hearts 3 - work    


#One Piece New Edition (Vol 99) - work


#QUMOX Micro SD A Memory Stick PRO Duo Adattatore per Sony PSP -work

#Metodo per leggere il file di testo da me creato dove conterrà i link review che analizzeremo
def leggi_file_e_crea_array(nome_file):
    try:
        with open(nome_file, 'r') as file:
            array_links = file.read().splitlines()
            return array_links
    except FileNotFoundError:
        print(f"File '{nome_file}' non trovato.")
        return []


#Metodo per ottenere/estrapolare le recensioni del prodotto da Amazon
def get_amazon_reviews():
        
        #Leggo il codice HTML dato dall'URL in input
        response = requests.get(product_url)
        html_content = response.text

        #La libreria BeautifulSoup analizzerà il codice HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        #Trovo il "tag div" "padre" da cui poi estrapolo i vari div figli
        #(ovvero le recensioni ed eventuali altre informazioni)
        divs = soup.find_all('div', {'class' : 'a-section review aok-relative'})
        
        #Creo una lista vuota
        data = []

        for div in divs:
            #estrapolo la valutazione "star" dalle recensioni
            span = div.find("span", class_="a-icon-alt")
            star = span.text if span else ''
            
            #estrapolo il testo effettivo della recensione
            span = div.find("span", class_="a-size-base review-text review-text-content")
            review = span.text if span else ''


            print("star: " , star)
            print("review: " , review)
            data.append({"star": star})
            data.append({"review": review})

        with open("data.json" , "w") as file:
            json.dump(data,file)

# Step 5: Esegui il codice e visualizza i risultati
if __name__ == '__main__':
    nome_file = 'reviewlinkAmazon.txt'
    array_links = leggi_file_e_crea_array(nome_file)
    product_url = array_links[0]
    print(product_url)
    #get_amazon_reviews()





#a-section a-spacing-none reviews-content a-size-base
#a-section a-spacing-none review-views celwidget
#a-section review aok-relative

