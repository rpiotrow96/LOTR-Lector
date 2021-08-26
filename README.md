# LOTR-Lector

LOTR-Lector is a Python script for reading text from The Lord of the rings: Journeys in Middle-Earth App

###Installation
* download and install tesseract https://github.com/UB-Mannheim/tesseract/wiki
* Configure path to tesseract.exe (in cnf.ini file)
* Configure language (supported languages: en, pl) in cnf.ini file.
  To use Polish (pl) language, you have to download pl.traineddata and copy this file to your tesseract ```path/tessdata```. https://github.com/tesseract-ocr/tessdata/blob/master/pol.traineddata
* run cmd ``` pip install  git+https://github.com/rpiotrow96/LOTR-Lector.git ```
* Play your game (1920x1080 reccomended), then run this script ``` python main.py```
* It works!


###How it works?
Im using OCR (optical character recognition) and GTTS (Google text to speech API).
Script is trying to find a border in game, then is reading text in border.

