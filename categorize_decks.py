
print("run categorize_decks")

#スタンダード
def check_arc_stan(deck):
    decktext = ",".join(deck)
    #1色
    deckname = "Rogue" 
    if 'Anax, Hardened in the Forge' in decktext:deckname = "Mono-Red"
    if 'Vivien, Arkbow Ranger' in decktext:deckname = "Mono-Green" 
    #2色
    if 'Shatter the Sky' in decktext and 'Teferi, Time Raveler' in decktext:deckname = "Azorius Control" 
    if 'Ugin, the Spirit Dragon' in decktext  and 'Hydroid Krasis' in decktext:deckname = "Simic Ramp" 
    if 'Mayhem Devil' in decktext  and 'Dreadhorde Butcher' in decktext: deckname = "Rakdos Sacrifice"
    if 'Tajic, Legion’s Edge' in decktext  and 'Legion Warboss' in decktext:deckname = "Boros Aggro" 
    if 'Gruul Spellbreaker' in decktext  and 'Questing Beast' in decktext:deckname = "Gruul Aggro" 
    if 'Opt' in decktext  and 'Shock' in decktext:deckname = "Izzet Aggro" 
    if 'Season of Growth' in decktext  and 'Karametra’s Blessing'  in decktext:deckname = "Selesnya Aggro" 
    #3色
    if 'Mayhem Devil' in decktext and  'Gilded Goose' in decktext:deckname = "Jund Sacrifice" 
    if 'Expansion // Explosion' in decktext  and 'Wilderness Reclamation' in decktext:deckname = "Temur Reclamation" 
    if 'Uro, Titan of Nature’s Wrath' in decktext  and 'Teferi, Time Raveler' in decktext:deckname = "Bant Ramp" 
    if 'General Kudro of Drannith' in decktext  and 'Inspiring Veteran' in decktext:deckname = "Mardu Knights" 
    if 'Teferi, Time Raveler' in decktext and  'Nightpack Ambusher' in decktext:deckname = "Bant Flash" 
    if 'Teferi, Time Raveler' in decktext and  'Atris, Oracle of Half-Truths' in decktext:deckname = "Esper Control" 
    if 'Uro, Titan of Nature’s Wrath' in decktext and  'Casualties of War' in decktext:deckname = "Sultai Ramp" 
    
    return deckname