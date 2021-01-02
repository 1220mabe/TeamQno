
# カテゴリ名とメディアIDをリターンする。
# メディアIDは'https://teamqno.work/wp-admin/upload.php'にアップロードされている画像を指定している
# 画像は220 x 160




#スタンダード
def check_arc_stan(deck):
    #初期値
    media_id = 12415   #密輸人の回転翼機
    deckname = "Rogue"
    decktext = ",".join(deck)
    #check_arc_base(decktext)

    # 1色全般(基本土地)
    if "Island" in decktext:
        deckname = "Mono-U"
        media_id = 12730
    if "Swamp" in decktext:
        deckname = "Mono-B"
        media_id = 12731
    if "Plains" in decktext:
        deckname = "Mono-W"
        media_id = 12732
    if "Mountain" in decktext:
        deckname = "Mono-R"
        media_id = 12733
    if "Forest" in decktext:
        deckname = "Mono-G"
        media_id = 12734
    # 2色全般(ショックランド)
    if "Plains" in decktext and "Island" in decktext:
        deckname = "UW"
        media_id = 12400
    if "Swamp" in decktext and "Island" in decktext:
        deckname = "UB"
        media_id = 12401
    if "Mountain" in decktext and "Swamp" in decktext:
        deckname = "RB"
        media_id = 12402
    if "Mountain" in decktext and "Forest" in decktext:
        deckname = "RG"
        media_id = 12403
    if "Plains" in decktext and "Forest" in decktext:
        deckname = "GW"
        media_id = 12404
    if "Plains" in decktext and "Swamp" in decktext:
        deckname = "BW"
        media_id = 12405
    if "Mountain" in decktext and "Island" in decktext:
        deckname = "UR"
        media_id = 12406
    if "Swamp" in decktext and "Forest" in decktext:
        deckname = "BG"
        media_id = 12407
    if "Mountain" in decktext and "Plains" in decktext:
        deckname = "RW"
        media_id = 12408
    if "Forest" in decktext and "Island" in decktext:
        deckname = "GU"
        media_id = 12409
    # 3色全般(トライランド)
    if "Plains" in decktext and "Swamp" in decktext and "Plains" in decktext:
        deckname = "BGW"
        media_id = 12410
    if "Plains" in decktext and "Mountain" in decktext and "Island" in decktext:
        deckname = "URW"
        media_id = 12411
    if "Forest" in decktext and "Swamp" in decktext and "Island" in decktext:
        deckname = "BGU"
        media_id = 12412
    if "Mountain" in decktext and "Swamp" in decktext and "Plains" in decktext:
        deckname = "BRU"
        media_id = 12413
    if "Mountain" in decktext and "Forest" in decktext and "Island" in decktext:
        deckname = "RGU"
        media_id = 12414
        #グリクシス BRU
        #バント GUW
        #ジャンド BRG
        #ナヤ GRW
        #エスパー BUW

    #1色
    if "Fervent Champion" in decktext:
        deckname = "Mono-R"
        media_id = 11434   #Fervent Champion
    if "Vivien, Arkbow Ranger" in decktext:
        deckname = "Mono-G"
        media_id = 1934   #Vivien, Arkbow Ranger
    if "The Great Henge" in decktext and "Wicked Wolf" in decktext:
        deckname = "Mono-G"
        media_id = 11433   #Wicked Wolf
    if "Spawn of Mayhem" in decktext and "Rankle, Master of Pranks" in decktext:
        deckname = "Mono-B"
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
    if "Edgewall Innkeeper" in decktext and "Bonecrusher Giant" in decktext:
        deckname = "Gruul Adventures"
        media_id = 11431   #Bonecrusher Giant
    if "Lurrus of the Dream-Den" in decktext and "Soaring Thought-Thief" in decktext:
        deckname = "Dimir Rogue"
        media_id = 11432   #Soaring Thought-Thief

    #3色
    if "Mayhem Devil" in decktext and "Gilded Goose" in decktext:
        deckname = "Jund Sacrifice"
        media_id = 353   #Mayhem Devil
    if "Expansion // Explosion" in decktext and "Wilderness Reclamation" in decktext:
        deckname = "Temur Reclamation"
        media_id = 369   #Wilderness Reclamation
    if "Genesis Ultimatum" in decktext:
        deckname = "Temur Ramp"
        media_id = 11436   #Genesis Ultimatum
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
    if "Uro, Titan of Nature’s Wrath" in decktext and "Liliana, Waker of the Dead" in decktext:
        deckname = "Sultai Control"
        media_id = 2176   #Liliana, Waker of the Dead
    if "Hydroid Krasis" in decktext and "Heartless Act" in decktext:
        deckname = "Sultai Control"
        media_id = 2284   #Hydroid Krasis
    if "Omen of the Sea" in decktext and "Doom Foretold" in decktext:
        deckname = "Esper Doom"
        media_id = 11435   #Hydroid Krasis

    return deckname,media_id

