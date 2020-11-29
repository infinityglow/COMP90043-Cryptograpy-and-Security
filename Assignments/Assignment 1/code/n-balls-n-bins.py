def solution(n, m):
    if n == 0 or m == 1:
        return 1
    if n < m:
        return solution(n, n)
    return solution(n, m-1) + solution(n-m, m)

print(solution(95, 2) + solution(96, 1))
print(solution(95, 2))