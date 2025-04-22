import pyperclip as keyb
import pyautogui as cur
import time
import os
import bot_model as bm

from pyautogui import ImageNotFoundException


def open_web(browser):
    url = "https://web.whatsapp.com"
    os.system(f'start {browser} "{url}"')
    time.sleep(45)


def check_new_msg(mode):
    status = "not found"
    result = {"status": status}
    try:
        if mode == 'light':
            pos = cur.locateOnScreen('images/bright1.png', confidence=0.8)
        elif mode == 'dark':
            pos = cur.locateOnScreen('images/dark.png', confidence=0.8)
        if pos is not None:
            result['status'] = "found"
            result['x'] = pos[0]
            result['y'] = pos[1]
            cur.moveTo(pos[0], pos[1])
    except Exception as e:
        print(e)

    return result


def drag(x1 = 488,y1 = 166,x2 = 1309,y2 = 643):
    cur.moveTo(x1,y1)
    cur.dragTo(x2,y2,duration=1)

def check_enc_msg(mode = 'light'):
    result = {"status":False}
    pos = None
    try:
        if mode =='light':
            pos = cur.locateOnScreen('images/enc_msg_bright.png',confidence=0.6)
        elif mode == 'dark':
            pos = cur.locateOnScreen('images/enc_msg_dark.png', confidence=0.6)
        if pos is not None:
            result['status'] = True
            result['x'] = pos[0]
            result['y'] = pos[1] + 70
            print(result)
            return result
    except ImageNotFoundException:
        return result

def copy_whole_msg(screen,mover = 0):
    # cur.click(x-100,y)
    time.sleep(3)
    if mover !=0:
        drag(x1 = screen[0],y1 = mover + 20,x2 = screen[2],y2 = screen[3])
    else:
        drag(screen[0],screen[1],screen[2],screen[3])
    cur.hotkey('ctrl','c')
    msg = keyb.paste()
    return msg


def filtermsg(fullchat):
    lmsg = ""
    user = ""
    try:
        if ']' in fullchat:
            msg = str(fullchat).split('\\n')[-1].split(":")
            user = msg[1][msg[1].index(']') + 1::].strip()
            lmsg = msg[-1][0::].strip()
        else:
            user = "Random"
            lmsg = fullchat
    except Exception as e:
        print(e)
    finally:
            return {'user': user, 'message': lmsg}

def typeable(mode):
    result = {'typeable': False}
    try:
        if mode == 'light':
            pos = cur.locateOnScreen('images/typer_light.png', confidence=0.8)
        elif mode == 'dark':
            pos = cur.locateOnScreen('images/typer_dark.png', confidence=0.8)
        if pos is not None:
            result['typeable'] = True
            result['x'] = pos[0]
            result['y'] = pos[1]
            return result
        else:
            print("none")
    except ImageNotFoundException:
        print("image not found")
    return result


def reply(msg):
    rep = "Thank you for contacting our company! We will forward your query to our senior staff"
    if msg != '' and len(msg) < 50 and msg != "0000":
        intent = bm.predict_class(msg.strip().lower())
        rep = bm.get_response(intent)
        return rep
    return rep


def full_process(screen,mode = "light"):
    new_msg_status = check_new_msg(mode)
    if new_msg_status['status'] == "found":
        cur.click(new_msg_status['x']-100,new_msg_status['y'])
        time.sleep(2)
        enc_msg = check_enc_msg(mode)
        if enc_msg['status']:
            print("Found enc")
            full_message = copy_whole_msg(screen,mover=enc_msg['y'])
        else:
            print("not Found enc")
            full_message = copy_whole_msg(screen)
        if full_message == "":
            if enc_msg['status']:
                print("Found enc")
                screen[0] = screen[0] + 10
                screen[1] = screen[1] + 23
                full_message = copy_whole_msg(screen, mover=enc_msg['y'])
            else:
                print("not Found enc")
                full_message = copy_whole_msg(screen)
        typer = typeable(mode)
        if typer['typeable']:
            print(full_message)
            user_details = filtermsg(full_message)
            print(user_details)
            keyb.copy(reply(user_details['message']))
            cur.click(typer['x'],typer['y'])
            cur.hotkey('ctrl','v')
            cur.press('enter')
            keyb.copy("")
            cur.press('esc')
        else:
            print("Not authorized to send messages")
    else:
        print("No message received")
