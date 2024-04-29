import random

def simple_hash(text):
    temp_hash_value = random.randint(1, 1000)
    hash_value = 0
    
    for char in text:
        hash_value = temp_hash_value + (hash_value << 5) + ord(char)
    
    return hash_value

text = "Hello, World!"
hashed_text = simple_hash(text)
print("Hashed value:", hashed_text)
