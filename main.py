import streamlit as st
import requests
import json

def consulta(cidade):
  """Criar estrutura para realizar a consulta através da API de tempo
    entrada: nome da cidade/ localização GPS (lat, lon).
    Retorno: Json com dados recebidos"""

  # dados da consulta
  url_base = 'https://api.weatherapi.com/v1'
  tipo = 'current.json'
  key = '87528c1a58b848118c130106230506'
  q = cidade
  aqi = 'no'

  # criando consulta
  chamada = f"{url_base}/{tipo}?key={key}&q={q}&aqi={aqi}"

  # realizar consulta
  dado_recebido = requests.get(chamada)
  print(f'Resposta consulta (status): {dado_recebido.status_code}')

  if dado_recebido.status_code == 200:
    return json.loads(dado_recebido.content)

  else:
    return False


def exibir(dado=None):
  """Criar estrutura para exibir os dados recebidos da API utili9zando o streamlit
  Entrada: Json com dados
  Retorno: nenhum"""
  
  # Gerando exibição 
  if dado:
    cidade = dado['location']['name']
    estado = dado['location']['region']
    pais = dado['location']['country']
    temperatura = dado['current']['temp_c']
    data = dado['current']['last_updated']
    condicao = dado['current']['condition']['text']
    icone = dado['current']['condition']['icon']
    sensacao = dado['current']['feelslike_c']
    umidade = dado['current']['humidity']
    uv = dado['current']['uv']
    icone = f'https:{icone}'

  # texto para exibição
    texto = f'Previsão do tempopara cidade {cidade} - {estado}'
    st.subheader(texto)

    texto = f'ultima atualização em: {data}:'
    st.write(texto)

    texto = f"\tTemperatura: {temperatura}°C\
              \n\tSensação Térmica: {sensacao}°C\
              \n\tCondição: {condicao}\
              \n\tUmidade relativa: {umidade}%\
              \n\tRadiação Solar (UV): {uv}"
    
    st.write(texto)
    st.image(icone)


  else:
    texto = 'Cidade não localizada'
    st.write(texto)


# dISCIPLINA = 'PROJETO DE BLOCO'
# link = 'https://lms.infnet.edu.br/moodle/login/index.php'
# titulo = f'Atividade da disciplina [{dISCIPLINA}] ({link}) '



titulo = 'Previsão do Tempo'
st.title(titulo)

cidade = st.sidebar.text_input('Informe a Cidade ou Latitude e longitude')

text = f'Previsão do tempo para {cidade}'
st.write(text)
if cidade: 
  dado = consulta(cidade)
  # exibir(dado)

