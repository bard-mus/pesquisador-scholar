import requests
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

# Função principal de busca com paginação
def buscar_artigos_serpapi(query, api_key):
    print(f"\n🔍 Iniciando extração para a busca: '{query}'")
    url = "https://serpapi.com/search.json"
    artigos = []

    for start in range(0, 60, 10):  # 0, 10, 20, 30, 40, 50 (Cada incremento em 10 é uma página de resultados)
        print(f"\n➡️ Buscando página com start={start}...")
        params = {
            "engine": "google_scholar",
            "q": query,
            "api_key": api_key,
            "start": start
        }

        response = requests.get(url, params=params)
        print(f"   🔗 URL: {response.url}")
        print(f"   📡 Status: {response.status_code}")

        if response.status_code != 200:
            print(f"   ❌ Erro ao acessar a página {start // 10 + 1}. Encerrando.")
            break

        data = response.json()
        results = data.get("organic_results", [])

        if not results:
            print(f"   ⚠️ Nenhum resultado encontrado na página {start // 10 + 1}.")
            break

        for result in results:
            artigo = {
                "Title": result.get("title"),
                "Snippet": result.get("snippet"),
                "Link": result.get("link"),
                "Authors": result.get("publication_info", {}).get("authors", [{}])[0].get("name") if result.get("publication_info", {}).get("authors") else None,
                "Publication Date": result.get("publication_info", {}).get("summary")
            }
            artigos.append(artigo)

    print(f"\n✅ Total de artigos extraídos: {len(artigos)}")
    return artigos

# Salvando em Excel
def salvar_para_excel(artigos, query, pasta_destino):
    data_atual = datetime.now().strftime("%Y-%m-%d")
    nome_arquivo = f"{query}_{data_atual}.xlsx".replace(" ", "_")
    caminho_completo = f"{pasta_destino}/{nome_arquivo}" if pasta_destino else nome_arquivo

    df = pd.DataFrame(artigos)
    df.to_excel(caminho_completo, index=False)

    print(f"📁 Dados salvos em: {caminho_completo}")
    return caminho_completo

# Navegação
def selecionar_pasta():
    pasta = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, pasta)

# Função principal da interface
def executar_extracao():
    query = entry_query.get()
    api_key = entry_apikey.get()
    pasta = entry_folder.get()

    if not query or not api_key:
        label_status.config(text="⚠️ Preencha a query e a API key.")
        return

    artigos = buscar_artigos_serpapi(query, api_key)
    caminho = salvar_para_excel(artigos, query, pasta)
    label_status.config(text=f"✅ Extração concluída. Arquivo salvo: {caminho}")

# Interface gráfica (Tkinter)
window = tk.Tk()
window.title("Google Scholar Scraper via SerpApi")
window.geometry("430x300")

tk.Label(window, text="🔍 Palavra-chave ou título:").pack()
entry_query = tk.Entry(window, width=50)
entry_query.pack()

tk.Label(window, text="🔑 API Key do SerpApi:").pack()
entry_apikey = tk.Entry(window, width=50, show="*")
entry_apikey.pack()

tk.Label(window, text="📁 Pasta de destino (opcional):").pack()
entry_folder = tk.Entry(window, width=50)
entry_folder.pack()

tk.Button(window, text="📂 Procurar", command=selecionar_pasta).pack(pady=5)
tk.Button(window, text="🚀 Extrair Artigos", command=executar_extracao).pack(pady=10)

label_status = tk.Label(window, text="")
label_status.pack()

window.mainloop()
