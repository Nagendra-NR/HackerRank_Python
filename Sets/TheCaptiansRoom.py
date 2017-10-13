_ = int(input())
room_numbers = [int(x) for x in input().split()]

#We actually dont need sets here
#captain_room = set()
#tourist_rooms = set()

captain_room = []
tourist_rooms = []


for n in room_numbers:
    if n not in tourist_rooms:
        if n not in captain_room:
            captain_room.append(n) #use .add Set is used
        else:
            captain_room.remove(n)
            tourist_rooms.append(n) # use .add if Set is used
            
print(captain_room.pop())
