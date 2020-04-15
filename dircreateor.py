import os
import shutil
import time
import sys
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

os.chdir(sys.argv[1])#Change directory

def get_filetype(f): #extract file extension
    for i in range (1,len(f)-1):
        if f[-i]=='.':
            return f[-i+1:]
    return "None"

class MyHandler(FileSystemEventHandler): #move file to directory named by file's extension
    def on_created(self,event):
        if not event.is_directory:
            filetype=get_filetype(event.src_path)
            if not os.path.isdir(filetype): #if directory doesnt exist, create it
                os.mkdir(filetype)
            shutil.move(event.src_path,filetype)

observer=Observer()
event_handler=MyHandler()
observer.schedule(event_handler,sys.argv[1],recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

