from multiprocessing.pool import ThreadPool

def distance(x1 , x2 ,y1 ,y2):
    dist = (((x2 - x1)**2) + ((y2-y1)**2))**(1/2)
    return dist
  
def recognise(dst1 , dst2 , dst3,dst4,dst5,dst6,dst7,dst8,dst9):
    ''' This func will return the name of hand gesture, for HANDGES function. '''
    if (150 >= dst1 and dst1 >=50) and (50>=dst2 and dst2>=25) and (60>=dst3 and dst3 >=20) and (90>=dst4 and dst4>=25):
        return "open_palm"
    elif(200 >= dst1 and dst1 >=65) and (200>=dst2 and dst2>=60) and (35>=dst3 and dst3 >=5) and (145>=dst4 and dst4>=45):
        return "yoo"
    elif (200 >= dst1 and dst1 >=60) and (44>=dst2 and dst2>=7) and (188>=dst3 and dst3 >=65) and (32>=dst4 and dst4>=10) and (84 >= dst5 and dst5 >=24) and (90>=dst6 and dst6>=25) and (69>=dst7 and dst7 >=0) and (60>=dst8 and dst8>=0) and dst9>=70:
        return "Gun_shot"
    elif (225 >= dst1 and dst1 >=80) and (140>=dst2 and dst2>=35) and (253>=dst3 and dst3 >=86) and (40>=dst4 and dst4>=3):
        return "Victory"
    elif (150 >= dst1 and dst1 >=50) and (35>=dst2 and dst2>=12) and (37>=dst3 and dst3 >=13) and (35>=dst4 and dst4>=11):
        return "Thumb_up"
    elif (125 >= dst1 and dst1 >=8) and (10>=dst2 and dst2>=0) and (18>=dst3 and dst3 >=1) and (29>=dst4 and dst4>=8) and (52 >= dst5 and dst5 >=14) and (58>=dst6 and dst6>=17) and (60>=dst7 and dst7 >=18) and (48>=dst8 and dst8>=15):
        return "C_gest"
    elif (178>= dst1 and dst1 >=16) and (192>=dst2 and dst2>=38) and (44>=dst3 and dst3 >=11) and (36>=dst4 and dst4>=6):
        return "pointer"
    elif (22 >= dst1 and dst1 >=5) and (115>=dst2 and dst2>=32) and (55>=dst3 and dst3 >=20) and (100>=dst4 and dst4>=22):
        return "peacock"
    else:
        return "NO_gesture"
def HandGes(handLMS:list , w :int, h:int):
    '''This func takes list of landmarks, width and height of image. it returns the detected Hand Gesture'''
    pool = ThreadPool(processes=8)  
    dst1 = pool.apply(distance,[handLMS[4][1].x * w, handLMS[8][1].x *w,handLMS[4][1].y*h,handLMS[8][1].y*h])
    dst2 = pool.apply(distance,[handLMS[8][1].x * w, handLMS[12][1].x *w,handLMS[8][1].y*h,handLMS[12][1].y*h])
    dst3 = pool.apply(distance,[handLMS[12][1].x * w, handLMS[16][1].x *w,handLMS[12][1].y*h,handLMS[16][1].y*h])
    dst4 = pool.apply(distance,[handLMS[16][1].x * w, handLMS[20][1].x *w,handLMS[16][1].y*h,handLMS[20][1].y*h])
    #distance of bottum of finger(5,9,13,17)
    dst5 = pool.apply(distance,[handLMS[5][1].x * w, handLMS[6][1].x *w,handLMS[5][1].y*h,handLMS[6][1].y*h])
    dst6 = pool.apply(distance,[handLMS[9][1].x * w, handLMS[10][1].x *w,handLMS[9][1].y*h,handLMS[10][1].y*h])
    dst7 = pool.apply(distance,[handLMS[13][1].x * w, handLMS[14][1].x *w,handLMS[13][1].y*h,handLMS[14][1].y*h])
    dst8 = pool.apply(distance,[handLMS[17][1].x * w, handLMS[18][1].x *w,handLMS[17][1].y*h,handLMS[18][1].y*h])
    #dst9 is (4-20)
    dst9 = pool.apply(distance,[handLMS[4][1].x * w, handLMS[20][1].x *w,handLMS[4][1].y*h,handLMS[20][1].y*h])

    gesture = recognise(dst1,dst2,dst3,dst4,dst5,dst6,dst7,dst8,dst9)
    return gesture
   
