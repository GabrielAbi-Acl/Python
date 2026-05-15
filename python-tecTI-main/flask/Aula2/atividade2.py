from flask import Flask

app = Flask(__name__)

@app.route('/')
def curriculo():
    nome = "Gabriel"
    endereco = "Rua professora bartira mourao 126"
    ocupacao = "Engenheiro de Software"
    educacao = "Ensino medio/tecnico incompleto"
    
    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo - {nome}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 40px;
                color: #333;
            }}
            .container {{
                max-width: 600px;
                background: #fff;
                padding: 30px;
                margin: 0 auto;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
                margin-bottom: 5px;
            }}
            .cargo {{
                color: #7f8c8d;
                font-size: 1.2em;
                margin-top: 0;
                margin-bottom: 20px;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
            }}
            .info-section {{
                margin-bottom: 15px;
            }}
            .label {{
                font-weight: bold;
                color: #2c3e50;
            }}
        </style>
    </head>
    <body>

    <div class="container">
        <h1>{nome}</h1>
        <p class="cargo">{ocupacao}</p>
        
        <div class="info-section">
            <p><span class="label">Endereço:</span> {endereco}</p>
        </div>
        
        <div class="info-section">
            <p><span class="label">Educação:</span> {educacao}</p>
        </div>
    </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
