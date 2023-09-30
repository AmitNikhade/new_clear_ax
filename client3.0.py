from __future__ import division
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/axona/Downloads/axona-375707-c94e508b440f.json"   

"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.
Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
def tts_(text):

    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-IN", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
        global pqrst
        pqrst=vlc.MediaPlayer("output.mp3")
        pqrst.play()
    
    
###########################################################################################



import os
from datetime import datetime
import time, os, requests
from termcolor import colored
import requests, json
from gtts import gTTS
# import pygame
import re
import sys
import pyspeedtest
import pafy
import vlc
import time
import re
import urllib.parse
import urllib.request
import subprocess
subprocess.Popen(['sh ./speech.sh '+str("Initializing.. ")],shell=True )

time.sleep(7)
# if int(pyspeedtest.SpeedTest("ai.silai.ml").ping())>100:
#     subprocess.Popen(['sh ./speech.sh '+"Warning, Your Internet connection is not stable please do have a proper internet speed to get good experience "], shell=True)
time.sleep(7)
# pygame.init()
# pygame.mixer.init()

# from google.cloud import speech
try:
    from queue import Queue  # Python 3 import
except ImportError:
    from Queue import Queue
import pyaudio
from six.moves import queue

def play(name):
    global media
    query_string = urllib.parse.urlencode({"search_query": name})
    formatUrl = urllib.request.urlopen(
        "https://www.youtube.com/results?" + query_string)
    search_results = re.findall(
        r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    video = pafy.new(clip2)
    videolink = video.getbestaudio()
#     print("Playing ", video.title)
    media = vlc.MediaPlayer(videolink.url)
    media.play()
#     time.sleep(video.length)
#     media.stop()
# import torch
# import datasets
# import librosa
import requests, json

import multiprocessing
import pyaudio, numpy as np
# import pyaudio
import wave
from array import array
import time

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()
def main():

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    print("recording...")
    frames = []
    k = []
    vc  = []
    nu = []
    for i in range(0, int(RATE / CHUNK*1000)):
        data = stream.read(CHUNK)
        frames.append(data)
        vol = max(array('h', stream.read(100)))
#         print("current vol:",vol)
        vc.append(vol)
        if vol < 10000:
            print("low")
            k.append(vol)
            d = 0
        if vol > 3000:
            print("raised")
            k.clear()
            d = 1
#         print("mean",np.mean(vc))
        print('>>>',k)
        if len(k)>=10:
      
#             print(vc)
            print("mean",np.mean(vc))
            if sum(vc)/len(vc) < 1500:
#                 print("mean",np.mean(vc))
                print("no speeches")
                nu.append(1)
                if len(nu) == 3:
                    print("limit exceeded")
#                     pygame.mixer.init()
#                     pygame.mixer.music.load("/home/axona/Documents/Axona/Audio_files_tc.wav")
#                     pygame.mixer.music.play()
                    pq=vlc.MediaPlayer("/home/axona/Documents/Axona/Audio_files_tc.wav")
                    pq.play()
                    stream.close()
#                 stream.close()
# 
#                 main()
      
            else:
#                 pygame.mixer.music.load("/home/axona/Documents/Axona/Audio_files_tonl.wav")
#                 pygame.mixer.music.play()
                pqx=vlc.MediaPlayer("/home/axona/Documents/Axona/Audio_files_tc.wav")
                pqx.play()
                print(np.mean(vc))
                print("done")
                nu.clear()
      
                payload={
                            "buff":str(frames),
                            # "lang":'en'
                            }
                headers = {
                        'Content-Type': 'application/json'

                        }
                response = requests.post("https://axona.silai.ml/stt", headers=headers, data=json.dumps(payload))
                print("requested posted")
                print(response.text)
                if "200" in str(response):
                    pass
                    
                else:
                    os.popen('sh ./speech.sh '+str("server not reachable, please try again later"))
                    stream.close()
                    run_()
                if response.text.split()[0]=="play" or response.text.split()[0]=="play":
                    try:
                        media.stop()
                    except:
                        pass
#                     os.popen('sh ./speech.sh '+str(response.text))
#                     play(response.text)
#                     listen_t2 = multiprocessing.Process(target=play, args = (str(response.text),))
#                     listen_t2.start()
                    listen_t3 = threading.Thread(target=play, args = (response.text,))
                    listen_t3.start()
                if "stop" in response.text:
                    media.stop()
#                 print(str(response))
                
#                 if "Departments" in response.text:
#                     try:
#                         print(response.text)
#                         resp=str(response.text).split(",")
#                         for i in resp:
#                             print(i.replace(" ","").replace(".",""))
#                             os.popen('sh ./speech.sh '+str(i))
#                             print(round(len(i.replace(" ",""))/8))
# #                             time.sleep(len(i.replace(" "+""))/3)
#                             time.sleep(len(i.replace(" ",""))/8)
#                     except:
#                         pass 
#                     gTTS(str(response.text), lang='en', slow=False).save("/home/luci/clearence/performances.mp3")
#                     
#                 if "?" in response.text:
#                     try:
# #                       gTTS(str(response.text), lang="hi", slow=False).save('file.mp3')
# #                       pygame.mixer.music.load("file.mp3")
# #                       pygame.mixer.music.play()
# #                       time.sleep(10)
#                       os.popen('sh ./speech.sh '+str(response.text).replace("'",""))
#                       time.sleep(round(len(response.text.split(' '))/2))
#                       pygame.mixer.music.play()
#                       main()
#                     except:
#                         pass
                if 1+1 ==2:
                    if response.text.split()[0]!="play" or response.text.split()[0]!="play" or "stop" in response.text:
#                         pass
#                     try:
                        print(response.text)
                        text = (response.text).replace("'","").replace("[","").replace("[","")
                        tts_(text)
#                        
                        
#                         pygame.mixer.music.load("/home/axona/Documents/Axona/output.mp3")
#                         pygame.mixer.music.play()
#                         
#                     except:
#                         pass
                stream.close()
      
# from array import array
import threading
import struct
import pvporcupine
from playsound import playsound
# import pygame

# pygame.mixer.pre_init(16000, -16, 1, 64)
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("/home/axona/Documents/Axona/Audio_files_tonl.wav")

                    
porcupine = None
pa= None
stream = None
################

os.system('color')
url = 'https://www.google.com/'
timeout = 2
sleep_time = 10
op = None
#################
por = pvporcupine.create(access_key='ZoeA5cRZIHS7VKE3O2lgG9BaBaNhKjaFncPefALssGlfD+ISY1QnEw==',keyword_paths=[r'Axona_de_raspberry-pi_v2_1_0.ppn'], model_path='porcupine_params_de.pv')

if __name__ == "__main__":
    
    def run_():
        audio = pyaudio.PyAudio()
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK = 128 
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=por.frame_length)
        vol = max(array('h', stream.read(CHUNK)))
        print("stream started")
        try:
            while True:
                pcm = stream.read(por.frame_length)
                
                pcm = struct.unpack_from("h" * por.frame_length, pcm)
                ki = por.process(pcm)
                if ki >= 0:
                    
    #                 main()
    #             else:
    #                 pass
                    if vol >= 100:
                        try:
                            print("1")
                            try:
                                pqrst.stop()
                                media.stop()
                            except:
                                pass
