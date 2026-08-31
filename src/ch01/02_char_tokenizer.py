# %%
encoded = '가'.encode("utf-8")
print(encoded)
print(list(encoded))
decoded = encoded.decode("utf-8")
print(decoded)

ids = [65]
decoded = bytes(ids).decode("utf-8")
print(decoded)
