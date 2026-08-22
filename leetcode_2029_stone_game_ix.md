# LeetCode 2029: Stone Game IX

- **Difficulty:** Medium
- **Tags:** Game Theory, Math, Greedy, Array
- **Video Reference:** [Leetcode Daily - 2029. Stone Game IX](https://www.youtube.com/watch?v=4MRFDQtxGTk)

---

## Problem Statement

Alice and Bob play a game with an array of positive integers `stones`.
- Alice goes first.
- On each turn, a player chooses and removes a stone.
- If the **sum of all removed stones is divisible by 3**, the player who made that move **loses immediately**.
- If all stones are removed and the sum was never divisible by 3, **Bob wins**.
- Both players play optimally. Return `true` if Alice wins, or `false` if Bob wins.

---

## Key Game Theory Insights

### 1. Modulo 3 Equivalence
The absolute values of stones do not matter, only their remainder modulo 3:
- **Type 0:** `val % 3 == 0`
- **Type 1:** `val % 3 == 1`
- **Type 2:** `val % 3 == 2`

Count the occurrences of each: `cnt0`, `cnt1`, and `cnt2`.

### 2. The Role of Type 0 ("Turn Skippers")
- Playing a Type 0 stone adds 0 to the sum modulo 3, maintaining the current valid sum state while flipping whose turn it is.
- **Even number of Type 0 stones (`cnt0 % 2 == 0`):**
  - Pairs of Type 0 stones cancel each other out.
  - Alice wins if and only if she has both Type 1 and Type 2 stones available to start and steer the game:
    $$\text{cnt0} \pmod 2 == 0 \implies \text{cnt1} \ge 1 \land \text{cnt2} \ge 1$$
- **Odd number of Type 0 stones (`cnt0 % 2 == 1`):**
  - Leaves 1 net turn skip, which flips the parity of the game.
  - Alice needs a large imbalance between Type 1 and Type 2 stones to overwhelm Bob and force him into an invalid sum:
    $$\text{cnt0} \pmod 2 == 1 \implies |\text{cnt1} - \text{cnt2}| > 2$$

---

## Code Implementations

### Python 3

```python
class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for val in stones:
            rem = val % 3
            if rem == 0:
                cnt0 += 1
            elif rem == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
        return abs(cnt1 - cnt2) > 2
```

### Java

```java
class Solution {
    public boolean stoneGameIX(int[] stones) {
        int cnt0 = 0, cnt1 = 0, cnt2 = 0;
        for (int val : stones) {
            int rem = val % 3;
            if (rem == 0) cnt0++;
            else if (rem == 1) cnt1++;
            else cnt2++;
        }

        if (cnt0 % 2 == 0) {
            return cnt1 >= 1 && cnt2 >= 1;
        }
        return Math.abs(cnt1 - cnt2) > 2;
    }
}
```

### C++

```cpp
#include <vector>
#include <cmath>

class Solution {
public:
    bool stoneGameIX(std::vector<int>& stones) {
        int cnt0 = 0, cnt1 = 0, cnt2 = 0;
        for (int val : stones) {
            int rem = val % 3;
            if (rem == 0) cnt0++;
            else if (rem == 1) cnt1++;
            else cnt2++;
        }

        if (cnt0 % 2 == 0) {
            return cnt1 >= 1 && cnt2 >= 1;
        }
        return std::abs(cnt1 - cnt2) > 2;
    }
};
```

### JavaScript / TypeScript

```javascript
/**
 * @param {number[]} stones
 * @return {boolean}
 */
var stoneGameIX = function(stones) {
    let cnt0 = 0, cnt1 = 0, cnt2 = 0;
    for (const val of stones) {
        const rem = val % 3;
        if (rem === 0) cnt0++;
        else if (rem === 1) cnt1++;
        else cnt2++;
    }

    if (cnt0 % 2 === 0) {
        return cnt1 >= 1 && cnt2 >= 1;
    }
    return Math.abs(cnt1 - cnt2) > 2;
};
```

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ — Linear scan over the stones array.
- **Space Complexity:** $\mathcal{O}(1)$ — Constant space (3 integer counters).
