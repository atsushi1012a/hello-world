import random

#相手の数値の設定関数
def generate_secret_number():
    #3桁の1~9の乱数を設定
    secret_number = random.sample(range(0, 10), 3)
    return secret_number

#自分の予想を入力する関数
def get_user_guess():
    #文字列を表示させ、ユーザーに値を入力させる
    user_guess = input("3桁の予想を入力してください（重複のない数字）: ")
    #入力された値が3桁の数値でない場合入力しなおさせる
    while len(user_guess) != 3 or not user_guess.isdigit():
        user_guess = input("正しい形式の予想を入力してください（3桁の数字）: ")
    #入力された値をfor文で一つ一つ数値に変換し、リストとして持つ
    user_guess = [int(num) for num in user_guess]
    return user_guess

#数値比較の関数
def compare_numbers(secret_number, user_guess):
    exact_matches = 0
    partial_matches = 0
    secret_copy = secret_number.copy()
    
    # 正確な数字と位置の比較
    for i in range(3):
        if user_guess[i] == secret_number[i]:
            exact_matches += 1
            secret_copy[i] = None
    
    # 別の位置にある数字の比較
    for i in range(3):
        if user_guess[i] in secret_copy:
            partial_matches += 1
            secret_copy[secret_copy.index(user_guess[i])] = None
    
    return exact_matches, partial_matches

def play_game():
    print("ヌメロンを開始します！")
    secret_number = generate_secret_number()

    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1

        exact_matches, partial_matches = compare_numbers(secret_number, user_guess)
        print(f"結果: {exact_matches}つの数字が正確位置にあり、{partial_matches}つの数字が別の位置にあります。")

        if exact_matches == 3:
            print(f"正解です！{attempts}回目の予想で当たりました！")
            break

play_game()
