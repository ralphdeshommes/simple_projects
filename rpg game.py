import random
from time import sleep



class charater:
    def __init__(self,name,attack=None,defense = 0, health=100,dodge=5, potion=0,shit_talk=None):

        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.dodge = dodge
        self.potion = potion
        self.shit_talk = shit_talk





def engaging_battle_player(player,enemy):
   
    print("--------------------------------------------------------------------------------------------------------")
    print(f"{player.name} is approching an {enemy.name} choose a number corlating to the attack")
    sleep(2)
    for i, n in enumerate(player.attack):
        print(f"{(i + 1)}. {n}")
    print("5. potions")
    print("6. defend")
    
    
    
    
    chosen_attack = int(input("please select the number"))
    
    
    # if the number is 5 the player will use the potion and the enemy will start attacking
    if chosen_attack == 5:
        number_of_potions(player,chosen_attack,player.name)
        engaging_battle_enemy(enemy,player)
        return
    elif chosen_attack == 6:
        defend_attack(player,player.name,enemy)
        engaging_battle_enemy(enemy,player)
    
   
  
    key = list(player.attack)[chosen_attack - 1]

    print(f"{player.name} use {key}")
    sleep(2.5)
    print(f"the enemy has a defense of {enemy.defense} ")
    sleep(2.5)
    print(f"{enemy.name} recieved {player.attack[key] - enemy.defense} damage")


    enemy_health = enemy.health - (player.attack[key]- enemy.defense)
    enemy.health = max(0,enemy_health)
    if enemy.health == 0:
        print(f"{enemy.name} has been defeated!")
        return
    print(f"{enemy.name}'s health: {enemy.health}")

    engaging_battle_enemy(enemy,player)



   
    
    




    
        

slime_shit_talk = "a hero like you dont belong here"

hero_attacks = {
    "Justice kick": 12,
    "honesty impact" : 14,
    "brave soul" : 10,
    "prideful judgement" : 21

}



slime_attacks = {
    "Goo bomb": 10,
    "slimey whip":15,
    "dew drop" : 5,
    "flubber" : 8

}

skeleton_attacks = {
    "unbrritle" : 32

}

final_boss_attacks = {
    "worlds edge" : 45,
    "final departure" : 45,
    "all seeing strike" : 50,
    "journeys end" : 54

}



slime_charater = charater("slime",attack=slime_attacks,defense=5, potion=2, shit_talk=slime_shit_talk)
player_charater  = charater("hero",attack=hero_attacks,defense=5,potion=3)




def defend_attack(player, enemy,enemy_attack_key):
    print(f"{player.name} used {player.defense} defense to protect against {enemy_attack_key}")
    print("players defense got chipped during the attack")
    player.health = max(0,player.health - (enemy.attack[enemy_attack_key] - player.defense))
    player.defense -= 1
    print(f"{player.name}'s defense: {player.defense}")
    print(f"{player.name}'s health: {player.health}")
    return 



def engaging_battle_enemy(enemy,player,chosen_attack=0):
    print("-------------------------------------------------------------------------------")
    print("the enemy is engaging")
    enemy_attack_key = list(enemy.attack)[random.randint(0,3)]
    enemy_potion_chance = random.randint(0,5)
    if enemy.potion == 0 and enemy_potion_chance == 5:
        enemy_potion_chance = 0
    elif enemy_potion_chance == 5:
        number_of_potions(enemy,enemy_attack_key,enemy.name)
        return
    elif chosen_attack == 6:
        defend_attack(player,enemy,enemy_attack_key)
        return

    print(f"{enemy.name} used {enemy_attack_key}")
    sleep(2)
    half_defense = player.defense // 2
    print(f"{player.name} has defended with of his defense of {half_defense}")
    
    sleep(2)
    player.health = max(0,player.health - (enemy.attack[enemy_attack_key] - half_defense))
    if player.health == 0:
        print(f"{enemy.name}: {enemy.shit_talk}")
        print(f"{player.name} has been defeated, you lose")
        return
    
    print(f"{player.name}'s health: {player.health} ")



def number_of_potions(charater, potion: int, name: str):
    if charater.potion > 0:
        charater.potion -= 1
        charater.health += 10
        print(f"{name} has used one of their potions and has {charater.potion} left")
        print(f"health: {charater.health}")
        return
    else:
        print("--------------------------------------------------------------------------")
        print("you have no more potions in your bag, please pick a number for an attack")
        engaging_battle_player(player_charater,slime_charater)






while slime_charater.health > 0 and  player_charater.health > 0:
    engaging_battle_player(player_charater,slime_charater)


player_charater = charater("hero",attack=hero_attacks,defense=5,potion=3)

print("good job on defeating the slime")
sleep(3)

print("but how about the ruthless skeleton ")



























