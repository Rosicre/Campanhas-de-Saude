from flask import Blueprint, flash, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from flask_babel import format_datetime
import requests

from ..models import Post
from ..forms import RegistrationForm, UpdateAccountForm
from ..controllers import register_user, update_user, get_user_data
from ..controllers.helpers import get_medico
from ..models.historico import Historico
from .clima import obter_previsao
from . import views  # Certifique-se de que está importando a instância de "views"




views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home():
    postagens = Post.query.all()

    # Formata a data para exibição
    for post in postagens:
        post.data_formatada = format_datetime(
            post.data_publicacao, "EEEE, d 'de' MMMM 'de' yyyy")

    return render_template('home.html', postagens=postagens)


@views.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        return register_user(form=form)

    return render_template('register.html', title='Registrar', form=form)


@views.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    medico = get_medico()
    if form.validate_on_submit():
        update_user(form=form)
    elif request.method == 'GET':
        get_user_data(form=form)
    return render_template(
        'account.html',
        title='Conta', form=form, crm=medico.crm if medico else None)

@views.route('/dengue')
def dengue_info():
    return render_template('dengue_info.html')


@views.route('/contato')
def contato():
    return render_template('contato.html')



@views.route('/enviar-contato', methods=['POST'])
def enviar_contato():
    try:
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        # Processamento
        return redirect(url_for('views.obrigado'))
    except Exception as e:
        flash(f'Ocorreu um erro: {str(e)}', 'danger')
        return redirect(url_for('views.contato'))


@views.route('/aids_info')
def aids_info():
    return render_template('aids_info.html')


@views.route('/saude_mental_info')
def saude_mental_info():
    return render_template('saude_mental_info.html')

@views.route('/gripe-covid')
def gripe_covid_info():
    return render_template('gripe-covid_info.html')


@views.route('/cancer_de_pele_info')
def cancer_de_pele_info():
    return render_template('cancer_de_pele_info.html')


@views.route('/campanha_do_sono_info')
def campanha_do_sono_info():
    return render_template('campanha_do_sono_info.html')


from flask import render_template

@views.route('/historico')
def historico():
    # Exemplo de dados a serem exibidos (isto pode vir de um banco de dados, por exemplo)
    historico_data = [
        {'id': 1, 'data': '19/11/2024', 'descricao': 'Exemplo de entrada no histórico'},
        {'id': 2, 'data': '18/11/2024', 'descricao': 'Outra entrada no histórico'},
    ]
    return render_template('historico.html', historico_data=historico_data)




# Token da API do Climatempo
TOKEN = "7c159c5956afcec3b61ee03c10ecb2ac"

def obter_previsao(cidade_id):
    url_previsao = f"http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{cidade_id}/days/1?token={TOKEN}"
    response = requests.get(url_previsao)

    if response.status_code == 200:
        retorno = response.json()
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
    return None

@views.route('/clima', methods=['GET', 'POST'])
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
        print(f"Cidade ID recebido: {cidade_id}")
        if cidade_id:
            previsao = obter_previsao(cidade_id)
            if not previsao:
                print("Previsão não encontrada.")
        else:
            print("ID da cidade está vazio.")

    return render_template('clima.html', capitais=capitais, previsao=previsao)
