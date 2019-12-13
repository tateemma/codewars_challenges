def solution(n):
     total = sum([i for i in range(n) if i%3==0 or i%5==0])
     return total
