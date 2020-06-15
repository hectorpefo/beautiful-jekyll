---
layout: post
published: true
title: Eternal Contagion
date: 2020-06-13
---

>You are studying a new strain of bacteria, Riddlerium classicum (or R. classicum, as the researchers call it). Each R. classicum bacterium will do one of two things: split into two copies of itself with probability $p$, or die. 
>
>If you start with a single R. classicum bacterium, what is the probability that it will lead to an everlasting colony?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/how-long-will-the-bacterial-colony-last/))

## Solution

Let $E$ be the event of eventual extinction. Eventual extinction is equivalent to the disjunctive event of either immediate extinction (with probability $(1-p)$), or (with probability $p$) an initial two offspring, both of whose lineages go extinct (with probability $P(E)^2$). This yields a quadratic equation in $P(E)$, namely:

$$P(E) = (1-p) + pP(E)^2$$

For $p < .5$, this has two solutions, only one of which is in range: extinction with probability $1$.

For $p>.5$, there are also two solutions, namely $1$ and $\frac{1}{p} - 1$, which is less than $1$ for these values of $p$. It turns out that the correct probability is the latter. But it will take a little work to show that.

Let $E_n$ be the event of there being extinction as of (or before) generation $n$. Then $P(E_0)$ is $0$, $P(E_1)$ is $(1-p)$, and (this will sound familiar) since $E_{n+1}$ is equivalent to the disjunctive event of $E_1$ (going extinct immediately) and the negation of $E_1$ (having two offspring) followed by two instances of $E_{n}$:

$$P(E_{n+1}) = (1-p) + pP(E_{n})^2$$

Let's use $F(x)$ to abbreviate this function of $P(E_n)$. Then we have:

$$F(x) = (1-p) + px^2$$

So:

$$P(E_n) = F^n(0)$$

(where $F^n(0)$ means $n$ nested applications of the function $F$.)

Let $q$ be the smaller solution to our quadratic equation for $p > .5$, namely, $1-\frac{1}{p}$. Since $q$ is a solution, we know that:

$$F(q) = q$$

Now:

$$0 \leq q$$

Since $F$ is an increasing function, it follows that:

$$F(0) \leq F(q) = q$$

$$F(F(0)) \leq F(q) = q$$

$$\cdots$$

$$ F^n(0) \leq q $$

$$ \lim_{n \rightarrow \infty} F^n(0) \leq q$$

$$ P(E) \leq q $$

Thus $P(E)$ must be $\frac{1}{p}-1$, and so the probability of eternal survival is $2 - \frac{1}{p}$.

<br>