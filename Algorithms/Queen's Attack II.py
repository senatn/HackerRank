def queensAttack(n, k, r_q, c_q, obstacles):
    u = n - r_q
    d = r_q - 1
    r = n - c_q
    l = c_q - 1
    ru = min(u,r)
    lu = min(l,u)
    rd = min(r,d)
    ld = min(l,d)
    for o in obstacles:
        if o[0] == r_q:
            if o[1] < c_q:
                l = min(l, c_q-1-o[1])
            else:
                r = min(r, o[1]-1-c_q)
        elif o[1] == c_q:
            if o[0] < r_q:
                d = min(d, r_q-1-o[0])
            else:
                u = min(u, o[0]-1-r_q)
        elif abs(o[0]-r_q) == abs(o[1]-c_q):
            if o[1] < c_q:
                if o[0] > r_q:
                    lu = min(lu, c_q-1-o[1])
                else:
                    ld = min(ld, c_q-1-o[1])
            else:
                if o[0] > r_q:
                    ru = min(ru, o[1]-c_q-1)
                else:
                    rd = min(rd, o[1]-c_q-1)
    return u + d + r + l + ru + rd + lu + ld

def main():
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
main()