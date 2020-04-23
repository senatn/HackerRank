if __name__ == '__main__':
    student_score = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_score.append([name, score])
        score_list.append(score)

s = sorted(list(set(score_list)))[1]

for a,b in sorted(student_score):
    if b == s:
        print(a)