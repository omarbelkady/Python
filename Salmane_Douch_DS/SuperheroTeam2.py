def superhero_team(heroes: tuple)->str:
    if not heroes:
        print("Nothing in the tuple")
    else:
        return max(heroes, key=lambda heroes[1])[0]


superheroes= [("Superman", 85),("Batman", 212),("Ironman", 212), ("iRobot", 15)]
print(superhero_team(superheroes))
