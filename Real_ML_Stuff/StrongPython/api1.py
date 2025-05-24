import requests

response = requests.get( "https://api.freeapi.app/api/v1/social-media/profile", headers= {'accept':'application/json'})
result = response.headers

for k in result:
    print(f"{k}: {result[k]}")

print(response.headers['content-type'])
print(response.status_code)