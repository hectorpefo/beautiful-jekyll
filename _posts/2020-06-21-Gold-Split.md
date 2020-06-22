---
layout: post
published: true
title: Gold Split
date: 2020-06-21
---

>What is the smallest $N$ such that the set of the first $N$ cubes can be partitioned into $K$ subsets whose sums are equal?

<!--more-->

(See the original framing in terms of golden orbs at [fivethirtyeight](https://fivethirtyeight.com/features/can-you-flip-the-magic-coin/))

## Solution

My approach is not only computational, but pretty brute-force to boot: for each number $K$ of subsets, we step through the sets of the first $N$ cubes, and search the tree of partial assignments of cubes to partitions until we find a complete assignment to $K$ same-sum subsets.

On my PC, this code finds the solution for $K$ up to $8$ in about $72$ minutes: $1, 12, 23, 24, 24, 35, 41, 47$.

I'll be curious to see if there are analytic approaches to this. I'm sure there are at least more efficient computational ones, given that puzzle author Dean Ballard [has determined](http://oeis.org/A330212) values up to at least $N = 10$.

```python
import time

# Returns True if arr can be  
# partitioned into K subsets with equal sum
# Modified from a method found online:
# https://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/

def isEqualSumPartitionPossible(arr, K): 

  if (K == 1): 
      return True
    
  # If total number of partitions is more than N, or
  # array sum is not divisible by K, then a partition 
  # into equal-sum subsets is not possible  
  N = len(arr)
  if (N < K): 
      return False
  sum = 0
  for i in range(N): 
      sum += arr[i]  
  if (sum % K != 0): 
      return False

  targetSum = sum // K

  # initialize first subset sum as   
  # last element of array and mark that as taken 
  subsetSums = [0] * K  
  taken = [0] * N  
  subsetSums[0] = arr[N - 1]  
  taken[N - 1] = True

  # We avoid explicit recursion to hopefully save a
  # little runtime, using a state stack instead.
  # [Actual result: no time savings.]
  stack = [[subsetSums,taken,0,N-1]]
  while not stack == [] :
    subsetSums,taken,curIdx,limitIdx = stack.pop()
    if subsetSums[curIdx] == targetSum: 
            
      # current index (K - 2) means we've found
      # (K - 1) subsets of sum targetSum. Untaken 
      # numbers must then form the Kth.
      if (curIdx == K - 2): 
        return True
      
      # otherwise start next partition
      stack.append([list(subsetSums),list(taken),curIdx+1,N-1])
      continue

    # still adding to a partition. we start from limitIdx and add  
    # untaken elements into current partition
    for i in range(limitIdx, -1, -1): 
            
      if (taken[i]): 
        continue
      
      taken[i] = True
      subsetSums[curIdx] += arr[i]

      # if no greater than targetSum, add task to stack
      if (subsetSums[curIdx] <= targetSum):
        stack.append([list(subsetSums),list(taken),curIdx,i-1])
                               
      # unmark the element and remove from sum as we move 
      # to previous element in arr  
      taken[i] = False
      subsetSums[curIdx] -= arr[i]
  return False
      
# Main loop
startTime = time.time()
K = 0
while True:
  K += 1
  arr = []
  N = 0
  while True:
    N += 1
    arr.append(N**3)
    if (isEqualSumPartitionPossible(arr, K)): 
      print(K,N, "in", (time.time()-startTime))
      break
```

<br>