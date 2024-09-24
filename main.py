import yt_dlp

def download_audio(url):  
    Title = input("Entrez le nom du fichier audio : ")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{Title}.%(ext)s',  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_video(url):  
    Title = input("Entrez le nom du fichier vidéo : ")
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  
        'merge_output_format': 'mp4',  
        'outtmpl': f'{Title}.%(ext)s',  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    logo = """
  _____                      _                 _  __     __         _         _          
 |  __ \                    | |               | | \ \   / /        | |       | |         
 | |  | | _____      ___ __ | | ___   __ _  __| |  \ \_/ /__  _   _| |_ _   _| |__   ___ 
 | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |   \   / _ \| | | | __| | | | '_ \ / _ \\
 | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |    | | (_) | |_| | |_| |_| | |_) |  __/
 |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|    |_|\___/ \__,_|\__|\__,_|_.__/ \___|
                                                                                         
                                                                                         
 """
    print (logo)
    video_url = input("Entrez l'URL de la vidéo YouTube : ")
    while True:
        print('Menu : \n 1- Télécharger l\'audio de la vidéo')
        print(' 2- Télécharger la vidéo')
        print(' 3- Quitter')
        
        choice = input("Votre choix : ").strip()
        
        if choice == '1':
            download_audio(video_url)
            break  
        elif choice == '2':
            download_video(video_url)
            break  
        elif choice == '3':
            print("Fermeture du script.")
            break  
        else:
            print("Choix invalide, veuillez réessayer.")
