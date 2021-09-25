#1

N = int(input())

n_list = map(int, input().split())

cnt = 0

for n in n_list:
    if n != 1:
        for i in range(2, n): #1과 자기자신을 제외한 수로 나뉘면 X
            if n % i == 0:
                break
        else:
            cnt += 1


print(cnt)


#2

min_num = int(input())
max_num = int(input())
decimal_list = []

for i in range(min_num, max_num + 1):  # 첫 입력값과 두번째 입력값 사이만 진행
    count = 0
    for j in range(1, i + 1):  # 1부터 i항까지 진행
        if i % j == 0:
            count += 1  # 나뉘면 count증가
            if count > 2:  # 2보다 크면 소수가 아니므로(소수는 1과 자기자신으로만 나뉨) 바로 다음식 진행
                break
    if count == 2:  # 소수
        decimal_list.append(i)
if len(decimal_list) != 0:  # 소수리스트에 값이 있다면 밑의 값을 출력
    print(sum(decimal_list))
    print(decimal_list[0])
else:  # 소수가 하나도 없다면
    print('-1')


#3

m, n = map(int, input().split())

def prime_list(m, n):
    n += 1
    sieve = [True] * n

    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(2*i, n, i):
                sieve[j] = False

    # return [i for i in range(2, n) if sieve[i] == True]
    for k in range(m, n):
        if k > 1 and sieve[k] == True:
            print(k)


prime_list(m, n)


# 4 솔루션

n = int(input())

def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True							#소수 구하는 방식은 위와 같다

all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []								#for문 밖에 리스트 정의

for i in all_list:						#2부터 2*123,456 범위
    if sosu(i):							#sosu함수에 해당하면
        memo.append(i)					#리스트에 추가


while True:
    count=0					#갯수를 세야하는 조건 때문에 카운트
    if n == 0 :
            break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
    n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음


#5

# n이하의 숫자들 중 소수 찾기
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

# n이하의 소수들 중 합이 n
def sosu(n):
    li = prime_list(n)
    idx = max([i for i in range(len(li)) if li[i] <= n/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(li)):
            if li[i] + li[j] == n:
                return [li[i], li[j]]

for _ in range(int(input())):
    n = int(input())
    print(" ".join(map(str, sosu(n))))


#6


x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))


#7

x_n = []
y_n = []

for i in range(3):

    x, y = map(int, input().split())
    x_n.append(x)
    y_n.append(y)

for i in range(3):
    if x_n.count(x_n[i]) == 1:
        x = x_n[i]
    if y_n.count(y_n[i]) == 1:
        y = y_n[i]

print(x, y)


#8

while True:
    a = list(map(int, input().split()))
    max_num = max(a)
    if sum(a) == 0:
        break
    a.remove(max_num)
    if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
        print('right')
    else:
        print('wrong')


#9


from math import pi

n = int(input())

x = n * n * pi

y = n * n * 2

print("{:.6f}".format(x))
print("{:.6f}".format(y))


#10

import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)  # 그 외에