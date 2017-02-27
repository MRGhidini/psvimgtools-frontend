#! /usr/bin/env python
#
# Support module generated by PAGE version 4.8.9
# In conjunction with Tcl version 8.6
#    Feb 25, 2017 07:14:41 PM
import os
import sys
import tkFileDialog
import tkMessageBox

from os.path import expanduser

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def auto():
    import cmaDir
    if sys.platform.__contains__("linux"):
            home = expanduser("~")
            text_file = open(home+"/.config/codestation/qcma.conf", "r")
            line = text_file.read()
            line = line.splitlines()[1]
            line = line[9:]
            text_file.close()

            text_file = open("cmadir.txt", "w+")
            text_file.write(line)
            text_file.close()
            print "CMA Dir: " + line
            cmaDir.close_window(root)
            tkMessageBox.showinfo(title="Cma Directory",message="Detected: ["+line+"]!")

    if sys.platform.__contains__("win"):
        import _winreg
        qcma = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\codestation\qcma")
        path = _winreg.QueryValueEx(qcma, "appsPath")
        print "CMA Dir: " + path[0]
        text_file = open("cmadir.txt", "w+")
        text_file.write(path[0])
        text_file.close()
        _winreg.closeKey()
        cmaDir.close_window(root)
        tkMessageBox.showinfo(title="Cma Directory", message="Detected: [" + path + "]!")





    sys.stdout.flush()

def submit(DIR):
    import cmaDir
    text_file = open("cmadir.txt", "w+")
    text_file.write(DIR)
    text_file.close()
    cmaDir.close_window(root)
    sys.stdout.flush()

def browse():
    import cmaDir
    text_file = open("cmadir.txt", "w+")
    text_file.write(tkFileDialog.askdirectory(title="CMA Directory"))
    text_file.close()
    cmaDir.close_window(root)
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import cmaDir
    cmaDir.vp_start_gui()

