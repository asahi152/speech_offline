import snowboydecoder
import signal
import paddle
from paddlespeech.cli.asr import ASRExecutor
import speech_recognition as sr
import sys

from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

# 定义 PaddleSpeech 的 ASR 识别函数
def recognize(audio_file):
    print("唤醒成功，开始语音识别")
    
    asr_executor = ASRExecutor()
    try:
        text = asr_executor(
            model='conformer_aishell',
            lang='zh',
            sample_rate=16000,
            config=None,  # 使用预训练模型
            ckpt_path='../stt_model/model.yaml',
            audio_file=audio_file,
            force_yes=False,
            device=paddle.get_device()
        )
        print('ASR 识别结果: \n{}'.format(text))
    except Exception as e:
        print("ASR 识别错误:", e)

#从系统麦克风拾取音频数据，采样率为 16000。能在用户结束说话时自动停止录制。
def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print('正在获取声音中...')
        audio = r.listen(source)

    with open("../audio/recording.wav", "wb") as f:
        f.write(audio.get_wav_data())
        print('声音获取完成.')

    return "../audio/recording.wav"  

# 语音唤醒之后播放的应答
model = 'resources/models/snowboy.umdl'

# 终止方法为ctrl+c
signal.signal(signal.SIGINT, signal_handler)

# 这里可以设置识别灵敏度
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# sys.argv[1]: name of the network interface
ChannelFactoryInitialize(0, sys.argv[1])   #初始化通道

def callback():
    print("唤醒之后的回调函数")
    print("开始录音...")
    audio_file = rec()  # 使用 rec 函数进行录音
    recognize(audio_file)  # 调用语音识别函数，识别录制的音频
    
detector.start(detected_callback=callback, # 自定义回调函数
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    
# 释放资源
detector.terminate()