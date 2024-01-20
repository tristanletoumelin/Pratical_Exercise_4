import requests

r = requests.get("https://www.google.com/")
print(type(r))  # <class 'requests.models.Response'>
print("\n")
print(r.status_code) # 200
print("\n")
print(r.encoding)   # ISO-8859-1
print("\n")
print(r.apparent_encoding)  # utf-8
print("\n")
print(r.headers)
print("\n")
# print(r.text)
# print("\n")
# print(r.content)