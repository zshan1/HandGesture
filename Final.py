from Leap import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
import globalVariables as gv
import pickle
from random import randint
import time
def CenterData(X):
    allXCoordinates = X[0,::3]
    meanValue = allXCoordinates.mean()
    X[0,::3] = allXCoordinates - meanValue
    allYCoordinates = X[0,1::3]
    meanValue = allYCoordinates.mean()
    X[0,1::3] = allYCoordinates - meanValue
    allZCoordinates = X[0,2::3]
    meanValue = allZCoordinates.mean()
    X[0,2::3] = allZCoordinates - meanValue
    return X

def DrawImageToHelpUserPutTheirHandOverTheDevice():
    inslines = []
    image_file = open("/Users/apple/Desktop/hand/leap.jpg")
    image = plt.imread(image_file)
    
    ax2.imshow(image)
    inslines.append(ax2.plot([50,75],[450,425]))
    inslines.append(ax2.plot([50,75],[400,425]))
    inslines.append(ax2.plot([100,125],[450,425]))
    inslines.append(ax2.plot([100,125],[400,425]))
    inslines.append(ax2.plot([150,175],[450,425]))
    inslines.append(ax2.plot([150,175],[400,425]))
        

def HandOverDevice():
    if(len(frame.hands) > 0):
        return True
    
def instructHand(v1,v2):
    global programState,q
    if v1 <100 and v2 > -100:
        programState = 2
        if (q == 1):
            ax2.clear()
            image_file = open("/Users/apple/Desktop/hand/goto2.jpg")
            image = plt.imread(image_file)
            ax2.imshow(image)
            q = 2
            plt.pause(1)
    else:
        programState = 1
        q = 1
        ax2.clear()
        image_file = open("/Users/apple/Desktop/hand/1.png")
        image = plt.imread(image_file)
        ax2.imshow(image)
        if v1 > 100:
            inslines = []
            inslines.append(ax2.plot([200,225],[450,425]))
            inslines.append(ax2.plot([200,225],[400,425]))
            inslines.append(ax2.plot([275,300],[450,425]))
            inslines.append(ax2.plot([275,300],[400,425]))
            while ( len(inslines) > 0 ):
                plt.pause(0.001)
                ln = inslines.pop()
                ln.pop(0).remove()
                del ln
                ln = []
        if v2 < -100:
            inslines = []
            inslines.append(ax2.plot([225,200],[400,425]))
            inslines.append(ax2.plot([225,200],[450,425]))
            inslines.append(ax2.plot([300,275],[400,425]))
            inslines.append(ax2.plot([300,275],[450,425]))
            while ( len(inslines) > 0 ):
                plt.pause(0.001)
                ln = inslines.pop()
                ln.pop(0).remove()
                del ln
                ln = []
    
def HandleState0():
    global programState,userName
    DrawImageToHelpUserPutTheirHandOverTheDevice()
    ax3.clear()
    ax4.clear()
    if HandOverDevice():
        programState = 1
        
def HandleState1():
    #ax1.scatter3D(-10.0,-100.0,140.0, cmap='Greens')
    global programState,testData,status, intchoose
    if(len(frame.hands) > 0):
        hand = frame.hands[0]
        k = 0
        for i in range(0,5):
            finger = hand.fingers[i]
            for j in range(0,4):
                bone = finger.bone(j)
                boneBase = bone.prev_joint
                boneTip = bone.next_joint
                xBase = boneBase[0]
                yBase = boneBase[1]
                zBase = boneBase[2]
                
                xTip = boneTip[0]
                yTip = boneTip[1]
                zTip = boneTip[2]
                lines.append(ax1.plot([-xBase,-xTip],[zBase,zTip],[yBase,yTip],'r'))
                if( (j == 0) | (j == 3) ):
                    testData[0,k] = xTip
                    testData[0,k+1] = yTip
                    testData[0,k+2] = zTip
                    k = k+3   
        instructHand(-frame.hands[0].fingers[0].bone(3).next_joint[0], -frame.hands[0].fingers[4].bone(3).next_joint[0])
        if programState == 2:
            plt.pause(0.0000001)
            HandleState2()
    else:
        programState = 0
        ax2.clear()

