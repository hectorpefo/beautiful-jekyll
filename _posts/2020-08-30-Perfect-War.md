---
layout: post
published: true
title: Perfect War
date: 2020-08-30
---

>Assuming a deck is randomly shuffled before every game, how many games of War would you expect to play until you had a game that lasted just 26 turns?

[fivethirtyeight](https://fivethirtyeight.com/features/are-you-a-pinball-wizard/).

<!--more-->

## Solution

There are $52!$ different, equally likely deals. If we can find the number of match-free deals that result in a $26$-turn game, we can divide the former by the latter number to get our answer (which is the inverse of the probability of getting a $26$-turn game).

Most match-free deals do not result in a perfect game, because player 1 wins some hands while player 2 wins others. However, there is a simple relation between the total number of match-free hands and the total number of perfect ones: there are two perfect hands one among $2^26$ hands that see the same pair of cards every hand (but differ as to which player gets which card in some hands).

We will use a recurrence to calculate the number of match-free, perhaps partial deals that lead to a given game state, where a state lists the number of card values of which just one remains, two remain, and so on. So we'll use $M(a_1,a_2,a_3,a_4)$, or $M(\mathbf{a})$, to mean the number of match-free deals that get you to $\mathbf{a}$, starting from $(0,0,0,13)$. Our goal is to find $M(0,0,0,0)$, the number of match-free deals of the whole deck. Of course $M(0,0,0,13)$ is $1$.

We can calculate values of $M(\mathbf{a})$ from those of $M$ at preceding states. $M(\mathbf{a})$ is a sum: for each $\mathbf{a^p}$ that describes a possible preceding state to $\mathbf{a}$, we count all ways in which we can match-freely reach $\mathbf{a}$ from $\mathbf{a^p}$, and include the product of that count and $M(\mathbf{a^p})$ in $M(\mathbf{a})$. If we let $P(\mathbf{a})$ name the set of possible predecessor states to $\mathbf{a}$, and $W(\mathbf{a^p},\mathbf{a})$ count the number of ways of getting from one to the next state by dealing two among the remaining cards, then:

$$M(\mathbf{a}) =
\sum_{\mathbf{a^p} \in P(\mathbf{a})} 
M(\mathbf{a^p}) W(\mathbf{a^p},\mathbf{a})$$

Suppose we're calculating $M(3,3,1,2)$. One possible preceding state is $(4,3,2,2)$. To get to the new state without matching, we can choose any of the $6$ cards in the three-of-the-value group and any of the $6$ in the two-of-the-value group, and distribute these two cards in either of the two possible ways. So the number of ways of arriving match-freely at $(3,3,1,2)$ having previously been at $(4,3,2,2)$ is $72 \cdot M(4,3,3,2)$.

The code below implements this, yielding an expectation of $159,620,171$ deals!

```python
from math import factorial

# Return number of ways to deal matchlessly from a state [a,b,c,d] where
# among remaining cards are a,b,c,d card values with 1,2,3,4 each to
# final state [0,0,0,0]
def matchFreeDealsFrom (state):
	global alreadyDone
	if state in alreadyDone:
		return alreadyDone[state]
	totalWaysFromHere = 0
	# index of player 1's next card
	for i in range(4):
		if state[i] == 0:
			continue
		# choose among i+1 cards each of state[i] values
		choicesOfPlayer1Card = (i + 1) * state[i]
		stateAfterPlayer1 = list(state)
		stateAfterPlayer1[i] -= 1
		if i > 0:
			stateAfterPlayer1[i-1] += 1
		player1CardValueNowAt = i - 1
		# index of player 2's card
		for j in range(4):
			if (stateAfterPlayer1[j] == 0) or (stateAfterPlayer1[j] == 1 and player1CardValueNowAt == j):
				continue
			if player1CardValueNowAt == j:
				choicesOfPlayer2Card = (j + 1) * (stateAfterPlayer1[j] - 1)
			else:
				choicesOfPlayer2Card = (j + 1) * stateAfterPlayer1[j]
			stateAfterPlayer2 = list(stateAfterPlayer1)
			stateAfterPlayer2[j] -= 1
			if j > 0:
				stateAfterPlayer2[j-1] += 1
			choicesOfBothCards = choicesOfPlayer1Card * choicesOfPlayer2Card
			totalWaysFromHere += choicesOfBothCards * matchFreeDealsFrom(tuple(stateAfterPlayer2))
	alreadyDone[state] = totalWaysFromHere
	return totalWaysFromHere

alreadyDone = { (0,0,0,0) : 1 }
numCardValues = 13

numMFDeals = matchFreeDealsFrom((0,0,0,numCardValues))
numPerfectDeals = numMFDeals/(2**(2*numCardValues-1))
print("Number of match-free deals:", numMFDeals)
print("Number of perfect deals",numPerfectDeals)
totDeals = factorial(4*numCardValues)
print("Total number of deals:",totDeals)
probMF = numMFDeals/totDeals
print("Probability of a match-free deal:", probMF)
print("Expected deals until a match-free one:", 1/probMF)
probPerfect = numPerfectDeals/totDeals
print("Probability of a perfect deal:", probPerfect)
print("Expected deals until a perfect one:", 1/probPerfect)
```

```
Number of match-free deals: 16955496445780676751668866346010770786368985164896766506565632000000
Number of perfect deals 5.053131713205778e+59
Total number of deals: 80658175170943878571660636856403766975289505440883277824000000000000
Probability of a match-free deal: 0.2102142332112751
Expected deals until a match-free one: 4.757051816729048
Probability of a perfect deal: 6.2648723486445885e-09
Expected deals until a perfect one: 159620171.7049113
[Finished in 0.3s]
```

<br>
