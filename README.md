# Chat com Gemini AI - Lógica Proposicional e Dedução Natural

Este projeto é uma aplicação web simples usando Flask e a API Gemini (Google Generative AI) para gerar lógicas proposicionais e deduções naturais a partir de uma expressão fornecida pelo usuário.

## Descrição

A aplicação permite ao usuário enviar uma expressão em linguagem natural, e a IA do Gemini irá gerar uma lógica proposicional correspondente, assim como uma dedução natural baseada nessa expressão. A resposta é exibida de forma formatada no navegador, com suporte para negrito e outros estilos de texto.

## Funcionalidades

- Recebe uma expressão em linguagem natural do usuário.
- Gera uma lógica proposicional e uma dedução natural.
- Exibe a resposta de forma formatada (incluindo negrito).
- Comunicação com a API Gemini da Google para processamento e geração de respostas.

## Tecnologias

- **Flask**: Framework web em Python.
- **Google Gemini API**: API de IA generativa para processar e gerar respostas.
- **HTML/CSS**: Para estrutura e estilo da página.
- **JavaScript**: Para interatividade e envio de dados via AJAX.
- **Jinja2**: Template engine para renderizar HTML no Flask.

## Como Executar

### Pré-requisitos

- Python 3.x
- Instalação do Flask
- Acesso à API do Gemini (necessário uma chave API válida: [Google API Key](https://makersuite.google.com/app/apikey))

### Instalação

1. Instale o Flask:
    ```bash
    pip install Flask
    ```

2. Instale a biblioteca do Gemini:
    ```bash
    pip install -U google-generativeai
    ```

### Executando o Servidor

1. Inicie o servidor Flask:
    ```bash
    python app.py
    ```

2. Abra o navegador e acesse:
    ```
    http://127.0.0.1:5000/
    ```

3. Interaja com a IA fornecendo uma expressão e veja a lógica proposicional e a dedução natural geradas.

## Estrutura do Projeto

