# 📚 Scholar Scraper via SerpApi

Este script permite extrair até **60 resultados** de artigos acadêmicos do **Scholar** usando a **API do SerpApi**, com base em uma **palavra-chave ou expressão de busca personalizada**. Ele salva os resultados em um arquivo `.xlsx` (Excel), contendo título, autores, data de publicação, snippet (resumo) e link direto para o artigo.

A aplicação possui uma interface gráfica amigável desenvolvida em **Tkinter**, facilitando seu uso sem necessidade de linha de comando.

---

## ✅ Funcionalidades

- Busca automatizada no **Scholar** via SerpApi.
- Retorna até **60 artigos por consulta**.
- Salva os seguintes campos:
  - Título
  - Autores
  - Data de publicação
  - Snippet (resumo)
  - Link direto
- Geração automática de planilha `.xlsx` com nome baseado na **query** + **data atual**.
- Interface gráfica simples para facilitar o uso.

---

## 📦 Requisitos

Antes de executar o script, certifique-se de ter os seguintes pacotes instalados:

```bash
pip install requests pandas openpyxl
```

Você também precisa criar uma conta gratuita no [SerpApi](https://serpapi.com/) para obter sua **API Key**.

- Com a conta gratuita, você pode realizar até **100 buscas por mês** gratuitamente.
- A chave é necessária para autenticar as requisições ao Scholar.

---

## ▶️ Como usar

1. Clone este repositório ou baixe os arquivos.
2. Instale as dependências indicadas com `pip`.
3. Crie uma conta gratuita no [SerpApi](https://serpapi.com/) e copie sua **API Key**.
4. Execute o script principal:

```bash
python pesquisador_v1.py
```

5. Na interface que abrir:
   - Insira a sua **palavra-chave de busca**.
   - Insira sua **API Key do SerpApi**.
   - (Opcional) Escolha uma **pasta de destino** para salvar a planilha.
   - Clique em **“Extrair Artigos”**.
6. O arquivo será salvo no formato:  
   `sua_busca_YYYY-MM-DD.xlsx`

---

## 🧪 Exemplo de uso

Consulta:  
```
musealization AND emulation
```

Arquivo gerado:  
```
musealization_AND_emulation_2025-04-07.xlsx
```

---

## ⚠️ Limitações

- O script depende da SerpApi, que possui um **limite de 100 buscas gratuitas por mês** com a conta gratuita.
- A extração é limitada a **60 artigos por query**, respeitando a paginação da API. Entretanto isso pode ser alterado no código, leve em consideração que cada página de resultados conta como **uma busca** para o SerpApi.

---

## 📃 Licença

Este projeto pode ser utilizado livremente com os devidos créditos. Licença MIT.
