from gtts import gTTS
from playsound import playsound
import random
import pytesseract
import os
from queue import Queue
import threading
import configparser

config = configparser.ConfigParser()
config.read('cnf.ini')
pytesseract.pytesseract.tesseract_cmd = config.get('tesseract', 'path')


class ImageReader:
    image = None
    text = None
    text_array = None
    q = None
    lang = None

    def __init__(self, image):
        self.image = image
        self.lang = config.get('language', 'lang')

    def read_from_img(self):
        lng = self.lang
        if self.lang == 'en':
            lng = 'eng'
        text = pytesseract.image_to_string(self.image, lang=lng, config='psm=6')
        self.text = text
        self.replace_special_signs(self)
        print(self.text)
        return self.text

    def read_gtts(self):
        for txt in self.text_array:
            r1 = random.randint(1, 10000000)
            randfile = str(r1) + ".mp3"
            tts = gTTS(txt, lang=self.lang, slow=False)
            tts.save(randfile)
            self.q.put(randfile)

    def play_sound(self):
        ix = 0
        while ix < len(self.text_array):
            if not self.q.empty():
                filename = self.q.get()
                playsound(filename, block=True)
                os.remove(filename)
                ix = ix + 1

    def read_sentence_by_sentence(self):
        filtered_array = filter(None, self.text.split('.'))
        self.text_array = list(filtered_array)
        self.q = Queue(maxsize=len(self.text_array))

        t1 = threading.Thread(target=self.read_gtts)
        t2 = threading.Thread(target=self.play_sound)

        t1.start()
        t2.start()

    def read_text(self):
        r1 = random.randint(1, 10000000)
        randfile = str(r1) + ".mp3"

        tts = gTTS(self.text, lang=self.lang, slow=False)
        tts.save(randfile)
        playsound(randfile, block=True)
        os.remove(randfile)

    @staticmethod
    def replace_special_signs(self):
        self.clean_up_text(self)

        if self.lang == 'pl':
            self.text = self.text.replace('1.', 'jeden')
            self.text = self.text.replace('2.', 'dwa')
            self.text = self.text.replace('3.', 'trzy')
            self.text = self.text.replace('4.', 'cztery')
            self.text = self.text.replace('5.', 'pięć')

            self.text = self.text.replace('©', 'symbol przeznaczenia')
            self.text = self.text.replace('&', 'symbol sukcesu')
            self.text = self.text.replace('$', 'atak dystansowy')
            self.text = self.text.replace('£', 'rana')
            self.text = self.text.replace('%', 'strach')
            self.text = self.text.replace('€', 'przedmiot: ')

            if 'test' in self.text:
                self.text = self.text.replace(']', 'siły')
                self.text = self.text.replace('=', 'mądrości')
                self.text = self.text.replace('+', 'zręczności')
                self.text = self.text.replace('[', 'ducha')
                self.text = self.text.replace('*', 'sprytu')
            else:
                self.text = self.text.replace(']', 'siła')
                self.text = self.text.replace('=', 'mądrość')
                self.text = self.text.replace('+', 'zręczność')
                self.text = self.text.replace('[', 'duch')
                self.text = self.text.replace('*', 'spryt')
        else:
            self.text = self.text.replace('©', 'fate')
            self.text = self.text.replace('&', 'success')
            self.text = self.text.replace('$', 'ranged')
            self.text = self.text.replace('£', 'damage')
            self.text = self.text.replace('%', 'fear')
            self.text = self.text.replace('€', 'trinket: ')

            self.text = self.text.replace(']', 'might')
            self.text = self.text.replace('=', 'wisdom')
            self.text = self.text.replace('+', 'agility')
            self.text = self.text.replace('[', 'spirit')
            self.text = self.text.replace('*', 'wit')

    @staticmethod
    def clean_up_text(self):
        self.text = self.text.replace('\n', ' ').strip()
        self.text = self.text.replace(';', '')
        self.text = self.text.replace('\'', '')
        self.text = self.text.replace('\"', '')
