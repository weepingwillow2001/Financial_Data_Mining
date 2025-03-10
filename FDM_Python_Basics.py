#Q1
a = "Finance"
print(a[:3])
#Q2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1+list2)
#Q3
total = 0
for n in range(1, 11):
    total =+ n
print(total)
#Q4
odd = []
for n in range(1, 21):
    if n % 2 == 0:
        pass
    else:
        odd.append(n)
print(odd)
#Q5
square_n = []
for n in range(1, 51):
    if int(n**0.5)**2 == n:
        square_n.append(n)
print(square_n)
#Q6
def fibonacci(n):
    # n개의 피보나치 수열을 반환
    fib_sequence = [0, 1]  # 처음 두 수는 0과 1
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    
    # 3번째 수부터 계산
    for i in range(2, n):
        next_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_num)
    
    return fib_sequence

# 예시: 10개의 피보나치 수열 출력
result = fibonacci(10)
print(result)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#Q7
def prime_numbers(n):
    primes = []
    
    for num in range(2, n):  # 2부터 n-1까지 검사
        is_prime = True
        
        # 2부터 num의 제곱근까지 나누어보기
        # 예를 들어, 36 = 6 × 6 = 4 × 9 = 3 × 12 = 2 × 18 = 1 × 36 등으로 표현할 수 있습니다.
        # 모든 약수 쌍을 나열해보면, 항상 한 약수는 √36(=6) 이하이고, 다른 약수는 √36 이상입니다.
        #`num`이 소수인지 판별하기 위해서는 2부터 `√num`까지의 수로만 나눠보면 됩니다. 이 범위 내에서 어떤 수로도 나누어지지 않는다면, `num`은 소수입니다.
        for i in range(2, int(num**0.5) + 1):
            #'int(num**0.5)`는 계산된 제곱근의 정수 부분만 취합니다(ex. 35)
            #`+ 1`은 Python의 range 함수가 마지막 수를 포함하지 않기 때문에 추가됩니다
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime: #참 이라면
            primes.append(num)
    
    return primes
print(prime_numbers(50))