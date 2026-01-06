
player = {
    "name": "Knight",
    "stats": {
        "health": 100,
        "attack": 25,
        "defense": 10
    },
    "level": 1
}


damage = 30
player["stats"]["health"] -= damage

if player["stats"]["health"] <= 0:
    print("Game Over")
else:
    player["level"] += 1
    print("Level Up!")

print(player)

# Output:
# Level Up!                    
# {'name': 'Knight', 'stats': {'health': 70, 'attack': 25, 'defense': 10}, 'level': 2}