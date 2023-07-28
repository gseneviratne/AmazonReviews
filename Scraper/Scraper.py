# Web Scraping delle recensioni di un prodotto su Amazon utilizzando Beautiful Soup.


#div class="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"

#span class="a-size-medium a-color-base a-text-normal"

#span class="a-icon-alt"


# Importa le librerie necessarie
import requests
from bs4 import BeautifulSoup
import json

# Definisci l'URL del prodotto Amazon da cui estrarre le recensioni
#product_url = 'https://www.amazon.it/Console-Portatile-quad-core-funzione-bluetooth/dp/B0BHKMKKGD/ref=rvi_sccl_8/258-1633243-3972465?pd_rd_w=oVk1O&content-id=amzn1.sym.547ce61e-33fb-4876-9984-dcdd97a99f53&pf_rd_p=547ce61e-33fb-4876-9984-dcdd97a99f53&pf_rd_r=T1Z9VGH312NZNP01GEXA&pd_rd_wg=zCdgX&pd_rd_r=3aa3088f-6c17-457a-9cb9-a16bc63ede2e&pd_rd_i=B0BHKMKKGD&psc=1'

#https://www.amazon.it/Kingdom-Come-Deliverance-Royal-Playstation/dp/B07SV8K836/ref=sr_1_7?__mk_it_IT=ÅMÅŽÕÑ&keywords=ps4&qid=1690556359&s=music&sr=1-7-catcorr


#URL PAGINA GIOCHI PS4
product_url = 'https://www.amazon.it/s?i=videogames&rh=n%3A412603031%2Cn%3A2569674031%2Cn%3A2569677031&dc&fs=true&ds=v1%3AieAKOR%2F8sJjjPGizhRciufqECbJsyeNrE9vNb36OrXY&qid=1690554748&rnid=412603031&ref=sr_nr_n_5'
#URL PAGINA MUSICA CLASSICA
#product_url = "https://www.amazon.it/s?rh=n%3A435475031&fs=true&ref=lp_435475031_sar"

#product_url = "https://www.amazon.it/Kingdom-Come-Deliverance-Royal-Playstation/dp/B07SV8K836/ref=sr_1_7?__mk_it_IT=ÅMÅŽÕÑ&keywords=ps4&qid=1690556359&s=music&sr=1-7-catcorr"

product_url = "https://www.amazon.it/Kingdom-Come-Deliverance-Royal-Playstation/product-reviews/B07SV8K836/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

# Funzione per ottenere le recensioni del prodotto da Amazon
def get_amazon_reviews():
        # Step 1: Scarica il codice HTML della pagina del prodotto
        response = requests.get(product_url)
        html_content = response.text

        # Step 2: Utilizza Beautiful Soup per analizzare il codice HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        #print(soup)

        # Step 3: Trova tutti gli elementi delle recensioni

        #class usata per le pagine inerenti alla lista uscita per categoria
        divs = soup.find_all('div', {'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'})



        #Creo una lista vuota
        data = []

        for div in divs:
            span = div.find("span", class_="a-size-medium a-color-base a-text-normal")
            title = span.text if span else ''
            print("title " , title)
            data.append({"title": title})

        with open("data.json" , "w") as file:
            json.dump(data,file)

# Step 5: Esegui il codice e visualizza i risultati
if __name__ == '__main__':
    get_amazon_reviews()