#ヒストリック
def check_arc_hist(deck):
    #初期値
    media_id = 12415   #密輸人の回転翼機
    deckname = "Rogue"
    decktext = ",".join(deck)
    #check_arc_base(decktext)

    # 1色全般(基本土地)
    if "Island" in decktext:
        deckname = "Mono-U"
        media_id = 12730
    if "Swamp" in decktext:
        deckname = "Mono-B"
        media_id = 12731
    if "Plains" in decktext:
        deckname = "Mono-W"
        media_id = 12732
    if "Mountain" in decktext:
        deckname = "Mono-R"
        media_id = 12733
    if "Forest" in decktext:
        deckname = "Mono-G"
        media_id = 12734
    # 2色全般(ショックランド)
    if "Plains" in decktext and "Island" in decktext:
        deckname = "UW"
        media_id = 12400
    if "Swamp" in decktext and "Island" in decktext:
        deckname = "UB"
        media_id = 12401
    if "Mountain" in decktext and "Swamp" in decktext:
        deckname = "RB"
        media_id = 12402
    if "Mountain" in decktext and "Forest" in decktext:
        deckname = "RG"
        media_id = 12403
    if "Plains" in decktext and "Forest" in decktext:
        deckname = "GW"
        media_id = 12404
    if "Plains" in decktext and "Swamp" in decktext:
        deckname = "BW"
        media_id = 12405
    if "Mountain" in decktext and "Island" in decktext:
        deckname = "UR"
        media_id = 12406
    if "Swamp" in decktext and "Forest" in decktext:
        deckname = "BG"
        media_id = 12407
    if "Mountain" in decktext and "Plains" in decktext:
        deckname = "RW"
        media_id = 12408
    if "Forest" in decktext and "Island" in decktext:
        deckname = "GU"
        media_id = 12409
    # 3色全般(トライランド)
    if "Plains" in decktext and "Swamp" in decktext and "Swamp" in decktext:
        deckname = "BGW"
        media_id = 12410
    if "Plains" in decktext and "Mountain" in decktext and "Island" in decktext:
        deckname = "URW"
        media_id = 12411
    if "Forest" in decktext and "Swamp" in decktext and "Island" in decktext:
        deckname = "BGU"
        media_id = 12412
    if "Mountain" in decktext and "Swamp" in decktext and "Plains" in decktext:
        deckname = "BRU"
        media_id = 12413
    if "Mountain" in decktext and "Forest" in decktext and "Island" in decktext:
        deckname = "RGU"
        media_id = 12414

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
    if "Heliod, Sun-Crowned" in decktext:
        deckname = "Mono-White"
        media_id = 590   #Heliod, Sun-Crowned
    if "Muxus, Goblin Grandee" in decktext:
        deckname = "Mono-Red Goblin"
        media_id = 2474   #Muxus, Goblin Grandee

    #2色
    if "Shatter the Sky" in decktext and "Teferi, Time Raveler" in decktext:
        deckname = "Azorius Control"
        media_id = 709   #Teferi, Time Raveler
    if "Ugin, the Spirit Dragon" in decktext and "Hydroid Krasis" in decktext:
        deckname = "Simic Ramp"
        media_id = 373   #Ugin, the Spirit Dragon
    if "Mayhem Devil" in decktext and "Priest of Forgotten Gods" in decktext:
        deckname = "Rakdos Sacrifice"
        media_id = 353   #Mayhem Devil
    if "Mayhem Devil" in decktext and "Woe Strider" in decktext:
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
    if "Lukka, Coppercoat Outcast" in decktext and "Craterhoof Behemoth" in decktext:
        deckname = "Lukka Combo"
        media_id = 2472   #Lukka, Coppercoat Outcast
    if "Lurrus of the Dream-Den" in decktext and "Dreadhorde Arcanist" in decktext:
        deckname = "Rakdos Arcanist"
        media_id = 11597   #Dreadhorde Arcanist

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
    if "Uro, Titan of Nature’s Wrath" in decktext and "Liliana, Waker of the Dead" in decktext:
        deckname = "Sultai Control"
        media_id = 2176   #Liliana, Waker of the Dead
    if "Hydroid Krasis" in decktext and "Fatal Push" in decktext:
        deckname = "Sultai Midrange"
        media_id = 2284   #Hydroid Krasis
    if "Kethis, the Hidden Hand" in decktext and "Mox Amber" in decktext:
        deckname = "Kethis Combo"
        media_id = 2384   #Kethis, the Hidden Hand
    if "Underworld Breach" in decktext and "Mox Amber" in decktext:
        deckname = "Breach Combo"
        media_id = 866   #Underworld Breach
    if "Paradox Engine" in decktext and "Mox Amber" in decktext and "Escape to the Wilds" in decktext:
        deckname = "Temur Paradox"
        media_id = 11591   #Temur Paradox
    if "Linvala, Shield of Sea Gate" in decktext and "Collected Company" in decktext:
        deckname = "Bant Company"
        media_id = 12416   #Linvala, Shield of Sea Gate
    if "Uro, Titan of Nature’s Wrath" in decktext and "Nissa, Who Shakes the World" in decktext and "Extinction Event" in decktext:
        deckname = "Sultai Control"
        media_id = 592   #Uro, Titan of Nature’s Wrath


    #4色
    if "Uro, Titan of Nature’s Wrath" in decktext and "Yasharn, Implacable Earth" in decktext:
        deckname = "4C Control"
        media_id = 11593   #Yasharn, Implacable Earth
    if "Uro, Titan of Nature’s Wrath" in decktext and "Teferi, Time Raveler" in decktext and "Fatal Push" in decktext:
        deckname = "4C Control"
        media_id = 592   #Uro, Titan of Nature’s Wrath

    #5色
    if "Golos, Tireless Pilgrim" in decktext  and "Field of the Dead" in decktext:
        deckname = "5C Golos"
        media_id = 2537   #Golos, Tireless Pilgrim
    return deckname,media_id


