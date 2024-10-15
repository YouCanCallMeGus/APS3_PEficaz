import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"

def fazer_requisicao(endpoint, method="GET", params=None, data=None):
    url = f"{BASE_URL}/{endpoint}"

    try:
        if method == "GET":
            response = requests.get(url, params=params)

        elif method == "POST":
            response = requests.post(url, json=data)

        elif method == "PUT":
            response = requests.put(url, json=data)

        elif method == "DELETE":
            response = requests.delete(url, params=params)

        else:
            st.error("Método HTTP não suportado.")

        if response.status_code == 200:
            return response.json()  
        
        elif response.status_code == 404:
            st.warning("⚠️ Recurso não encontrado.")

        elif response.status_code == 500:
            st.error("⚠️ Erro interno do servidor.")

        else:
            st.error(f"⚠️ Erro: {response.status_code} - {response.text}")

        return None  

    except Exception as e:
        st.error(f"⚠️ Erro de conexão: {e}")

        return None
    
marca = st.sidebar.text_input("Marca")
modelo = st.sidebar.text_input("Modelo")
cidade = st.sidebar.text_input("Cidade")

def buscar_bikes():
    params = {
        'marca': marca,         
        'modelo': modelo,         
        'cidade': cidade,         
    }

    # Fazendo a requisição GET para o backend
    data = fazer_requisicao("bikes", method="GET", params=params)
    # Chama a função 'fazer_requisicao' para enviar uma requisição GET ao endpoint '/imoveis' do backend,
    # com os parâmetros (filtros) fornecidos pelo usuário.

    # Se houver dados na resposta, exibir os imóveis
    if data and data['resultados']['quantidade'] > 0:
        # Se a resposta contiver resultados (quantidade de imóveis for maior que 0), exibe os imóveis encontrados.
        df_imoveis = pd.DataFrame(data['resultados']['imoveis'])
        # Converte os imóveis em um DataFrame do Pandas para exibição em tabela.
        st.write("### 🏠 Resultados da Pesquisa")
        st.dataframe(df_imoveis)
        # Exibe os resultados da pesquisa em uma tabela interativa no frontend do Streamlit.
    elif data:
        st.write("❌ Nenhum imóvel encontrado para os filtros selecionados.")
        # Se não houver resultados (mas houver dados válidos na resposta), exibe uma mensagem dizendo que 
        # nenhum imóvel foi encontrado.