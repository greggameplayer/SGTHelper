from src.video.UIThread import UIThread
from src.sound.SoundThread import SoundThread
from src.video.VideoThread import VideoThread

uiThread = UIThread()
soundThread = SoundThread()
videoThread = VideoThread()
uiThread.start()
soundThread.start()
videoThread.start()

