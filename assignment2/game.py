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
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quizzes()
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
            ["Guido", "Linus", "James", "Mark"], #choices는 이미 리스트
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

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")

        # 문제 입력
        question = input("문제를 입력하세요: ").strip()
        if not question: #False 값 반환용
            print("문제는 비어있을 수 없습니다.")
            return

        # 선택지 입력
        choices = []
        for i in range(4):
            while True:
                choice = input(f"선택지 {i+1}: ").strip() #i>0부터 시작
                if choice:
                    choices.append(choice)
                    break
                else:
                    print("선택지는 비어있을 수 없습니다.")

        # 정답 입력(예외처리 구현)
        while True:
            answer = input("정답 번호 (1~4): ").strip()

            if not answer: #빈 값 반환
                print("값을 입력하세요.")
                continue

            if not answer.isdigit(): #기타문자 반환
                print("숫자를 입력하세요.")
                continue

            answer = int(answer)

            if 1 <= answer <= 4:
                break
            else:
                print("1~4 사이의 숫자를 입력하세요.")

        # Quiz 객체 생성 및 추가
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다!")

    def show_quizzes(self):
        print("\n등록된 퀴즈 목록")

        if not self.quizzes: #False값 반환
            print("퀴즈가 없습니다.")
            return

        print("-" * 40)

        for i, q in enumerate(self.quizzes, 1):
            print(f"[{i}] {q.question}")

        print("-" * 40)