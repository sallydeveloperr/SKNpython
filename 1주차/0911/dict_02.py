#list, set, tuple, dict
result = dict( [ ['name', '최유정'], ['age', 24]])
print(type(result))
print(result)
#두개의 리스트 한개는 키에 해당하는 값들의 집합
#다른 하나는 값에 해당하는 집합
#이걸 dict 구조로 만들려면
names = ['홍길동', '이순신', '강감찬']
scores = [100, 99, 98]
students = {}

""" count = 0
for name in names:
    students[name] = scores[count]
    count += 1 """


for i in range(len(names)):     #len() 함수는 길이(length)를 구하는 함수, 리스트의 원소 개수를 반환
    students[names[i]] = scores[i]
#비어있는 dict 변수를 생성
#변수['키'] = 값 형태로 생성 --> 순환문 통해서 