def average(lst):
    return sum(lst) / len(lst)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average = average(student_marks[query_name])
    print("%.2f" % round(average, 2))

