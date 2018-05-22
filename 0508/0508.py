# 파이썬 5월 8일(1주차) 수업

#print로 출력하기
print('안녕')
print('Hello World!')
print("Hello Python!")
print('이건 띄어쓰기야 \n이렇게!')
print('이건 tab 공백이야 \t이렇게!')

#변수
a = 1
b = 2
print(a+b)
# 변수에 지정할 수 있는 것은, String/number(integer, float, ...)/Boolean(True, False)/list/dictionary etc

# 내장함수 목록
import keyword
keyword.kwlist

# 주석처리는 앞에 샾을 붙이면 된다.

# 연산자

# indexing / slicing / split

# list

kospi_top10 = ['삼성전자','SK하이닉스','현대차','한국전력','아모레퍼시픽','제일모직','삼선정자우','삼성생명','네이버','현대모비스']
print('1등:',kospi_top10[0])
print('1등~5등:',kospi_top10[0:5])
print('6등~10등:',kospi_top10[5:])

# append, insert
kospi_top10
(kospi_top11) = (kospi_top10).copy()
kospi_top11.append('KAKAO')
print('1등~11등:',(kospi_top11))
dict_prac = {}
dict_prac[1] = 3
dict_prac['1'] = '3'
dict_prac
