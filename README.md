
# Randomized Quicksort and Hash Table with Chaining Implementation

## Project Overview

This project consists of two main parts:

1. **Randomized Quicksort Algorithm Implementation and Analysis**.
2. **Hash Table Implementation using Chaining for Collision Resolution**.

### Part 1: Randomized Quicksort

In this section, the **Randomized Quicksort** algorithm is implemented. The pivot element is chosen randomly from each subarray being partitioned. The algorithm ensures efficient sorting for various types of input arrays, including those with repeated elements, already sorted arrays, and reverse-sorted arrays. This method avoids worst-case scenarios by ensuring balanced partitions on average.

### Part 2: Hash Table with Chaining

In the second part of the project, a **Hash Table** is implemented using **chaining** to handle collisions. The chaining method uses linked lists (or lists in Python) to store multiple key-value pairs in the same bucket, making it effective at resolving hash collisions. The hash table supports essential operations such as **insertion**, **search**, and **deletion**, while dynamically resizing to maintain optimal performance.

---

## How to Run the Code

### Prerequisites

- **Python 3.x**: Ensure that you have Python 3 installed. You can download it from [here](https://www.python.org/downloads/).

### Steps to Run the Code

1. **Clone the Repository or Copy the Code**:
   - Copy the provided Python code for both the Randomized Quicksort and Hash Table implementation into a Python file (e.g., `quicksort_and_hashtable.py`).

2. **Run the Code**:
   - Run the Python file using the terminal or command prompt with the following command:
     ```
     python quicksort_and_hashtable.py
     ```

3. **View the Results**:
   - For **Randomized Quicksort**, the output will display the sorted array after applying the algorithm to an input array.
   - For **Hash Table with Chaining**, you will see the state of the hash table printed, along with the results of search and delete operations on specific keys.

---

## Summary of Findings

### Randomized Quicksort:
The randomized quicksort algorithm performed efficiently for different input arrays, including those with repeated elements, already sorted arrays, and reverse-sorted arrays. The random pivot selection helped balance partitions on average, avoiding worst-case time complexities and resulting in consistent performance with a time complexity of \(O(n \log n)\).

### Hash Table with Chaining:
The hash table implemented with chaining successfully handled key operations like insertion, search, and deletion. The chaining method efficiently resolved collisions by using linked lists (buckets) to store multiple key-value pairs at the same index. The dynamic resizing ensured that the load factor remained low, preserving efficient performance. Operations like search and insertion typically ran in constant time \(O(1)\), while deletion was also handled efficiently.

---

## Contact Information
For any issues or questions, feel free to open an issue on the GitHub repository.
