#!/usr/bin/env python

from random import shuffle
from math import ceil

#Define the list of suits so we can experiment
SUITS = (4, 6, 8, 10, 12, 14)

#What fraction of a suit's cards need to be dealt for the suit to win
#Fractions are rounded up, so read as "at least WIN_RATIO"
WIN_RATIO = 1 / 3

#How many hands to play (should really be a command-line argument)
HANDS = 10000

#Initialize some variables
winner = None
hand = []
winners = []

def BuildDeck(suits):
#This function only exists to save us typing if we try different sets of suits
	deck = []

	#For each suit, add that many cards to the deck
	for suit in suits:
		for i in range(1, suit + 1):	#range() goes from 0 to N-1 by default
			deck.append(suit)
	return deck

def PlayHand(deck):
	count = {}
	hand = []

	while True:	#This is a hacky way to avoid writing a proper UNTIL loop
		#Take the top card
		suit = deck.pop()

		#Add it to the cards dealt this hand
		hand.append(suit)

		#If the hand now has all the cards of this card's suit, this suit wins
		if hand.count(suit) == ceil(suit * WIN_RATIO):
			#Also return the whole hand in case we want to pick that apart
			return suit, hand

#Build a template for a fresh pack of cards for this game
DECK = BuildDeck(SUITS)

#This is the main loop
#We're playing all the hands
for i in range(1, HANDS + 1):
	#Crack open a fresh pack
	deck = list(DECK)	#The list() function creates a copy of DECK, a list object

	#The most intuitive line in here
	shuffle(deck)

	#Which suit won? What did the hand look like?
	#We're not actually doing anything with the hand record at this time
	winner, hand = PlayHand(deck)
	
	#Keep track of all the winners
	winners.append(winner)

#This is the results reporting loop
#We're printing how many times each suit won
for suit in SUITS:
	print(suit, winners.count(suit))
