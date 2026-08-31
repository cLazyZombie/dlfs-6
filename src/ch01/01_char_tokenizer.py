# %%
text = "hello월드"
print(list(text))


# %%
text = "hello월드"
ids = [ord(char) for char in list(text)]
print(ids)
ids = [char for char in list(text)]
print(ids)

# %%
print(ord('h'))
print(ord('한'))
print(chr(104))
print(chr(128513))

# %%
class CharTokenizer:
    def encode(self, text):
        return [ord(char) for char in text]

    def decode(self, ids):
        return ''.join([chr(i) for i in ids])

tokenizer = CharTokenizer()
text = "hello월드"

# 인코딩
ids = tokenizer.encode(text)
print(ids)

# 디코딩
decoded = tokenizer.decode(ids)
print(decoded)

# %%
chars = ['h', 'e', 'l', 'l', 'o']
print(''.join(chars))
print('-'.join(chars))
