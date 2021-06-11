from requests import get

res = get("https://jsonplaceholder.typicode.com/users")

print(res.json()[0])
