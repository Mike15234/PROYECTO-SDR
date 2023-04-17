import socket
import numpy as np
from scipy.io.wavfile import write
from threading import Thread
import speech_recognition 
import subprocess

IP = "127.0.0.1"  # Dirección IP en la que se escuchará
PORT = 5005  # Puerto en el que se escuchará
CHUNK_SIZE = 1024  # Tamaño del búfer de datos a recibir

# Crear un socket UDP
sock = socket.socket(socket.AF_INET,  # IPv4
                     socket.SOCK_DGRAM)  # UDP

# Vincular el socket al puerto y dirección IP
sock.bind((IP, PORT))

# Configurar el tiempo de espera en el socket
sock.settimeout(5.0)  # Esperar 15 segundos antes de lanzar una excepción

print(f"Escuchando en el puerto {PORT}...")

#Arreglo para concatenar datos
fill_data = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
#Arreglo para reniciar datos
empty = fill_data

#Ruta para el archivo WAV y TXT
archivo= '/home/popuser/Proyecto_TxRx/Archivos/output.wav'
ruta_txt1 = '/home/popuser/Proyecto_TxRx/Archivos/transcrito.txt'
ruta_txt2 = '/var/www/html'
comando = f"sudo -S cp -f {ruta_txt1} {ruta_txt2}"

#Cadena de texto a escribir 
text = ""

#Frecuencia de muestra 
samp_rate = 48000
#Volumen
volume = 30000
#Crear objeto para transcripcion
r = speech_recognition.Recognizer()
count = 0

#Transcripcion de audio a texto
def speech():
    global text
    comparador = "" 
    while True:
        try: 
            #Lectura del archivo wav
            with speech_recognition.AudioFile(archivo) as source:
                audio = r.record(source)
            text = r.recognize_google(audio, language='es-ES') #Español España
            
            #Escritura del archivo
            if(text != comparador):
                txt= open(ruta_txt1, "a")
                txt.write(text)
                txt.close()
                subprocess.call(f"echo 'qwerty' | {comando}", shell=True)
                comparador = text
        except:
            print('...')

#Ejecución del método de transcripcion en hilo alterno
thread = Thread(target=speech)
thread.daemon = True
thread.start()


#Recepción de datos desde GNU 
while True:
    try:
        data = sock.recv(CHUNK_SIZE) 
        datas = np.frombuffer(data, dtype=np.complex64, count=-1) #Decodificacion de datos
        fill_data = np.concatenate((fill_data, datas)) #Creación de arreglo de datos

        if(fill_data.shape[0] > 200000):
            max_value = np.max(np.abs(fill_data))
            data_to_write = fill_data*(volume/max_value) # Ajustar escala audible
            write('Proyecto_TxRx/Archivos/output.wav', samp_rate, data_to_write.astype(np.int16)) #Generacion de Archivo Wav
            print("###")
            fill_data = empty
    except socket.timeout: #Cerrar conexion
            print("Se ha alcanzado el tiempo de espera. Cerrando conexión...")
            break