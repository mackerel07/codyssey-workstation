import time
import json

def mac(pattern, filter_): #mac 함수:score=∑i=02​∑j=02​(patternij​×filterij​)
    result = 0.0
    n = len(pattern)
    
    for i in range(n):
        for j in range(n):
            result += pattern[i][j] * filter_[i][j]
        
    return result

def measure_time(pattern, filter_, repeat=10):
    total = 0

    for _ in range(repeat):
        start = time.time()

        mac(pattern, filter_)

        end = time.time()
        total += (end - start)

    avg_time = (total / repeat) * 1000  # ms
    return avg_time


def menu():
    while True:
        print("#---------------------------------------")
        print("# 모드 선택")
        print("#---------------------------------------")
        print("1. 사용자 입력 (3x3)")
        print("2. 데이터 분석 (data.json)")
        print("0. 종료")

        choice = input("선택: ")

        if choice == "1":
            mode1()
        elif choice == "2":
            mode2()
        elif choice == "0":
            print("종료")
            break
        else:
            print("잘못된 입력\n")

def mode1():
    print("\n[Mode 1] 사용자 입력\n")


    def input_matrix(name):
        matrix = []

        print(f"\n[{name}입력]")

        for i in range(3):
            while True:
                row = input(f"{i+1}번째 줄 입력 (0 또는 1만, 공백으로구분): ").split()

                if len(row) != 3:
                    print("반드시 3개 입력")
                    continue

                if not all(x in ['0', '1'] for x in row): #예외처리
                    print("0 또는 1만 입력 가능")
                    continue

                row = list(map(int, row)) #row 문자열에 int 전환
                matrix.append(row)
                break
        return matrix

    filter_a = input_matrix("필터 A")
    filter_b = input_matrix("필터 B")
    matrix = input_matrix("사용자패턴")

    print("입력된 3x3 배열:")

    for row in matrix:
        print(' '.join(map(str, row)))

    print("입력된 필터A 배열:")

    for row in filter_a:
        print(' '.join(map(str, row)))
    
    print("입력된 필터B 배열:")

    for row in filter_b:
        print(' '.join(map(str, row)))

    score_a = mac(matrix, filter_a)
    score_b = mac(matrix, filter_b)

    epsilon = 1e-9

    if abs(score_a - score_b) < epsilon:
        result = "UNDECIDED"
    elif score_a > score_b:
        result = "A"
    else:
        result = "B"
    
    avg_time = measure_time(matrix, filter_a)

    print("판정:", result)
    print(f"연산 시간(평균/10회): {avg_time:.6f} ms")
    print("#---------------------------------------")
    print("# [3] MAC 결과")
    print("#---------------------------------------")

    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")
    print(f"연산 시간(평균/10회): {avg_time:.6f} ms")
    print(f"판정: {result}")

def mode2():
    print("\n[Mode 2] 데이터 분석\n")

    def load_data(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"파일 로드 실패: {e}")
            return None

    def normalize_label(label):
        label = label.strip().lower() #공백제거 밑 대문자 제거

        if label in ["+", "cross", "c", "십자가"]:
            return "Cross"
        elif label in ["x", "엑스"]:
            return "X"
        
        return "UNKNOWN"

    def get_size(key): #N값 추출
        # "size_5_1" → 5
        return int(key.split("_")[1]) #문자열 나누고 첫번째 인덱스

    def analyze_patterns(data, filters):
        patterns = data["patterns"] #size(key), [input,exepcted] #여기서 patterns은 패턴데이터 전체

        total = 0 #테스트 수
        passed = 0
        failed_cases = []

        for key, value in patterns.items(): #key:size_5_1, value:input[]/expected:+(또다른딕셔너리)
            total += 1

            #딕셔너리 응용 코드
            size = get_size(key) #N
            pattern = value["input"] #key(input) 호출, #여기서 패턴은 메트릭스만
            expected = normalize_label(value["expected"])

            size_data = filters[f"size_{size}"]
            filter_cross = size_data.get("Cross") or size_data.get("cross") #filters[size_5] 딕셔너리 내부 Cross key 호출
            filter_x = size_data.get("X") or size_data.get("x") #대소문자처리

            if not validate_size(pattern, filter_cross): #cross와 x는 사이즈 똑같음
                print(f"--- {key} ---")
                print("FAIL: 패턴과 필터 크기 불일치")
                failed_cases.append(key)
                continue

            score_cross = mac(pattern, filter_cross)
            score_x = mac(pattern, filter_x)

            epsilon = 1e-9

            if abs(score_cross - score_x) < epsilon:
                result = "UNDECIDED"
            elif score_cross > score_x:
                result = "Cross"
            else:
                result = "X"

        
            # PASS / FAIL
            if result == expected:
                status = "PASS"
                passed += 1
            else:
                status = "FAIL"
                failed_cases.append(key)

            # 출력
            print(f"--- {key} ---")
            print(f"Cross 점수: {score_cross}")
            print(f"X 점수: {score_x}")
            print(f"판정: {result} | expected: {expected} | {status}")
            print()

        return total, passed, failed_cases

    def validate_size(pattern, filter_): #사이즈 다를 때 예외처리
        p_rows, p_cols = get_matrix_size(pattern)
        f_rows, f_cols = get_matrix_size(filter_)

        if p_rows != f_rows or p_cols != f_cols:
            return False
        
        return True


    def get_matrix_size(matrix):
        return len(matrix), len(matrix[0]) #(행,열 개수)


    def print_summary(total, passed, failed_cases):
        print("#---------------------------------------")
        print("# [4] 결과 요약")
        print("#---------------------------------------")

        print(f"총 테스트: {total}개")
        print(f"통과: {passed}개")
        print(f"실패: {total - passed}개")

        if failed_cases:
            print("\n실패 케이스:")
            for case in failed_cases:
                print(f"- {case}")

    def print_performance():
        print("#---------------------------------------")
        print("# [5] 성능 분석 (평균/10회)")
        print("#---------------------------------------")

        print("크기       평균 시간(ms)    연산 횟수")
        print("-------------------------------------")

        def make_dummy(n):
            mat = [[0]*n for _ in range(n)]
            mat[n//2][n//2] = 1 
            return mat

        for n in [3, 5, 13, 25]:
            pattern = make_dummy(n)
            filter_ = make_dummy(n)

            avg_time = measure_time(pattern, filter_)
            operations = n * n

            print(f"{n}x{n}      {avg_time:.6f}         {operations}")

    data = load_data("data.json")
    if data is None:
        return
    filters = data["filters"]

    total, passed, failed_cases = analyze_patterns(data, filters)
    print_performance()
    print_summary(total, passed, failed_cases)


#코드 실행부분
if __name__ == "__main__":
    menu()
