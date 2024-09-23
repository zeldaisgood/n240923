#경기
time=int(input("경기는 몇시입니까?"))
win=input("이긴 팀은 어디인갑쇼?")
lose=input("진 팀은 어디입니까?")
mvp=input("우수선수는 누구입니까?")
score = input("스코어는 몇 대 몇 입니까?")


print("=======================================================")
print('''오늘 {0}시에 야구 경기가 열렸습니다.\n
{1}과 {2}는 치열한 공방전을 펼쳤습니다.\n
{3}가 맹활약을 하였습니다.\n
결국 {1}이 {2}를 {4}로 이겼습니다.
      '''.format(time,win,lose,mvp,score))
#초를 분으로 계산
sec=int(input("초 입력: "))
min=sec//60
second=sec%60

print(sec,"초는",min,"분",second,"초 입니다.")
#화씨->섭씨
F=int(input("화씨온도:"))
C=(F-32)*5/9
print("섭씨온도:",C)
#bmi
weight=float(input("몸무게 kg을 입력하시오:"))
height=float(input("키를 미터 단위로 입력하시오:"))

bmi=(weight/(height**2))
print("당신의 BMI=",bmi)
'''
money=int(input("투입한 돈:"))
price=int(input("물건값:"))
change=int(input("거스름돈:"))
five=(charge//500)
one=(charge//100)
print("500원 동전의 개수:",five)
print("100원 동전의 개수:",one)'''
