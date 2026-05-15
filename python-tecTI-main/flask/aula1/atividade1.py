from flask import Flask


app = Flask(__name__) # inicio o flask


@app.route('/decorar') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def decorar():
    return 'Decoradores (decorators) em Python são funções especiais que modificam ou estendem o comportamento de outras funções ou métodos sem alterar seu código-fonte original.' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento