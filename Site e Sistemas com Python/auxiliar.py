# Lista:
lista_nomes = ["Harry", "Laura", "Geovane", "José"]
lista_nomes.append("Laura")
print(lista_nomes)

primeiro_item = lista_nomes[0]
print(primeiro_item)

# Dicionario python:
    # role = quem enviou a mensagem = "função"
    # content = texto da mensagem = "conteudo"
mensagem = {"role": "user", "content": "Eaii pessoal"}
# dicionario = {chave: valor, chave: valor}
# 1 elemento -> dicionario[chave] -> valor

texto_mensagem = mensagem["content"]
print(texto_mensagem)

# lista + dicionario:
lista_mensagens = [
    {"role": "user", "content": "Eaii pessoal"},
    {"role": "assistant", "content": "Resposta da IA"},
    {"role": "user", "content": "Tamo junto"}
]

lista_mensagens.append(
    {"role": "assistant", "content": "Eu desisto de você"}
)

print(lista_mensagens)

# Exibir todos os itens da lista:
for nome in lista_nomes:
    print(nome)

for mensagem in lista_mensagens:
    print(mensagem)
