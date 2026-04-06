class Quiz:
    def __init__(self, question, choices, answer): # 위 변수들은 외부 값을 받기 위한 지역변수(init에서만 존재)
        self.question = question
        self.choices = choices #self.choices는 전체 리스트임
        self.answer = answer 

    def show(self):
        print("\n" + "-"*40)
        print(f"문제: {self.question}")
        print("-"*40)
        for i, choice in enumerate(self.choices, 1): #인덱스의 1번부터 시작하도록 지정
            print(f"{i}. {choice}") #enumerate로 생성한 인덱스번호+선지 출력, self.choices중 하나인 choice변수

    def check_answer(self, user_input): #game.py에 True or False 반환e
        return user_input == self.answer