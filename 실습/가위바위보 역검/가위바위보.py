# -*- coding: utf-8 -*-

import pygame
import random
import time

pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("가위바위보 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 폰트 설정
font = pygame.font.SysFont('malgun gothic', 48)
small_font = pygame.font.SysFont('malgun gothic', 36)

# 게임 옵션
options = ["가위", "바위", "보"]

# 게임 상태
STATE_INTRO = 0
STATE_COUNTDOWN = 1
STATE_PLAY = 2
STATE_RESULT = 3

# 이기는 조합
my_turn_winning_combinations = {
    "가위": "보",
    "바위": "가위",
    "보": "바위"
}
opp_turn_winning_combinations = {
    "가위": "바위",
    "바위": "보",
    "보": "가위"
}


# 게임 루프
running = True
state = STATE_INTRO
result = ""
my_choice = ""
opponent_choice = ""
start_time = 0
countdown_start = 0
is_my_turn = False
input_choice = ""

while running:
    current_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and state == STATE_PLAY:
            if event.key == pygame.K_LEFT:
                input_choice = "가위"
            elif event.key == pygame.K_DOWN:
                input_choice = "바위"
            elif event.key == pygame.K_RIGHT:
                input_choice = "보"

            if is_my_turn:
                if my_turn_winning_combinations[my_choice] == input_choice:
                    result = "이겼습니다!"
                else:
                    result = "틀렸습니다!"
            else:
                if opp_turn_winning_combinations[opponent_choice] == input_choice:
                    result = "이겼습니다!"
                else:
                    result = "틀렸습니다!"
            state = STATE_RESULT
            start_time = current_time

    screen.fill(WHITE)

    if state == STATE_INTRO:
        intro_text = font.render("게임을 시작합니다! 준비하세요...", True, BLACK)
        screen.blit(intro_text, (width // 2 - intro_text.get_width() // 2, height // 2))
        if current_time - start_time > 1:
            state = STATE_COUNTDOWN
            countdown_start = current_time
            is_my_turn = random.choice([True, False])
            if is_my_turn:
                my_choice = random.choice(options)
            else:
                opponent_choice = random.choice(options)

    elif state == STATE_COUNTDOWN:
        countdown_time = current_time - countdown_start
        if countdown_time < 0.5:
            text = font.render("가위!", True, BLACK)
        elif countdown_time < 1.0:
            text = font.render("가위!, 바위!", True, BLACK)
        elif countdown_time < 1.5:
            text = font.render("가위!, 바위!, 보!", True, BLACK)
        else:
            state = STATE_PLAY
            start_time = current_time

        if state == STATE_COUNTDOWN:
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2))

    elif state == STATE_PLAY:
        vs_text = font.render("나 VS 상대", True, BLACK)
        screen.blit(vs_text, (width // 2 - vs_text.get_width() // 2, height // 2 - 100))

        if is_my_turn:
            my_text = font.render(my_choice, True, RED)
            opponent_text = font.render("??", True, BLACK)
            instruction_text = small_font.render(f"내가 {my_choice}를 냈습니다. 이기는 것을 선택하세요.", True, BLACK)
        else:
            my_text = font.render("??", True, BLACK)
            opponent_text = font.render(opponent_choice, True, RED)
            instruction_text = small_font.render(f"상대가 {opponent_choice}를 냈습니다. 이기는 것을 선택하세요.", True, BLACK)

        screen.blit(my_text, (width // 4 - my_text.get_width() // 2, height // 2))
        screen.blit(opponent_text, (3 * width // 4 - opponent_text.get_width() // 2, height // 2))
        screen.blit(instruction_text, (width // 2 - instruction_text.get_width() // 2, height // 2 + 100))

        time_left = 3 - (current_time - start_time)
        if time_left <= 0:
            result = "시간 초과! 틀렸습니다."
            state = STATE_RESULT
            start_time = current_time

    elif state == STATE_RESULT:
        vs_text = font.render("나 VS 상대", True, BLACK)
        screen.blit(vs_text, (width // 2 - vs_text.get_width() // 2, height // 2 - 100))

        if is_my_turn:
            my_text = font.render(my_choice, True, BLACK)
            opponent_text = font.render(input_choice, True, BLACK)
            screen.blit(my_text, (width // 4 - my_text.get_width() // 2, height // 2))
            screen.blit(opponent_text, (3 * width // 4 - opponent_text.get_width() // 2, height // 2))
        else:
            my_text = font.render(input_choice, True, BLACK)
            opponent_text = font.render(opponent_choice, True, BLACK)
            screen.blit(my_text, (width // 4 - my_text.get_width() // 2, height // 2))
            screen.blit(opponent_text, (3 * width // 4 - opponent_text.get_width() // 2, height // 2))

        result_text = font.render(result, True, RED)
        screen.blit(result_text, (width // 2 - result_text.get_width() // 2, height // 2 + 100))

        if current_time - start_time > 2:
            state = STATE_INTRO
            start_time = current_time
            my_choice = ""
            opponent_choice = ""

    pygame.display.flip()

pygame.quit()
