try:         #예외가 발생할 가능성이 있는 코드
    num1, num2 = map(int, input('공백을 기준으로 두 개의 숫자를 입력 : ').split())
    calc_lists = [num1+num2, num1-num2, num1*num2, num1/num2]

    print('1. 더하기', end = '\t')
    print('2. 빼기', end = '\t')
    print('3. 곱하기', end = '\t')
    print('4. 나누기', end = '\t')
    choice = int(input('원하는 결과를 입력하세요 '))
    print(f'결과는 = {calc_lists[choice - 1]}')

except ValueError as e:
    print(f'오류발생 : {e}')
    
except IndexError as e:
    print(f'오류발생 : {e}')

except Exception as e:
    print(f'그밖의 에러 : {e}')


print('프로그램 종료')