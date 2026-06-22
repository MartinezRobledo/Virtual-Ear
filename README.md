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
config.json

Ejemplo:
```json
{
  "audio": {
    "system": "Voicemeeter Out B1 (VB-Audio Voicemeeter VAIO)",
    "microphone": "Micrófono (NVIDIA Broadcast)"
  },
  "whisper": {
    "model": "large-v3",
    "device": "cuda"
  }
}
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
config.json

## 🎧 Audio en Windows

### Requisito: VoiceMeeter

En Windows, ffmpeg no puede capturar audio del sistema y pasártelo al mismo tiempo sin software adicional. **VoiceMeeter** resuelve esto como mixer virtual.

Instalar: https://vb-audio.com/Voicemeeter/

### Configurar VoiceMeeter

1. **Hardware Input 1**: Seleccionar el dispositivo de audio del sistema (ej: CABLE Output si usás VB-Cable)
2. **Hardware Input 2**: Seleccionar el micrófono (ej: NVIDIA Broadcast)
3. **Hardware Out A1**: Seleccionar tus parlantes/auriculares reales
4. En el strip del **micrófono**: desactivar A1 (para no escucharte a vos mismo), activar B1
5. En el strip del **sistema**: activar A1 (para escuchar) y B1 (para grabar)

### Configurar Windows

Establecer **VoiceMeeter Input (VB-Audio Voicemeeter VAIO)** como dispositivo de reproducción por defecto en Windows.
Así todo el audio del sistema pasa por VoiceMeeter.

Para capturar audio de una aplicación específica (Zoom, Teams, Chrome, etc.),
configurá su salida de audio a **VoiceMeeter Input (VB-Audio Voicemeeter VAIO)**
en la configuración de audio de esa aplicación.

### Configurar config.json

```json
{
  "audio": {
    "system": "Voicemeeter Out B1 (VB-Audio Voicemeeter VAIO)"
  }
}
```

### Flujo de audio

```
App (Zoom, Teams, Chrome...)
  └→ VoiceMeeter Input (VB-Audio Voicemeeter VAIO)
       └→ VoiceMeeter
            ├→ A1 → Parlantes (vos escuchás)
            └→ B1 → ffmpeg (grabación)
```

> **Tip**: Si querés capturar solo el audio de una app específica (ej: Zoom),
> configurá esa app para que use **VoiceMeeter Input** como salida de audio.
> El resto del sistema no se ve afectado.