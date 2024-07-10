from driver import *
import argparse
from input_parser import parse_input_data
import time
import pyautogui
import os

# parse argument
parser = argparse.ArgumentParser()
parser.add_argument('-input', type=str, dest="input_txt", action='store', default="input.txt", help='input text file')
args = parser.parse_args()

# version info
VERSION = 1.2
print("[Info] CaptureMacro V" + str(VERSION))

# config setting
pyautogui.FAILSAFE = False

# input
input_text = args.input_txt
input_file = open(input_text, "r", encoding="UTF8")
input_data=input_file.readlines()
input_file.close()
websites, output_path, capture_interval = parse_input_data(input_data)


while True:
    # 현재 날짜를 기반으로 폴더 경로 생성
    current_date = time.strftime("%Y%m%d")
    current_output_path = os.path.join(output_path, current_date)

    # 폴더가 없으면 생성
    if not os.path.exists(current_output_path):
        os.makedirs(current_output_path)

    driver = getDriver()
    for website in websites:
        driver.get(website)
        # 웹 페이지가 로드되고 렌더링될 때까지 대기 (원하는 대기 시간으로 변경 가능)
        time.sleep(5)

        # 웹 브라우저 창을 최대화
        driver.maximize_window()
        time.sleep(5)

        # 이미지 파일 이름을 현재 시간으로 생성
        image_filename = "capture_" + time.strftime("%Y%m%d%H%M%S") + ".jpg"
        image_path = os.path.join(current_output_path, image_filename)
        pyautogui.screenshot(image_path) #전체 화면 스크린샷 찍고 파일로 저장
        # screenshot.save(image_path)

    # 웹 드라이버 종료
    driver.quit()
    
    # 일정 시간 대기 후 다음 캡처 진행 (capture_interval 초마다 반복)
    time.sleep(int(capture_interval))

