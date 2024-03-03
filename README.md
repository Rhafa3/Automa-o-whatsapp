
---

# Envio de Mensagens WhatsApp

Este é um programa desenvolvido em Python que permite enviar mensagens para contatos do WhatsApp usando a interface web do WhatsApp Web. Ele foi criado usando a biblioteca `selenium` para automatizar a interação com o navegador e a biblioteca `tkinter` para criar a interface gráfica.

## Funcionalidades

- Carregar contatos a partir de um arquivo Excel.
- Permitir que o usuário digite a mensagem a ser enviada.
- Enviar a mesma mensagem para todos os contatos carregados.
- Exibir mensagens de erro caso ocorra algum problema durante o envio.

## Pré-requisitos

- Python 3.x instalado.
- Bibliotecas `selenium`, `pandas`, `tkinter` e `ttkthemes` instaladas. Você pode instalá-las usando pip:
  ```
  pip install selenium pandas ttkthemes
  ```
- Um driver de navegador compatível com o Selenium. Neste código, usamos o ChromeDriver.

## Como usar

1. Clone ou baixe este repositório para o seu computador.
2. Certifique-se de ter todos os pré-requisitos instalados.
3. Execute o arquivo `envio_mensagens_whatsapp.py`.
4. Na interface gráfica, clique no botão "Escolher Arquivo" e selecione um arquivo Excel contendo a lista de contatos.
5. Digite a mensagem que deseja enviar no campo de entrada.
6. Clique no botão "Iniciar Envio de Mensagens" para enviar a mensagem para todos os contatos carregados.

## Avisos

- Este programa utiliza a interface web do WhatsApp Web para enviar mensagens. Certifique-se de não violar os termos de serviço do WhatsApp ao utilizá-lo.
- Este programa pode não funcionar corretamente se houver mudanças na estrutura do WhatsApp Web.

---
