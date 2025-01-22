command=""
prevcom=""
while command != quit:
    command=input("")
    if command=="start":
        print("car started")
    elif command=="stop":
        print("car stopped")
    elif command=="help":
        print("crazy shit")
    elif command=="quit":
        print("game ended")
        break
    else:
        print("command not recognised!, type help for help")