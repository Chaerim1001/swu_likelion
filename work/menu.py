'''
< 카페 키오스크를 제작해보자! >
1. 영수증 주문 시각 출력을 위한 초기 설정 (구글링으로 해결하기)
2. 초기 설정 (딕셔너리와 리스트 모두 활용) -> 딕셔너리에서 key는 메뉴명, value는 해당 메뉴의 금액
3. 메뉴판에서 메뉴를 고르면 장바구니에 추가됨 (디저트와 음료 각각 추가) -> 'q'를 누르면 장바구니에 담긴 디저트와 음료를 각각 출력
4. 장바구니에 담긴 메뉴 중에서 삭제하고 싶은 메뉴 삭제 (디저트와 음료 각각 삭제) -> 'q'를 누르면 최종 장바구니에 담긴 디저트와 음료를 각각 출력
5. 최종 주문 영수증 출력 (주문 시각, 주문 내역, 주문한 메뉴의 총 금액 필수 포함) -> 주문 내역은 디저트와 음료를 합쳐서 출력
'''


# 1. 영수증 주문 시각 출력을 위한 초기 설정 (구글링으로 해결하기)
from datetime import datetime
current_time = datetime.now()

# 2. 초기 설정
dessert = {"치즈 조각 케이크" : 7000, "초코 조각 케이크" : 7000, "블루베리 조각 케이크" : 8000, "녹차 조각 케이크" : 7500, "딸기 조각 케이크" : 8000}
drink = {"아이스 아메리카노" : 3000, "복숭아 아이스티" : 4000, "청포드 에이드" : 4500, "오레오초코" : 5000, "요거트 스무디" : 5500}
choice_total1, choice_total2 = 0,0
dessert_bag = []
drink_bag = []

# 3. 메뉴판에서 메뉴 고르면 장바구니에 담기는 기능 (디저트와 음료를 각각 주문받기)
print("\n ※ 디저트 카페에 오신 것을 환영합니다! ※\n\n ※ 주문을 중단하고 싶으시다면 'q'를 눌러주세요! 아래는 메뉴판입니다. ※\n\n")
print("디저트류 => ", dessert,"\n", "음료 => ", drink, "\n\n")

while True:
   
    dessert_item = input("장바구니에 담고 싶은 디저트 1개를 선택해주세요 :")

    if(dessert_item == "q"):
        print("※ 장바구니에 담긴 디저트를 알려드립니다. ※\n", dessert_bag, "\n")
        print("※ 장바구니에 담긴 음료를 알려드립니다. ※\n", drink_bag, "\n\n")
        break
    else:
        dessert_bag.append(dessert_item)
        print(dessert_item + " 메뉴가 장바구니에 담겼습니다. \n")


    drink_item = input("장바구니에 담고 싶은 음료 1개를 선택해주세요 : ")

    if(drink_item == "q"):
        print("\n※ 장바구니에 담긴 디저트를 알려드립니다. ※\n", dessert_bag, "\n\n")
        print("※ 장바구니에 담긴 음료를 알려드립니다. ※\n", drink_bag, "\n\n")
        break
    else:
        drink_bag.append(drink_item)
        print(drink_item + " 메뉴가 장바구니에 담겼습니다. \n" + "=" * 130)

    
# 4. 장바구니에 담긴 메뉴 중에서 삭제하고 싶은 메뉴 삭제하는 기능 (디저트와 음료 각각 삭제하기)
set_dessert_bag = set(dessert_bag)
set_drink_bag = set(drink_bag)

while True:
    item = input("장바구니에서 삭제하고 싶은 메뉴 1개를 입력해주세요 : ")

    if(item == "q"):
        print("※ 최종 장바구니에 담긴 내역을 알려드립니다※.\n", '디저트 : ', set_dessert_bag,'음료 : ', set_drink_bag)
        break

    else:
        set_dessert_bag = set_dessert_bag - set([item])
        set_drink_bag = set_drink_bag - set([item])
        print("\n현재 장바구니 현황입니다.\n", set_dessert_bag, set_drink_bag, "\n\n")

# 5. 주문 영수증을 출력하는 기능
print("\n====================영수증을 출력해드리겠습니다.====================\n")

for i in list(set_dessert_bag):
    choice_total1 += dessert[i]

for j in list(set_drink_bag):
    choice_total2 += drink[j]

total_sum = choice_total1+choice_total2

print("주문 시각 : ", current_time,"\n")
# 주문 내역은 디저트와 음료를 합쳐서 출력
print("주문 내역 : ", set_dessert_bag | set_drink_bag, '\n\n')
print("주문하신 메뉴의 총 금액은", total_sum, "원 입니다.")
print("\n\n※ 카페를 이용해주셔서 감사합니다. ※")