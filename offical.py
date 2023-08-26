import math
import random

def calculate_catch_probability(HPmax, HPcurrent, rate, ball_bonus, status_bonus):
    a = ((3 * HPmax - 2 * HPcurrent) * rate * ball_bonus) / (3 * HPmax) * status_bonus

    if a >= 255:
        return 1.0  # 100% 확률로 포획 성공
    else:
        b = 65535 * math.pow(a / 255, 1/4)
        shake_count = 0
        selected_numbers = [random.randint(0, 65535) for _ in range(4)]
        
        for num in selected_numbers:
            if num > b:
                return False  # 포획 실패
            shake_count += 1
        
        return shake_count  # 흔들린 횟수

# 포켓몬의 정보 및 환경 설정
HPmax = 100  # 최대 HP
HPcurrent = 1  # 남은 HP
rate = 150  # 포획률
ball_bonus = 1.0  # 몬스터 볼 보너스
status_bonus = 1.0  # 상태이상 보너스

# 포획 확률 계산
result = calculate_catch_probability(HPmax, HPcurrent, rate, ball_bonus, status_bonus)

if result == 1.0:
    print("포획 성공! 확률: 100%")
elif result:
    print(f"포획 성공! {result}번 흔들림")
else:
    print("포획 실패!")
