---
layout: post
published: true
title: Catch Yertle
date: 2020-07-17
---

>The tortoise and the hare are about to begin a 10-mile race along a “stretch” of road. The tortoise is driving a car that travels 60 miles per hour, while the hare is driving a car that travels 75 miles per hour. (For the purposes of this problem, assume that both cars accelerate from 0 miles per hour to their cruising speed instantaneously.)
>
>The hare does a quick mental calculation and realizes if it waits until two minutes have passed, they’ll cross the finish line at the exact same moment. And so, when the race begins, the tortoise drives off while the hare patiently waits.
>
>But one minute into the race, after the tortoise has driven 1 mile, something extraordinary happens. The road turns out to be magical and instantaneously stretches by 10 miles! As a result of this stretching, the tortoise is now 2 miles ahead of the hare, who remains at the starting line.
>
>At the end of every subsequent minute, the road stretches by 10 miles. With this in mind, the hare does some more mental math.
>
>How long after the race has begun should the hare wait so that both the tortoise and the hare will cross the finish line at the same exact moment?

[(fivethirtyeight)](https://fivethirtyeight.com/features/can-the-hare-beat-the-tortoise/)

<!--more-->

## Solution

The key effect of the growing road is that it decreases the runners' velocities relative to the road's length. For instance, the tortoise runs at $1$ mile per minute, or, equivalently, $1$ tenth of a road-length per minute. After the first minute, the pace still is $1$ mile per minute, but now is half of a tenth of a a road-length per minute. So we can equivalently consider an unchanging, ten-mile road with diminishing velocities: at (integer) minute $m$, each runner's pace is reduced by the multiplicative factor $\frac{m}{m+1}$. So between times $m$ and $m+1$, the tortoise's pace in miles per minute is:

$$v_m = \prod_{i=1}^m \frac{i}{i+1} = \frac{1}{m+1}$$

Letting $T_m$ be the position of the tortoise at the end of minute $m$, we have:

$$T_0 = 0$$

$$T_{m+1} = T_m + v_m$$

$$T_{m} = \sum_{i=1}^m \frac{1}{i}$$

Thus the tortoise's positions at integer minutes form the partial sums of the [harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)), which are also called harmonic numbers. Since the harmonic numbers grow approximately logarithmically, we know that the tortoise will get to $10$ miles eventually. 

When the hare is running, its pace is always $5/4$ of that of the tortoise, and so it covers $5/4$ of the distance the tortoise covers during that time. Therefore the hare needs to start running the full $10$ miles when the tortoise reaches mile $2$, with $8$ miles to go (or in the original, when it reaches $.2$ of whatever the road length is at that point). When will that be?

The least harmonic number greater than or equal to $2$ is the fourth, namely $25/12$, and so the tortoise will reach mile $2$ in under $4$ minutes. Since the tortoise has been running at $1/4$ mile per minute at that point, the time it takes to get from $2$ miles to $25/12$ miles is $(1/12)/(1/4)$, or $1/3$ of a minute. Therefore the hare must start running at $3$ minutes and $40$ seconds into the race. 

We can calculate the total race duration in the same way. As can be computed easily (or [looked up](https://oeis.org/A004080)), the least harmonic number greater than or equal to $10$ is $H_{12367}$, and at minute $12367$, the tortoise has been running at $1/12367$ miles per minute. So the race duration is:

$$12367 - \frac{H_{12367} - 10}{\frac{1}{12367}} \approx 12366.468$$

That's $8$ days, $14$ hours, $6$ minutes, and about $28.087$ seconds. Which is a long time to run.

<br>