import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Esempio di dataset con testi generati da IA e testi umani
testi_ia = [
    "Questo testo è stato generato da un'intelligenza artificiale.",
    "Un algoritmo di IA ha scritto questo paragrafo.",
    "Questo è il risultato di un modello di intelligenza artificiale."
]

testi_umani = [
    "Questo è un esempio di testo scritto da un essere umano.",
    "Gli esseri umani hanno scritto questo articolo.",
    "Questa è una frase composta da una persona reale."
]

# Etichette per i due tipi di testi: 0 per testi generati da IA, 1 per testi umani
etichette_ia = [0] * len(testi_ia)
etichette_umani = [1] * len(testi_umani)

# Unisci i due dataset e le etichette
testi_totali = testi_ia + testi_umani
etichette_totali = etichette_ia + etichette_umani

# Shuffle dei dati per evitare bias durante l'addestramento
dati_completi = list(zip(testi_totali, etichette_totali))
random.shuffle(dati_completi)
testi_totali, etichette_totali = zip(*dati_completi)

# Converti il testo in vettori di features utilizzando CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(testi_totali)

# Dividi il dataset in training set e test set
X_train, X_test, y_train, y_test = train_test_split(X, etichette_totali, test_size=0.2, random_state=42)

# Addestramento del modello di Support Vector Machine (SVM)
model = SVC(kernel='linear', C=1.0, random_state=42)
model.fit(X_train, y_train)

# Fai previsioni sul test set
y_pred = model.predict(X_test)

# Valutazione delle prestazioni del modello
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Esempio di testo da classificare
nuovo_testo = "Questo paragrafo è stato generato da GPT-3."

# Converti il testo in vettore di features utilizzando il vectorizer
nuovo_testo_vettore = vectorizer.transform([nuovo_testo])

# Fai la previsione per il nuovo testo
previsione = model.predict(nuovo_testo_vettore)

if previsione[0] == 0:
    print("Il testo è stato generato da un'intelligenza artificiale.")
else:
    print("Il testo è stato scritto da un essere umano.")


