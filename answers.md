# CMPS 2200 Assignment 3
## Answers

**Name:** Dylan Mondrus


Place all written answers from `assignment-03.md` here for easier grading.

Part 1

1a). To produce as few coins as possible, use this algorithm: Have an empty list coins = []. 
While N > 0,
 - Find the largest 2^k such that 2^k <= N. 
 - Subtract 2^k from N
 - Add 2^k to coins
 Repeat until N = 0.
 Return the list. 

1b). The greedy choice(picking the largest coin <= N) is optimal because 2^k is the appropriate denominatin for the exchange. A coin of size 2^k aims to get the largest denomination as long as it is not larger than N. This reduces the number of coins used as much as possible and is therefore optimal. Additionally, it is optimal by the optimal substructure properties because each step reduces N to N - 2^k. Each step is optimal as proved by the greedy choice proof. Therefore, since every step is optimal, the whole algorithm is optimal .

1c). The work is O(log N), the span is O(log N). 

Part 2

2a). An example of the greedy algorithm not working in Fortuito is as follows: 
Say Fortuito has denominations of 1, 3, 4. And you want to make change for N = 6. 
Using the greedy algorithm, you pick the 4 denomination, so you're left with 2 coins. Then you take 1 coin, and then 1 coin, for a total of 3 coins. This is not optimal. Instead, you could have used the 3 denomination twice for a total of 2 coins. This shows the greedy algorithm is not optimal in Fortuito. 

2b). This problem can still be proven to have an optimal substructure property. Let C(N) be the minimum number of coins for N dollars using the set of denominations D = {D0, D1, ... , Dk}. In other words, let C(N) be the optimal number of coins for N dollars and D denominations. Therefore, after every stepn C(N) = N - D, or C(N - D). If every step is optimal, then the whole algorithm is optimal based on the substructure property. 

2c). 
Have a list DP of size N+1, where DP[i] stores the minium number of coins needed to make amount i. 
Set DP[0] = 0.
Set all other DP[i] = infinity.
For each amount i from 1 to N:
    - For each coin value c in the list of denominations:
        if i - c >= 0 and DP[i -c] is not infinity:
            Set DP[i] = min(DP[i], DP[i - c] + 1)
After filling in the table:
    - If DP[N] is still infinity, return "Not possible to make change"
    - Otherwise, return DP[N] as the minimum number of coins
