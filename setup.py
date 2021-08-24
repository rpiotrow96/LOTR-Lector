from distutils.core import setup

setup(name='LOTR-Lector',
      version='1.0',
      description='LOTR-Lector for LOTR: Journeys in Middle-Earth App',
      author='Rafal Piotrowski',
      author_email='rpiotrow96@gmail.com',
      packages=['gtts', 'playsound==1.2.2', 'pytesseract', 'opencv-python', 'pywin32'],
      )
