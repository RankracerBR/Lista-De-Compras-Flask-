from flask import Flask,render_template,request

app = Flask(__name__)

lista = dict()

class Produto:
  def __init__(self,nome,marca,valor):
    self.nome = nome    
    self.marca = marca
    self.valor = valor

@app.route('/')
def index():
    return render_template('index.html',produtos=lista)

@app.route('/cadastrar',methods=['GET','POST'])
def cadastro():  #método para cadastro
    nome = request.form['nome']
    marca= request.form['marca']
    valor = request.form['valor']
    lista[marca] = Produto(nome,marca,valor)
    return render_template('index.html',produto=lista)


@app.route('/mostrar',methods=['GET'])
def mostrar(): #mostrar os produtos que foram registrados
    return render_template('index2.html',produtos=lista)


@app.route('/marcas',methods=['GET'])
def marcas_parceiras():
    return render_template('index3.html')

@app.route('/remover',methods=['POST'])
def remover():
    nome = request.form['nome']
    marca= request.form['marca']
    valor = request.form['valor']
    lista[marca] = Produto(nome,marca,valor)
    del lista[marca]
    return render_template('index2.html',produtos=lista)


@app.route('/somar',methods=['POST'])
def soma_total():
    nome = request.form['nome']
    marca= request.form['marca']
    valor = request.form['valor']
    lista[marca] = Produto(nome,marca,valor)
    total = int(valor[0]) + int(valor[::-1])
    return render_template('index2.html',total=total)   

app.run(port=5000)
