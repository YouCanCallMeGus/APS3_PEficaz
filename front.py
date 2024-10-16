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
def buscar_bikes():
    data = fazer_requisicao("bikes", method="GET")
    if data['bikes']:
        df_bikes = pd.DataFrame(data['bikes'])
        
        st.write("### 🏠 Resultados da Pesquisa")
        st.dataframe(df_bikes) 
    else:
        st.write("❌ Nenhuma Bike encontrada")

def criar_bikes(marca,modelo,cidade):
    datas = {
        'marca': marca,         
        'modelo': modelo,         
        'cidade': cidade,
    }
    data = fazer_requisicao("bikes", method="POST", data=datas)
    try:
        st.write(data['mensagem'])
    except:
        st._main.write(data["erro"])

def atualizar_bike(marca,modelo,cidade,id_bike):
    dados = {
        'marca': marca,         
        'modelo': modelo,         
        'cidade': cidade,
    }
    data = fazer_requisicao(f"bikes/{id_bike}", method="PUT", data=dados)
    if data:
        st.write(data['mensagem'])

def deletar_bike(id_bike):
    data = fazer_requisicao(f"bikes/{id_bike}", method="DELETE")
    if data:
        st.write(data['mensagem'])   

def buscar_bikes_id(id_bike):
    data = fazer_requisicao(f"bikes/{id_bike}", method="GET")

    if data:
        df_bike = pd.DataFrame(data)
        
        st.write("### 🏠 Resultados da Pesquisa")
        st.dataframe(df_bike) 
    elif data:
        st.write("❌ Nenhuma Bike encontrada")


#inputs bike
df_bike = ''
st.sidebar.header("Bikes")

if st.sidebar.button("Buscar Todas As Bikes"):
    buscar_bikes()

with st.sidebar.popover("Criar Bike"):
    marca = st.text_input('Marca', key='POST_marca')
    modelo = st.text_input("Modelo", key='POST_modelo')
    cidade = st.text_input("Cidade", key='POST_cidade')
    enviar = st.button("Enviar", key="POST_envio_bike")
if enviar:
    criar_bikes(marca,modelo,cidade)

with st.sidebar.popover("Atualizar Bike"):
    marca = st.text_input('marca', key='PUT_marca')
    modelo = st.text_input("modelo", key='PUT_modelo')
    cidade = st.text_input("cidade", key='PUT_cidade')
    id_bike = st.text_input("ID", key='PUT_ID')
    enviar = st.button("Enviar",key="PUT_envio_bike")
if enviar:
    atualizar_bike(marca,modelo,cidade,id_bike)

with st.sidebar.popover("Deletar Bike"):
    id_bike = st.text_input("ID", key='DELETE_ID')
    enviar = st.button("Enviar",key="DELETE_envio_bike")
if enviar:    
    deletar_bike(id_bike)

with st.sidebar.popover("Achar Bike"):
    id_bike = st.text_input("ID", key='GET_ID')
    enviar = st.button("Enviar",key="GET_envio_bike")
if enviar:
    buscar_bikes_id(id_bike)

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