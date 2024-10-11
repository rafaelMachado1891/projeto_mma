import requests



url ="http://lumitest.com/myip.json"


response = request.get(url)

if response.status_code == 200:
    
    print(response.json())
    
else:
    print("erro")