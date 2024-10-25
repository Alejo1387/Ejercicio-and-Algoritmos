def promedio():
    suma = 0
    for i in range(3):
        suma += student_marks[query_name][i]
    promedio = suma / 3
    print(f"{promedio:.2f}")

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    promedio()