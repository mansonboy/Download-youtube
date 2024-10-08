from tkinter import *
from tkinter.messagebox import showerror, showinfo
import yt_dlp

# Fonction for download audio
def download_audio():  
    Title = value2.get()  
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{Title}.%(ext)s',  
    }
    
    #Verify status of download
    video_url = entree.get()  
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        showinfo("Téléchargement terminé", f"Le fichier {Title}.mp3 a été téléchargé avec succès !")
    except Exception as e:
        showerror("Erreur de téléchargement", f"Le téléchargement a échoué : {str(e)}")

# Fonction for download video
def download_video():  
    Title = value2.get() 
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  
        'merge_output_format': 'mp4',  
        'outtmpl': f'{Title}.%(ext)s',  
    }

    #Verify status of download
    video_url = entree.get()  
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        showinfo("Téléchargement terminé", f"Le fichier {Title}.mp4 a été téléchargé avec succès !")
    except Exception as e:
        showerror("Erreur de téléchargement", f"Le téléchargement a échoué : {str(e)}")

# Fonction for choice of download
def download():
    if value_radio.get() == "mp3":
        download_audio()
    elif value_radio.get() == "video":
        download_video()
    else:
        showerror("Erreur", "Veuillez sélectionner un format de téléchargement.")

# Create window
fenetre = Tk()
fenetre['bg'] = 'white'

# Title App
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE, width=400)
Frame1.pack(side=TOP, padx=30, pady=30, anchor=N, fill="x")
Label(Frame1, text="Downloader Youtube", font=("Helvetica", 30)).pack(padx=10, pady=10)

# Title link
link = LabelFrame(Frame1, text="Vidéo", padx=20, pady=20, font=("Helvetica", 22))
link.pack(fill="both", expand=True, padx=10, pady=10)
Label(link, text="Lien de la vidéo :", font=("Helvetica", 16), anchor=W).pack(side=LEFT, padx=10, pady=10)

# Input
value = StringVar() 
entree = Entry(link, textvariable=value, width=30, bg="white")
entree.pack(side=LEFT, padx=10, pady=10)

# Option mp3 or mp4
value_radio = StringVar()  
bouton1 = Radiobutton(link, text="MP3", variable=value_radio, value="mp3")
bouton2 = Radiobutton(link, text="VIDEO", variable=value_radio, value="video")
bouton1.pack(side=LEFT, padx=10, pady=5)  
bouton2.pack(side=LEFT, padx=10, pady=5)  

# Title file
titleFile = LabelFrame(Frame1, text="Votre fichier", padx=20, pady=20, font=("Helvetica", 22))
titleFile.pack(fill="both", expand=True, padx=10, pady=10)
Label(titleFile, text="Nom pour votre fichier :", font=("Helvetica", 16), anchor=W).pack(side=LEFT, padx=10, pady=10)

# Input file
value2 = StringVar() 
choiceTitle = Entry(titleFile, textvariable=value2, width=30, bg="white")
choiceTitle.pack(side=LEFT, padx=10, pady=10)

# Button download
buttonDownload = Button(Frame1, text="Télécharger", command=download)
buttonDownload.pack(padx=10, pady=10)

fenetre.mainloop()
