from senha import API_KEY  # Certifique-se de que o arquivo senha.py contém a variável API_KEY
import json
import openai

# Configurando a chave da API do OpenAI
openai.api_key = API_KEY

# Variável que define a mensagem inicial para o comportamento do modelo
mensagens = [
    {"role": "system", "content": "Você é um analisador de sentenças lógicas de qualquer tipo, seja ela lógica proposicional ou qualquer outra."}
]

# Loop principal para interação com o usuário
while True:
    # Solicita a entrada do usuário
    prompt = input('Digite sua mensagem (ou digite "fim" para encerrar): ')
    
    # Verifica se o usuário deseja encerrar o programa
    if prompt.strip().lower() == 'fim':
        print("Encerrando o programa. Até mais!")
        break

    # Adiciona a mensagem do usuário à lista de mensagens
    mensagens.append({"role": "user", "content": prompt})

    try:
        # Faz a chamada para a API do OpenAI
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=mensagens,
            temperature=1.0,  # Controle da aleatoriedade da resposta
            max_tokens=2000   # Número máximo de tokens para a resposta
        )

        # Extrai a resposta gerada pelo modelo
        resposta = response['choices'][0]['message']['content']

        # Adiciona a resposta à lista de mensagens para manter a memória do chat
        mensagens.append({"role": "assistant", "content": resposta})

        # Exibe a resposta ao usuário
        print("Resposta:", resposta)

    except Exception as e:
        # Trata erros de maneira elegante
        print("Ocorreu um erro ao acessar a API:", e)
