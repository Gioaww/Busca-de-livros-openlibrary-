import requests as rq
import json


API_URL = "https://openlibrary.org/search.json"
ARQUIVO = "livros.json"
GENEROS = {
    "filme": "film",
    "musica": "music",
    "música": "music",
    "fantasia": "fantasy",
    "literatura": "literature",
    "poesia": "poetry",
    "ficção científica": "science_fiction",
    "ficcao cientifica": "science_fiction",
    "jovem adult": "young adult",
    "biologia": "biology",
    "matemática": "mathematics",
    "matematica": "mathematics",
    "programação": "programming",
    "programacao": "programming",
    "história": "history",
    "historia": "history",
    "ciência": "science",
    "ciencia": "science",
    "terror": "horror",
    "mistério": "mystery",
    "misterio": "mystery",
}

def main():
#    while True:
        print("\n=== Buscador de Livros ===")
        print("1. Buscar livros")
        print("2. Ver minha lista")
        print("3. Marcar livro como lido")
        print("4. Ver estatisticas")
        print("5. Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            buscar_livros()

def buscar_livros():
    print("Como deseja fazer sua busca? (Titulo, Autor ou Gênero)")
    tipo_busca = input("").lower().strip()
    params = {"limit": 5}

    if tipo_busca == "titulo" or tipo_busca == "título":
        titulo = input("\nTítulo que deseja buscar: ").lower().strip()
        params["title"] = titulo

    elif tipo_busca == "autor":
        autor = input("\nNome do autor que deseja buscar:").lower().strip()
        params["author"] = autor

    elif tipo_busca == "genero" or tipo_busca == "gênero":
        genero = input("\nGênero que deseja: ").lower().strip()
        params["subject"] = traduz_genero(genero)

    resposta = rq.get(API_URL, params=params)
    dados = resposta.json()
    formatar_livro(dados)


def formatar_livro(dados):
    i = 1

    for livro in dados["docs"]:
        titulo = livro.get("title", "Sem Título")
        autores = livro.get("author_name", ["Autor Desconhecido"])
        autor = autores[0]
        ebook = livro.get("ebook_access", "Indisponível")
        data_lancamento = livro.get("first_publish_year", "Desconhecido")

        print(f"{i} {titulo.title()}\n  Autor: {autor}\n  Data de lançamento: {data_lancamento}\n  Disponibilidade Ebook: {ebook}\n")
        i += 1


def traduz_genero(genero):
    return GENEROS.get(genero, genero)

if __name__ == "__main__":
    main()