import re
import math

def solution(n, k):
    answer = 0
    
    ## n을 k진수로 만들기
    n_prime = make_prime(n, k)
    
    ## 0을 기준으로 나누기
    num_lst = re.split('0+', n_prime)
    
    ## num_lst의 최대값 구하기
    ## 에스토스테네스의 체에 활용됨
    max_num = max(num_lst)
    
    ## 에스토스테네스의 체로 소수 리스트 반환
    prime_lst = is_prime_number(int(max_num))
    
    ## num_lst에 있는 숫자가 소수인지 판별
    for i in num_lst:
        if prime_lst[int(i)]:
            answer += 1
    
    return answer

## n을 k진수로 변환하기
def make_prime(n, k):
    prime = ''
    while n >= k:
        rest = n % k
        n = n // k
        prime += str(rest)
    prime += str(n)
    
    return prime[::-1]

## 에스토스테네스의 체를 활용해서 소수 확인
def is_prime_number(x):
    array = [True for i in range(x+1)]
    array[1] = False
    
    for i in range(2, int(math.sqrt(x))+1):
        if array[i] == True:
            j = 2
            while i * j < x:
                array[i*j] = False
                j += 1
    
    return array