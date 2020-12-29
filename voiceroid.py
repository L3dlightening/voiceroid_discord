import pywinauto
import subprocess
import configparser
import psutil
import logging

#logger = getLogger(__name__)

config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')
program_path = config.get('voiceroid', 'path')


def search_child_byname(name, uiaElementInfo):
    for childElement in uiaElementInfo.children():
        if childElement.name == name:
            return childElement
    return False


def launch_voiceroid():
    logging.info('looking for voiceroid2 process.')
    if 'VoiceroidEditor.exe' in [p.name() for p in psutil.process_iter()]:
        logging.info('found VOICEROID2')
    else:
        logging.info('launching VOICEROID2')
        

if __name__ == '__main__':
    launch_voiceroid()