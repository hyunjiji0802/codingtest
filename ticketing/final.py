import pyautogui
import time
from PIL import ImageGrab
import smtplib
from email.mime.text import MIMEText
import keyboard
import random
import winsound


def play_alarm_sound():
    print("🔊 소리 재생 중...")
    duration = 10000  # 10초
    freq = 1000       # 1000Hz (알람음)
    for _ in range(300):
        winsound.Beep(freq, duration)
        time.sleep(0.1)

# ----------------------------- 좌표 입력 함수 ----------------------------- #
def wait_for_z_key(prompt):
    print(f"\n🖱 {prompt} → 마우스를 원하는 위치로 이동한 뒤 'Z' 키를 누르세요.")
    while True:
        if keyboard.is_pressed("z"):
            pos = pyautogui.position()
            print(f"✅ {prompt} 좌표: {pos}")
            while keyboard.is_pressed("z"):
                pass
            return pos
        time.sleep(0.05)

# ----------------------------- 좌표 비율 계산 함수 ----------------------------- #
def relative_point(left_top, right_bottom, rel_x, rel_y):
    width = right_bottom.x - left_top.x
    height = right_bottom.y - left_top.y
    return pyautogui.Point(left_top.x + int(width * rel_x), left_top.y + int(height * rel_y))

# ----------------------------- 좌석 탐색 ----------------------------- #
def detect_orange_seat(area_top_left, area_bottom_right):
    x1, y1 = area_top_left.x, area_top_left.y
    x2, y2 = area_bottom_right.x, area_bottom_right.y
    bbox = (x1, y1, x2, y2)
    screenshot = ImageGrab.grab(bbox=bbox).convert("RGB")

    width, height = screenshot.size
    target_color = (251, 126, 78)
    tolerance = 10

    def is_close(p, t):
        return all(abs(p[i] - t[i]) <= tolerance for i in range(3))

    for x in range(width):
        for y in range(height):
            pixel = screenshot.getpixel((x, y))
            if is_close(pixel, target_color):
                return (x1 + x, y1 + y)

    return None

# ----------------------------- 이메일 알림 ----------------------------- #
def send_email_alert():
    subject = "🎯 [예매 가능] 좌석이 떴어요!"
    body = "좌석 자동 선택 및 예매 단계가 완료되었습니다. 원격 접속 후 결제를 마무리하세요."
    from_email = to_email = "guswl4174@gmail.com"
    app_password = "lsdggblxpglweonr"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, app_password)
            server.send_message(msg)
        print("✅ 이메일 알림 전송 완료")
    except Exception as e:
        print(f"⚠️ 이메일 전송 실패: {e}")

# ----------------------------- 자동 클릭 시퀀스 ----------------------------- #
def execute_automated_sequence(top_left, bottom_right):
    print("\n=== 자동 클릭 시퀀스 실행 중 ===")
    coords = {
        "매수입력1": (0.6497, 0.3426),
        "매수입력2": (0.6429, 0.4136),
        "다음단계": (0.9190, 0.9580),
        "생년월일입력": (0.4490, 0.3426),
        "다음단계2": (0.9190, 0.9580),
        "결제정보1": (0.5122, 0.3531),
        "결제정보2": (0.5144, 0.4954),
        "다음단계3": (0.9190, 0.9580),
        "동의": (0.0399, 0.7562),
        "결제하기": (0.8470, 0.9580)
    }

    for label, (rx, ry) in coords.items():
        point = relative_point(top_left, bottom_right, rx, ry)
        print(f"➡️  {label} 클릭 중... {point}")
        pyautogui.click(point)
        time.sleep(1.2)

        if "생년월일" in label:
            time.sleep(0.5)
            pyautogui.typewrite("000802", interval=0.05)

# ----------------------------- 전체 실행 ----------------------------- #
def run_macro():
    print("=== 🎟 예매 자동화 시작 ===")
    top_left = wait_for_z_key("예매창 왼쪽 위")
    bottom_right = wait_for_z_key("예매창 오른쪽 아래")
    area_top_left = wait_for_z_key("탐색 영역 왼쪽 위")
    area_bottom_right = wait_for_z_key("탐색 영역 오른쪽 아래")
    seat_confirm_btn = wait_for_z_key("좌석 선택 완료 버튼")
    print("\n🔁 반복 클릭할 좌표들을 입력하세요. 완료 시 'X' 입력")

    repeat_click_coords = []
    while True:
        label = input("반복 클릭 좌표 설명 (예: 좌석감지영역 or X 입력 시 종료): ").strip()
        if label.upper() == "X":
            break
        coord = wait_for_z_key(f"{label}")
        repeat_click_coords.append(coord)

    print("\n[좌석 감지 시작] 1초 후 시작됩니다...")
    time.sleep(1)

    while True:
        for click_coord in repeat_click_coords:
            pyautogui.click(click_coord)
            time.sleep(random.uniform(0.4, 0.6))

            seat = detect_orange_seat(area_top_left, area_bottom_right)
            if seat:
                print(f"🎯 좌석 감지됨: {seat} → 클릭")
                pyautogui.click(seat)
                pyautogui.click(seat_confirm_btn)
                time.sleep(1.5)
                execute_automated_sequence(top_left, bottom_right)
                send_email_alert()
                play_alarm_sound()
                return

        print("⏳ 이번 라운드 전체 탐색 완료... 0.5초 후 반복")
        time.sleep(random.uniform(0.3, 0.5))


run_macro()