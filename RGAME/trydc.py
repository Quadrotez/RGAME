import os, tkinter
from configparser import ConfigParser
path = f'C://Users/{os.getlogin()}/AppData/Roaming/PULV/RGAME'
fsconfig_path = f'{path}/config.ini'
fsconfig = ConfigParser()
def start():
    global fsconfig_path, fsconfig, path
    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(fsconfig_path):
        with open(fsconfig_path, 'w', encoding='UTF-8') as f:
            f.write('')

        fsconfig.read(fsconfig_path, encoding='UTF-8')
        fsconfig.add_section('GENERAL')
        fsconfig.set('GENERAL', 'RECORD', '0')

        root = tkinter.Tk()

        screen_width = str(root.winfo_screenwidth())
        screen_height = str(root.winfo_screenheight())

        root.destroy()


        fsconfig.set('GENERAL', 'SCREEN_SIZE_X', screen_width)
        fsconfig.set('GENERAL', 'SCREEN_SIZE_Y', screen_height)

        with open(fsconfig_path, 'w') as f:
            fsconfig.write(f)


fsconfig = ConfigParser()
fsconfig.read(fsconfig_path)