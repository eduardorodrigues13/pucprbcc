import requests
import time

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao Broker MQTT!")
    else:
        print("Falha na conexão, código de retorno %d\n", rc)

def on_publish(client, userdata, mid):
    print("Mensagem publicada com ID:", mid)

# Dados de conexão
broker_address = "mqtt-dashboard.com"
broker_port = 8883
topic = "teste22"
username = "edu"
password = "edu"

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=LAF4F1SOZ1DKIJC1'
r = requests.get(url)
data = r.json()

print(data)

def buscar_taxa_de_cambio():
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BRL&to_currency=USD&apikey=X57VJYEY6BDE0RMQ'
    r = requests.get(url)
    data = r.json()
    moedaOrigem = data['Realtime Currency Exchange Rate']['1. From_Currency Code']
    nomeMoedaOrigem = data['Realtime Currency Exchange Rate']['2. From_Currency Name']
    moedaDestino = data['Realtime Currency Exchange Rate']['3. To_Currency Code']
    nomeMoedaDestino = data['Realtime Currency Exchange Rate']['4. To_Currency Name']
    taxaCambio = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    taxaCambio = float(taxaCambio)
    taxaCambio = round(taxaCambio, 2)
    ultimaAtualizacao = data['Realtime Currency Exchange Rate']['6. Last Refreshed']
    return moedaOrigem, moedaDestino, taxaCambio, ultimaAtualizacao

# Cria o cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Define as credenciais
client.username_pw_set(username, password)

# Habilita TLS
client.tls_set()

# Conecta ao broker
client.connect(broker_address, broker_port)

# Inicia o loop de rede em segundo plano
client.loop_start()

taxa_cambio_anterior = None

while True:
    moedaOrigem, moedaDestino, taxaCambio, ultimaAtualizacao = buscar_taxa_de_cambio()
    
    if taxa_cambio_anterior is None:
        print(f"{moedaOrigem} ---> {moedaDestino}")
        print(taxaCambio)
        print(ultimaAtualizacao)
    else:
        if taxaCambio > taxa_cambio_anterior:
            print(f"Taxa de câmbio aumentou de {taxa_cambio_anterior} para {taxaCambio}")
        elif taxaCambio < taxa_cambio_anterior:
            print(f"Taxa de câmbio diminuiu de {taxa_cambio_anterior} para {taxaCambio}")
        else:
            print(f"Taxa de câmbio permanece a mesma: {taxaCambio}")
    
    taxa_cambio_anterior = taxaCambio
    
    # Mensagem a ser enviada
    mensagem = f'{moedaOrigem} ---> {moedaDestino} \n {taxaCambio}'

    # Publica a mensagem
    result = client.publish(topic, mensagem)

    # Verifica o resultado da publicação
    status = result[0]
    if status == 0:
        print(f"Mensagem enviada para o tópico '{topic}'")
    else:
        print(f"Falha ao enviar mensagem para o tópico '{topic}'")

    # Aguarda 5 segundos
    time.sleep(5)

# Encerra o loop de rede
client.loop_stop()
