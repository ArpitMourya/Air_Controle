import cv2
import mediapipe as mp
import screen_brightness_control as sbc
import pyautogui
from multiprocessing.pool import ThreadPool
#import xlwt
import pickle
import os
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#from functools import partial
class MyClass():
    def __init__(self, static,two_step='',dynamic=''):
        self.static = static
        self.two_step = two_step
        self.dynamic = dynamic
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

# output_folder = "D:\programming\setup_Air_control[1]"
global dic_task_ges
history = []
def his(gest):
    history.append(gest)
    if len(history) >5:
            del history[0]  
    print(history)
#functions for task completion
def KeyPress(gest,alt_plus):
    if history.count(gest) <1:
            pyautogui.hotkey("altleft", alt_plus)





def Volume(dist,gest):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
         
         
         
         

    volMin,volMax = volume.GetVolumeRange()[:2]
    vol = np.interp(dist,[10,120],[volMin,volMax]) 
    if volume.GetMute()==True:
          volume.SetMute(0,None)
          
            
    
    volume.SetMasterVolumeLevel(vol, None)
    # his(gest)

def distance(x1 , x2 ,y1 ,y2):
    dist = (((x2 - x1)**2) + ((y2-y1)**2))**(1/2)
    return dist


def angle(x1,x2,y1,y2,x0,y0):
    v1 = np.array([x1 - x0, y1 - y0])
    v2 = np.array([x2 - x0, y2 - y0])
    angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))) * 180 / np.pi
    return angle

def Brightness(dist,gest):
    sbc.set_brightness(dist,display=0)
    # his(gest)

def mousePointer(gest,dist1,x1,y1):
    movx , movy = (1920/640)*(x1-50), (1080/480)*(y1-50)
    # his(gest)
    movx=1920-(movx)

        
    pyautogui.moveTo(movx, movy, duration =0)
    if dist1<=60:
        pyautogui.click(movx, movy)

def CloseTab(gest):
        
        KeyPress(gest,"f4")
        # his(gest)
def ToggleTab(gest):
        
        KeyPress(gest,"tab")
        # his(gest)
def Scroll(gest,dist1,x1,y1):
     if (200 >= dst1 and dst1 >=80):
          pyautogui.scroll(200)
     elif (60 >= dst2 and dst2 >=0):
          pyautogui.scroll(-200)
     
def recognise(dst1 , dst2 , dst3,dst4,dst5,dst6,dst7,dst8,dst9,ang1,ang2):
    if (150 >= dst1 and dst1 >=50) and (50>=dst2 and dst2>=25) and (60>=dst3 and dst3 >=20) and (90>=dst4 and dst4>=25):
        return "open_palm"
    elif(125 >= dst1 and dst1 >=8) and (200>=dst2 and dst2>=60) and (35>=dst3 and dst3 >=5) and (145>=dst4 and dst4>=45):
        return "yoo"
    elif (200 >= dst1 and dst1 >=20) and (44>=dst2 and dst2>=7) and (188>=dst3 and dst3 >=65) and (32>=dst4 and dst4>=10) and (84 >= dst5 and dst5 >=24) and (90>=dst6 and dst6>=25) and (69>=dst7 and dst7 >=0) and (60>=dst8 and dst8>=0) and dst9>=70:
        return "gun_shot"
    elif (225 >= dst1 and dst1 >=80) and (140>=dst2 and dst2>=35) and (253>=dst3 and dst3 >=86) and (40>=dst4 and dst4>=3):
        return "victory"
    elif  (150 >= dst1 and dst1 >=50) and (35>=dst2 and dst2>=12) and (37>=dst3 and dst3 >=13) and (35>=dst4 and dst4>=11):
        return "thumb_up"
    elif  (125 >= dst1 and dst1 >=8) and (10>=dst2 and dst2>=0) and (18>=dst3 and dst3 >=1) and (29>=dst4 and dst4>=8) and (52 >= dst5 and dst5 >=14) and (58>=dst6 and dst6>=17) and (60>=dst7 and dst7 >=18) and (48>=dst8 and dst8>=15):
        return "C_gesture"
    elif (178>= dst1 and dst1 >=16) and (192>=dst2 and dst2>=38) and (44>=dst3 and dst3 >=11) and (36>=dst4 and dst4>=6):
        return "pointing_up"
    elif (22 >= dst1 and dst1 >=5) and (115>=dst2 and dst2>=32) and (55>=dst3 and dst3 >=20) and (100>=dst4 and dst4>=22):
        print("closing")
        os._exit(0)
    elif  (125 >= dst1 and dst1 >=8) and (170>=dst2 and dst2>=80) and (18>=dst3 and dst3 >=1) and (29>=dst4 and dst4>=8) and (52 >= dst5 and dst5 >=14) and (58>=dst6 and dst6>=17) and (60>=dst7 and dst7 >=18) and (48>=dst8 and dst8>=15):
        return "L_gesture"
    # elif (90 >= ang1 and ang1 >=60 )and ( 120>= dst1 and dst1 >=60) and (35>=dst2 and dst2>=10) and (35>=dst3 and dst3 >=10) and (35>=dst4 and dst4>=10):  
    #     # if (150 >= dst1 and dst1 >=50) and (35>=dst2 and dst2>=12) and (37>=dst3 and dst3 >=13) and (35>=dst4 and dst4>=11): 
    #          return "left"   
    # elif (125 >= ang1 and ang1 >=80) :
    #     # if (150 >= dst1 and dst1 >=50) and (35>=dst2 and dst2>=12) and (37>=dst3 and dst3 >=13) and (35>=dst4 and dst4>=11):
    #        return "right"
    else:
        return "NO_gesture"
