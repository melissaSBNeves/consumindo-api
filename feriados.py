import requests;

ano = int(input("Digite o ano: "))

url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'

reponse = requests.get(url)
data = reponse.json()

if reponse.status_code == 200:
    for i in range(0, len(data)):
        print(data[i])
else:
    print("Deu erro parça")
