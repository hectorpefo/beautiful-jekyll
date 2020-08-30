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

The code below does this for every possible match-free deal. I believe (or hope) that it is correct. But unfortunately, even though it is not so brute-force as to enumerate all match-free deals, it is far too inefficient to produce an answer in a reasonable runtime. (Hey, we're doing mathematics, not engineering? If correct, it gives you the answer in nothing flat when run, in the words of the late Jon Barwise, at the speed of logic.) It at least clarifies the functions $P$ and $W$.

The expectation seems to be roughly proportional to the log of the number of card values in the deck. Projecting on that basis, we might expect about 165,718,000 deals before a match-free game with a standard deck. Maybe that's a worthy echo of Euler's amazing result about the somewhat similar, but apparently importantly different, [Game of Coincidence](http://eulerarchive.maa.org/hedi/HEDI-2004-09.pdf).

![straightish-line plot with log y-axis](/img/PerfectWar.jpg)

```python
from math import factorial

# Return number of ways to deal match-freely from a state [a,b,c,d] where
# among remaining cards are a,b,c,d card values with 1,2,3,4 cards to
# final state [0,0,0,0]
def match-freeDealsFrom (state):
	if state == [0,0,0,0]:
		return 1
	totalWaysHere = 0
	for i in range(4):
		# index of first card dealt to get here
		newState = list(state)
		if newState[i] == 0:
			continue
		waysHere = (i + 1) * newState[i]
		newState[i] -= 1
		if i > 0:
			newState[i-1] += 1
		firstValueAt = i - 1
		for j in range(4):
			if newState[j] == 0 or (newState[j] == 1 and firstValueAt == j):
				continue
			if j == firstValueAt:
				waysHere *= (j + 1) * (newState[j] - 1)
			else:
				waysHere *= (j + 1) * newState[j]
			newState[j] -= 1
			if j > 0:
				newState[j-1] += 1
			totalWaysHere += waysHere * match-freeDealsFrom(newState)
	return totalWaysHere

for n in range(2,14):
	print(n,",",factorial(4*n)/match-freeDealsFrom([0,0,0,n]))
```

<br>
