# https://www.ultrasev.com/blog/2024/whisper
# 语言识别
# 使用whisper库进行语言识别
import torch
import whisper

device = 'cuda' if torch.cuda.is_available() else 'cpu'


# audio_path = "3c62ba218b4617014d826d8fddcbdfe7_VR_133139800_1737593699068945199_0.mp3"
audio_path = "8ba96b7cf0425a575011efba83288146_VR_137993835_1737600883628319012_0.mp3"
model = whisper.load_model(name="tiny",download_root="models").to(device)


audio = whisper.load_audio(audio_path)
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)


# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")