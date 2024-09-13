from random import *
cards = list('23456789JQKA') + ['10']
suits = list('♥♦♣♠')
power = 0
hand = []
vision = []
bothand = []

def check(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] and hand[2][2] - hand[1][2] == 1 and hand[1][2] - hand[0][1] == 1:
        return ('Street Flash!', 6)
    elif hand[0][0] == hand[1][0] == hand[2][0]:
        return('Tripple', 5)
    elif hand[2][2] - hand[1][2] == 1 and hand[1][2] - hand[0][1] == 1:
        return('Street', 4)
    elif hand[0][1] == hand[1][1] == hand[2][1]:
        return('Flash', 3)
    elif hand[0][0] == hand[1][0] or hand[1][0] == hand[2][0]:
        return('Coupe', 2)
    else:
        return('High', 1)

def creat_deck():
    deck = []
    cards = list('23456789JQKA') + ['10']
    suits = list('♥♦♣♠')
    for i in range(len(cards)):
        for j in range(len(suits)):
            if cards[i] == 'J':
                power = 11
            elif cards[i] == 'Q':
                power = 12
            elif cards[i] == 'K':
                power = 13
            elif cards[i] == 'A':
                power = 14
            else:
                power = int(cards[i])
            deck.append([cards[i], suits[j], power])
    shuffle(deck)
    return deck

def sort_hand(hand):
    hand.sort(key=lambda card: card[2])
    return hand

def screen_hand(hand):
    vision = ''.join((hand[0][0], hand[0][1])), \
             ''.join((hand[1][0], hand[1][1])), \
             ''.join((hand[2][0], hand[2][1]))
    return vision

def bot_option(bothand):
    if hand[0][1] == hand[1][1] or hand[1][1] == hand[2][1] or hand[0][1] == hand[2][1] \
            and not(hand[0][1] == hand[1][1] == hand[2][1]):
        bothand.sort(key=lambda card: card[1])
        suits = bothand[1][1]
        print('Бот меняет карту не идущую по возрастанию')
        for i in range(3):
            if bothand[i][1] != suits:
                bothand.pop(i)
                bothand.append(playdeck.pop())
        return bothand
    elif bothand[0][2] == bothand[1][2] and bothand[1][2] != bothand[2][2]:
        print('Бот меняет карту, чтобы собрать Tripple')
        bothand.pop(2)
        bothand.append(playdeck.pop())
    elif bothand[1][2] == bothand[2][2] and bothand[0][2] - bothand[1][2]  != 1:
        print('Бот меняет карту, чтобы собрать Tripple')
        bothand.pop(0)
        bothand.append(playdeck.pop())
    elif bothand[1][2] - bothand[0][2] == 1 and bothand[2][2] - bothand[1][2] != 1:
        print('Бот меняет карту не идущую по возрастанию')
        bothand.pop(2)
        bothand.append(playdeck.pop())
    elif bothand[2][2] - bothand[1][2] == 1 and bothand[1][2] - bothand[0][2] != 1:
        print('Бот меняет карту не идущую по возрастанию')
        bothand.pop(2)
        bothand.append(playdeck.pop())
    elif bothand[0][1] == bothand[1][1] or \
        bothand[1][1] == bothand[2][1] or \
        bothand[0][1] == bothand[2][1] and not \
        bothand[0][1] == bothand[1][1] == bothand[2][1]:
        hand.sort(key=lambda card: card[1])
        suits = bothand[1][1]
        print('Бот меняет карту другой масти')
        for i in range(3):
            if bothand[i][1] != suits:
                bothand.pop(i)
                bothand(playdeck.pop())
    else:
        print('бот пытается собрать хотя бы пару')
        bothand.pop(0)
        bothand.append(playdeck.pop())
    return bothand

playdeck = creat_deck()
hand = []

for i in range(3):
    hand.append(playdeck.pop())
sort_hand(hand)
for j in range(3):
    bothand.append(playdeck.pop())
sort_hand(hand)
print('Вам пришли вот такие карты с раздачи:', *screen_hand(hand))

cnt = 0
while True:
    option = input('Вы хотите заменить карту?\n1. Да\n2. Нет\n')
    if option == '1':
        cnt += 1
        while True:
            cards_num = input('введите номер карты, которую хотите заменить: ')
            if cards_num in '123' and len(cards_num) == 1:
                hand.pop(int(cards_num) - 1)
                hand.append(playdeck.pop())
                sort_hand(hand)
                break
            else:
                print('Неверный формат ввода')
    elif option == '2':
        break
    else:
        print('Неверный формат ввода')

    print(screen_hand(hand))

    bot_option(hand)
    sort_hand(hand)

    if cnt == 3:
        break

if check(hand)[1] > check(bothand)[1]:
    print('Вы победили')
elif check(hand)[1] < check(bothand)[1]:
    print('Вы проиграли')
else:
    if hand[2][2] > bothand[2][2]:
        print('Вы победили')
    else:
        print('Вы проиграли')

print(*screen_hand(hand), check(hand))
print(*screen_hand(bothand), check(bothand))