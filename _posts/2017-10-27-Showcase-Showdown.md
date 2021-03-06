---
layout: post
published: true
title: Showcase Showdown
date: 2017-10-27
---

>On the brilliant and ageless game show “The Price Is Right,” there is an important segment called the Showcase Showdown. Three players step up, one at a time, to spin an enormous, sparkling wheel. The wheel has 20 segments at which it can stop, labeled from five cents up to one dollar, in increments of five cents. Each player can spin the wheel either one or two times. The goal is for the sum of one’s spins to get closer to one dollar than the other players, without going over. (Any sum over a dollar loses. Ties are broken by a single spin of the wheel, where the highest number triumphs.)
>
>For what amounts should the first spinner stop after just one spin, assuming the other two players will play optimally?

<!--more-->

## Solution

(A picky point to start with: that's not Showcase Showdown, but The Wheel.  Showcase Showdown is where the contestants guess the price of a Showcase of merchandise, the winner being the closest guess that is not over the actual price.)

We'll work backwards, first figuring out player $3$'s probability of winning given what she has witnessed, including her first spin, then the probability that one of players $2$ and $3$ win given player $1$'s score and player $2$'s first spin, and finally player $1$'s probabilities of winning if she holds and if she spins, given the value of her first spin.

Let $H$ be the highest score so far when player $3$ spins (a player has score zero if they bust), let her first spin have value $C$, and let $t$ be $1/3$ if the first two players are currently in a tie, and $1/2$ otherwise ($t$ represents the chance that player $3$ wins if she is in a tie-break). Then, if $C>H$, which has probability $1-H$, she holds and wins with probability $1$. If $C<H$, which has probability $\max(0,H-.05)$, she spins and has probability $.05$ of a tie (and then probability $t$ of winning the tie-break), and probability $1-H$ of an outright win. And if $C=H$, which has probability $.05$, if $H > 1-t$, she holds and has probability $t$ of winning the tie-break, and if $H\leq 1-t$ she spins and has probability $1-H$ of winning outright.

So we can express player $3$'s chance of winning as follows:

$$P_3(H,t) = (1-H) + (H-.05)(.05t + 1 - H) + \max(t,1-H)$$

Let $A$ be player 1's score, and let $B_1$ be the value of player $2$'s first spin.  We will calculate the probability $P_{2,3}(A,B_1)$, that one of players $2$ and $3$ will go on to win.

First, suppose $B_1<A$. Then player $2$ must spin; call his new total score $B_2$. If $B_2<A$, which happens with probability $\max(0,A-.05-B1)$, then player $3$ has probability $P_3(A,.5)$ of winning. If $B_2=A$, and there is probability $.05$ of that, then there's probability $P_3(A,1/3)$ that player $3$ wins, and probability $.5 \times (1-P_3(A,1/3))$ that player $2$ wins in a tie-break. If $1\geq B_2>A$, and there's probability $.05$ of that for each of the $(1-A)/.05$ possible values of $B_2$ from $A+.05$ to $1$, then there is certainty that one of players $2$ and $3$ will win. And if $B_2>1$, and there's probability $B_1$ of that, then player $3$ has probability $P_3(A,.5)$ of winning. This lets us calculate $P_{2,3}(A,B_1\ \&\ B_1<A)$.

Second, suppose $B_1>A$. If player $2$ holds, he'll have probability $1-P_3(B_1,.5)$ of winning, and player $3$ will have $P_3(B_1,.5)$. If he spins, then, calling his new total $B_2$, there's probability $.05$ of each value of $B_2$ between $B_1+.05$ and $1$, and for each of those he has probability $1-P_3(B_2,.5)$ of winning, and player $3$ has probability $P_3(B_2,.5)$; and if $B_2>1$, and there's probability $B_1$ of that, then player $3$ has probability $P_3(A,.5)$ of winning. This lets us calculate $P_{2,3}(A,B_1\ \&\ B_1>A)$ as the hold or spin total that includes the greatest probability of player $2$ winning.

Finally, suppose $B_1=A$. Then if player $2$ holds, player $3$ has probability $P_3(A,1/3)$ of winning and player $2$ has probability $(1/2)(1-P_3(A,1/3))$. And if he spins, then, calling the new total $B_2$, for each value of $B_2$ between $A+.05$ and $1$, he has probability $.05\times (1-P_3(B_2,.5))$ of winning; and if $B_2>1$, and there's probability $B_1$ of that, then player $3$ has probability $P_3(A,.5)$ of winning. Again $P_{2,3}(A,B_1\ \&\ B_1=A)$ is calculated based on whether holding or spinning is best for player $2$. 

Because the three cases partition the possibilities,

$$P_{2,3}(A,B_1) = P_{2,3}(A,B_1\ \&\ B_1<A) + P_{2,3}(A,B_1\ \&\ B_1>A) + P_{2,3}(A,B_1\ \&\ B_1=A)$$

Player $1$, with first spin value $A_1$, now has a straightforward calculation. If she holds, then there's probability $.05$ that $B_1$ will be each of the possible values, so her chance of winning is the average of the values of $(1-P_{2,3}(A_1,B_1))$. And if she spins, for each of the values of $A_2$ between $A_1+.05$ and $1$ she has a chance of $.05$ of landing on that value and then having the probability of winning that she'd have had if her first spin had had that value and she were to have held. 

The upshot is that, when her first spin is $.65$ or below, it pays to spin, and when $.70$ or above, it pays to hold. But the first player is already in an unfortunate position, having less than a $31$ percent chance of winning if everyone plays optimally.

[There's enough algebra here that there's a good chance a mistake or two has crept in; thanks for any corrections!]

### Code (Python)

```python
P3 = {}
for i in (2,3):
	t = 1.0/i
	for j in range(21):
		H = j*.05
		P3[(j,i)] = (1-H) + max(0,(H-.05))*(.05*t + (1-H)) + .05*max(t,1-H)
P23 = {}
for i in range(21):
	A = i*.05
	for j in range(1,21):
		B1 = j*.05
		if B1 < A:
			P23[(i,j)] = (max(0,A-.05-B1))*P3[(i,2)] + .05*(P3[(i,3)] + .5*(1-P3[(i,3)])) + (1-A) + B1*P3[(i,2)]
		else:
			if B1 > A:
				Holds = 1-P3[(j,2)]
			elif B1 == A:
				Holds = .5*(1-P3[(j,3)])
			Spins = 0
			for k in range(j+1,21):
				Spins += .05*(1-P3[(k,2)])
			if Holds > Spins:
				if B1 > A:
					P23[(i,j)] = Holds + P3[(j,2)]
				elif B1 == A:
					P23[(i,j)] = Holds + P3[(j,3)]
			else:
				P23[(i,j)] = Spins
				for k in range(j+1,21):
					P23[(i,j)] += .05*P3[(k,2)]
				P23[(i,j)] += B1*P3[(i,2)]
print "First Spin, P(Win if Hold), P(Win if Spin):"
for h in range(1,21):
	Holds = 0
	for j in range(1,21):
		Holds +=  .05*(1-P23[(h,j)])
	Spins = 0
	for i in range(h+1,21):
		for j in range(1,21):
			Spins += .05*.05*(1-P23[(i,j)])
	print h*.05, Holds, Spins
```

Output:

```
First Spin, P(Win if Hold), P(Win if Spin):
0.05 0.00034375 0.2059465625
0.1 0.00121458333333 0.205885833333
0.15 0.00285208333333 0.205743229167
0.2 0.005396875 0.205473385417
0.25 0.00906458333333 0.20502015625
0.3 0.0141458333333 0.204312864583
0.35 0.02100625 0.203262552083
0.4 0.0300864583333 0.201758229167
0.45 0.0419020833333 0.199663125
0.5 0.05704375 0.1968109375
0.55 0.0834583333333 0.192638020833
0.6 0.118289583333 0.186723541667
0.65 0.1631875 0.178564166667
0.7 0.21563125 0.167782604167
0.75 0.284158333333 0.1535746875
0.8 0.368177083333 0.135165833333
0.85 0.4699 0.111670833333
0.9 0.591689583333 0.0820863541667
0.95 0.736058333333 0.0452834375
1.0 0.90566875 0
[Finished in 0.1s]
```

<br>
