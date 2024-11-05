### Problem and corresponding algorithms

1. [Tortoise and hare algorithm](https://github.com/sleepingcat4/niche-algo/blob/master/tortoise_hare.py) - 287. Find the Duplicate Number (LeetCode)

-> **reading material:** https://cp-algorithms.com/others/tortoise_and_hare.html

2. [Sliding window Algorithm + a freq counter](https://github.com/sleepingcat4/niche-algo/blob/master/sliding_window_freq.py) - 76 Minimum window substring (LeetCode)

It takes uses the traditional sliding window technique + a hash based frequency counter using the ```Counter``` module. ```inf``` means infinity. It uses two pointers to find out the window length where the valid characters are situated and then uses slice in return statement to get them back. 

-> **reading material:** https://medium.com/@anil.goyal0057/mastering-the-sliding-window-algorithm-with-practical-examples-in-java-67bc327469d3

3. [Invert Binary Tree](https://github.com/sleepingcat4/niche-algo/blob/master/invert_tree.py) - 226. Invert Binary Tree (LeetCode)

I used a BFS + queue combined algorithm to do the inversion. It's kinda neat and fun. 

-> **reading material:** https://en.wikipedia.org/wiki/Breadth-first_search 

4. [Pascal tri](https://github.com/sleepingcat4/niche-algo/blob/master/pascal.py) - 118 Pascal Triangle (LeetCode)

I did it in 0ms runtime on LeetCode. I used this formula \( C(n, k + 1) = C(n, k) \times \frac{n - k}{k + 1} \) to iteratively calculate from left to right to prevent duplication of work. 

-> **reading material:** https://www.britannica.com/science/Pascals-triangle#:~:text=Pascal's%20triangle%2C%20in%20algebra%2C%20a,but%20it%20is%20far%20older.

5. [Next permutation](https://github.com/sleepingcat4/niche-algo/blob/master/next_perm.py) - 31. Next Permutation

-> **reading material:** https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
