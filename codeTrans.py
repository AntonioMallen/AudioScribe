import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Función para convertir milisegundos a formato (HH:MM:SS)
def ms_a_tiempo(milisegundos):
    segundos = int(milisegundos / 1000)
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    return f"{horas:02}:{minutos:02}:{segundos:02}"

# Función para transcribir audio a texto con formato personalizado
def transcribir_audio_a_texto(ruta_audio):
    # Cargar el archivo de audio
    audio = AudioSegment.from_file(ruta_audio, format="mp4")
    
    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()
    
    # Dividir el audio en segmentos basados en silencios
    segmentos = split_on_silence(
        audio,
        min_silence_len=1200,  # Duración mínima del silencio en milisegundos
        silence_thresh=-40,   # Umbral de silencio en dB
        keep_silence=500      # Mantener un poco de silencio alrededor de cada segmento
    )
    
    tiempo_acumulado = 0  # Tiempo acumulado en milisegundos
    
    # Procesar cada segmento de audio
    for i, segmento in enumerate(segmentos):
        # Calcular la marca de tiempo inicial
        tiempo_inicial = ms_a_tiempo(tiempo_acumulado)
        
        # Exportar el segmento a un archivo temporal
        segmento.export(f"temp_segment_{i}.wav", format="wav")
        
        # Cargar el segmento en SpeechRecognition
        with sr.AudioFile(f"temp_segment_{i}.wav") as fuente:
            audio_segmento = recognizer.record(fuente)
            
            try:
                # Transcribir el segmento
                texto = recognizer.recognize_google(audio_segmento, language="es-ES")
                
                # Añadir la marca de tiempo y el hablante al texto transcrito
                texto_transcrito += f"({tiempo_inicial}) {texto}\n"
                
            except sr.UnknownValueError:
                print(f"No se pudo transcribir el segmento {i}")
            except sr.RequestError as e:
                print(f"Error en la solicitud: {e}")
        
        # Actualizar el tiempo acumulado
        tiempo_acumulado += len(segmento)
        
        # Eliminar el archivo temporal
        os.remove(f"temp_segment_{i}.wav")
    
    return texto_transcrito

# Ruta al archivo de audio (en la misma carpeta)
ruta_audio = "audio.mp4"

# Verifica si el archivo existe
if not os.path.exists(ruta_audio):
    print(f"Error: El archivo '{ruta_audio}' no existe en la carpeta actual.")
else:
    # Transcribir el audio a texto
    texto_final = transcribir_audio_a_texto(ruta_audio)

    # Guardar el texto transcrito en un archivo
    with open("transcripcion.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto_final)

    print("Transcripción completada y guardada en 'transcripcion.txt'")