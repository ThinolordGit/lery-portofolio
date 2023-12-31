from exo import *
from random import *
class Player ():
    def __init__(self,name :str,life: int = 20,defense :int = 10,focus: str = 30, focusReduice :list =[0,8,15],attackPoint :list = [{"min":6,"max":10},{"min":11,"max":17},{"min":18,"max":24}]) -> None:
        print(f"{name} with {life} as health, {defense} as defense and {focus} as focus")
        self.name :str = name
        self.attackPoint :list = attackPoint
        self.defense :int = defense
        self.life :int = life
        self.focus :int = focus
        self.gain :int = 0.4
        self.focusReduice = focusReduice
    
    def calcDemage (self, adversHealth: int, attackStrong :map,adversDef: int = 10):
        damage = randint(attackStrong["min"],attackStrong["max"])
        attack = damage - int((adversHealth+adversDef)/2)
        if (attack < 0):
            attack = 0
        finalHealth = adversHealth - attack
        print (finalHealth)
    def useChoose (self, numberChoice: int):
        attackeWith = f"attack tween {self.attackPoint[numberChoice-1]['min']} - {self.attackPoint[numberChoice-1]['max']}"
        self.defense -= self.focusReduice[numberChoice-1]
        if (self.defense < 0):
            self.defense = 0
        print (self.defense)
        self.calcDemage (20,self.attackPoint[numberChoice-1])
        
    def userChoices (self):
        print(f"1 coups minim -{self.focusReduice[0]} de concentration")
        print(f"2 coups normal -{self.focusReduice[1]} de concentration")
        print(f"3 coups fort -{self.focusReduice[2]} de concentration")
    
    def askChoose (self) :
        while True :
            option = input(f"{self.name} choose one option (1 or 2 or 3) to attack by entry number choosed (please only number tween 1 and 3): ")
            if (isNum(option)) :
                option = int(option)
                if (isNum(option) and option >=1 and option <= 3):
                    break
            
        self.useChoose(option)
        
        
        
user = Player (userName)
user.userChoices ()
user.askChoose ()