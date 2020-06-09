import pyautogui
import time

# time.sleep(4)
# print('a')
# print(pyautogui.position())
# pyautogui.moveTo(744,240)
def send_requests(num):
    for i in range(1,num):
        print (i)
        pyautogui.click()
        pyautogui.scroll(-62)
        if(i%30==0):
            #savepos
            pos=pyautogui.position()
            x=pos[0]
            y=pos[1]
            pyautogui.moveTo(852,376)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(x,y)
            # pyautogui.click()
        if(i%10==0):
            pyautogui.scroll(-8)
            
        time.sleep(1)
def send_requests_filter(num):
    for i in range(1,num):
        print (i)

        pos=pyautogui.position()
        x=692
        y=pos[1]
        pyautogui.moveTo(x,y)
        
        #check if clickable
        PIXEL = pyautogui.screenshot(
            region=(
                x, y, 1, 1
            )
        )
        COLOR = PIXEL.getcolors()
        if(COLOR[0][1]==(245,246,247)):
            pyautogui.click()
        else:
            pyautogui.scroll(-62)
        
        pyautogui.moveTo(x+100,y)
        pyautogui.click()
        time.sleep(1)
        pyautogui.scroll(-80)
        pyautogui.moveTo(x,y)
        

        # if(i%10==0):
        #     pyautogui.scroll(-8)
            
        time.sleep(1)
def get_key_interupt():
    for i in range(10):
        if(input()):
            print("s")


def confirm_requests(num):
    for i in range(1,num):
        
        pyautogui.click()
        pyautogui.scroll(-69)
        if(i%70==0):
            pyautogui.scroll(-8)
            
        time.sleep(1)

def fb_login(email,password):
    pyautogui.moveTo(872,148)
    pyautogui.click()
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')
    pyautogui.write(email)

    pyautogui.moveTo(1019,148)
    pyautogui.click()
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')
    pyautogui.write(password)

    pyautogui.moveTo(1140,148)
    pyautogui.click()
    
def cancel_requests():
    for i in range(500):
        pyautogui.moveTo(685,281)
        pyautogui.click()
        pyautogui.moveTo(685,401)
        if(i%10!=0):
            pyautogui.click()
        time.sleep(1)
        pyautogui.scroll(-69)
        time.sleep(1)

def scroll_down(num):
    for i in range(num):
        pyautogui.scroll(-1000)
        # time.sleep(1)
# pyautogui.scroll(-69)

# fb_login('silvatemporary@gmail.com','Silva.mkc123456#')
# print(pyautogui.position()[0])
# print(pyautogui.position()[1])
# print(pyautogui.position())
# cancel_requests()
# scroll_down(1000)
send_requests_filter(10)

# pyautogui.scroll(-8)
# confirm_requests(33)
# get_key_interupt()





def gradient(y1,y2,x=1):
    return((y2-y1)/x)

# x=[1,2,3,4,100,5,6,1,9,10,12,20]
# def change(prev):
#     max_grad=1
#     for i in range(len(prev)):
#         if(gradient(prev[i],prev[i+1])>max_grad):
#             x=1
#             while True:
#                 x+=1
#                 if(gradient(prev[i],prev[i+x],x)>max_grad):
                    



def adspend_check(prev):
    stt=prev[0]*8
    for i in range(1,len(prev)):
        gap=prev[i]-prev[i-1]
        if(gap<0):
            # print('gap')
            prev[i]=prev[i-1]

        # next_gap=prev[i+1]-prev[i]
        # if(next_gap<0):
        #     print('nxtgap')
        #     prev[i+1]=prev[i]

        if(stt<prev[i]):
            # print(prev[i])
            next_correct_index=len(prev)-1
            for j in range(i+1,len(prev)):
                if(stt>prev[j]):
                    next_correct_index=j
                    break
            prev[i]=(prev[i-1]+prev[next_correct_index])/2
            # print(prev[i])
            # print('w')
            # break
        # print('s')
        # gap=prev[i]-prev[i-1]
        # next_gap=prev[i+1]-prev[i]
        # if(next_gap>gap*20):
        #     prev[i+1]=prev[i]
            
    return prev

# prev=[27,27,27,27,1033,265,265,173,265,265,265,208,210,233,251,254,207,217,203,392,393]
# sss=adspend_check(prev)
# print(sss)