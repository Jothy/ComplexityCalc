from PyQt5.QtCore import QFileSystemWatcher
import time

class Watcher():
    def __init__(self):
        print('.................................')
        self.fileWatcher = QFileSystemWatcher()
        self.fileWatcher.addPath('D://Projects//ComplexityCalc//Docs')
        self.fileWatcher.directoryChanged.connect(self.filesAdded)
        print('Watching...')

    def filesAdded(self):
        print('new files added')

while True:
    Watchdog=Watcher()
    time.sleep(1)  # make function to sleep for 10 seconds







