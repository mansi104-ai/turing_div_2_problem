## Title : Medical pixels problem
**Time limit:** 2 seconds  
**Memory limit:** 512 MB  

---

## Story

In a **medical imaging lab**, you are given a sequence of pixel intensity values extracted from a high-resolution MRI scan.  
To transmit the data efficiently, the lab uses a **Pixel Compression Tree (PCT)** — a special kind of Huffman-like tree, but with an additional **spatial penalty**.

Each pixel has an intensity value `a[i]`.  
You can think of `a[i]` as the frequency of occurrence of that pixel in a compressed grayscale region.

Normally, Huffman coding minimizes the sum of `freq * depth`, but in this system, there is also a **spatial connection penalty `p`** added each time two pixel groups are merged.

---

## Your Task

You need to build an **optimal Pixel Compression Tree** for the given pixels.

Each merge operation behaves as follows:

- Pick two groups with the **smallest combined cost**.  
- When merging groups with total weights `w1` and `w2`, the **merge cost** is:
n p
a1 a2 ... an


- `n` — number of pixels (2 ≤ n ≤ 2×10⁵)  
- `p` — spatial penalty (0 ≤ p ≤ 10⁹)  
- `a[i]` — intensity weight of the i-th pixel (1 ≤ a[i] ≤ 10⁹)

---

## Output Format

Print a single integer — the **minimum total compression cost**.

---

## Example 1

**Input**
4 3
5 2 8 3


**Output**
38


**Explanation**

Steps that lead to the optimal merge sequence:

1. Merge (2, 3): `cost = 2 + 3 + 3 = 8` → new node weight = 5  
   Remaining: [5, 5, 8]

2. Merge (5, 8): `cost = 5 + 8 + 3 = 16` → new node weight = 13  
   Remaining: [5, 13]

3. Merge (5, 13): `cost = 5 + 13 + 3 = 21`

**Total cost = 8 + 16 + 14 = 38**

---

## Example 2

**Input**
5 2
4 7 6 3 9

**Output**
59

## Hint

Think of a **Huffman tree**, but every merge also adds a fixed penalty `p`.  
Using a **min-heap (priority queue)** is essential.
