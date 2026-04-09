   def generate_cross(n):
        matrix = [[0] * n for _ in range(n)] #정사각형 생성
        mid = n // 2 #가운데 열

        for i in range(n):
            matrix[i][mid] = 1
            matrix[mid][i] = 1

        return matrix


    def generate_x(n):
        matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            matrix[i][i] = 1
            matrix[i][n - 1 - i] = 1 #왼쪽 아래 대각선

        return matrix

    def create_filters():
        filters = {}

        for n in [5, 13, 25]:                              
            filters[f"size_{n}"] = {                #딕셔너리 생성:filters = {a:b, c:d}, 요소추가:filter[size_n]=value
                "Cross": generate_cross(n), #Cross와 X가 또 하나의 딕셔너리key                                                      #key 
                "X": generate_x(n)      
            }

        return filters
