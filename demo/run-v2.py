import whisper


file_path = "../demo-one/downloaded_audio.mp3"
audio = whisper.load_audio(file_path)
audio = whisper.pad_or_trim(audio)

model_path = "../models"
# model_name = "large-v3"
model_name = "base.en"
model = whisper.load_model(name=model_name,download_root=model_path)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)
print("You say:",result.text)