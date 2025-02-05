from openai import OpenAI
import os

# 获取环境变量
api_key =  os.getenv("OPENAI_API_KEY")
base_url = "https://api.siliconflow.cn/v1"
model_name = "FunAudioLLM/SenseVoiceSmall"

# 检查环境变量是否存在
if not api_key or not base_url:
    raise ValueError("请确保环境变量 'deepseek_api_key' 和 'deepseek_api_url' 已正确设置。")

# 初始化OpenAI客户端
client = OpenAI(api_key=api_key, base_url=base_url)

# 使用with语句管理文件资源
audio_path="84ec7b3bfc452c18d12639b2e5ec5d65_VR_140870317_1737607691186754772_0.mp3"
audio_file= open(audio_path, "rb")
transcription = client.audio.transcriptions.create(model=model_name, file=audio_file)
        
# 打印转录结果中的单词
print(transcription.text)