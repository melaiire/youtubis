from pytubefix import YouTube
import tkinter as tk
from tkinter import messagebox, filedialog
import os
from PIL import ImageTk, Image

#holi mi test de apis y automatizacion  y tkinter basico
#me demore un huevo pa poder ponerle bg y icono tuve que buscar un webo en stackoverflow ff

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def descargar_video():
    url = entrada_url.get()  #pa sacar la url del textbox
    
    try:
        # objetoyutubis
        yt = YouTube(url)
        
        video = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()

        carpeta_destino = filedialog.askdirectory()
        
        if not carpeta_destino:
            return
        
        video.download(output_path=carpeta_destino)
        messagebox.showinfo("salio bien", f"descarga completada (❁´◡`❁)\n{yt.title}")
    
    except Exception as e:
        messagebox.showerror("error", f"hubo un error con:\n{str(e)}")
ventana = tk.Tk()
ventana.title("Youtube video DOWNLOADER ‱ ")
ventana.geometry("587x856")

bg_img_path = os.path.join(BASE_DIR, "nubby.png")
icon_path = os.path.join(BASE_DIR, "icono.ico")


#testeo de fondo sino no me abre el hijo de la m
try:
    img = Image.open(bg_img_path)
    bg_image = ImageTk.PhotoImage(img)
    
    bg_label = tk.Label(ventana, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 
    
except FileNotFoundError:
    bg_label = tk.Label(ventana, bg="white")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    print(f"error no se encontro el{bg_img_path}")

#pa probar el icono 
try:
    ventana.iconbitmap(icon_path)
except tk.TclError:
    print(f"error no se encontro el icono en: {icon_path}")

#el coso de la etiqueta por si se me olvida q es esto q se me olvida el tkinter
tk.Label(ventana, text="Pegar enlace del yutubis\nヾ(•ω•`)o").pack(pady=5)
entrada_url = tk.Entry(ventana, width=50)
entrada_url.pack(pady=50)

# boton de descarga tbm por si las moscas
btn_descargar = tk.Button(ventana, text="descargar vidio (❁´◡`❁)", command=descargar_video, bg="white")
btn_descargar.pack(pady=5)



ventana.mainloop()
