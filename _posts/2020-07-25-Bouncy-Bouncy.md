---
layout: post
published: true
title: Bouncy Bouncy
date: 2020-07-25
---

>For the problem statement, see the post at [fivethirtyeight](https://fivethirtyeight.com/features/are-you-a-pinball-wizard/).

<!--more-->

## Solution

Here's a rather hand-wavey argument to "show" that it's possible to achieve infinitely many bounces.

We'll focus on possible ball paths that at some point hit the very top of the circle. Since the "physics" here is time-reversal invariant, we can think of the ball as starting there and at some point reaching the "start." If we aim straight up, obviously there will be infinitely many bounces, but the ball will never reach the start. If we aim very slightly left, there will be a lot of bounces, but eventually the ball will bounce for the last time, either on the circle or on the wall. A small adjustment of the initial angle [waves hands] will ensure that the last bounce is on the wall, and that after that bounce the ball crosses the start. There is nothing preventing this strategy from producing arbitrarily many bounces: more bounces as the initial angle approaches straight up. Now consider those paths in reverse, that is, starting from the start, reaching the top of the circle after a lot of bounces, and then proceding symmetrically with the same number of bounces to the right of center. From the start, the initial angle to the first bounce on the wall is steeper the greater the number of bounces. But obviously that angle is bounded, given that straight-up produces just one bounce. Therefore, it approaches a limit $\theta$ as the number of bounces increases. For angles steeper than $\theta$, the ball never makes it to the top of the circle, but reverses its horizontal direction after some number of bounces, the closer to $\theta$, the greater that number. For any number $n$ of bounces, however large, there is a small enough window around $\theta$ such that all angles in that window produce at least $n$ bounces. Surely, then, [waves hands] $\theta$ itself must produce infintely many bounces and, while the ball will approach the top of the circle, it will never reach it. (The value of $\theta$ is left as an exercise for the reader.)

<br>
