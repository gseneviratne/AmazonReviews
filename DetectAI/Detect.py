from model import GPT2PPL
model = GPT2PPL()
sentence = "your text here"
model(sentence, "number of words per chunk", "v1.1")

print(model)
