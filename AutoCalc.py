import sys
# from PyQt5 import QtCore, QtWidgets
#
# F=QtWidgets.QFileSystemModel()
#
# def directory_changed(path):
#     print('Directory Changed: %s' % path)
#     print(path.contents)
#
# def file_changed(path):
#     print('File Changed: %s' % path)
#
# app = QtCore.QCoreApplication(sys.argv)
#
# paths = ['D://Projects/ComplexityCalc//Docs']
#
# fs_watcher = QtCore.QFileSystemWatcher(paths)
# fs_watcher.directoryChanged.connect(directory_changed)
# fs_watcher.fileChanged.connect(file_changed)
#
# F.setRootPath(paths[0])
# ff=F.rowsInserted()
#
# sys.exit(app.exec_())


import os,time
from PyQt5 import QtGui, QtWidgets
ImgFolder='D:\\Projects\ComplexityCalc\\Docs'
LoopToggle=True

#Check for new file in a folder
def CheckForNewFile():
    print(ImgFolder)
    while True:
        before = dict ([(f, None) for f in os.listdir (ImgFolder)])
        after = dict ([(f, None) for f in os.listdir (ImgFolder)])
        added = [f for f in after if not f in before]
        #removed = [f for f in before if not f in after]
        if added:
            print("Added: ", ", ".join (added))
            QtWidgets.QApplication.processEvents()

CheckForNewFile()

