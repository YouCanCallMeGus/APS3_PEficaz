import streamlit as st
import requests
import pandas as pd

certo = "Tudo certo"

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
        
        elif response.status_code == 201:
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
    
st.title("APS3")


#Bikes
st.sidebar.header("🔍 Bikes")
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
    # Chama a função 'fazer_requisicao' para enviar uma requisição GET ao endpoint '/bikes' do backend,
    # com os parâmetros (filtros) fornecidos pelo usuário.

    # Se houver dados na resposta, exibir os imóveis
    if data:
        df_imoveis = pd.DataFrame(data['bikes'])
        
        # Converte os imóveis em um DataFrame do Pandas para exibição em tabela.
        st.write("### 🏠 Resultados da Pesquisa")
        st.dataframe(df_imoveis) 
        # Exibe os resultados da pesquisa em uma tabela interativa no frontend do Streamlit.
    elif data:
        st.write("❌ Nenhum imóvel encontrado para os filtros selecionados.")
        # Se não houver resultados (mas houver dados válidos na resposta), exibe uma mensagem dizendo que 
        # nenhum imóvel foi encontrado.

if st.sidebar.button("🔍 Buscar Bikes"):
    buscar_bikes()


def criar_bikes():
    datas = {
        'marca': marca,         
        'modelo': modelo,         
        'cidade': cidade,
    }
    data = fazer_requisicao("bikes", method="POST", data=datas)
    try:
        st.write(data['mensagem'])
    except:
        st.write(data["erro"])


if st.sidebar.button("🔍 Criar Bikes"):
    criar_bikes()

id_bike = st.sidebar.text_input("Id")

def atualizar_bike():
    dados = {
        'marca': marca,         
        'modelo': modelo,         
        'cidade': cidade,
    }
    st.write(data['mensagem'])
    data = fazer_requisicao(f"bikes/{id}", method="PUT", data=dados)

if st.sidebar.button("🔍 Atualizar bike"):
    atualizar_bike()

def deletar_bike():
    params = {
    }
    data = fazer_requisicao(f"bikes/{id}", method="DELETE", params=params)
    st.write(data['mensagem'])    
if st.sidebar.button("🔍 Deletar bike"):
    deletar_bike()

def buscar_bikes_id():

    data = fazer_requisicao(f"bikes/{id}", method="GET")

    if data:
        df_imoveis = pd.DataFrame(data)
        
        st.write("### 🏠 Resultados da Pesquisa")
        st.dataframe(df_imoveis) 
    elif data:
        st.write("❌ Nenhum imóvel encontrado para os filtros selecionados.")

if st.sidebar.button("🔍 Buscar bikes"):
    buscar_bikes_id()

#usuarios

st.sidebar.header("🔍 Usuarios")
nome = st.sidebar.text_input("Nome")
cpf = st.sidebar.text_input("cpf")
nascimento = st.sidebar.text_input("Nascimento")

def Criar_usuario():
    dados = {
        'nome': nome,         
        'cpf': cpf,         
        'data_de_nascimento': nascimento,
    }
    requisicao = fazer_requisicao("usuarios", method="POST", data=dados)
    try:
        st.write(requisicao['mensagem'])
    except:
        st.write({requisicao['id']})

def buscar_usuarios():
    # Fazendo a requisição GET para o backend
    data = fazer_requisicao("usuarios", method="GET")
    # Chama a função 'fazer_requisicao' para enviar uma requisição GET ao endpoint '/bikes' do backend,
    # com os parâmetros (filtros) fornecidos pelo usuário.

    # Se houver dados na resposta, exibir os imóveis
    if data:
        df_imoveis = pd.DataFrame(data['usuarios'])
        
        # Converte os imóveis em um DataFrame do Pandas para exibição em tabela.
        st.write("### 🏠 Resultados da Pesquisa")
        st.dataframe(df_imoveis) 
        # Exibe os resultados da pesquisa em uma tabela interativa no frontend do Streamlit.
    elif data:
        st.write("❌ Nenhum Usuário encontrado")
        # Se não houver resultados (mas houver dados válidos na resposta), exibe uma mensagem dizendo que 
        # nenhum imóvel foi encontrado.

if st.sidebar.button("🔍 Buscar usuarios"):
    buscar_usuarios()

if st.sidebar.button("🔍 Criar Usuario"):
    Criar_usuario()

id = st.sidebar.text_input("ID")

def atualizar_usuarios():
    datas = {
        'nome': nome,         
        'cpf': cpf,         
        'data_de_nascimento': nascimento,
    }

    data = fazer_requisicao(f"usuarios/{id}", method="PUT", data=datas)
    st.write(data['mensagem'])

if st.sidebar.button("🔍 Atualizar usuarios"):
    atualizar_usuarios()

def buscar_usuarios_id():
    params = {
        'nome': nome,         
        'cpf': cpf,         
        'data_de_nascimento': nascimento,
    }

    data = fazer_requisicao(f"usuarios/{id}", method="GET", params=params)

    if data:
        df_imoveis = pd.DataFrame(data)
        
        st.write("### 🏠 Resultados da Pesquisa")
        st.dataframe(df_imoveis) 
    elif data:
        st.write("❌ Nenhum imóvel encontrado para os filtros selecionados.")

if st.sidebar.button("🔍 Buscar usuarios por id"):
    buscar_usuarios_id()

def deletar_usuario():
    params = {
    }
    data = fazer_requisicao(f"usuarios/{id}", method="DELETE", params=params)
if st.sidebar.button("🔍 Deletar usuarios"):
    deletar_usuario()