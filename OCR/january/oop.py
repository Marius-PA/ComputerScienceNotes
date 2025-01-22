class Dungeon:
    """Create a Dungeon"""

    # constructor
    def __init__(self, playerlevel, NumberMonsters, floors, difficulty):
        # set initial attributes
        
        self._level = playerlevel
        self._NumberMonsters = NumberMonsters
        self._floors = floors
        self._difficulty = difficulty
    
    def level(self):
        return {'Current level':self.level}
    
    def CheckDifficulty(self):
        if self._level / 2 >= self._difficulty:
            return "You can do this dongeon"
        else:
            return "U need to level up to access this dongeon"

playerlevel = int(input("Player Level : "))
easydungeon = Dungeon(playerlevel,10,2,1)

print(easydungeon._level)
print(easydungeon._floors)
print(easydungeon._NumberMonsters)
print(easydungeon._difficulty)

print(easydungeon.CheckDifficulty())