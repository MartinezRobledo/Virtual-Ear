Virtual Ear Tool

Graba reuniones y genera transcripciones locales usando FFmpeg y Faster Whisper.

Características
Grabación de audio del sistema y micrófono.
Transcripción local usando Whisper.
Soporte CPU y GPU NVIDIA (CUDA).
Sin servicios externos.
Compatible con Windows y Linux.
Requisitos
FFmpeg

Verificar instalación:

ffmpeg -version
Python
python --version

Recomendado:

Python 3.12+
UV

Verificar:

uv --version

Instalar:

pip install uv
Instalación

Clonar repositorio:

git clone <repo>
cd virtual-ear

Crear entorno e instalar dependencias:

uv sync
Configuración

Archivo:

config.yaml

Ejemplo:

whisper:
  model: large-v3
  device: cuda

audio:
  sample_rate: 16000
Dispositivos válidos
device: cpu
device: cuda
device: auto
Diagnóstico

Ejecutar:

uv run earing doctor

Ejemplo:

✓ ffmpeg
✓ audio sistema
✓ micrófono
✓ recordings/
✓ transcripts/
✓ whisper
✓ cuda
Grabar una reunión

Iniciar:

uv run earing start

Detener:

uv run earing stop

Archivo generado:

recordings/
Transcribir
uv run earing transcribe recordings/meeting.wav

Salida:

transcripts/meeting.md
GPU NVIDIA (Opcional)
Verificar GPU
nvidia-smi

Debe mostrar algo similar a:

CUDA Version: 12.x

o superior.

Instalar CUDA

Faster Whisper actualmente requiere bibliotecas CUDA 12.

Instalar:

CUDA Toolkit 12.9

Verificar:

Get-ChildItem `
"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.9" `
-Recurse `
-Filter cublas64_12.dll

Debe existir:

cublas64_12.dll
Problemas conocidos
CUDA runtime not found

Error:

RuntimeError:
CUDA runtime not found

Solución:

Instalar CUDA 12.x.
Verificar que exista:
cublas64_12.dll
Transcripción incorrecta

Si el audio contiene largos períodos de silencio:

vad_filter=True

puede mejorar significativamente los resultados.

Arquitectura
virtual_ear/
├── cli.py
├── recorder.py
├── transcriber.py
├── doctor.py
├── config.py

recordings/
transcripts/
config.yaml
Flujo típico
uv run earing doctor

uv run earing start

uv run earing stop

uv run earing transcribe recordings/meeting.wav


Audio en Windows
Capturar audio del sistema

Instalar:

VB-Cable

Configurar:

Windows Output
    ↓
CABLE Input
    ↓
FFmpeg
Capturar micrófono

Seleccionar:

Micrófono (NVIDIA Broadcast)

o

Micrófono físico
Escuchar mientras se graba

Activar:

Escuchar este dispositivo

sobre:

CABLE Output