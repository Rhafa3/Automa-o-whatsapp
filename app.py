from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# Função para enviar mensagem para um contato/grupo
def enviar_mensagem(contato_grupo, mensagem):
    try:
        # Localiza o campo de pesquisa
        search_box = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
        # Digita o nome do contato/grupo
        search_box.send_keys(contato_grupo)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)  # Aguarda um pouco para garantir que o chat seja aberto

        # Localiza o campo de mensagem
        message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')

        # Digita a mensagem
        message_box.send_keys(mensagem)
        # Envia a mensagem
        message_box.send_keys(Keys.ENTER)
        time.sleep(2)  # Aguarda um pouco para enviar a próxima mensagem
    except Exception as e:
        print(f"Erro ao enviar mensagem para {contato_grupo}: {str(e)}")
        # Mostra a mensagem de erro apenas para quem está com o código
        messagebox.showerror("Erro", f"Erro ao enviar mensagem para {contato_grupo}: {str(e)}")

# Função para carregar contatos do arquivo Excel
def carregar_contatos():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
    if file_path:
        return pd.read_excel(file_path)
    else:
        return None

# Função para enviar mensagens para contatos
def enviar_mensagens():
    mensagem = entry_mensagem.get()  # Obtém a mensagem digitada pelo usuário
    if not mensagem:
        messagebox.showerror("Erro", "Por favor, digite uma mensagem.")
        return
    contatos_df = carregar_contatos()
    if contatos_df is not None:
        for index, row in contatos_df.iterrows():
            contato_grupo = row['Contato']
            enviar_mensagem(contato_grupo, mensagem)
        driver.quit()

# Inicializa o navegador
driver = webdriver.Chrome()

# Cria a interface gráfica
root = tk.Tk()
root.title("Envio de Mensagens WhatsApp")

# Define o estilo do tema
style = ttk.Style(root)
style.theme_use("clam")

# Define estilos para os widgets
style.configure("TButton", padding=10, font=("Arial", 12))
style.configure("TLabel", padding=10, font=("Arial", 12))
style.configure("TEntry", padding=10, font=("Arial", 12))

# Campo de entrada para a mensagem
lbl_mensagem = ttk.Label(root, text="Digite a mensagem:")
lbl_mensagem.pack(pady=10)
entry_mensagem = ttk.Entry(root, width=50)
entry_mensagem.pack(pady=5)

# Função para iniciar o envio de mensagens
def iniciar_envio():
    enviar_mensagens()
    root.destroy()

# Botão para iniciar o envio de mensagens
btn_iniciar = ttk.Button(root, text="Iniciar Envio de Mensagens", command=iniciar_envio)
btn_iniciar.pack(pady=20)

root.mainloop()