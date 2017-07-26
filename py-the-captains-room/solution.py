# https://www.hackerrank.com/challenges/py-the-captains-room

_ = input()
rooms = sorted(list(map(int, input().split())))
capt_room = set(rooms[0::2]).symmetric_difference(set(rooms[1::2]))
print(capt_room.pop())