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
