import os
from gtts import gTTS
import tkinter as tk
from tkinter import Text, Button, Label, ttk
import threading

def criar_audio():
    texto = texto_entry.get("1.0", "end-1c")  # "1.0" indica o início do texto e "end-1c" é o final sem o caractere final de quebra de linha
    lingua = "pt"  # Defina o idioma desejado

    criar_audio_button.config(state="disabled")  # Desativa o botão enquanto o áudio está sendo criado
    progress_bar.start()  # Inicia a barra de progresso

    def criar_audio_thread():
        tts = gTTS(texto, lang=lingua)
        tts.save("audio.mp3")

        # Toca o áudio sem precisar abrir o arquivo
        os.system("ffplay -autoexit -nodisp audio.mp3")

        progress_bar.stop()  # Para a barra de progresso
        criar_audio_button.config(state="normal")  # Reativa o botão

    audio_thread = threading.Thread(target=criar_audio_thread)
    audio_thread.start()

# Cria uma janela principal
janela = tk.Tk()
janela.title("Texto Para Falar")

# Cria um rótulo explicativo
label = Label(janela, text="Digite o texto que você deseja transformar em áudio:")
label.pack()

# Cria um campo de texto para o usuário digitar o texto
texto_entry = Text(janela, height=5, width=40)
texto_entry.pack()

# Cria um botão para criar o áudio
criar_audio_button = Button(janela, text="Criar Áudio", command=criar_audio)
criar_audio_button.pack()

# Cria uma barra de progresso
progress_bar = ttk.Progressbar(janela, mode="indeterminate")
progress_bar.pack()

# Inicia a interface gráfica
janela.mainloop()