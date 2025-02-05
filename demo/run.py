import whisper
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
isFp16 = False
if device == 'cuda':
    isFp16 = True

#  name 可以是tiny,base,small,medium,large,large-v3
model = whisper.load_model(name="medium",download_root="../models").to(device)

file_path = "../demo-one/84ec7b3bfc452c18d12639b2e5ec5d65_VR_140870317_1737607691186754772_0.mp3"
# result = model.transcribe(file_path,fp16=isFp16,verbose=True,language="zh")

languagearr =["zh","en" ]
for language in languagearr:
    result = model.transcribe(file_path,fp16=isFp16,verbose=False,language=language)
    print(result["text"],"\n")


