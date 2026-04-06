from quiz import Quiz #quiz.py와 연동

class QuizGame:
    def show_menu(self):
        print("1.퀴즈 풀기")
        print("2.퀴즈 추가")
        print("3.퀴즈 목록")
        print("4.점수 확인")
        print("5.종료")

    def run(self):
        while True:
            self.show_menu()   

            choice = input("선택: ").strip() # 입력값 공백제거

            if choice == "1":
                print("퀴즈 풀기")
            elif choice == "2":
                print("퀴즈 추가")
            elif choice == "3":
                print("퀴즈 목록")
            elif choice == "4":
                print("점수 확인")
            elif choice == "5":
                print("종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")

    def __init__(self): #QuizGame의 생성자(매갸변수 필요x) **
        self.quizzes = []
        self.best_score = 0

        #__init__(self,question, choices, answer)
        q1 = Quiz(
            "파이썬 만든 사람은?",
            ["Guido", "Linus", "James", "Mark"], 
            1
        )

        q2 = Quiz(
            "리눅스 만든 사람은?",
            ["Guido", "Linus", "James", "Mark"],
            2
        )

        self.quizzes.append(q1)
        self.quizzes.append(q2)

    def play_quiz(self):
        if not self.quizzes: #빈 리스트는 False(if not False)
            print("퀴즈가 없습니다.")
            return

        score = 0

        for q in self.quizzes: # q = q1, q2, q3
            q.show()
            answer = int(input("정답: "))

            if q.check_answer(answer):
                print("정답!")
                score += 1
            else:
                print("오답!")

        print(f"총 점수: {score}/{len(self.quizzes)}")