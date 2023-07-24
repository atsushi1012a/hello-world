import random

def get_user_choice():
    user_choice = input("じゃんけんをします！（グー、チョキ、パーのいずれかを入力してください）: ")
    user_choice = user_choice.lower()
    while user_choice not in ["グー", "チョキ", "パー"]:
        user_choice = input("正しい選択肢を入力してください（グー、チョキ、パー）: ")
        user_choice = user_choice.lower()
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(["グー", "チョキ", "パー"])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    print(f"あなたの選択: {user_choice}")
    print(f"コンピュータの選択: {computer_choice}")
    if user_choice == computer_choice:
        return "引き分け"
    elif (
        (user_choice == "グー" and computer_choice == "チョキ") or
        (user_choice == "チョキ" and computer_choice == "パー") or
        (user_choice == "パー" and computer_choice == "グー")
    ):
        return "あなたの勝ち"
    else:
        return "コンピュータの勝ち"

def play_game():
    print("じゃんけんゲームを開始します！")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        print(winner)
        play_again = input("もう一度プレイしますか？（はい/いいえ）: ")
        if play_again.lower() != "はい":
            break

play_game()
