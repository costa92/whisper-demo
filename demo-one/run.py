from openai import OpenAI
import os

# 获取环境变量
# api_key =  os.getenv("OPENAI_API_KEY")
# base_url = "https://api.siliconflow.cn/v1"
# model_name = "FunAudioLLM/SenseVoiceSmall"

api_key =""
api_base=""

if not api_key or not api_base:
    api_key = os.getenv("DEERAPI_KEY")
    api_base = os.getenv("DEERAPI_URL")

# 检查环境变量是否存在
if not api_key or not api_base:
    raise ValueError("请确保环境变量 'deepseek_api_key' 和 'deepseek_api_url' 已正确设置。")

# 初始化OpenAI客户端
client = OpenAI(api_key=api_key, base_url=api_base)

# 使用with语句管理文件资源
audio_path="84ec7b3bfc452c18d12639b2e5ec5d65_VR_140870317_1737607691186754772_0.mp3"
audio_file= open(audio_path, "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="verbose_json",
    timestamp_granularities=["word"]
)
        
# 打印转录结果中的单词
print(transcription.text)