#                             pygame.mixer.music.play()
                            pq1=vlc.MediaPlayer("/home/axona/Documents/Axona/Audio_files_tonl.wav")
                            pq1.play()
                            print("reached main")
                            main()
                        except:
                            pass
                    else:
                        pass
                else:
                    pass
        except:
            run_() 
    def check_q(stream):
        khh = 1
        while True:
          


            now = datetime.now()
            try:
                op = requests.get(url, timeout=timeout).status_code
                if op == 200:
                    print(now, colored("Connected", "green"))
                    
                    if khh == 1:
                        khh = khh+1
                        os.popen('sh ./speech.sh '+str(" we are live"))
#                         pygame.mixer.music.load("/home/axona/Documents/Axona/Audio_files_tc.wav")
                        
                    else:
                        pass
                    
                    sleep_time = 10
                else:
                    print(now, colored("Status Code is not 200", "red"))
#                     pygame.mixer.music.load("/home/axona/Documents/Axona/hello1.mp3")
#                     pygame.mixer.music.play()
                    pq1=vlc.MediaPlayer("/home/axona/Documents/Axona/hello1.mp3")
                    pq1.play()
                    print("status Code", op)
#                     stream.close()
                    khh=1
            except:
                print(now, colored("Not Connected", "red"))
#                 pygame.mixer.music.load("/home/axona/Documents/Axona/hello1.mp3")
#                 pygame.mixer.music.play()
                pq1=vlc.MediaPlayer("/home/axona/Documents/Axona/hello1.mp3")
                pq1.play()
                print("status Code", op)
#                 stream.close()
                khh=1
                sleep_time = 10
            time.sleep(sleep_time)
            
    listen_t = threading.Thread(target=check_q, args = (stream,))
    listen_t.start()
    
    listen_t2 = multiprocessing.Process(target=run_())
    listen_t2.start()
#     run_()
