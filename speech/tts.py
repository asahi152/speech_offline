import paddle
from paddlespeech.cli.tts import TTSExecutor

from pydub import AudioSegment
from pydub.playback import play
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
import sys

 #使用pydub播放音频
def play_audio(wav_file):
    audio = AudioSegment.from_wav(wav_file)
    play(audio) 

# sys.argv[1]: name of the network interface
ChannelFactoryInitialize(0, sys.argv[1])   #初始化通道

tts_executor = TTSExecutor()
wav_file = tts_executor(
    text=input('请输入想要转化为语音的文本：'),
    output='../audio/output.wav',
    am='fastspeech2_csmsc',
    am_config=None,
    am_ckpt='../tts_models/fastspeech2_nosil_baker_static_0.4/fastspeech2_csmsc.pdiparams',
    am_stat=None,
    spk_id=0,
    phones_dict=None,
    tones_dict=None,
    speaker_dict=None,
    voc='pwgan_csmsc',
    voc_config=None,
    voc_ckpt='../tts_models/fpwg_baker_ckpt_0.4/pwg_default.yaml',
    voc_stat=None,
    lang='zh',
    device=paddle.get_device())
print('Wave file has been generated: {}'.format(wav_file))

wav_file='../audio/output.wav'
play_audio(wav_file)

input('语音已播放完毕，按下回车键可退出！')