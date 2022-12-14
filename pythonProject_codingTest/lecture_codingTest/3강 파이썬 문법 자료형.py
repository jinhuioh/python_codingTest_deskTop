# 자료형: 정수형,실수형,복소수형,문자열,튜플,리스트,사전 등
# 오늘날 가장 널리 쓰이는 표준에서는 4,8 바이트의 고정된 크기의 메모리를 할당하므로
# 컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 느낀다.
a = 0.3
b = 0.6
# c = 9가 나올 것 같지만 컴퓨터에서는 0.899999... 가 나옴
c = a+b
print(c)

# 해결방법
# round(숫자, n번째자리에서 반올림) 함수 활용
c1 = round(c,4)
# 9가 나옴
print(c1)

# /, %, //차이점
# / = 나눠진 결과의 실수
# % = 나머지
# // = 몫 연산자

