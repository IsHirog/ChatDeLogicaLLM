from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configuração da API
genai.configure(api_key="DIGITE SUA CHAVE")

# Inicialização do modelo
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_with_ai():
    user_input = request.form['user_input']
    
    # Atualizando o texto da solicitação com a instrução para gerar a lógica proposicional e dedução natural
    texto2 = f"Dada uma expressão: {user_input}, eu quero uma lógica proposicional esquematizada em texto. Me gere também uma dedução natural de: {user_input}"
    
    try:
        # Enviando a mensagem ao modelo de IA
        response = chat.send_message(texto2)
        ai_response = response.text

        # Retornando a resposta gerada pelo AI em formato JSON
        return jsonify({'response': ai_response})

    except Exception as e:
        # Caso ocorra algum erro ao processar a solicitação, retornamos um erro
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
