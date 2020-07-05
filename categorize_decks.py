
print("run categorize_decks")

#スタンダード
def check_arc_stan(deck):
    decktext = ",".join(deck)
    #1色
    deckname = "Rogue"
    if "Anax, Hardened in the Forge" in decktext:deckname = "Mono-Red"
    if "Vivien, Arkbow Ranger" in decktext:deckname = "Mono-Green"
    #2色
    if "Shatter the Sky" in decktext and "Teferi, Time Raveler" in decktext:deckname = "Azorius Control"
    if "Ugin, the Spirit Dragon" in decktext and "Hydroid Krasis" in decktext:deckname = "Simic Ramp"
    if "Mayhem Devil" in decktext and "Dreadhorde Butcher" in decktext:deckname = "Rakdos Sacrifice"
    if "Mayhem Devil" in decktext and "Serrated Scorpion" in decktext:deckname = "Rakdos Sacrifice"
    if "Tajic, Legion’s Edge" in decktext and "Legion Warboss" in decktext:deckname = "Boros Aggro"
    if "Gruul Spellbreaker" in decktext and "Questing Beast" in decktext:deckname = "Gruul Aggro"
    if "Opt" in decktext and "Shock" in decktext:deckname = "Izzet Aggro"
    if "Season of Growth" in decktext and "Karametra’s Blessing" in decktext:deckname = "Selesnya Aggro"
    #3色
    if "Mayhem Devil" in decktext and "Gilded Goose" in decktext:deckname = "Jund Sacrifice"
    if "Expansion // Explosion" in decktext and "Wilderness Reclamation" in decktext:deckname = "Temur Reclamation"
    if "Uro, Titan of Nature’s Wrath" in decktext and "Teferi, Time Raveler" in decktext:deckname = "Bant Ramp"
    if "General Kudro of Drannith" in decktext and "Inspiring Veteran" in decktext:deckname = "Mardu Knights"
    if "Teferi, Time Raveler" in decktext and "Nightpack Ambusher" in decktext:deckname = "Bant Flash"
    if "Teferi, Time Raveler" in decktext and "Atris, Oracle of Half-Truths" in decktext:deckname = "Esper Control"
    if "Uro, Titan of Nature’s Wrath" in decktext and "Casualties of War" in decktext:deckname = "Sultai Ramp"

    return deckname

#パイオニア
def check_arc_pion(deck):
    decktext = ",".join(deck)
    #1色
    deckname = "Rogue"
    if "Champion of Dusk" in decktext:deckname = "Mono-Black Vampires"
    if "Spawn of Mayhem" in decktext:deckname = "Mono-Black Aggro"
    if "Heliod, Sun-Crowned" in decktext:deckname = "Mono-White Devotion"
    if "Torbran, Thane of Red Fell" in decktext:deckname = "Mono-Red Aggro"
    #2色
    if "Inverter of Truth" in decktext and "Thassa's Oracle" in decktext:deckname = "Dimir Inverter"
    if "Teferi, Hero of Dominaria" in decktext and "Supreme Verdict" in decktext:deckname = "Azorius Control"
    if "Lurrus of the Dream-Den" in decktext and "Hateful Eidolon" in decktext:deckname = "Orzhov Auras"
    if "Boros Charm" in decktext and "Eidolon of the Great Revel" in decktext:deckname = "Boros Burn"
    if "Lurrus of the Dream-Den" in decktext and "Tenth District Legionnaire" in decktext:deckname = "Boros Feather(Lurrus)"
    if "Feather, the Redeemed" in decktext and "Tenth District Legionnaire" in decktext:deckname = "Boros Feather"
    if "Ghalta, Primal Hunger" in decktext and "Rotting Regisaur" in decktext:deckname = "Golgari Stompy"
    if "Ensoul Artifact" in decktext and "Skilled Animator" in decktext:deckname = "Izzet Ensoul"
    if "Supreme Phantom" in decktext and "Rattlechains" in decktext:deckname = "Azorius Spirits"
    #3色
    if "Traverse the Ulvenwald" in decktext and "Thoughtseize" in decktext and "Jace, Vryn's Prodigy" in decktext:deckname = "Sultai Delirium"
    if "Teferi, Time Raveler" in decktext and "Oath of Kaya" in decktext:deckname = "Esper Control"
    if "Winota, Joiner of Forces" in decktext and "Voice of Resurgence" in decktext:deckname = "Naya Midrange"
    if "Uro, Titan of Nature's Wrath" in decktext and "Supreme Verdict" in decktext:deckname = "Bant Control"
    if "Possibility Storm" in decktext and "Enter the Infinite" in decktext:deckname = "Possibility Storm"
    if "Supreme Phantom" in decktext and "Collected Company" in decktext:deckname = "Bant Spirits"
    if "Underworld Breach" in decktext and "Lotus Field" in decktext:deckname = "Lotus Breach"
    #5色
    if "Niv-Mizzet Reborn" in decktext:deckname = "Niv to Light"

    return deckname