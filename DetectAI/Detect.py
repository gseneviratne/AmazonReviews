from model import GPT2PPL
model = GPT2PPL()

#Funzione che legge il file onlydesc.txt riga per riga
def separate_operations(file_path):
    operazioni = []
    current_operation = ""

    with open(file_path, 'r',encoding='utf-8') as file:
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

# Percorso relativo al file onlydesc.txt in Scraper folder
file_path = '../Scraper/onlydesc.txt'
result = separate_operations(file_path)

#Inserire qui, le varie descrizioni/recensioni date dallo scraper
for operation in result:
    #if len(operation) >= 100:
    print(operation)
    sentence = operation
    model(sentence)

    

