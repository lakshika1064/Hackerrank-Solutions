if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    total = 0
    for i in student_marks[query_name]:
        total+=i
    avg=total/3
    print("{:.2f}".format(avg))