def HandleState2():
    global programState,testData,status, intchoose, database, userName, start, switch, tendigit, gotonext, end1, calnum2, good, better
    testData = CenterData(testData)
    predictedClass = clf.predict(testData)
    intlist = [0,1,2,3,4,5,6]            
    ax2.clear()
    userNum2 = 0
    if switch == False:
        txt1 = ax2.text(0.4, 0.4,intlist[intchoose],family='fantasy',fontsize=100, color='white',transform=ax2.transAxes)
    if switch == True and gotonext == False:
        if showmath == False:
            txt1 = ax2.text(0.2, 0.4,tendigit,family='fantasy',fontsize=100, color='black',transform=ax2.transAxes)
            txt2 = ax2.text(0.5, 0.4,intlist[intchoose],family='fantasy',fontsize=100, color='black',transform=ax2.transAxes)
        else:
            newnum = (tendigit*10)+intlist[intchoose]           
            calnum2 = newnum - calnum1
            if calnum2 < 0:
                txt0 = ax2.text(0.1, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt1 = ax2.text(0.25, 0.4,calnum1,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt3 = ax2.text(0.6, 0.4,calnum2,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt4 = ax2.text(0.9, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
            else:
                txt0 = ax2.text(0.1, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt1 = ax2.text(0.25, 0.4,calnum2,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt2 = ax2.text(0.5, 0.4,"-",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt3 = ax2.text(0.6, 0.4,calnum1,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt4 = ax2.text(0.9, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
        userNum2 = str(tendigit)
    userNum = str(intlist[intchoose])
    if userNum not in database[userName]['attempt']:
        database[userName]['attempt'][userNum]= 0
        database[userName]['time'][userNum]= []
        database[userName]['proficiency'][userNum] = False
        database[userName]['reduced'][userNum] = False
    if switch == True:
        if userNum2 not in database[userName]['attempt']:
            database[userName]['attempt'][userNum2]= 0
            database[userName]['time'][userNum2]= []
            database[userName]['proficiency'][userNum2] = False
            database[userName]['reduced'][userNum2] = False
    ax4.clear()
    image_file = open("/Users/apple/Desktop/hand/hint.jpg")
    image = plt.imread(image_file)
    ax4.imshow(image)
    next_t = time.time()
    if gotonext == False:
        if switch == True:
            if showmath == False: 
                ax2.set_facecolor('xkcd:blue')
                txt1 = ax2.text(0.2, 0.4,tendigit,family='fantasy',fontsize=100, color='grey',transform=ax2.transAxes)
                txt2 = ax2.text(0.5, 0.4,intlist[intchoose],family='fantasy',fontsize=100, color='red',transform=ax2.transAxes)
            else:
                if calnum2 < 0:
                    txt0 = ax2.text(0.1, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                    txt1 = ax2.text(0.25, 0.4,calnum1,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                    txt3 = ax2.text(0.6, 0.4,calnum2,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                    txt4 = ax2.text(0.9, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                else:
                    txt0 = ax2.text(0.1, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                    txt1 = ax2.text(0.25, 0.4,calnum2,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                    txt2 = ax2.text(0.5, 0.4,"-",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                    txt3 = ax2.text(0.6, 0.4,calnum1,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                    txt4 = ax2.text(0.9, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
        if next_t - start < 10:
            if intlist[intchoose] == predictedClass.astype(int)[0,1]:
                database[userName]['time'][userNum].append(next_t - start)
                ax3.clear()
                ax3.bar(1,10,align='center',edgecolor='white',color = 'white')
                ax3.bar(2, 10-(next_t - start) ,align='center',edgecolor='black',color = 'green')
                ax3.bar(3,10,align='center',edgecolor='white',color = 'white')
                if switch == False:
                    status = True
                gotonext = True
                database[userName]['attempt'][userNum] += 1
                if showmath == True and next_t - start>8:
                    better = 2
                good += 1
                plt.pause(1)        
            else:
                ax3.clear()
                ax3.bar(1,10,align='center',edgecolor='white',color = 'white')
                ax3.bar(2, 10-(next_t - start) ,align='center',edgecolor='black',color = 'red')
                ax3.bar(3,10,align='center',edgecolor='white',color = 'white')
               
        else:
            database[userName]['time'][userNum].append(10)
            database[userName]['attempt'][userNum] += 1
            status = True
            gotonext = True
            if better>4:
                better = 2
            print better
            ax2.clear()
            plt.pause(1)
            ax3.clear()
        end1 = time.time()   
    if gotonext == True and switch == True and status == False:
        ax2.clear()
        ax3.clear()
        if showmath == False: 
            txt1 = ax2.text(0.2, 0.4,tendigit,family='fantasy',fontsize=100, color='red',transform=ax2.transAxes)
            txt2 = ax2.text(0.5, 0.4,intlist[intchoose],family='fantasy',fontsize=100, color='green',transform=ax2.transAxes)
        else:
            if calnum2 < 0:
                txt0 = ax2.text(0.1, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt1 = ax2.text(0.25, 0.4,calnum1,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt3 = ax2.text(0.6, 0.4,calnum2,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt4 = ax2.text(0.9, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
            else:
                txt0 = ax2.text(0.1, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt1 = ax2.text(0.25, 0.4,calnum2,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt2 = ax2.text(0.5, 0.4,"-",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt3 = ax2.text(0.6, 0.4,calnum1,family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
                txt4 = ax2.text(0.9, 0.4,"|",family='fantasy',fontsize=40, color='white',transform=ax2.transAxes)
        second_next_t = time.time()
  #      print second_next_t - end1
        if second_next_t - end1 < 10:
            if userNum2 == predictedClass.astype(int)[0,1]:
                database[userName]['time'][userNum2].append(second_next_t - end1)
                ax3.clear()
                ax3.bar(1,10,align='center',edgecolor='white',color = 'white')
                ax3.bar(2, 10-(second_next_t - end1) ,align='center',edgecolor='black',color = 'green')
                ax3.bar(3,10,align='center',edgecolor='white',color = 'white')
                status = True
                end = time.time()
                if showmath == True and second_next_t - end1>8:
                    better = 2
                database[userName]['attempt'][userNum2] += 1
                plt.pause(1)        
            else:
                ax3.clear()
                ax3.bar(1,10,align='center',edgecolor='white',color = 'white')
                ax3.bar(2, 10-(second_next_t - end1) ,align='center',edgecolor='black',color = 'red')
                ax3.bar(3,10,align='center',edgecolor='white',color = 'white')
        else:
            database[userName]['time'][userNum2].append(10)
            database[userName]['attempt'][userNum2] += 1
            status = True
            ax2.clear()
            plt.pause(1)
            if better>4:
                better = 2
            ax3.clear()
    pickle.dump(database,open('/Users/apple/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/userData/database.p','wb'))



avgcompare = False
hcompare = False
switch = False
database = pickle.load(open('/Users/apple/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/userData/database.p','rb'))
userName = raw_input('Please enter your name to start: ')
if userName in database:
    print 'welcome back ' + userName + '!'
    database[userName]['logins'] +=1
    if (len(database[userName]['avg']) == 7):
        avgcompare = True
else:
    database[userName] = {}
    print 'welcome ' + userName + '!'
    logins = 1
    database[userName]['chooselst'] = [0,1,2,3,4,5,6]
    database[userName]['logins'] = logins
    database[userName]['time'] = {}
    database[userName]['attempt'] = {}
    database[userName]['proficiency'] = {}
    database[userName]['reduced'] = {}
    database[userName]['avg'] = {}
pickle.dump(database,open('/Users/apple/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/userData/database.p','wb'))
#print database
        
controller = Controller()
lines = []
dots = []
q=0
programState = 0
start = 0
x = 0
intchoose = 0
good = 0
end1 = 0
better = 0
calnum1 = 0
status = False
gotonext = False
checkone = False
checktwo = False
showmath = False
matplotlib.interactive(True)
fig = plt.figure( figsize=(16,8) )
ax1 = fig.add_subplot(2,2,1,projection='3d' )
ax1.set_xlim(-200,180)
ax1.set_ylim(-250,50)
ax1.set_zlim(0,280)
ax1.view_init(azim=90)
ax2 = fig.add_subplot(2, 2, 3)
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
ax2.set_facecolor('xkcd:blue')
ax3 = fig.add_subplot(2, 2, 2)
ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)
ax4 = fig.add_subplot(2, 2, 4)
ax4.get_xaxis().set_visible(False)
ax4.get_yaxis().set_visible(False)
k = 0
clf = pickle.load( open('userData/classifier.p','rb') )
testData = np.zeros((1,1*30),dtype='f')
while True:
    frame = controller.frame()
    if ( programState == 0 ):
        HandleState0()
    elif ( programState == 1 ):
        HandleState1()
    elif ( programState == 2 ):
        if status == True:            
            intchoose = database[userName]['chooselst'][0]
            database[userName]['chooselst'].pop(0)
            if (len(database[userName]['chooselst']) < 3):
                database[userName]['chooselst'].append(randint(1, 6))
                if good >3:
                    switch = True
            if switch == True:
                tendigit = randint(1, 1)
                better +=1
            if better > 4:
                if better < 11:
                    calnum1 = randint(1, 30)
                    while calnum1-intchoose < 0:
                        calnum1 = randint(1, 20)
                    showmath = True
                if better > 10:
                    calnum1 = randint(1, 100)
                    showmath = True
            elif(better < 6):
                showmath = False
            start = time.time()
            status = False
            gotonext = False
        HandleState1()
  #      print database[userName]['chooselst']
    plt.pause(0.00001)
    pickle.dump(database,open('/Users/apple/Desktop/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib/userData/database.p','wb'))
    while ( len(lines) > 0 ):
        ln = lines.pop()
        ln.pop(0).remove()
        del ln
        ln = []