#パイオニア
def check_arc_pion(deck):
    #初期値
    media_id = 12415   #密輸人の回転翼機
    deckname = "Rogue"
    decktext = ",".join(deck)
    #check_arc_base(decktext)

    # 1色全般(基本土地)
    if "Island" in decktext:
        deckname = "Mono-U"
        media_id = 12730
    if "Swamp" in decktext:
        deckname = "Mono-B"
        media_id = 12731
    if "Plains" in decktext:
        deckname = "Mono-W"
        media_id = 12732
    if "Mountain" in decktext:
        deckname = "Mono-R"
        media_id = 12733
    if "Forest" in decktext:
        deckname = "Mono-G"
        media_id = 12734
    # 2色全般(ショックランド)
    if "Plains" in decktext and "Island" in decktext:
        deckname = "UW"
        media_id = 12400
    if "Swamp" in decktext and "Island" in decktext:
        deckname = "UB"
        media_id = 12401
    if "Mountain" in decktext and "Swamp" in decktext:
        deckname = "RB"
        media_id = 12402
    if "Mountain" in decktext and "Forest" in decktext:
        deckname = "RG"
        media_id = 12403
    if "Plains" in decktext and "Forest" in decktext:
        deckname = "GW"
        media_id = 12404
    if "Plains" in decktext and "Swamp" in decktext:
        deckname = "BW"
        media_id = 12405
    if "Mountain" in decktext and "Island" in decktext:
        deckname = "UR"
        media_id = 12406
    if "Swamp" in decktext and "Forest" in decktext:
        deckname = "BG"
        media_id = 12407
    if "Mountain" in decktext and "Plains" in decktext:
        deckname = "RW"
        media_id = 12408
    if "Forest" in decktext and "Island" in decktext:
        deckname = "GU"
        media_id = 12409
    # 3色全般(トライランド)
    if "Plains" in decktext and "Swamp" in decktext and "Swamp" in decktext:
        deckname = "BGW"
        media_id = 12410
    if "Plains" in decktext and "Mountain" in decktext and "Island" in decktext:
        deckname = "URW"
        media_id = 12411
    if "Forest" in decktext and "Swamp" in decktext and "Island" in decktext:
        deckname = "BGU"
        media_id = 12412
    if "Mountain" in decktext and "Swamp" in decktext and "Plains" in decktext:
        deckname = "BRU"
        media_id = 12413
    if "Mountain" in decktext and "Forest" in decktext and "Island" in decktext:
        deckname = "RGU"
        media_id = 12414

    #1色
    if "Champion of Dusk" in decktext:
        deckname = "Mono-B Vampires"
        media_id = 851   #Rankle, Master of Pranks
    if "Spawn of Mayhem" in decktext:
        deckname = "Mono-B Aggro"
        media_id = 377   #Rankle, Master of Pranks
    if "Heliod, Sun-Crowned" in decktext:
        deckname = "Mono-W Devotion"
        media_id = 590   #Heliod, Sun-Crowned
    if "Torbran, Thane of Red Fell" in decktext:
        deckname = "Mono-R"
        media_id = 691   #Torbran, Thane of Red Fell
    if "Collective Defiance" in decktext:
        deckname = "Mono-R"
        media_id = 11444   #Collective Defiance

    if "Goblin Piledriver" in decktext:
        deckname = "Mono-R Goblin"
        media_id = 2169   #Goblin Piledriver
    if "Karn, the Great Creator" in decktext and "Nissa, Who Shakes the World" in decktext:
        deckname = "Mono-G PW"
        media_id = 11439   #Goblin Piledriver

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
        media_id = 11441   #Sram, Senior Edificer
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
        media_id = 592   #Uro, Titan of Nature’s Wrath
    if "Kroxa, Titan of Death's Hunger" in decktext and "Young Pyromancer" in decktext:
        deckname = "Rakdos Aggro"
        media_id = 1893   #Kroxa, Titan of Death's Hunger
    if "Scrapheap Scrounger" in decktext and "Garruk, Unleashed" in decktext:
        deckname = "Golgari Aggro"
        media_id = 838   #Garruk, Unleashed
    if "Kroxa, Titan of Death's Hunger" in decktext and "Liliana, Waker of the Dead" in decktext:
        deckname = "Rakdos Control"
        media_id = 2176   #Liliana, Waker of the Dead
    if "Gruul Spellbreaker" in decktext and "Questing Beast" in decktext:
        deckname = "Gruul Aggro"
        media_id = 713   #Gruul Spellbreaker
    if "Vraska, Golgari Queen" in decktext and "Traverse the Ulvenwald" in decktext:
        deckname = "Golgari Delirium"
        media_id = 2916   #Vraska, Golgari Queen
    if "Lurrus of the Dream-Den" in decktext and "Chained to the Rocks" in decktext  and "Soul-Scar Mage" in decktext:
        deckname = "Boros Burn"
        media_id = 11442   #Soul-Scar Mage

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
    if "Vizier of Tumbling Sands" in decktext and "Lotus Field" in decktext:
        deckname = "Lotus Combo"
        media_id = 11445   #Underworld Breach
    if "Expansion // Explosion" in decktext and "Wilderness Reclamation" in decktext:
        deckname = "Temur Reclamation"
        media_id = 1947   #Expansion // Explosion
    if "Satyr Wayfinder" in decktext and "Prized Amalgam" in decktext:
        deckname = "Sultai Dredge"
        media_id = 878   #Prized Amalgam
    if "Neoform" in decktext and "Swamp" in decktext:
        deckname = "Sultai Neoform"
        media_id = 2173   #Neoform
    if "Kethis, the Hidden Hand" in decktext and "Mox Amber" in decktext:
        deckname = "Kethis Combo"
        media_id = 2384   #Kethis, the Hidden Hand
    if "Kethis, the Hidden Hand" in decktext and "Mox Amber" in decktext:
        deckname = "Kethis Combo"
        media_id = 2384   #Kethis, the Hidden Hand
    if "Balustrade Spy" in decktext:
        deckname = "The Spy"
        media_id = 11438   #Four-Color Omnath
    if "Uro, Titan of Nature’s Wrath" in decktext and "Nissa, Who Shakes the World" in decktext and "Extinction Event" in decktext:
        deckname = "Sultai Control"
        media_id = 592   #Uro, Titan of Nature’s Wrath
    if "Uro, Titan of Nature’s Wrath" in decktext and "Wilderness Reclamation" in decktext and "Extinction Event" in decktext:
        deckname = "Sultai Control"
        media_id = 592   #Uro, Titan of Nature’s Wrath
    if "Uro, Titan of Nature’s Wrath" in decktext and "Nissa, Who Shakes the World" in decktext and "Thoughtseize" in decktext:
        deckname = "Sultai Control"
        media_id = 592   #Uro, Titan of Nature’s Wrath

    #4色
    if "Omnath, Locus of Creation" in decktext and "Genesis Ultimatum" in decktext:
        deckname = "4C Omnath"
        media_id = 11437   #Four-Color Omnath

    #5色
    if "Niv-Mizzet Reborn" in decktext:
        deckname = "Niv to Light"
        media_id = 11443   #Niv-Mizzet Reborn

    return deckname,media_id
