# 🧠 Striver's A2Z DSA Sheet – Python Solutions

This repository contains Python solutions categorized by topics from the [Striver's A2Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/). Progress is tracked with checkboxes ✅.

---

## 📈 Overall Progress

| Section        | Total Problems | Done | Pending |
|----------------|----------------|------|---------|
| Step 1: Basics | 21             | 17   | 4       |
| Step 2: Sorting| 5              | 5    | 0       |
| Step 3: Arrays | –              | –    | –       |
| ...            | ...            | ...  | ...     |



---

## 📚 Step 1: Learn the Basics

### 🧮 1.3: Maths

| ✅   | #  | Problem                | Platform                                                                 | Solution                                                        | Notes                     |
|------|----|------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------|---------------------------|
| [x]  | 1  | Count Digits            | [CN](https://www.codingninjas.com/studio/problems/count-digits_8416387) | [count_digits.py](Step1_Basics/1.3_Maths/count_digits.py)       | Use `%` and integer division |
| [x]  | 2  | Reverse Integer        | [LC](https://leetcode.com/problems/reverse-integer/)                    | [reverse_integer.py](Step1_Basics/1.3_Maths/reverse_integer.py) | Handle negatives and overflow |
| [x]  | 3  | Check Palindrome Number | [LC](https://leetcode.com/problems/palindrome-number/)                  | [palindrome_number.py](Step1_Basics/1.3_Maths/palindrome_number.py) | Reverse & compare          |
| [x]  | 4  | GCD / HCF               | [CN](https://www.codingninjas.com/studio/problems/gcd_8417285)          | [gcd.py](Step1_Basics/1.3_Maths/gcd.py)                         | Use Euclidean algorithm    |
| [ ]  | 5  | LCM                     | [CN](https://www.codingninjas.com/studio/problems/lcm_8417489)          | [lcm.py](Step1_Basics/1.3_Maths/lcm.py)                         | `lcm = (a*b)//gcd`         |
| [x]  | 6  | Check Armstrong Number  | [CN](https://www.codingninjas.com/studio/problems/check-armstrong_589)  | [armstrong.py](Step1_Basics/1.3_Maths/armstrong.py)             | Power of digits            |
| [x]  | 7  | Print All Divisors      | [CN](https://www.codingninjas.com/studio/problems/print-divisors_3608828)| [divisors.py](Step1_Basics/1.3_Maths/divisors.py)               | Up to √n optimization      |
| [ ]  | 8  | Check Prime             | [CN](https://www.codingninjas.com/studio/problems/prime-number_624934)  | [is_prime.py](Step1_Basics/1.3_Maths/is_prime.py)               | Trial division up to √n    |


### 🔁 1.4: Recursion

| ✅ | # | Problem | Platform | Solution | Notes |
|----|---|---------|----------|----------|-------|
| [ ] | 1 | Print Name N times | [CN](https://www.codingninjas.com/studio/problems/print-name-n-times_3625289) | [print_name_n_times.py](Step1_Basics/1.4_Recursion/print_name_n_times.py) | Simple base case recursion |
| [ ] | 2 | Print 1 to N | [CN](https://www.codingninjas.com/studio/problems/print-1-to-n_628290) | [print_1_to_n.py](Step1_Basics/1.4_Recursion/print_1_to_n.py) | Tail recursion |
| [ ] | 3 | Print N to 1 | [CN](https://www.codingninjas.com/studio/problems/print-n-to-1_628290) | [print_n_to_1.py](Step1_Basics/1.4_Recursion/print_n_to_1.py) | Base case-first |
| [ ] | 4 | Sum of first N numbers | [CN](https://www.codingninjas.com/studio/problems/sum-of-first-n-numbers_8876068) | [sum_of_n.py](Step1_Basics/1.4_Recursion/sum_of_n.py) | `sum = n + f(n-1)` |
| [ ] | 5 | Factorial of N | [LC](https://leetcode.com/problems/factorial-trailing-zeroes/) | [factorial.py](Step1_Basics/1.4_Recursion/factorial.py) | Classic recursive factorial |
| [ ] | 6 | Reverse an array | [CN](https://www.codingninjas.com/studio/problems/reverse-array_1232638) | [reverse_array.py](Step1_Basics/1.4_Recursion/reverse_array.py) | Two-pointer + recursion |
| [x] | 7 | Check Palindrome (Recursion) | [LC](https://leetcode.com/problems/valid-palindrome/) | [check_palindrome.py](Step1_Basics/1.4_Recursion/check_palindrome.py) | Compare first and last |
| [x] | 8 | Fibonacci Number | [LC](https://leetcode.com/problems/fibonacci-number/) | [fibonacci.py](Step1_Basics/1.4_Recursion/fibonacci.py) | Naive recursive solution |


### 🔐 1.5: Hashing

| ✅   | #  | Problem                 | Platform                                                                 | Solution                                                                 | Notes                            |
|------|----|-------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------|
| [x]  | 1  | Two Sum                 | [LC](https://leetcode.com/problems/two-sum/)                             | [two_sum.py](Step1_Basics/1.5_Hashing/two_sum.py)                         | Use hashmap for O(n) lookup      |
| [x]  | 2  | Valid Anagram           | [LC](https://leetcode.com/problems/valid-anagram/)                       | [valid_anagram.py](Step1_Basics/1.5_Hashing/valid_anagram.py)             | Count characters using hashmap   |
| [x]  | 3  | Group Anagrams          | [LC](https://leetcode.com/problems/group-anagrams/)                      | [group_anagrams.py](Step1_Basics/1.5_Hashing/group_anagrams.py)           | Use sorted tuple as key in map   |
| [x]  | 4  | Happy Number            | [LC](https://leetcode.com/problems/happy-number/)                        | [happy_number.py](Step1_Basics/1.5_Hashing/happy_number.py)               | Use set to detect cycles         |
| [x]  | 5  | Contains Duplicate      | [LC](https://leetcode.com/problems/contains-duplicate/)                  | [contains_duplicate.py](Step1_Basics/1.5_Hashing/contains_duplicate.py)   | Detect duplicates using a set    |

---

## 📚 Step 2: Learn Important Sorting Techniques

### 📂 2.1: Sorting – Part 1

| ✅   | #  | Problem                     | LeetCode Link                                                                 | Solution                                               | Notes                                  |
|------|----|-----------------------------|------------------------------------------------------------------------------|--------------------------------------------------------|----------------------------------------|
| [x]  | 1  | Bubble Sort                 | [Sort‑an‑Array](https://leetcode.com/problems/sort-an-array/)                | [bubble_sort.py](Step2_Sorting/2.1_Sorting/bubble_sort.py)         | Compare adjacent, O(n²) worst-case     |
| [x]  | 2  | Selection Sort              | [Sort‑an‑Array](https://leetcode.com/problems/sort-an-array/)                | [selection_sort.py](Step2_Sorting/2.1_Sorting/selection_sort.py)   | Select min, O(n²), stable improvement possible |
| [x]  | 3  | Insertion Sort              | [Sort‑an‑Array](https://leetcode.com/problems/sort-an-array/)                | [insertion_sort.py](Step2_Sorting/2.1_Sorting/insertion_sort.py)   | Build sorted subarray, O(n²)          |
| [x]  | 4  | Merge Two Sorted Arrays     | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)     | [merge_two_sorted.py](Step2_Sorting/2.1_Sorting/merge_two_sorted.py) | Two-pointer merge technique           |
| [x]  | 5  | Merge Sort (Recursion)      | [Sort‑an‑Array](https://leetcode.com/problems/sort-an-array/)                | [merge_sort.py](Step2_Sorting/2.1_Sorting/merge_sort.py)           | Divide & merge, O(n log n)            |


---

---

## 🧠 Time Complexity vs Input Size Guide

Use this chart to estimate the acceptable time complexity based on the input size `n`. It will help you choose the right approach for coding problems.

| Time Complexity | Handles Up To (n ≈) | Notes / Use Cases                            |
|------------------|---------------------|----------------------------------------------|
| O(1)             | Any size            | Constant-time operations                     |
| O(log n)         | 10⁸+                | Binary Search, Bit Manipulations             |
| O(n)             | 10⁷ – 10⁸           | Single pass loops                            |
| O(n log n)       | 10⁶ – 10⁷           | Efficient sorting (Merge Sort, Heap Sort)    |
| O(n²)            | 10³ – 10⁴           | Double loops, simple brute-force             |
| O(n³)            | 100 – 300           | Triple loops, basic dynamic programming      |
| O(2ⁿ)            | ≤ 20                | Backtracking, subset problems                |
| O(n!)            | ≤ 8 – 10            | Permutations, exhaustive search              |

### ⚡ Quick Tips

- If `n ≤ 10⁸` → Use **O(log n)** or better
- If `n ≤ 10⁶` → Go for **O(n log n)** or better
- If `n ≤ 10⁴` → **O(n²)** is acceptable
- If `n ≤ 100` → **O(n³)** is safe
- If `n ≤ 20` → **O(2ⁿ)** or bitmasking possible
- If `n ≤ 10` → Even **O(n!)** is fine

_Keep this table handy while planning your algorithm!_

---


---
## 📁 Folder Structure

