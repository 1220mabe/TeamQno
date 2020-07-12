# カテゴリ名とメディアIDをリターンする。
# メディアIDは'https://teamqno.work/wp-admin/upload.php'にアップロードされている画像を指定している


#スタンダード
def check_arc_stan(deck):
    decktext = ",".join(deck)
    media_id = 55   #Team QnoLogo
    deckname = "Rogue"

    #1色
    if "Anax, Hardened in the Forge" in decktext:
        deckname = "Mono-Red"
        media_id = 1933   #Anax, Hardened in the Forge
    if "Vivien, Arkbow Ranger" in decktext:
        deckname = "Mono-Green"
        media_id = 1934   #Vivien, Arkbow Ranger
    if "The Great Henge" in decktext:
        deckname = "Mono-Green"
        media_id = 1935   #The Great Henge
    if "Spawn of Mayhem" in decktext and "Rankle, Master of Pranks" in decktext:
        deckname = "Mono-Black"
        media_id = 377   #Rankle, Master of Pranks

    #2色
    if "Shatter the Sky" in decktext and "Teferi, Time Raveler" in decktext:
        deckname = "Azorius Control"
        media_id = 709   #Teferi, Time Raveler
    if "Ugin, the Spirit Dragon" in decktext and "Hydroid Krasis" in decktext:
        deckname = "Simic Ramp"
        media_id = 373   #Ugin, the Spirit Dragon
    if "Mayhem Devil" in decktext and "Dreadhorde Butcher" in decktext:
        deckname = "Rakdos Sacrifice"
        media_id = 353   #Mayhem Devil
    if "Mayhem Devil" in decktext and "Serrated Scorpion" in decktext:
        deckname = "Rakdos Sacrifice"
        media_id = 353   #Mayhem Devil
    if "Tajic, Legion’s Edge" in decktext and "Legion Warboss" in decktext:
        deckname = "Boros Aggro"
        media_id = 715   #Legion Warboss
    if "Gruul Spellbreaker" in decktext and "Questing Beast" in decktext:
        deckname = "Gruul Aggro"
        media_id = 713   #Gruul Spellbreaker
    if "Opt" in decktext and "Shock" in decktext:
        deckname = "Izzet Aggro"
        media_id = 1936   #Opt
    if "Season of Growth" in decktext and "Karametra’s Blessing" in decktext:
        deckname = "Selesnya Aggro"
        media_id = 1937   #Season of Growth

    #3色
    if "Mayhem Devil" in decktext and "Gilded Goose" in decktext:
        deckname = "Jund Sacrifice"
        media_id = 353   #Mayhem Devil
    if "Expansion // Explosion" in decktext and "Wilderness Reclamation" in decktext:
        deckname = "Temur Reclamation"
        media_id = 369   #Wilderness Reclamation
    if "Uro, Titan of Nature’s Wrath" in decktext and "Teferi, Time Raveler" in decktext:
        deckname = "Bant Ramp"
        media_id = 592   #Uro, Titan of Nature’s Wrath
    if "General Kudro of Drannith" in decktext and "Inspiring Veteran" in decktext:
        deckname = "Mardu Knights"
        media_id = 704   #General Kudro of Drannith
    if "Teferi, Time Raveler" in decktext and "Nightpack Ambusher" in decktext:
        deckname = "Bant Flash"
        media_id = 501   #Nightpack Ambusher
    if "Teferi, Time Raveler" in decktext and "Atris, Oracle of Half-Truths" in decktext:
        deckname = "Esper Control"
        media_id = 1938   #Atris, Oracle of Half-Truths
    if "Uro, Titan of Nature’s Wrath" in decktext and "Casualties of War" in decktext:
        deckname = "Sultai Ramp"
        media_id = 1939   #Casualties of War
    if "Nissa, Who Shakes the World" in decktext and "Discontinuity" in decktext and "Titans' Nest" in decktext:
        deckname = "Sultai Discontinuity"
        media_id = 1009   #Discontinuity

    return deckname,media_id

