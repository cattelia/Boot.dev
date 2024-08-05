

def meditate(mana, max_mana, energy, energy_potions):

    while mana <= max_mana:
        if mana + 1 > max_mana or energy == 0 and energy_potions == 0:
            return mana, energy, energy_potions


        if energy == 0 and energy_potions > 0:
            print("Using 1 potion")
            energy_potions -= 1
            energy += 50
        

        if mana == 0:
            print("Mana is 0, adding 3 mana.")
            energy -= 1
            mana += 3
            print(f"Mana: {mana}, Max Mana: {max_mana}, Energy: {energy}")

        elif mana + 3 <= max_mana:
            energy -= 1
            mana += 3            

        else:
            energy -= 1
            mana += ((max_mana - mana) % 3)
            print(f"Mana: {mana}, Max Mana: {max_mana}, Energy: {energy}")









#print(meditate(50, 50, 1, 0)) # Full mana
#print(meditate(12, 50, 0, 0))  # Empty energy and energy potions
#print(meditate(12, 50, 0, 1))  # Need energy potion
print(meditate(0, 10, 3, 0))
