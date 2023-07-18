# 1. 큰따옴표로 양쪽 둘러싸기
print("Hello World")

# 2. 작은따옴표로 양쪽 둘러싸기
print('Python is fun')

# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")

# 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print('''Life is too short, You need python''')

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
# 문자열을 만들어 주는 주인공은 작은따옴표(')와 큰따옴표(")이다. 
# 그런데 문자열 안에도 작은따옴표와 큰따옴표가 들어 있어야 할 경우가 있다. 
# 이때는 좀 더 특별한 기술이 필요하다. 예제를 하나씩 살펴보면서 원리를 익혀 보자.

# 5. 문자열에 작은따옴표 포함하기
food = "Python's favorite food is perl"

# 작은 따옴표로 감쌌을때,
# >>> food = 'Python's favorite food is perl'
#   File "<stdin>", line 1
#     food = 'Python's favorite food is perl'
#                    ^
# SyntaxError: invalid syntax

# 이스케이프 코드란?
# 문자열 예제에서 여러 줄의 문장을 처리할 때 역슬래시 문자와 소문자 n을 조합한 \n 이스케이프 코드를 사용했다. 이스케이프(escape) 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 ‘문자 조합’을 말한다. 주로 출력물을 보기 좋게 정렬하는 용도로 사용한다. 몇 가지 이스케이프 코드를 정리하면 다음과 같다.

# 코드	설명
# \n	문자열 안에서 줄을 바꿀 때 사용
# \t	문자열 사이에 탭 간격을 줄 때 사용
# \\	\를 그대로 표현할 때 사용
# \'	작은따옴표(')를 그대로 표현할 때 사용
# \"	큰따옴표(")를 그대로 표현할 때 사용
# \r	캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
# \f	폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
# \a	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
# \b	백 스페이스
# \000	널 문자
# 이 중에서 활용 빈도가 높은 것은 \n, \t, \\, \', \"이다. 나머지는 프로그램에서 잘 사용하지 않는다.

# 6. 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)

# 7. 문자열 곱하기
a = "python"
print(a * 2)

# 8. 문자열 길이 구하기
a = "Life is too short"
print(len(a))

# 9. 문자열 인덱싱과 슬라이싱
# 인덱싱(indexing)이란 무엇인가를 ‘가리킨다’, 
# 슬라이싱(slicing)은 무엇인가를 ‘잘라 낸다’라는 의미이다. 이런 의미를 생각하면서 다음 내용을 살펴보자.

a = "Life is too short, You need Python"
print(a[0:4])
