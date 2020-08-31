---
layout: post
published: true
title: Perfect War
date: 2020-08-30
---

>Assuming a deck is randomly shuffled before every game, how many games of War would you expect to play until you had a game that lasted just 26 turns?

[fivethirtyeight](https://fivethirtyeight.com/features/are-you-a-pinball-wizard/).

<!--more-->

## Solutionish Musings

There are $52!$ different, equally likely deals. If we can find the number of match-free deals, which result in a $26$-turn game, we can divide the former by the latter number to get our answer (which is the inverse of the probability of getting a $26$-turn game).

We will use a recurrence to calculate the number of match-free, perhaps partial deals that lead to a given game state, where a state lists the number of card values of which just one remains, two remain, and so on. So we'll use $M(a_1,a_2,a_3,a_4)$, or $M(\mathbf{a})$, to mean the number of match-free deals that get you to $\mathbf{a}$, starting from $(0,0,0,13)$. Our goal is to find $M(0,0,0,0)$, the number of match-free deals of the whole deck. Of course $M(0,0,0,13)$ is $1$.

We can calculate values of $M(\mathbf{a})$ from those of $M$ at preceding states. $M(\mathbf{a})$ is a sum: for each $\mathbf{a^p}$ that describes a possible preceding state to $\mathbf{a}$, we count all ways in which we can match-freely reach $\mathbf{a}$ from $\mathbf{a^p}$, and include the product of that count and $M(\mathbf{a^p})$ in $M(\mathbf{a})$. If we let $P(\mathbf{a})$ name the set of possible predecessor states to $\mathbf{a}$, and $W(\mathbf{a^p},\mathbf{a})$ count the number of ways of getting from one to the next state by dealing two among the remaining cards, then:

$$M(\mathbf{a}) =
\sum_{\mathbf{a^p} \in P(\mathbf{a})} 
M(\mathbf{a^p}) W(\mathbf{a^p},\mathbf{a})$$

Suppose we're calculating $M(3,3,1,2)$. One possible preceding state is $(4,3,2,2)$. To get to the new state without matching, we can choose any of the $6$ cards in the three-of-the-value group and any of the $6$ in the two-of-the-value group, and distribute these two cards in either of the two possible ways. So the number of ways of arriving match-freely at $(3,3,1,2)$ having previously been at $(4,3,2,2)$ is $72 \cdot M(4,3,3,2)$.

The code below is meant to implement this, and it gets correct answers for small states (e.g., $384$ ways forward from $(0,3,0,0)$), but gives a crazy result for $(0,0,0,13)$, far greater than $52!$. Any debugging help would be most appreciated!

The expectation seems to be roughly proportional to the log of the number of card values in the deck.  Maybe that's a worthy echo of Euler's amazing result about the somewhat similar, but evidently importantly different, [Game of Coincidence](http://eulerarchive.maa.org/hedi/HEDI-2004-09.pdf).

![straightish-line plot with log y-axis](/img/PerfectWar.jpg)

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
				choicesOfBothCards = choicesOfPlayer1Card * (j + 1) * (stateAfterPlayer1[j] - 1)
			else:
				choicesOfBothCards = choicesOfPlayer1Card * (j + 1) * stateAfterPlayer1[j]
			stateAfterPlayer2 = list(stateAfterPlayer1)
			stateAfterPlayer2[j] -= 1
			if j > 0:
				stateAfterPlayer2[j-1] += 1
			totalWaysFromHere += choicesOfBothCards * matchFreeDealsFrom(tuple(stateAfterPlayer2))
	alreadyDone[state] = totalWaysFromHere
	return totalWaysFromHere

alreadyDone = { (0,0,0,0) : 1 }
numCardValues = 2
# for numCardValues in range(2,101):
# 	numMFDeals = matchFreeDealsFrom((0,0,0,numCardValues))
# 	print(numCardValues,",",factorial(4*numCardValues)/numMFDeals)

#
numMFDeals = matchFreeDealsFrom((0,0,0,13))
print("Number of match-free deals:", numMFDeals)
print("Probability of a match-free deal:", numMFDeals/factorial(4*numCardValues))
print("Expected deals until a match-free one:", factorial(4*numCardValues)/numMFDeals)

```

```
Number of match-free deals: 16955496445780676751668866346010770786368985164896766506565632000000
Probability of a match-free deal: 4.205232253417827e+62
Expected deals until a match-free one: 2.377989941428905e-63
[Finished in 0.3s]
```

<br>