#パイオニア
def check_arc_pion(deck):
    decktext = ",".join(deck)
    media_id = 28   #Team QnoLogo
    deckname = "Rogue"

    #1色
    if "Champion of Dusk" in decktext:
        deckname = "Mono-Black Vampires"
        media_id = 851   #Rankle, Master of Pranks
    if "Spawn of Mayhem" in decktext:
        deckname = "Mono-Black Aggro"
        media_id = 377   #Rankle, Master of Pranks
    if "Heliod, Sun-Crowned" in decktext:
        deckname = "Mono-White Devotion"
        media_id = 590   #Heliod, Sun-Crowned
    if "Torbran, Thane of Red Fell" in decktext:
        deckname = "Mono-Red"
        media_id = 691   #Torbran, Thane of Red Fell
    #2色
    if "Inverter of Truth" in decktext and "Thassa's Oracle" in decktext:
        deckname = "Dimir Inverter"
        media_id = 588   #Inverter of Truth
    if "Teferi, Hero of Dominaria" in decktext and "Supreme Verdict" in decktext:
        deckname = "Azorius Control"
        media_id = 891   #Teferi, Hero of Dominaria
    if "Teferi, Time Raveler" in decktext and "Supreme Verdict" in decktext:
        deckname = "Azorius Control"
        media_id = 709   #Teferi, Time Raveler
    if "Lurrus of the Dream-Den" in decktext and "Hateful Eidolon" in decktext:
        deckname = "Orzhov Auras"
        media_id = 586   #Lurrus of the Dream-Den
    if "Boros Charm" in decktext and "Eidolon of the Great Revel" in decktext:
        deckname = "Boros Burn"
        media_id = 1941   #Eidolon of the Great Revel
    if "Lurrus of the Dream-Den" in decktext and "Tenth District Legionnaire" in decktext:
        deckname = "Boros Feather(Lurrus)"
        media_id = 586   #Lurrus of the Dream-Den
    if "Feather, the Redeemed" in decktext and "Tenth District Legionnaire" in decktext:
        deckname = "Boros Feather"
        media_id = 1796   #Feather, the Redeemed
    if "Ghalta, Primal Hunger" in decktext and "Rotting Regisaur" in decktext:
        deckname = "Golgari Stompy"
        media_id = 1945   #Ghalta, Primal Hunger
    if "Atarka's Command" in decktext and "Gruul Spellbreaker" in decktext:
        deckname = "Gruul Aggro"
        media_id = 1942   #Atarka's Command
    if "Ensoul Artifact" in decktext and "Skilled Animator" in decktext:
        deckname = "Ensoul Artifact"
        media_id = 1803   #Ensoul Artifact
    if "Supreme Phantom" in decktext and "Rattlechains" in decktext:
        deckname = "Azorius Spirits"
        media_id = 591   #"Supreme Phantom
    if "Uro, Titan of Nature's Wrath" in decktext and "Wilderness Reclamation" in decktext:
        deckname = "Simic Reclamation"
        media_id = 369   #Wilderness Reclamation
    if "Kroxa, Titan of Death's Hunger" in decktext and "Young Pyromancer" in decktext:
        deckname = "Rakdos Aggro"
        media_id = 1893   #Kroxa, Titan of Death's Hunger
    if "Scrapheap Scrounger" in decktext and "Garruk, Unleashed" in decktext:
        deckname = "Golgari Aggro"
        media_id = 838   #Garruk, Unleashed

    #3色
    if "Traverse the Ulvenwald" in decktext and "Thoughtseize" in decktext and "Jace, Vryn's Prodigy" in decktext:
        deckname = "Sultai Delirium"
        media_id = 1940   #Traverse the Ulvenwald
    if "Teferi, Time Raveler" in decktext and "Oath of Kaya" in decktext:
        deckname = "Esper Control"
        media_id = 1943   #Oath of Kaya
    if "Winota, Joiner of Forces" in decktext and "Voice of Resurgence" in decktext:
        deckname = "Naya Winota"
        media_id = 522   #Winota, Joiner of Forces
    if "Uro, Titan of Nature's Wrath" in decktext and "Supreme Verdict" in decktext:
        deckname = "Bant Control"
        media_id = 592   #Uro, Titan of Nature’s Wrath
    if "Possibility Storm" in decktext and "Enter the Infinite" in decktext:
        deckname = "Possibility Storm"
        media_id = 1946   #Possibility Storm
    if "Supreme Phantom" in decktext and "Collected Company" in decktext:
        deckname = "Bant Spirits"
        media_id = 591   #"Supreme Phantom
    if "Underworld Breach" in decktext and "Lotus Field" in decktext:
        deckname = "Lotus Breach"
        media_id = 866   #Underworld Breach
    if "Expansion // Explosion" in decktext and "Wilderness Reclamation" in decktext:
        deckname = "Temur Reclamation"
        media_id = 1947   #Expansion // Explosion
    #5色
    if "Niv-Mizzet Reborn" in decktext:
        deckname = "Niv to Light"
        media_id = 589   #Niv-Mizzet Reborn

    return deckname,media_id