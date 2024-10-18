import streamlit as st
import requests
import pandas as pd

certo = "Tudo certo"

BASE_URL = "https://aps-3-flask-rest-mongo-backend.onrender.com"

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
              
        elif response.status_code == 400:
            st.warning("⚠️ Ops, parece que algo deu errado com seu formulário...")      

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
        
        st.write("### 🚲 Resultados da Pesquisa")
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
    if data:
        st.write(data['mensagem'])

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

    if data['bike']:
        df_bike = pd.DataFrame(data['bike'])
        st.write("### 🚲 Resultados da Pesquisa")
        st.dataframe(df_bike) 
    else:
        st.write("❌ Nenhuma Bike encontrada")


#inputs bike
st.sidebar.header("Bikes")

if st.sidebar.button("🔍 Buscar Todas As Bikes"):
    buscar_bikes()

with st.sidebar.popover("🚲 Criar Bike"):
    marca = st.text_input('Marca', key='POST_marca')
    modelo = st.text_input("Modelo", key='POST_modelo')
    cidade = st.text_input("Cidade", key='POST_cidade')
    enviar = st.button("Enviar", key="POST_envio_bike")
if enviar:
    criar_bikes(marca,modelo,cidade)

with st.sidebar.popover("🔁 Atualizar Bike"):
    marca = st.text_input('Marca', key='PUT_marca')
    modelo = st.text_input("Modelo", key='PUT_modelo')
    cidade = st.text_input("Cidade", key='PUT_cidade')
    id_bike = st.text_input("ID", key='PUT_ID')
    enviar = st.button("Enviar",key="PUT_envio_bike")
if enviar:
    atualizar_bike(marca,modelo,cidade,id_bike)

with st.sidebar.popover("❌ Deletar Bike"):
    id_bike = st.text_input("ID", key='DELETE_ID')
    enviar = st.button("Enviar",key="DELETE_envio_bike")
if enviar:    
    deletar_bike(id_bike)

with st.sidebar.popover("📌 Achar Bike"):
    id_bike = st.text_input("ID", key='GET_ID')
    enviar = st.button("Enviar",key="GET_envio_bike")
if enviar:
    buscar_bikes_id(id_bike)

#usuarios
def Criar_usuario(nome,cpf,nascimento):
    dados = {
        'nome': nome,         
        'cpf': cpf,         
        'data_de_nascimento': nascimento,
    }
    requisicao = fazer_requisicao("usuarios", method="POST", data=dados)
    if requisicao:
        st.write(requisicao['mensagem'])

def buscar_usuarios():
    data = fazer_requisicao("usuarios", method="GET")
    if data['usuarios'] != []:
        df_usuarios = pd.DataFrame(data['usuarios'])
        st.write("### 🚲 Resultados da Pesquisa")
        st.dataframe(df_usuarios) 
    else:
        st.write("❌ Nenhum Usuário encontrado")

def atualizar_usuarios(nome,cpf,nascimento,id_usuario):
    datas = {
        'nome': nome,         
        'cpf': cpf,         
        'data_de_nascimento': nascimento,
    }

    data = fazer_requisicao(f"usuarios/{id_usuario}", method="PUT", data=datas)
    if data:
        st.write(data['mensagem'])

def buscar_usuarios_id(id_users):
    data = fazer_requisicao(f"usuarios/{id_users}", method="GET")
    if data:
        df_imoveis = pd.DataFrame(data)
        st.write("### 🚲 Resultados da Pesquisa")
        st.dataframe(df_imoveis) 


def deletar_usuario(id_user):
    data = fazer_requisicao(f"usuarios/{id_user}", method="DELETE")
    if data:
        st.write(data['mensagem'])  

#inputs usuarios
st.sidebar.header("Usuarios")

if st.sidebar.button("🔍 Buscar usuarios"):
    buscar_usuarios()

with st.sidebar.popover("🧕 Criar Usuário"):
    nome = st.text_input('Nome', key='POST_nome')
    cpf = st.text_input("Cpf", key='POST_cpf')
    nascimento = st.text_input("Data de nascimento", key='POST_nascimento')
    enviar = st.button("Enviar", key="POST_envio_usuario")
if enviar:
    Criar_usuario(nome,cpf,nascimento)

with st.sidebar.popover("🔁 Atualizar Usuário"):
    nome = st.text_input('Nome', key='PUT_nome')
    cpf = st.text_input("Cpf", key='PUT_cpf')
    nascimento = st.text_input("Data de nascimento", key='PUT_nascimento')
    id_usuario = st.text_input("ID", key='PUT_IDs')
    enviar = st.button("Enviar", key="PUT_envio_usuario")
if enviar:
    atualizar_usuarios(nome,cpf,nascimento,id_usuario)

with st.sidebar.popover("❌ Deletar usuario"):
    id_user = st.text_input("ID", key='DELETE_IDs')
    enviar = st.button("Enviar",key="DELETE_envio_usuario")
if enviar:    
    deletar_usuario(id_user)

with st.sidebar.popover("📌 Achar usuario"):
    id_users = st.text_input("ID", key='GET_IDs')
    enviar = st.button("Enviar",key="GET_envio_usuario")
if enviar:
    buscar_usuarios_id(id_users)


#emprestimos
def buscar_emprestimo():
    data = fazer_requisicao("emprestimos", method="GET")
    if data:
        df_usuarios = pd.DataFrame(data['emprestimos'])
        st.write("### Resultados da Pesquisa")
        st.dataframe(df_usuarios) 
    

def cria_emprestimo(id_usuario, id_bikes):
    dados = {
        'id_usuario': id_usuario,         
        'id_bikes': id_bikes     
    }
    requisicao = fazer_requisicao(f"/emprestimos/usuarios/{id_usuario}/bikes/{id_bikes}", method="POST", data=dados)
    if requisicao:
        st.write(requisicao['mensagem'])

def deletar_emprestimo(id_emprestimo):
    data = fazer_requisicao(f"emprestimos/{id_emprestimo}", method="DELETE")
    if data:
        st.write(data['mensagem']) 

#inputs emprestimos
st.sidebar.header("Empréstimo")

if st.sidebar.button("🔍 Buscar empréstimo"):
    buscar_emprestimo()

with st.sidebar.popover("Criar Empréstimo"):
    id_usuario = st.text_input('ID_user', key='POST_emprestimo')
    id_bikes = st.text_input("ID_bikes", key='POST_emprestimos')
    enviar = st.button("Enviar", key="POST_envio_emprestimo")
if enviar:
    cria_emprestimo(id_usuario, id_bikes)

with st.sidebar.popover("❌ Deletar Empréstimo"):
    id_emprestimo = st.text_input("ID Empréstimo", key='DELETE_ID_emprestimo')
    enviar = st.button("Enviar",key="DELETE_envio_emprestimo")
if enviar:    
    deletar_emprestimo(id_emprestimo)