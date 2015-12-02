## sensor and time lapse integration
from tkinter import filedialog
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
import sys, time, logging, os, csv, string, serial

#write Date, time, filename to csv file
def csvWriting(dirpath,templist):
    currentDate = time.strftime("%Y-%m-%d")
    currentTime = time.strftime("%I:%M:%S %p")
    onlyFileName = os.path.basename(dirpath)
    iterThis = (currentDate, currentTime, onlyFileName, templist[0], templist[1]) #list of relevant data
    global pre_written
    print(iterThis)
    with open('tempsensing.csv','a', newline='') as csvfile:
        fieldnames = ['Date','Time','File Name','Temp 1 (*C)', 'Temp 2 (*C)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
        if pre_written == False:
            writer.writeheader()
            pre_written = True
        writer.writerow({'Date': iterThis[0], 'Time': iterThis[1], 'File Name':iterThis[2], 'Temp 1 (*C)': iterThis[3], 'Temp 2 (*C)': iterThis[4]})

def TempSensing():
    DEFAULT_PORT = "COM4"
    x = serial.Serial(port=DEFAULT_PORT, baudrate=9600, timeout=40)
    time.sleep(3)
    x.write([1,2,3,4,5])
    strSense = x.read(210)
    strSense = str(strSense)
    strSense = strSense.split(',')
    temp1list = []
    temp2list = []
    pos = 0
    for z in strSense:

        if z == 'Sensor 1 Temp:':
            if len(temp1list) < 5:
                temp1list.append(strSense[pos+1])
        if z == 'Sensor 2 Temp:':
            if len(temp2list) < 5:
                temp2list.append(strSense[pos+1])
        pos += 1

    sum1 = 0
    sum2 = 0
    for p in temp1list:
        sum1 += float(p)

    for r in temp2list:
        sum2 += float(r)

    temp1 = sum1/len(temp1list)
    temp2 = sum2/len(temp2list)
    templist = (temp1, temp2)
    x.close()
    return(templist)


class LoggingTempHandler(FileSystemEventHandler):
    """Logs all the events captured."""
    def on_created(self, event):
        super(LoggingTempHandler, self).on_created(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Created %s: %s", what, event.src_path)
        templist = TempSensing()
        csvWriting(event.src_path, templist) #this happens last

def main():
    dirwatch = filedialog.askdirectory() #picks the directory to watch
    global pre_written
    pre_written = False
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
