from collections import Counter

def lines():
    with open('data/day07.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]

def parse_hands(lines):
    hands = []
    for line in lines:
        data = line.split(' ')
        hands.append((data[0], int(data[1])))

    return hands

def score(hand):
    cards = hand[0]
    frequencies = Counter(Counter(cards).values())

    if frequencies[5]:
        return 0
    elif frequencies[4]:
        return 1
    elif frequencies[3] and frequencies[2]:
        return 2
    elif frequencies[3]:
        return 3
    elif frequencies[2] == 2:
        return 4
    elif frequencies[2]:
        return 5
    else:
        return 6

if __name__ == '__main__':
    hands = parse_hands(lines())

    for hand in hands:
        hand_score = score(hand)
        print(f'hand: {hand[0]}, score: {hand_score}')





