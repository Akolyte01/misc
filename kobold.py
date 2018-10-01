import random

while True:
    for i in range(10):
        first = random.randint(1,20) + 4
        second = random.randint(1,20) + 4
        damageRoll = random.randint(1,6)
        advantage = first if first > second else second
        disadvantage = first if first < second else second
        print "normal: %2s  adv: %2s  dis: %2s | dmg: %2s  crit: %2s"%(first, advantage, disadvantage, damageRoll+ 2, damageRoll*2 +2)  
    raw_input("Generate more")
    
raw_input("wat")