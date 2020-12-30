# -*- coding: utf-8 -*
import main_decklist_mtgmelee
import getmelee.getMtgmeleeTournament
import getmelee.getBestEight

meleeurl = r'https://mtgmelee.com/Tournaments'
tournaments = []
decks = []

tournaments = getmelee.getMtgmeleeTournament.get_tournamentlist(meleeurl)
print(tournaments)

for tournament in tournaments:
    decks = getmelee.getBestEight.get_meleedecklist(tournament)
    print(decks)
    for decklist in decks:
        main_decklist_mtgmelee.get_and_postlist(decklist)
