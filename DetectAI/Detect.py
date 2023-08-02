from model import GPT2PPLV2
model = GPT2PPLV2()
sentence = "your text here"
model(sentence, "number of words per chunk", "v1.1")

print(model)
