import pyautogui
import PIL.Image
import time
import os
def get_screenshot_of_current_list():
    left = 40
    top = 310
    width = 460
    height = 1200
    im = pyautogui.screenshot(region=(left, top, width, height))
    return im
def connect_picture(a:PIL.Image.Image,b:PIL.Image.Image):
    # 1. 找到a和b的相同部分（a的下半部分与b的上半部分相同）
    for height in range(1,min(a.height,b.height)):
        if a.crop((0, a.height-height, a.width, a.height)).tobytes() == b.crop((0, 0, b.width, height)).tobytes():
            break
    print(height)
    # 2. 将a和b拼接起来
    result = PIL.Image.new('RGB', (a.width, a.height + b.height - height))
    result.paste(a, (0, 0))
    result.paste(b.crop((0, height, b.width, b.height)), (0, a.height))
    return result
while True:
    time.sleep(1)
    capture_time = time.ctime()
    total = get_screenshot_of_current_list()
    total.save('total.png')
    if os.system("git add ."): continue
    if os.system("git commit -m 'update'"): continue
    while True:
        os.system("git config unset http.proxy")
        if not os.system("git push"): break
        os.system("git config set http.proxy http://127.0.0.1:10808")
        if not os.system("git push"): break
    print(capture_time, "pushed")

# prev = PIL.Image.new('RGB', (0, 0))
# curr = get_screenshot_of_current_list()
# while prev.tobytes() != curr.tobytes():
#     total = connect_picture(total, curr)
#     prev = curr
#     pyautogui.moveTo(x=300, y=400)
#     pyautogui.hscroll(-500)
#     time.sleep(1)
#     curr = get_screenshot_of_current_list()
#     total.save('total.png')
# total.show()
