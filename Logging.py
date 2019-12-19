import logging

def appendFile():
    text_file = open("example.log", "a")
    text_file.write('----------\n')
    text_file.close()

logging.basicConfig(format='%(asctime)s', datefmt='%d.%m.%Y %H:%M:%S', filename='example.log',level=logging.DEBUG)
try: 0/0
except Exception as e:
        logging.exception(e)
        appendFile()

try: a/b
except Exception as e:
        logging.exception(e)
        appendFile()