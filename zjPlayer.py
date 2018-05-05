"""a simple programme which can display pics in a direction like a video"""


# input a dir path where many images are in it and display these pics in a custom speed


from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
import os
import time, threading



def get_subfilename(dirpath):
    names = []
    for name0 in os.listdir(dirpath):
        name = os.path.join(dirpath, name0)
        if os.path.isfile(name):
            names.append(os.path.abspath(name))
    names.sort()
    return names


def press(event):
    # pass
    # global iFrame
    global t
    global pauseornot
    if event.key == 'right':
        fresh_iFrame(+10)
    elif event.key == 'left':
        fresh_iFrame(-10)
    elif event.key == 'up':
        fresh_iFrame(-1)
    elif event.key == 'down':
        fresh_iFrame(+1)
    elif event.key == ' ':

        # plt.title(' (pause)')
        # t.cancel()
        pauseornot = 1 - pauseornot
        if pauseornot:
            print('pause')
            # plt.title(str(iFrame) + ' (pause)')
            sys.stdout.flush()
            t.stop()
        else:
            print('continune')
            t.start()
            t.run()
    else:
        # print(event.key)
        return
    if event.key != ' ':
        print(iFrame)
        disp_newframe(iFrame)


def fresh_iFrame(n):
    global iFrame
    iFrame = iFrame + n
    if iFrame < 1:
        iFrame = 1
    if iFrame > nFrame:
        iFrame = nFrame
        # return iFrame1



def disp_newframe(iframe):
    global pauseornot
    # if iframe > nFrame:
    #     pauseornot = 1
    if iframe < 1 or iframe > nFrame:
        return
    sys.stdout.flush()
    aximg.set_data(plt.imread(filenames[iframe - 1]))
    if pauseornot == 1:
        plt.title(str(iFrame) + ' (pause)')
    else:
        plt.title(iFrame)
    # ax.plot(np.random.rand(10))
    fig.canvas.draw()

# def recExe():
#     while 1:
#         disp_newframe(iFrame)
#         fresh_iFrame(+1)

class recClass:
    def __init__(self, stopornot):
        self.stopornot = stopornot
        #
        # fig, ax = plt.subplots()
        # # currentPath = os.getcwd()
        # # print(currentPath)
        # # print(os.path.join(currentPath, 'pic/cs16.jpg'))
        # img = plt.imread(filenames[iFrame])
        # aximg = ax.imshow(img)
        # plt.show()
    def stop(self):
        self.stopornot = 1

    def start(self):
        self.stopornot = 0
        # plt.title('')

    def run(self):
        if self.stopornot:
            pass
        else:
            disp_newframe(iFrame)
            fresh_iFrame(+1)


            threading.Timer(0.00001, self.run).start()
        # while 1:
        #     if not self.stopornot:
        #         fresh_iFrame(+1)
        #         disp_newframe(iFrame)
        #         print(iFrame)
        #     else:
        #         pass




if __name__ == '__main__':

    captureDir = '/home/zhaojin/matlab_tools/smallgames/textize_pic_and_video/source_img/mijyyi'
    filenames = get_subfilename(captureDir)
    nFrame = len(filenames)
    print(nFrame)
    iFrame = 1
    pauseornot = 0
    fig, ax = plt.subplots()
    # currentPath = os.getcwd()
    # print(currentPath)
    # print(os.path.join(currentPath, 'pic/cs16.jpg'))
    img = plt.imread(filenames[iFrame])
    aximg = ax.imshow(img)
    # aximg = ax.imshow([])
    # cid = fig.canvas.mpl_connect('button_press_event', onclick )
    # t = threading.Thread(target=recExe)
    t = recClass(pauseornot)
    t.run()
    # threading.Thread(target=recClass(pauseornot).run()).start()
    # t = recClass(pauseornot)

    fig.canvas.mpl_connect('key_press_event', press)
    plt.show()


    # captureDir = '/home/zhaojin/matlab_tools/smallgames/textize_pic_and_video/source_img/mijyyi'

    # for path, subdirs, files in os.walk(captureDir):
    #     print('<a new round')
    #     for name in files:
    #         print(os.path.join(path, name))
    #     print('_______')
        # for name in subdirs:
        #     print(os.path.join(path, name))
        # print('end of a new round>')