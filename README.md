# Striver's A2Z DSA Sheet – Python Solutions

Python solutions for [Striver's A2Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/). Progress is tracked below.

---


## Progress

| Section        | Total | Done | Pending |
|----------------|-------|------|---------|
| Step 1: Basics | 21    | 17   | 4       |
| Step 2: Sorting| 6     | 5    | 1       |
| Step 3: Arrays | –     | –    | –       |
| ...            | ...   | ...  | ...     |

---

## Step 1: Learn the Basics

### 1.3: Maths

| Status           | #  | Problem                | Platform                                                                 | Solution                                                        | Notes                     |
|------------------|----|------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------|---------------------------|
| - [x]   | 1  | Count Digits           | [CN](https://www.codingninjas.com/studio/problems/count-digits_8416387)  | [Step1_Basics/1.3_Maths/count_digits.py](Step1_Basics/1.3_Maths/count_digits.py)       | Use `%` and integer division |
|  - [x]    | 2  | Reverse Integer        | [LC](https://leetcode.com/problems/reverse-integer/)                     | [Step1_Basics/1.3_Maths/reverse_integer.py](Step1_Basics/1.3_Maths/reverse_integer.py) | Handle negatives and overflow |
|  - [x]    | 3  | Check Palindrome Number| [LC](https://leetcode.com/problems/palindrome-number/)                   | [Step1_Basics/1.3_Maths/palindrome_number.py](Step1_Basics/1.3_Maths/palindrome_number.py) | Reverse & compare          |
|  - [x]    | 4  | GCD / HCF              | [CN](https://www.codingninjas.com/studio/problems/gcd_8417285)           | [Step1_Basics/1.3_Maths/gcd.py](Step1_Basics/1.3_Maths/gcd.py)                         | Euclidean algorithm        |
|  - [ ]    | 5  | LCM                    | [CN](https://www.codingninjas.com/studio/problems/lcm_8417489)           | [Step1_Basics/1.3_Maths/lcm.py](Step1_Basics/1.3_Maths/lcm.py)                         | `lcm = (a*b)//gcd`         |
|  - [x]    | 6  | Armstrong Number        | [CN](https://www.codingninjas.com/studio/problems/check-armstrong_589)   | [Step1_Basics/1.3_Maths/armstrong.py](Step1_Basics/1.3_Maths/armstrong.py)             | Power of digits            |
|  - [x]    | 7  | Print All Divisors     | [CN](https://www.codingninjas.com/studio/problems/print-divisors_3608828)| [Step1_Basics/1.3_Maths/divisors.py](Step1_Basics/1.3_Maths/divisors.py)               | Up to √n optimization      |
|  - [ ]    | 8  | Check Prime            | [CN](https://www.codingninjas.com/studio/problems/prime-number_624934)   | [Step1_Basics/1.3_Maths/is_prime.py](Step1_Basics/1.3_Maths/is_prime.py)               | Trial division up to √n    |

### 1.4: Recursion

| Status           | # | Problem | Platform | Solution | Notes |
|------------------|---|---------|----------|----------|-------|
|  - [ ]    | 1 | Print Name N times | [CN](https://www.codingninjas.com/studio/problems/print-name-n-times_3625289) | [Step1_Basics/1.4_Recursion/print_name_n_times.py](Step1_Basics/1.4_Recursion/print_name_n_times.py) | Simple recursion |
|  - [ ]    | 2 | Print 1 to N | [CN](https://www.codingninjas.com/studio/problems/print-1-to-n_628290) | [Step1_Basics/1.4_Recursion/print_1_to_n.py](Step1_Basics/1.4_Recursion/print_1_to_n.py) | Tail recursion |
|  - [ ]    | 3 | Print N to 1 | [CN](https://www.codingninjas.com/studio/problems/print-n-to-1_628290) | [Step1_Basics/1.4_Recursion/print_n_to_1.py](Step1_Basics/1.4_Recursion/print_n_to_1.py) | Base case-first |
|  - [ ]    | 4 | Sum of first N numbers | [CN](https://www.codingninjas.com/studio/problems/sum-of-first-n-numbers_8876068) | [Step1_Basics/1.4_Recursion/sum_of_n.py](Step1_Basics/1.4_Recursion/sum_of_n.py) | `sum = n + f(n-1)` |
|  - [ ]    | 5 | Factorial of N | [LC](https://leetcode.com/problems/factorial-trailing-zeroes/) | [Step1_Basics/1.4_Recursion/factorial.py](Step1_Basics/1.4_Recursion/factorial.py) | Recursive factorial |
|  - [ ]    | 6 | Reverse an array | [CN](https://www.codingninjas.com/studio/problems/reverse-array_1232638) | [Step1_Basics/1.4_Recursion/reverse_array.py](Step1_Basics/1.4_Recursion/reverse_array.py) | Two-pointer recursion |
|  - [x]    | 7 | Check Palindrome (Recursion) | [LC](https://leetcode.com/problems/valid-palindrome/) | [Step1_Basics/1.4_Recursion/check_palindrome.py](Step1_Basics/1.4_Recursion/check_palindrome.py) | Compare first and last |
|  - [x]    | 8 | Fibonacci Number | [LC](https://leetcode.com/problems/fibonacci-number/) | [Step1_Basics/1.4_Recursion/fibonacci.py](Step1_Basics/1.4_Recursion/fibonacci.py) | Naive recursion |

### 1.5: Hashing

| Status           | #  | Problem                 | Platform                                                                 | Solution                                                                 | Notes                            |
|------------------|----|-------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------|
|  - [x]    | 1  | Two Sum                 | [LC](https://leetcode.com/problems/two-sum/)                             | [Step1_Basics/1.5_Hashing/two_sum.py](Step1_Basics/1.5_Hashing/two_sum.py)                         | Hashmap for O(n) lookup      |
|  - [x]    | 2  | Valid Anagram           | [LC](https://leetcode.com/problems/valid-anagram/)                       | [Step1_Basics/1.5_Hashing/valid_anagram.py](Step1_Basics/1.5_Hashing/valid_anagram.py)             | Count characters using hashmap   |
|  - [x]    | 3  | Group Anagrams          | [LC](https://leetcode.com/problems/group-anagrams/)                      | [Step1_Basics/1.5_Hashing/group_anagrams.py](Step1_Basics/1.5_Hashing/group_anagrams.py)           | Sorted tuple as key in map   |
|  - [x]    | 4  | Happy Number            | [LC](https://leetcode.com/problems/happy-number/)                        | [Step1_Basics/1.5_Hashing/happy_number.py](Step1_Basics/1.5_Hashing/happy_number.py)               | Set to detect cycles         |
|  - [x]    | 5  | Contains Duplicate      | [LC](https://leetcode.com/problems/contains-duplicate/)                  | [Step1_Basics/1.5_Hashing/contains_duplicate.py](Step1_Basics/1.5_Hashing/contains_duplicate.py)   | Detect duplicates using set    |

---

## Step 2: Sorting Techniques

| Status           | #  | Problem                  | LeetCode Link                                                                 | Solution                                               | Notes                                  |
|------------------|----|--------------------------|------------------------------------------------------------------------------|--------------------------------------------------------|----------------------------------------|
|  - [x]    | 1  | Bubble Sort              | [Sort‑an‑Array](https://leetcode.com/problems/sort-an-array/)                | [Step2_Sorting/bubble_sort.py](Step2_Sorting/bubble_sort.py)         | Compare adjacent, O(n²)     |
|  - [x]    | 2  | Selection Sort           | [Sort‑an‑Array](https://leetcode.com/problems/sort-an-array/)                | [Step2_Sorting/selection_sort.py](Step2_Sorting/selection_sort.py)   | Select min, O(n²)           |
|  - [x]    | 3  | Insertion Sort           | [Sort‑an‑Array](https://leetcode.com/problems/sort-an-array/)                | [Step2_Sorting/insertion_sort.py](Step2_Sorting/insertion_sort.py)   | Build sorted subarray       |
|  - [x]    | 4  | Merge Two Sorted Arrays  | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)      | [Step2_Sorting/merge_two_sorted.py](Step2_Sorting/merge_two_sorted.py) | Two-pointer merge           |
|  - [x]    | 5  | Merge Sort (Recursion)   | [Sort‑an‑Array](https://leetcode.com/problems/sort-an-array/)                | [Step2_Sorting/merge_sort.py](Step2_Sorting/merge_sort.py)           | Divide & merge, O(n log n)  |
|  - [ ]    | 6  | Quick Sort (Recursion)   | [Sort‑an‑Array](https://leetcode.com/problems/sort-an-array/)                | [Step2_Sorting/quick_sort.py](Step2_Sorting/quick_sort.py)           | Partition-based             |

---

## Step 3: Arrays

### 3.1: Easy Array Problems

| Status           | #  | Problem                                | Platform / Link                                                                  | Solution File                                           | Notes                                  |
|------------------|----|----------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------|----------------------------------------|
|  - [ ]    | 1  | Largest Element in Array               | [CN](https://www.codingninjas.com/studio/problems/ninja-and-the-largest-element_6581957) | –     | Traverse once, keep track of max      |
|  - [ ]    | 2  | Second Largest Element in Array        | [CN](https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960) | –      | One-pass or two-pass variant          |
|  - [ ]    | 3  | Check if Array is Sorted               | [GFG](https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1) | –                | Compare each pair a[i] <= a[i+1]      |
|  - [x]    | 4  | Remove Duplicates from Sorted Array    | [LC](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)           | [Step3_Arrays/3.1_Easy/remove_duplicates.py](Step3_Arrays/3.1_Easy/remove_duplicates.py) | Two-pointer method                    |
|  - [ ]    | 5  | Left Rotate an Array by One Place      | [CN](https://www.codingninjas.com/studio/problems/rotate-array_1230543)            | –    | Save first element, shift, append     |
|  - [x]    | 6  | Left Rotate by D Places                | [LC](https://leetcode.com/problems/rotate-array/)                                  | [Step3_Arrays/3.1_Easy/left_rotate_d.py](Step3_Arrays/3.1_Easy/left_rotate_d.py)        | Use reversal algorithm or temp array  |
|  - [x]    | 7  | Move Zeros to End                      | [LC](https://leetcode.com/problems/move-zeroes/)                                   | [Step3_Arrays/3.1_Easy/move_zeros.py](Step3_Arrays/3.1_Easy/move_zeros.py)              | Two-pointer or count-zero approach    |
|  - [ ]    | 8  | Union of Two Arrays                    | [CN](https://www.codingninjas.com/studio/problems/union-of-two-sorted-arrays_1082149) | –          | Two pointers on sorted arrays         |
|  - [x]    | 9  | Intersection of Two Arrays             | [LC](https://leetcode.com/problems/intersection-of-two-arrays/)                    | [Step3_Arrays/3.1_Easy/intersection.py](Step3_Arrays/3.1_Easy/intersection.py)          | Use set/hashmap or two pointers       |

### 3.2: Binary Search on Arrays

| Status           | #  | Problem                          | Platform / Link                                                                 | Solution File                                                                 | Notes                                  |
|------------------|----|----------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------|
|  - [x]    | 1  | Binary Search on 1D Array        | [LC](https://leetcode.com/problems/binary-search/)                              | [Step3_Arrays/3.2_BS/binary_search.py](Step3_Arrays/3.2_BS/binary_search.py)       | Classic binary search, O(log n)        |
|  - [x]    | 2  | Upper Bound / Lower Bound        | [LC](https://leetcode.com/problems/search-insert-position/)                     | [Step3_Arrays/3.2_BS/lower_upper_bound.py](Step3_Arrays/3.2_BS/lower_upper_bound.py) | Variants of binary search              |
|  - [x]    | 3  | First and Last Occurrence        | [LC](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Step3_Arrays/3.2_BS/first_last_occurrence.py](Step3_Arrays/3.2_BS/first_last_occurrence.py) | Two binary searches                   |
|  - [x]    | 4  | Search in Rotated Sorted Array I | [LC](https://leetcode.com/problems/search-in-rotated-sorted-array/)             | [Step3_Arrays/3.2_BS/search_rotated_array.py](Step3_Arrays/3.2_BS/search_rotated_array.py) | Pivot + binary search                  |
|  - [x]    | 5  | Search in Rotated Sorted Array II| [LC](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)          | [Step3_Arrays/3.2_BS/search_rotated_array_ii.py](Step3_Arrays/3.2_BS/search_rotated_array_ii.py) | Handle duplicates                     |
|  - [x]    | 6  | Single Element in Sorted Array   | [LC](https://leetcode.com/problems/single-element-in-a-sorted-array/)           | [Step3_Arrays/3.2_BS/single_element.py](Step3_Arrays/3.2_BS/single_element.py)     | XOR or binary search on pairs          |
|  - [x]    | 7  | Find Peak Element               | [LC](https://leetcode.com/problems/find-peak-element/)                          | [Step3_Arrays/3.2_BS/find_peak.py](Step3_Arrays/3.2_BS/find_peak.py)               | Binary search on slopes                |
|  - [x]    | 8  | Search in 2D Matrix             | [LC](https://leetcode.com/problems/search-a-2d-matrix/)                         | [Step3_Arrays/3.2_BS/search_2d_matrix.py](Step3_Arrays/3.2_BS/search_2d_matrix.py) | Treat matrix as flattened array        |
|  - [x]    | 9  | Search in 2D Matrix II          | [LC](https://leetcode.com/problems/search-a-2d-matrix-ii/)                      | [Step3_Arrays/3.2_BS/search_2d_matrix_ii.py](Step3_Arrays/3.2_BS/search_2d_matrix_ii.py) | Start from corner, O(m+n)              |

---

## Time Complexity Reference

| Complexity      | Handles Up To (n ≈) | Notes / Use Cases                |
|-----------------|---------------------|----------------------------------|
| O(1)            | Any size            | Constant-time                    |
| O(log n)        | 10⁸+                | Binary search, bit tricks        |
| O(n)            | 10⁷ – 10⁸           | Single pass                      |
| O(n log n)      | 10⁶ – 10⁷           | Efficient sorting                |
| O(n²)           | 10³ – 10⁴           | Double loops                     |
| O(n³)           | 100 – 300           | Triple loops, basic DP           |
| O(2ⁿ)           | ≤ 20                | Backtracking, subsets            |
| O(n!)           | ≤ 8 – 10            | Permutations                     |

Tips:
- If n ≤ 10⁸: Use O(log n) or better
- If n ≤ 10⁶: O(n log n) or better
- If n ≤ 10⁴: O(n²) is acceptable
- If n ≤ 100: O(n³) is safe
- If n ≤ 20: O(2ⁿ) or bitmasking
- If n ≤ 10: O(n!) is fine

---

## Folder Structure

...