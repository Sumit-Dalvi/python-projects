# GunGame.py
guns = ["Kar98", "AKM", "SCAR-L", "M416", "UMP"]
noOfKills =  0
while noOfKills != len(guns):
    print("you have ", guns[noOfKills] )
    kills = (input("Did u killed anyone y/n ? ") ).lower()
    if kills == "y":
        noOfKills = noOfKills + 1
    elif kills == "n":
        print("You R NOOB")
    else:
        print("Error, plz [Enter] y/n ")
print("GAME ENDED, YOU WON!")
