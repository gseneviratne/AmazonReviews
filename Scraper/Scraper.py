#Web Scraping delle recensioni di un prodotto su Amazon utilizzando Beautiful Soup.

# Importa le librerie necessarie
import requests
from bs4 import BeautifulSoup

# Definisci l'URL del prodotto Amazon da cui estrarre le recensioni
product_url = 'https://www.amazon.it/Console-Portatile-quad-core-funzione-bluetooth/dp/B0BHKMKKGD/ref=rvi_sccl_8/258-1633243-3972465?pd_rd_w=oVk1O&content-id=amzn1.sym.547ce61e-33fb-4876-9984-dcdd97a99f53&pf_rd_p=547ce61e-33fb-4876-9984-dcdd97a99f53&pf_rd_r=T1Z9VGH312NZNP01GEXA&pd_rd_wg=zCdgX&pd_rd_r=3aa3088f-6c17-457a-9cb9-a16bc63ede2e&pd_rd_i=B0BHKMKKGD&psc=1' #'https://www.amazon.com/your-product-url'

# Funzione per ottenere le recensioni del prodotto da Amazon
def get_amazon_reviews():
    try:
        # Step 1: Scarica il codice HTML della pagina del prodotto
        response = requests.get(product_url)
        html_content = response.text

        # Step 2: Utilizza Beautiful Soup per analizzare il codice HTML
        soup = BeautifulSoup(html_content, 'html.parser') #Riesce a prendere la pagina HTML 
        #print(soup)

        # Trova il contenitore delle recensioni
        reviews_container = soup.find('div', {'class': 'reviews'})
        print("reviews_container : " , reviews_container)

        # Verifica se l'elemento delle recensioni è stato trovato
        if reviews_container:
            # Trova tutte le recensioni all'interno del contenitore
            reviews = reviews_container.find_all('div', {'class': 'review'})

            # Analizza le recensioni e estraile i dati desiderati
            for review in reviews:
                # Estrai il titolo della recensione
                title = review.find('h2', {'class': 'review-title'}).text.strip()

                # Estrai il testo della recensione
                text = review.find('div', {'class': 'review-text'}).text.strip()

                # Estrai il punteggio della recensione
                rating = review.find('span', {'class': 'review-rating'}).text.strip()

                # Stampa i risultati delle recensioni
                print("Titolo:", title)
                print("Recensione:", text)
                print("Punteggio:", rating)
                print("-" * 30)
        else:
            print("Nessun elemento delle recensioni trovato.")


    except Exception as e:
        print("Si è verificato un errore:", e)

# Step 6: Esegui il codice e visualizza i risultati
if __name__ == '__main__':
    get_amazon_reviews()