#pip install requests

import requests

url = "http://127.0.0.1:8000"

def listar_livros():
    r = requests.get(f"{url}/livros")
    print(r.text)

def pesquisar_livro():
    titulo = input("Digite o título do livro: ")
    r = requests.get(f"{url}/livros/{titulo}")
    print(r.status_code)
    print(r.text)

def cadastrar_livro():
    titulo = input("Título: ")
    ano = int(input("Ano: "))
    edicao = int(input("Edição: "))
    livro = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }
    r = requests.post(f"{url}/livros", json=livro)
    print(r.status_code)
    print(r.text)

def deletar_livro():
    titulo = input("Digite o título do livro a deletar: ")
    r = requests.delete(f"{url}/livros/{titulo}")
    print(r.status_code)
    print(r.text)

def editar_livro():
    titulo = input("Digite o título do livro a editar: ")
    
    # Buscar livro atual
    r = requests.get(f"{url}/livros/{titulo}")
    if r.status_code != 200:
        print("Livro não encontrado!")
        return

    print("Dados atuais:", r.json())
    
    novo_titulo = input("Novo título (deixe vazio para manter): ") or titulo
    novo_ano = input("Novo ano (deixe vazio para manter): ")
    nova_edicao = input("Nova edição (deixe vazio para manter): ")

    livro_atual = r.json()
    livro_editado = {
        "titulo": novo_titulo,
        "ano": int(novo_ano) if novo_ano else livro_atual["ano"],
        "edicao": int(nova_edicao) if nova_edicao else livro_atual["edicao"]
    }

    r = requests.put(f"{url}/livros/{titulo}", json=livro_editado)
    print(r.status_code)
    print(r.text)

def menu():
    while True:
        print("\n=== Menu ===")
        print("1 - Listar todos os livros")
        print("2 - Pesquisar livro por título")
        print("3 - Cadastrar um livro")
        print("4 - Deletar um livro")
        print("5 - Editar um livro")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            pesquisar_livro()
        elif opcao == "3":
            cadastrar_livro()
        elif opcao == "4":
            deletar_livro()
        elif opcao == "5":
            editar_livro()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
