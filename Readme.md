# Transcripción de Audio a Texto 🎙️📝

![License](https://img.shields.io/badge/Licencia-CC%20BY--NC%204.0-lightgrey.svg)

Un script en Python para transcribir archivos de audio (.mp4) a texto, diseñado para ser simple y fácil de usar. Ideal para transcripciones rápidas de audios cortos.

---

## Descripción 📌

Este proyecto permite transcribir archivos de audio a texto utilizando:
- **FFmpeg** para el procesamiento de audio
- **SpeechRecognition** para la conversión de voz a texto
- Configuración personalizable de detección de silencios

Especialmente útil para:
- Transcripciones rápidas de audios cortos
- Proyectos personales o de aprendizaje
- Referencia para implementar funcionalidades similares

---

## Funcionalidades clave 🔑

- 🎧 Soporte para archivos .mp4
- ✂️ Detección de silencios configurable:
  - Duración mínima del silencio
  - Umbral de silencio en dB
  - Tiempo de silencio alrededor de cada segmento
- 📄 Generación de archivo .txt con la transcripción
- 🐍 Código Python fácil de modificar y adaptar

---

## ⚠️ Advertencia Importante

**Limitaciones conocidas**:
- Lentitud en audios mayores a 1 minuto
- Requiere ajuste manual de parámetros de silencio para óptimos resultados
- Dependencia de FFmpeg (debe estar instalado y en el PATH)

---

## Cómo funciona 🛠️

1. **Preparación**:
   - Coloca el archivo .mp4 en la misma carpeta que el script
   - Asegúrate de tener FFmpeg instalado y en el PATH

2. **Configuración (opcional)**:
   - Ajusta los parámetros de detección de silencio:
     ```python
     segmentos = split_on_silence(
         audio,
         min_silence_len=1200,  # Duración mínima del silencio en milisegundos
         silence_thresh=-40,   # Umbral de silencio en dB
         keep_silence=500      # Mantener silencio alrededor de cada segmento
     )
     ```

3. **Ejecución**:
   - Ejecuta el script
   - La transcripción se guardará en un archivo .txt en la misma carpeta

---

## Licencia 📜

Este proyecto se distribuye bajo **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**:
- ✅ Permite uso privado, modificaciones y aprendizaje
- ✅ Puedes compartir y adaptar el código
- ❌ Prohibido uso comercial o lucrativo
- ⚖️ [Ver licencia completa](https://creativecommons.org/licenses/by-nc/4.0/deed.es)

---

## Autor 👨💻

**Antonio Mallen**  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/AntonioMallen)

*¿Preguntas o sugerencias?* ¡Abre un *issue* o contribuye al proyecto!