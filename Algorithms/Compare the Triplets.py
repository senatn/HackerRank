def compareTriplets(a, b):
    score = [0,0]
    for i in range(3):
        if a[i] > b[i]:
            score[0] += 1
        if a[i] < b[i]:
            score[1] += 1
    return score
if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)