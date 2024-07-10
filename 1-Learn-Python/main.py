# https://www.boot.dev/lessons/d91979cc-c760-4dec-aff8-cbe25b0ea505

def meditate(mana, max_mana, energy, energy_potions):
    character_meditating = True

    while energy != 0 and energy_potions != 0:
                
        # If I do not have energy to consume
        #   Consume 1 energy_potion
        if energy == 0 and energy_potions > 0:
            energy_potions -= 1
            energy += 50

        # Mana cannot exceed max_mana 
        #   even if I have energy and energy_potions
        if mana + 3 > max_mana:
            return mana, energy, energy_potions
        else:
            # Convert 1 energy to 3 mana
            energy -= 1
            mana += 3
    
    return mana, energy, energy_potions