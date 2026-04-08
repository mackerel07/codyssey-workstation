import json
from quiz import Quiz #quiz.py와 연동

class QuizGame:
    def show_menu(self):
        print("1.퀴즈 풀기")
        print("2.퀴즈 추가")
        print("3.퀴즈 목록")
        print("4.점수 확인")
        print("5.종료")

    def run(self):
        try:
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
                    self.show_score()
                elif choice == "5":
                    self.save_data()
                    print("저장 후 종료합니다.")
                    break
                else:
                    print("잘못된 입력입니다.")
        except (KeyboardInterrupt, EOFError):
            print("\n프로그램이 중단되었습니다.")

            try:            #안전저장 시도 *********
                self.save_data()
                print("데이터를 저장하고 안전하게 종료합니다.")
            except Exception:
                print("저장 중 오류가 발생했습니다.")



    def __init__(self): #QuizGame의 생성자(매갸변수 필요x) **
        self.quizzes = []
        self.best_score = 0 #최고기록 확인

        self.load_data()
        if not self.quizzes: #파일 없을때만 기본데이터 추가
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

            q3 = Quiz(
                "파이썬에서 리스트의 길이를 구하는 함수는?",
                ["size()", "length()", "len()", "count()"],
                3
            )

            q4 = Quiz(
                "파이썬의 파일 확장자는?",
                [".java", ".py", ".cpp", ".txt"],
                2
            )

            q5 = Quiz(
                "반복문에서 사용되는 키워드는?",
                ["if", "for", "def", "class"],
                2
            )


            self.quizzes.append(q1)
            self.quizzes.append(q2)
            self.quizzes.append(q3)
            self.quizzes.append(q4)
            self.quizzes.append(q5)



    def play_quiz(self):
        if not self.quizzes: #빈 리스트는 False(if not False)
            print("퀴즈가 없습니다.")
            return

        score = 0

        for q in self.quizzes: # q = q1, q2, q3
            q.show()
            while True:     #예외처리 구현
                answer = input("정답: ").strip()

                if not answer: #빈 값 반환
                    print("값을 입력하세요.")
                    continue

                if not answer.isdigit(): #기타문자 반환
                    print("숫자를 입력하세요.")
                    continue

                answer = int(answer)    #입력값이 문자열인지 확인하기 위해 나중에 정수열 처리
                
                if 1 <= answer <= 4: #예외처리
                    break
                else:
                    print(f"1~4 사이의 숫자를 입력하세요.")

            if q.check_answer(answer): #True/False(q1.user_input, q2.user_input...)
                print("정답!")
                score += 1
            else:
                print("오답!")

        print(f"총 점수: {score}/{len(self.quizzes)}") #len>리스트길이(문제개수)

        #최고 점수 갱신
        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")

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

        for i, q in enumerate(self.quizzes, 1): #q = q1, q2, ...
            print(f"[{i}] {q.question}") #q1.question, q2.question...(Quiz클래스의 question부분)

        print("-" * 40)

    def show_score(self):
        if self.best_score == 0:
            print("아직 기록이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}")   

    def save_data(self): #***********************
        data = {           #JSON 딕셔너리 구조
            "quizzes": [],  #빈 리스트 생성
            "best_score": self.best_score  #최고점수
        }

        for q in self.quizzes: #q1, q2...
            quiz_data = {       #딕셔너리 변환
                "question": q.question,
                "choices": q.choices,
                "answer": q.answer
            }
            data["quizzes"].append(quiz_data) #아까 생성한 빈 리스트

        with open("state.json", "w", encoding="utf-8") as f: #with문(안전), 덮어쓰기, 한글깨짐방지
            json.dump(data, f, ensure_ascii=False, indent=4) #저장, 한글그대로, 들여쓰기

    def load_data(self):
        try:        #오류 대비
            with open("state.json", "r", encoding="utf-8") as f: #읽기모드
                data = json.load(f) #파이썬 데이터로 변환(파이썬>딕셔너리)

            self.best_score = data.get("best_score", 0)

            self.quizzes = [] #리스트 초기화
            for q in data.get("quizzes", []): #딕셔너리 객체변환
                quiz = Quiz(q["question"], q["choices"], q["answer"])
                self.quizzes.append(quiz)

            print("저장된 데이터를 불러왔습니다.")

        except FileNotFoundError:
            print("저장 파일이 없습니다. 기본 데이터 사용.")

        except json.JSONDecodeError: #파일 손상되었을떄
            print("저장 파일이 손상되었습니다. 데이터를 초기화합니다.")
            self.quizzes = []
            self.best_score = 0

if __name__ == "__main__": #직접 실행시킬 때만 작동(import과정에서 게임이 시작되는 걸 방지함)
    game = QuizGame() #클래스로부터 객체생성
    game.run() #run(self)실행

    