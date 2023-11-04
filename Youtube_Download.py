import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import os
import moviepy.editor as mp
import threading

def download_video():
    url = url_entry.get()
    if not url:
        status_label.config(text="Por favor, insira uma URL válida.")
        return

    download_button.config(state="disabled")
    progress_bar.start()

    def download_thread():
        try:
            video = YouTube(url)
            audio_stream = video.streams.filter(only_audio=True).first()
            video_stream = video.streams.get_highest_resolution()

            status_label.config(text="Baixando o vídeo e o áudio...")

            audio_stream.download(output_path='temp')
            video_stream.download(output_path='downloads')

            video_path = os.path.join('temp', audio_stream.default_filename)
            wav_path = os.path.join('temp', 'audio.wav')

            video_clip = mp.AudioFileClip(video_path)
            video_clip.write_audiofile(wav_path)

            status_label.config(text="Vídeo e áudio baixados com sucesso!")

        except Exception as e:
           status_label.config(text="Erro durante o download do vídeo. Por favor, verifique a URL ou sua conexão com a internet.")

        download_button.config(state="normal")
        progress_bar.stop()

    download_thread = threading.Thread(target=download_thread)
    download_thread.start()

window = tk.Tk()
window.title("Baixar Vídeo do YouTube")
window.geometry("700x400")

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#007acc", foreground="red")
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))

url_label = ttk.Label(window, text="URL do Vídeo:")
url_label.pack(pady=10)

url_entry = ttk.Entry(window, width=70, font=("Helvetica", 12))
url_entry.pack(pady=5)

download_button = ttk.Button(window, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=10)

status_label = ttk.Label(window, text="", font=("Helvetica", 12))
status_label.pack(pady=10)

progress_bar = ttk.Progressbar(window, mode='indeterminate', length=400)
progress_bar.pack()

window.mainloop()