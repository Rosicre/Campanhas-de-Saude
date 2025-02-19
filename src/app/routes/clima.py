import requests
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'
app.config['WTF_CSRF_ENABLED'] = False

# Substitua pelo seu token correto da API Climatempo
TOKEN = "7c159c5956afcec3b61ee03c10ecb2ac"

def obter_previsao(cidade_id):
    url_previsao = f"http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{cidade_id}/days/1?token={TOKEN}"
    print(f"URL chamada: {url_previsao}")
    response_previsao = requests.get(url_previsao)
    print(f"Status code: {response_previsao.status_code}")

    if response_previsao.status_code == 200:
        retorno = response_previsao.json()
        print(f"Resposta da API: {retorno}")

        if 'data' in retorno and retorno['data']:
            data = retorno['data'][0]
        else:
            data = {}

        return {
            'name': retorno.get('name', 'Nome não disponível'),
            'state': retorno.get('state', 'Estado não disponível'),
            'data': data.get('date_br', 'Data não disponível'),
            'chuva': data.get('rain', {}).get('probability', 'Não disponível'),
            'temp_min': data.get('temperature', {}).get('min', 'Não disponível'),
            'temp_max': data.get('temperature', {}).get('max', 'Não disponível'),
        }
    else:
        print(f"Falha ao obter dados: {response_previsao.text}")
        return None
    


@app.route('/clima', methods=['GET', 'POST'])
def clima():
    capitais = [
        {'id': '3477', 'nome': 'São Paulo'},
        {'id': '3456', 'nome': 'Rio de Janeiro'},
        {'id': '3666', 'nome': 'Brasília'},
        {'id': '3772', 'nome': 'Salvador'},
        {'id': '3478', 'nome': 'Curitiba'},
    ]

    previsao = None

    if request.method == 'POST':
        cidade_id = request.form.get('cidade_id')
        print(f"Cidade ID selecionado: {cidade_id}")
        if cidade_id:
            previsao = obter_previsao(cidade_id)

    return render_template('clima.html', capitais=capitais, previsao=previsao)

if __name__ == '__main__':
    app.run(debug=True)
