from gtts import gTTS
from newspaper import Article
import tkinter as tk
from tkinter import Entry, Button, Label

def converter_site_para_audio():
    url = url_entry.get().strip()  # Remove espaços em branco no início e no fim da URL
    if not url:
        loading_label.config(text="Por favor, insira um URL válido.")
        return

    loading_label.config(text="Convertendo para Áudio...")  # Atualiza a mensagem de carregamento
    janela.update()  # Atualiza a janela para mostrar a mensagem

    try:
        article = Article(url)
        article.download()
        article.parse()
        lingua = "pt"
        tts = gTTS(article.text, lang=lingua)
        tts.save("audioWeb.mp3")
        loading_label.config(text="Conversão concluída. O áudio foi salvo como 'audioWeb.mp3'.")
    except Exception as e:
        loading_label.config(text=f"Erro: {str(e)}")

# Crie uma janela principal
janela = tk.Tk()
janela.title("Conversor de Site para Áudio")

# Crie um rótulo explicativo
label = Label(janela, text="Insira o link do site que deseja converter para áudio:")
label.pack()

# Crie um campo de entrada para o URL do site
url_entry = Entry(janela, width=40)
url_entry.pack()

# Crie um botão para iniciar a conversão
converter_button = Button(janela, text="Converter para Áudio", command=converter_site_para_audio)
converter_button.pack()

# Crie uma etiqueta para indicar o status de carregamento
loading_label = Label(janela, text="", font=("Arial", 10, "italic"))
loading_label.pack()

# Inicie a interface gráfica
janela.mainloop()