obj= load_object("data.pickle")
print(obj)
dynamic = obj.dynamic
two = obj.two_step
stat = obj.static
print(dynamic,two,stat,sep="\n")
'''dynamic={
     "yoo":bright,
     "C_gest":volume,
     
     

}
stat={
     "Victory":close,
      "Thumb_up":opentabs,
     
}
two={
     "pointer":mouse,
      "Gun_shot":scroll
}'''
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.8,
            min_tracking_confidence=0.8)
mpDraw = mp.solutions.drawing_utils
pool = ThreadPool(processes=8)

# obj = load_object("data.pickle")
# dic_task_ges=obj.param
# print(dic_task_ges)

# wrte = xlwt.Workbook()
# ws =wrte.add_sheet("master_sheet")
# r,cl = 1,0
while True:

    success, img = cap.read()
    h,w,c =img.shape
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            id =list( enumerate(handLms.landmark))   
            #fingertip distances (4,8,12,16,20)
            dst1 = pool.apply(distance,[id[4][1].x * w, id[8][1].x *w,id[4][1].y*h,id[8][1].y*h])
            ang1=pool.apply(angle,[id[5][1].x*w, id[17][1].x*w,id[5][1].y*h,id[17][1].y*h,id[0][1].x*w,id[0][1].y*h])
            ang2=pool.apply(angle,[id[6][1].x*w, id[18][1].x*w,id[6][1].y*h,id[18][1].y*h,id[0][1].x*w,id[0][1].y*h])
            
            dst2 = pool.apply(distance,[id[8][1].x * w, id[12][1].x *w,id[8][1].y*h,id[12][1].y*h])
            dst3 = pool.apply(distance,[id[12][1].x * w, id[16][1].x *w,id[12][1].y*h,id[16][1].y*h])
            dst4 = pool.apply(distance,[id[16][1].x * w, id[20][1].x *w,id[16][1].y*h,id[20][1].y*h])
            #distance of bottum of finger(5,9,13,17)
            dst5 = pool.apply(distance,[id[5][1].x * w, id[6][1].x *w,id[5][1].y*h,id[6][1].y*h])
            dst6 = pool.apply(distance,[id[9][1].x * w, id[10][1].x *w,id[9][1].y*h,id[10][1].y*h])
            dst7 = pool.apply(distance,[id[13][1].x * w, id[14][1].x *w,id[13][1].y*h,id[14][1].y*h])
            dst8 = pool.apply(distance,[id[17][1].x * w, id[18][1].x *w,id[17][1].y*h,id[18][1].y*h])
            #dst9 is (4-20)
            dst9 = pool.apply(distance,[id[4][1].x * w, id[20][1].x *w,id[4][1].y*h,id[20][1].y*h])

            gesture = recognise(dst1,dst2,dst3,dst4,dst5,dst6,dst7,dst8,dst9,ang1,ang2)
            # l3=list(static.keys())
            # l4=list(static.values())
            # print(l3)
            for i in range(2):
                 l1=list(dynamic.keys())
                 l2=list(dynamic.values())
                 l3=list(stat.keys())
                 l4=list(stat.values())
                 l5=list(two.keys())
                 l6=list(two.values())
                 
                 if gesture==l1[i]:
                      eval(l2[i])(dst1,gesture)
            
               
                 if gesture==l3[i]:
                  pool.apply(eval(l4[i]),[gesture])
                 if gesture==l5[i]:
                            eval(l6[i])(gesture,dst1,id[4][1].x*w,id[4][1].y*h)
              
            
            
                 
            his(gesture)
                    
                      
                      
            # ws.write(r,cl,dst1) , ws.write(r,cl+1 ,dst2),ws.write(r,cl+2,dst3) , ws.write(r,cl+3 ,dst4)
            # ws.write(r,cl+5,ang1) , ws.write(r,cl+6 ,ang2)#,ws.write(r,cl+7,dst7) , ws.write(r,cl+8 ,dst8)
            # r+=1 
            cv2.putText(img,str(gesture),(0,20),cv2.FONT_HERSHEY_SIMPLEX,1,(256,256,256),2,cv2.LINE_AA,False)
            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)
            
# wrte.save( output_folder + "//"+ 'master sheet.xls')
    cv2.imshow("image" , img)
    cv2.waitKey(1)

