import random

def simple_hash(text):
    hash_value = random.randint(1, 1000)
    
    for char in text:
        hash_value = (hash_value << 5) + ord(char)
    
    return hash_value

text = "Hello, World!"
hashed_text = simple_hash(text)
print("Hashed value:", hashed_text)
