class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKGRAY = '\033[55m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def text_logo():
    print(bcolors.OKBLUE + r'''
   __  ___                       ______          __  
  /  |/  /__ ____  ___ ____ ____/_  __/__  ___  / /__
 / /|_/ / _ `/ _ \/ _ `/ _ `/___// / / _ \/ _ \/ (_-<
/_/  /_/\_,_/_//_/\_, /\_,_/    /_/  \___/\___/_/___/
                 /___/                                                        
          ''' + bcolors.ENDC)
