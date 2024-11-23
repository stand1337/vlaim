import configparser
from ctypes import WinDLL
import time



(user32, kernel32, shcore) = (
    WinDLL('user32', use_last_error=True),
    WinDLL('kernel32', use_last_error=True),
    WinDLL('shcore', use_last_error=True),
)


shcore.SetProcessDpiAwareness(2)

class CONFIG:
    def __init__(self):
        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)
        self.ZONE = 3
        self.GRAB_ZONE = (int(self.width / 2 - self.ZONE), int(self.height / 2 - self.ZONE),
                          int(self.width / 2 + self.ZONE), int(self.height / 2 + self.ZONE))
        self.detection_threshold = 3
        self.counterstrafe = False
        self.cooldowntime = 3.0
        self.hotkey_trigger = "shift"
        self.vandal_ht = "alt"
        self.initial_num = 0.015
        self.last_num = 0.018
        self.low_color = (139, 95, 188)  # Lower HSV:  (139, 95, 188) ##upper_color = 148,154,194 
        self.high_color = (156, 255, 255)  # Upper HSV:  (156, 255, 255)
        self.config = configparser.ConfigParser()
        self.shoot_key = 'k'
        self.target_fps = 60
        self.aim = False
        self.fov = False
        self.not1shot = False

        self.getconfig()

    def saveconfig(self):
        self.config['Config'] = {
            'ht': str(self.hotkey_trigger),
            'cs': str(self.counterstrafe),
            'cd': str(self.cooldowntime),
            'tf': str(self.target_fps),
            'zn': str(self.ZONE),
            'in': str(self.initial_num),
            'ln': str(self.last_num),
            'dt': str(self.detection_threshold),
            'ai': str(self.aim),
            'fv': str(self.fov),
            'nt': str(self.not1shot)
        }
        with open('test.ini', 'w') as configfile:
            self.config.write(configfile)

    def getconfig(self):
        try:
            config = configparser.ConfigParser()
            config.read('test.ini')
            self.hotkey_trigger = config['Config'].get('ht', 'shift')
            self.counterstrafe = config['Config'].getboolean('cs', False)
            self.cooldowntime = config['Config'].getfloat('cd', 3.0)
            self.target_fps = config['Config'].getint('tf', 60)
            self.ZONE = config['Config'].getint('zn', 3)
            self.initial_num = config['Config'].getfloat('in', 0.015)
            self.last_num = config['Config'].getfloat('ln', 0.018)
            self.detection_threshold = config['Config'].getint('dt', 3)
            self.aim = config['Config'].getboolean('ai', False)
            self.fov = config['Config'].getboolean('fv', False)
            self.not1shot = config['Config'].getboolean('nt', False)
        except Exception as e:
            self.saveconfig()
            time.sleep(2)
            self.getconfig()


#361cbc9926f48069715a8ff439b6815b
#770196231d0d9b02ebff0eb551be44d2
#7452cf07e074fae2897de5a64e175d4b
#e66dd1e64333868ecba760b94f84d950
#cd58638140f83679691e3599712dfe66
#338e2f4c86d1e84632af5fa937265d79
#1505ec39a6beff25d9dcb18b1deafc78
#78d58d4345742bd41a059bc77aab76fc