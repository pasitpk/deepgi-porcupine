import os
from datetime import datetime
import pvporcupine
from pvrecorder import PvRecorder
from dotenv import load_dotenv
load_dotenv()

access_key = os.getenv('ACCESS_KEY')
keyword_paths = [r'hey-deep-g-i_en_windows_v2_2_0/hey-deep-g-i_en_windows_v2_2_0.ppn',
                 r'hey-dip-g-i_en_windows_v2_2_0/hey-dip-g-i_en_windows_v2_2_0.ppn',
                 ]
porcupine = pvporcupine.create(access_key=access_key, keyword_paths=keyword_paths)
recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

try:
    recoder.start()
    print("Ready")

    while True:
        keyword_index = porcupine.process(recoder.read())
        if keyword_index >= 0:
            print(f"{datetime.now()} : Detected")


except KeyboardInterrupt:
    recoder.stop()
finally:
    porcupine.delete()
    recoder.delete()
