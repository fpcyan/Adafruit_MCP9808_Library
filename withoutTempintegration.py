## sensor and time lapse integration
from tkinter import *
import sys
import time
import logging
import csv
import string
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

#write Date, time, filename to csv file
def csvWriting(dirpath):
    currentDate = time.strftime("%Y-%m-%d")
    currentTime = time.strftime("%I:%M:%S %p")
    onlyFileName = dirpath[str.find(dirpath, '\\'):len(dirpath)]
    iterThis = (currentDate, currentTime, onlyFileName) #list of relevant data
    global pre_written
    print(iterThis)
    with open('test.csv','a', newline='') as csvfile:
        fieldnames = ['Date','Time','File Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
        if pre_written == False:
            writer.writeheader()
            pre_written = True
        writer.writerow({'Date': iterThis[0], 'Time': iterThis[1], 'File Name':iterThis[2]})

# def dothethingtothisfile():
    #open serial port and read 5 temperatures from each sensor
    #save average of each 5 temperatures to file
    
    
class LoggingTempHandler(FileSystemEventHandler):
    """Logs all the events captured."""
    def on_created(self, event):
        super(LoggingTempHandler, self).on_created(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Created %s: %s", what, event.src_path)
        csvWriting(event.src_path)
        
def main():
    dirwatch = filedialog.askdirectory() #picks the directory to watch
    pre_written = False
    global pre_written
    logging.basicConfig(filename='testlog.log',
                        filemode='w',
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = dirwatch if len(dirwatch) > 1 else '.'
    event_handler = LoggingTempHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()    




if __name__ == "__main__":
    main()


