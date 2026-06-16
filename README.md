# 🎧 Virtual Ear Tool

Graba reuniones y genera transcripciones locales usando **FFmpeg** y **Faster Whisper**.

---

## ✨ Características

- 🎙️ Grabación de audio del sistema y micrófono
- 🧠 Transcripción local usando Whisper
- ⚡ Soporte para CPU y GPU NVIDIA (CUDA)
- 🔒 No utiliza servicios externos
- 🖥️ Compatible con Windows y Linux

---

## 📦 Requisitos

### FFmpeg

Verificar instalación:

```bash
ffmpeg -version
```

## Python
Verificar versión:
```bash
python --version
```

## UV
Verificar instalación:
```bash
uv --version
```
Instalar:
```bash
pip install uv
```

🚀 Instalación
Clonar el repositorio:
```bash
git clone https://github.com/MartinezRobledo/Virtual-Ear.git
cd virtual-ear
```

Crear entorno e instalar dependencias:
```bash
uv sync
```

## ⚙️ Configuración
Archivo:
config.yaml

Ejemplo:
```yaml
whisper:
  model: large-v3
  device: cuda

audio:
  sample_rate: 16000
```

🧩 Dispositivos válidos
```yaml
device: cpu
device: cuda
device: auto
```

## 🩺 Diagnóstico
Ejecutar:
```bash
uv run earing doctor
```

Ejemplo de salida:
✓ ffmpeg
✓ audio sistema
✓ micrófono
✓ recordings/
✓ transcripts/
✓ whisper
✓ cuda

🎙️ Grabar una reunión
Iniciar grabación:
```bash
uv run earing start
```
Detener grabación:
```bash
uv run earing stop
```
Archivo generado:
recordings/

## 📝 Transcribir
```bash
uv run earing transcribe recordings/meeting.wav
```
Salida:
transcripts/meeting.md

## 🚀 GPU NVIDIA (Opcional)
Verificar GPU
```bash
nvidia-smi
```
Debe mostrar algo similar a:
CUDA Version: 12.x

Instalar CUDA
Faster Whisper requiere actualmente bibliotecas CUDA 12.
Instalar:

CUDA Toolkit 12.9

### Verificar instalación
```bash
Get-ChildItem `
"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.9" `
-Recurse `
-Filter cublas64_12.dll
```
Debe existir:
- cublas64_12.dll

## 🏗️ Arquitectura
virtual_ear/
├── cli.py
├── recorder.py
├── transcriber.py
├── doctor.py
├── config.py

recordings/
transcripts/
config.yaml

## 🎧 Audio en Windows
Capturar audio del sistema
Instalar:
- VB-Cable

Configurar:
Windows Output
    ↓
CABLE Input
    ↓
FFmpeg


## 🎤 Capturar micrófono
Seleccionar:
Micrófono virtual
o
Micrófono físico


## 🔊 Escuchar mientras se graba
Activar:
"Escuchar este dispositivo"

sobre:
CABLE Output