from pygame  import mixer # Carregar a biblioteca necessária
from tkinter.filedialog import askopenfilename
from tkinter import *

musicas = []
TAM     = len(musicas)

class Reprodutor :
	def __init__ (self):
		pass

	def reproduzir(_musica):
		mixer.init()
		print(_musica)
		musica_atual = mixer.music.load(_musica)
		musica_atual = mixer.music.play()

	def reproduzira():
		Reprodutor.reproduzir("binaural_144.0_157.0 - ALFA.wav")

	def reproduzirb():
		Reprodutor.reproduzir("binaural_144.0_178.0 - BETA.wav")

	def reproduzirt():
		Reprodutor.reproduzir("binaural_144.0_149.0 - TETA.wav")

	def reproduzird():
		Reprodutor.reproduzir("binaural_144.0_146.0 - DELTA.wav")

	def pausar ():
		musica_atual = mixer.music.pause()
		

player = Reprodutor

janela =Tk()

janela.title("REPRODUTOR - BINAURAL") #Titulo

bt_alfa    = Button(janela, width=14, text="Relaxamento\n(ALFA)",    command=player.reproduzira)
bt_beta   = Button(janela, width=16, text="Estado de Alerta\n(BETA)",  command=player.reproduzirb)
bt_teta    = Button(janela, width=15, text="Adormecimento\n(TETA)",   command=player.reproduzirt)
bt_delta  = Button(janela, width=26, text="Sono Profundo sem Sonhos\n(DELTA)", command=player.reproduzird)
bt_pausar   = Button(janela, width=12, text="PAUSAR ⏸",  command=player.pausar)
msg = Label(janela, text="-Esteja deitado em um ambiente calmo, sem muita luminosidade, de preferência em um bom lugar acústico.\n-Escolha uma onda que melhor condiz com o seu problema.\n-Use fones de ovido(estéreo).\n-Não exagere no volume, entre 25 dB até no máximo 55 dB.")

bt_alfa.place   (x=10,  y=0)
bt_beta.place  (x=128, y=0)
bt_teta.place   (x=260, y=0)
bt_delta.place (x=385, y=0)
bt_pausar.place (x=250, y=50)
msg.place (x=10, y=100)

janela.geometry("600x200+450+350")
janela.mainloop()
