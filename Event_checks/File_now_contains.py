from .Utils import Utils

def File_now_contains(setting):
    data = setting.split(':')
    filename = data[0]
    string = data[1]
    if Utils.string_exists(filename, string):
            return True
    else:
            return False        