# !/usr/bin/env python

import sys
import time
import tkinter as tk

startPoint = [0, 0]
endPoint = [6, 6]

if (len(sys.argv)) == 3:
    '''get value from command line to grid'''
    try:
        endPoint = [int(sys.argv[1]), int(sys.argv[2])]
        if endPoint[0] > 10 or endPoint[1] > 10:
            print('''your grid is {}x{}, it will take a 
            long time to calculate all the path!!!'''.format(endPoint[0], endPoint[1]))
    except:
        print("Error on purse value from command line, use 8x8 grid as default setting")


# start here
# print("the grid is {0}x{1}".format(endPoint[0], endPoint[1]))


def goNext(apath, aPoint):
    '''find path from startPoing to end point'''
    if (aPoint[0] == endPoint[0]) and (aPoint[1] == endPoint[1]):  # at the right edge
        global mycount
        global myPathList
        global msg
        mycount += 1
        myPathList.append(list(apath))
        msg.config(text="Calculating, {0} path found!!!".format(mycount))
        msg.update()
        # print ("add #{0} path|".format(mycount), apath)
        return

    if (aPoint[0] < endPoint[0]):  # not at the right edge
        newPoint = list(aPoint)
        goright_path = list(apath)
        newPoint[0] = newPoint[0] + 1  # go right first
        goright_path.append(newPoint)
        goNext(goright_path, newPoint)

    if (aPoint[1] < endPoint[1]):  # not at the bottom edge
        newPoint = list(aPoint)
        godown_path = list(apath)
        newPoint[1] = newPoint[1] + 1  # go down 1 step
        godown_path.append(newPoint)
        goNext(godown_path, newPoint)


def draw_grid(canvas, GridSize):
    canvas.delete('all')
    global margin
    for x in range(0, GridSize[0] + 1):
        canvas.create_line(x * 30 + margin, margin,
                           x * 30 + margin, GridSize[1] * 30 + margin)
        canvas.update()
        time.sleep(0.05)
    for y in range(0, GridSize[1] + 1):
        canvas.create_line(margin, y * 30 + margin,
                           GridSize[0] * 30 + margin, y * 30 + margin)
        canvas.update()
        time.sleep(0.05)


def simulate():
    global entry, myPathList, msg, margin
    print("simulating...")
    t = entry.get()
    pos = int(t)
    print(pos)
    if pos < 0 or pos >= len(myPathList):
        msg.config(text="wrong number, please re-input")
        msg.update()
        return
    posList = myPathList[pos]
    msg.config(text=str(posList))
    msg.update()
    global canvas
    draw_grid(canvas, endPoint)
    lastCur = []
    for cur in posList:
        if len(lastCur) == 0:
            lastCur = list(cur)
            continue
        x = lastCur[0]
        y = lastCur[1]
        x1 = cur[0]
        y1 = cur[1]
        lastCur = list([x1, y1])
        canvas.create_line(margin + x * 30, margin + y * 30,
                           margin + x1 * 30, margin + y1 * 30,
                           fill="red", arrow="last")
        canvas.update()
        time.sleep(0.1)


if __name__ == '__main__':
    path1 = []
    mypoint = startPoint[:]
    mycount = 0
    path1.append(list(mypoint))
    myPathList = []
    margin = 15

    myFrame = tk.Tk()
    myFrame.title("Grid Path Simulator")
    msg = tk.Message(myFrame,
                     text="Drawing the Grid of {0}x{1}".format(endPoint[0], endPoint[1]),
                     justify="left",
                     width=400)
    msg.grid(row=0, column=0, sticky='W')

    msglabel = tk.Message(myFrame, text="choose path #", justify='left')
    msglabel.grid(row=1, column=0, sticky="W")

    entry = tk.Entry(myFrame, width=8)
    entry.grid(row=1, column=1, sticky="W")

    btnSim = tk.Button(myFrame, text="simulate", command=simulate, state="disabled")
    btnSim.grid(row=1, column=2, sticky="W")
    btnQuit = tk.Button(myFrame, text="Quit", command=myFrame.destroy)
    btnQuit.grid(row=1, column=3, sticky="W")

    canvas = tk.Canvas(myFrame, width=400, heigh=600)
    canvas.grid(row=2, column=0)

    draw_grid(canvas, endPoint)

    goNext(path1, mypoint)
    # start to calculate the path and show message

    btnSim.config(state="normal")
    msglabel.config(text="choose path # between 0 and {0}:".format(mycount - 1), width=120)
    msglabel.update()
    myFrame.mainloop()
    # print(endPoint[0], endPoint[1], mycount)
