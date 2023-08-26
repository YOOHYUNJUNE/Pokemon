import random

def poke_calculator(my_pokemon_hp, my_pokemon_attack, wild_pokemon_hp, wild_pokemon_attack):
    # 내 포켓몬과 야생 포켓몬의 능력치 차이를 계산
    hp_difference = my_pokemon_hp - wild_pokemon_hp
    attack_difference = my_pokemon_attack - wild_pokemon_attack

    # 포획 확률을 계산하는 간단한 공식 (능력치 차이에 따라 계산)
    catch_probability = 50 + (hp_difference * (my_pokemon_attack - wild_pokemon_attack)) / 10 + random.randint(0, 20)
    # 포획 확률이 0과 100 사이에 있도록 조정
    catch_probability = max(min(catch_probability, 100), 0)

    return catch_probability

def try_catch_pokemon(my_pokemon_hp, my_pokemon_attack, wild_pokemon_hp, wild_pokemon_attack):
    catch_probability = poke_calculator(my_pokemon_hp, my_pokemon_attack, wild_pokemon_hp, wild_pokemon_attack)
    
    print(f"포획 확률: {int(catch_probability)}%") # 포획 확률을 소숫점 자리 없게

    # 포획 성공 여부를 판단
    if catch_probability == 100 or random.random() * 100 <= catch_probability:
        return True
    else:
        return False

# 내 포켓몬과 야생 포켓몬의 능력치
my_pokemon_hp = 100
my_pokemon_attack = 50

wild_pokemon_hp = 100
wild_pokemon_attack = 30

# 포획 시도
if try_catch_pokemon(my_pokemon_hp, my_pokemon_attack, wild_pokemon_hp, wild_pokemon_attack):
    print("포획 성공!")
else:
    print("포획 실패!")
