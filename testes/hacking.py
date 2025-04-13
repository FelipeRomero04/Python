import requests

# URL de exemplo
url = "https://jsonplaceholder.typicode.com/posts/1"

# Fazendo a requisição GET
response = requests.get(url)

# Exibindo informações
print(f'Status Code: response.status_code\n')
print(f'Cabeçalhos: {response.headers}\n')
print(f'Conteúdo (JSON): {response.json()}\n')
