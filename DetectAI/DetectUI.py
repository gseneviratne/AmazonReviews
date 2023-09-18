#Ho provato a dare un'interfaccia UI allo script detect
#il tutto mediante la libreria tkinter che permette
#l'uso di From grafici
import tkinter as tk
from tkinter import scrolledtext
from model import GPT2PPL  # Assicurati che il percorso dell'import sia corretto

#Funzione che legge il file onlydesc.txt riga per riga
def separate_operations(file_path):
    operazioni = []
    current_operation = ""

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        if line.strip():
            current_operation += line
        else:
            if current_operation:
                operazioni.append(current_operation.strip())
                current_operation = ""

    if current_operation:
        operazioni.append(current_operation.strip())

    return operazioni

#Funzione che prende in lettura il file "onlydesc.txt" e ne esegue le operazioni
#riportando i testi risultati nella TextArea
def process_file():
    file_path = 'onlydesc.txt'
    result = separate_operations(file_path)
    for operation in result:
        sentence = operation
        results, out = model(sentence)
        text_area.insert(tk.END, f"{sentence}\nPerplexity/Perplessità: {results['Perplexity']}\nPerplexity per line: {results['Perplexity per line']}\nBurstiness: {results['Burstiness']}\n{out}\n\n")


# Creazione dell'istanza del modello GPT2PPL
model = GPT2PPL()

# Creazione della finestra Tkinter
root = tk.Tk()
root.title("Detect.py GUI")

# Creazione di un widget ScrolledText per mostrare i risultati
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
text_area.pack()

# Creazione di un pulsante per avviare l'elaborazione
process_button = tk.Button(root, text="Analizza onlydesc.txt", command=process_file)
process_button.pack()

# Avvio del loop principale della GUI
root.mainloop()
