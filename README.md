# 离线语音转文字和文字转语音

## 说明

项目的语音识别通过部署snowboy的预训练模型进行语音唤醒，此外使用paddlespeech的模型进行语音转文字。
语音合成同样使用paddlespeech的模型。

## 环境要求

- Python 3.x
- 操作系统 Ubuntu20.04
- 相关库：
  - `unitree_sdk2py` - Unitree 机器人 SDKi
  - snowboy 语音唤醒处理
  - paddlepaddle 版本2.5.2
  - paddlespeech 语音识别和合成的库
  - SpeechRecognition 用于音频录制
  - pyaudio
  - nltk 自然语言处理

## 安装依赖

### 安装SpeechRecognition
   
  pip install SpeechRecognition

### 安装snowboy

1.建立conda虚拟环境
  conda create -n <环境名称> python==3.8
  conda activate <环境名称>

2.配置环境，snowboy需要swig,alsa等

  sudo apt-get install swig
  sudo apt-get install libatlas-base-dev
  sudo apt-get install sox==14.4.2
  sudo apt-get install libasound2-dev

3.安装pyaudio

  sudo apt-get install portaudio19-dev python-all-dev python3-all-dev jackd1 portaudio19-doc jack-tools meterbridge liblo-dev
  sudo apt-get install pyaudio

### 安装paddlepaddle

1.用到的是cCPU版本，也可以跟据自己的CUDA选择对应的GPU版本。
  python -m pip install paddlepaddle==2.5.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
建议使用pip安装，conda安装容易出错

2.安装完成后，检查paddlepaddle是否安装成功：

  python3
  >import paddle
  >paddle.utils.run_check()

### 安装paddlespeech

  pip install pytest-runner -i https://pypi.tuna.tsinghua.edu.cn/simple 
  pip install paddlespeech -i https://pypi.tuna.tsinghua.edu.cn/simple

### 安装nltk包
1.前往https://github.com/nltk/nltk_data/tree/gh-pages下载zip文件，解压后将packages文件夹重命名为nltk_data。
2.运行
    import nltk
    nltk.find('.')
  找到对应的目录，将上面的文件夹放进任一路径即可。

## 使用方法

1. **克隆仓库**

   ```bash
   git clone https://github.com/asahi152/speech_offline.git
   cd speech_offline/speech
   ```
2. **运行程序**

   执行主程序：

   ```bash
   python3 stt.py <网络接口名>
   python3 tts.py <网络接口名>
   ```
3.  **说明**
   需要自己在项目根目录新建audio文件夹存放相关的音频文件。
   语音识别用到的预处理模型是comformer_aishell-zh-16k，语音合成用到的声学模型是fastspeech2_csmsc。两者都是中文模型。
   更多模型请查看https://github.com/PaddlePaddle/PaddleSpeech文档。
