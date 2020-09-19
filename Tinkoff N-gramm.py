text = ["this is a sentence", "so is this one"]
bigrams = [b for l in text for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
print(bigrams)