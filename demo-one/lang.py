import os
from openai import OpenAI


# 获取环境变量
# api_key =  os.getenv("OPENAI_API_KEY")
# base_url = "https://api.siliconflow.cn/v1"
# model_name = "FunAudioLLM/SenseVoiceSmall"
# https://doc.zhizengzeng.com/
# api_key =  ""
# base_url = "https://api.zhizengzeng.com/v1"
model_name = "whisper-1"

api_key =""
base_url=""

if not api_key or not base_url:
    api_key = os.getenv("DEERAPI_KEY")
    base_url = os.getenv("DEERAPI_URL")


model_name = "whisper-1"
# 检查环境变量是否存在
if not api_key or not base_url:
    raise ValueError("请确保环境变量 'deepseek_api_key' 和 'deepseek_api_url' 已正确设置。")

# 初始化OpenAI客户端
client = OpenAI(api_key=api_key, base_url=base_url)

audio_path="84ec7b3bfc452c18d12639b2e5ec5d65_VR_140870317_1737607691186754772_0.mp3"
audio_file= open(audio_path, "rb")

transcription = client.audio.transcriptions.create(
    file=audio_file,
    model=model_name,
    response_format="verbose_json",
    timestamp_granularities=["word"]
)

print(transcription)