import random

answer = random.randint(1, 20)
tries = 0

print("🎮 업다운 게임! (1~20)")
print("맞혀보세요!")

while True:
    guess = int(input("숫자 입력: "))
    tries += 1

    if guess < answer:
        print("⬆️ 업!")
    elif guess > answer:
        print("⬇️ 다운!")
    else:
        print(f"🎉 정답! {tries}번 만에 맞혔어요!")
        break
