# Loop Invariant  
**What is a loop invariant?**  
![loop](/Topics/computer_science/Design-and-Analysis-of-Algorithm-Project/loop_invariant_bigO_master_theorem/images/loop.png)

Imagine following a recipe. At each step, you need to ensure certain ingredients or conditions are correct to achieve a good final result. A **loop invariant** is like this condition that must hold true at every step of the process.  

To prove that an algorithm (e.g., a loop) is correct, we demonstrate three key aspects:  
1. **Initialization**: Before the loop starts, the invariant condition (or property) is already true.  
2. **Maintenance**: During each loop iteration, if the invariant holds at the beginning of the iteration, it remains true at the end.  
3. **Termination**: When the loop terminates, the invariant—combined with the loop’s termination condition—ensures the final result is correct.  

---

## How to Discover the Invariant Property  
To identify the loop invariant, focus on what the loop accomplishes. Typically, it builds or modifies part of the solution. Ask:  
- What do we know about the algorithm’s state at the start of the loop?  
- What is guaranteed to hold after each iteration?  

---

## Example: Insertion Sort  
Consider the Insertion Sort algorithm, which sorts an array.  

**Pseudocode**:  
```pseudocode  
InsertionSort(V)  
  // V[1..n] is the array to be sorted  
  for i from 2 to n do  
    tmp ← V[i]  
    j ← i - 1  
    while j > 0 and V[j] > tmp do  
      V[j + 1] ← V[j]  
      j ← j - 1  
    V[j + 1] ← tmp  
```  

### Discovering the Invariant  
1. **Initialization**:  
   - Before the loop starts (when `i = 2`), the subarray `V[1..1]` contains a single element.  
   - **Invariant**: A single-element subarray is trivially sorted. Thus, "`V[1..i-1]` is sorted" holds before the loop begins.  

2. **Maintenance**:  
   - Assume the subarray `V[1..i-1]` is sorted at the start of an iteration (our hypothesis).  
   - The algorithm takes `V[i]` (stored in `tmp`) and inserts it into the correct position within the sorted subarray.  
   - This is done by shifting larger elements to the right until the correct position for `tmp` is found.  
   - By the end of the iteration, `V[1..i]` remains sorted, preserving the invariant.  

3. **Termination**:  
   - The loop terminates when `i = n + 1`.  
   - By the invariant, `V[1..n]` (the entire array) is now sorted.  

---

## Another Example: Bubble Sort  
In Bubble Sort, the goal is to "bubble" the largest element to the end of the array in each pass.  

**Pseudocode (simplified)**:  
```pseudocode  
BubbleSort(V)  
  n ← length(V)  
  for i from 1 to n-1 do  
    for j from 1 to n-i do  
      if V[j] > V[j+1] then  
        swap V[j] and V[j+1]  
```  

### Discovering the Invariant  
1. **Initialization**:  
   - Before the outer loop starts, no specific condition is required, but after the first inner loop pass, the largest element is placed at the end.  

2. **Maintenance**:  
   - Each comparison and swap in the inner loop ensures that, by the end of the pass, the largest unsorted element moves to its correct position.  
   - **Invariant**: After each complete outer loop iteration (for a given `i`), the last `i` elements are in their correct sorted positions.  

3. **Termination**:  
   - After `n-1` passes, all elements are correctly positioned, resulting in a sorted array.  

---

## Tips for Discovering Loop Invariants  
1. **Identify the loop’s goal**: What should be true after each iteration? Examples:  
   - "The first `i` elements are sorted."  
   - "The largest element is at the end."  
2. **Check the initial state**: What is true before the loop starts? Often simple (e.g., a single-element array is sorted).  
3. **Track progress**: Analyze how each iteration modifies the state while preserving the invariant.  
4. **Conclude at termination**: Combine the invariant with the termination condition to prove correctness.  

---

## Summary  
- **Master Theorem**:  
  The recurrence relation `T(n) = aT(n/b) + f(n)` describes a recursive algorithm dividing a problem into `a` subproblems of size `n/b`, with a cost `f(n)` for dividing/combining. The comparison between `f(n)` and `n^(log_b(a))` determines the dominant cost.  

- **Loop Invariant**:  
  A property that remains true before, during, and after loop execution. It helps prove algorithm correctness by verifying:  
  - **Initialization**: The invariant holds before the loop.  
  - **Maintenance**: The invariant holds after each iteration.  
  - **Termination**: The invariant ensures the final result is correct.  

