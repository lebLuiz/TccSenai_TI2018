import math
import wave
import struct
import array
 
def make_soundfile(left_freq=440, right_freq=460, data_size=10000, fname="test.wav"):
    """
    criar um arquivo wave 'senoidal' sintético com freqüência freq
     arquivo fname tem um comprimento de cerca de data_size * 2
    """
    frate = 11025.0  # framerate como um flutuador
    amp = 8000.0     # multiplicador para amplitude
 
    # criação de lista senoidal
    sine_list = []
    for x in range(data_size):
        
        left = math.sin(2*math.pi*left_freq*(x/frate))
        right = math.sin(2*math.pi*right_freq*(x/frate))
        sine_list.append((left,right))
 
    # pra salvar o arquivo
    wav_file = wave.open(fname, "w")
    # parâmetros necessários
    nchannels = 2
    sampwidth = 2
    framerate = int(frate)
    nframes = data_size
    comptype = "NONE"
    compname = "Não comprimido"
    # definindo todos os parâmetros de uma só vez
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    # agora escreva o arquivo
    print( "Aguarde..." )
    for s in sine_list:
        data = array.array('h')
        data.append(int(s[0]*amp/2)) # Canal Esquerdo
        data.append(int(s[1]*amp/2)) # Canal Direito
        # Gravar os quadros de aúdio para arquivo
        wav_file.writeframes(data.tostring())
    wav_file.close()
    print( "%s escrito" % fname )
 
# definindo as frequências - L - R
left_freq = 144.0
right_freq = 150.0
# tamanho dos dados, o tamanho do arquivo será de cerca de 2 vezes
# duração é de cerca de 4 segundos para um data_size de 40000 - POR EXEMPLO -
data_size = 600000
 
# nome do arquivo
fname = "binaural_%s_%s.wav" % (left_freq, right_freq)
 
make_soundfile(left_freq, right_freq, data_size, fname)
