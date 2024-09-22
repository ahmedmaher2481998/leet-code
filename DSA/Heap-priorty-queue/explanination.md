Priority Queue Overview
A Priority Queue is a data structure where each element has a priority, and elements are dequeued based on their priority. The highest-priority element is dequeued first. A common implementation is using a Min Heap or Max Heap.

For this lesson, we’ll implement a Min Heap-based Priority Queue, where the smallest element is always at the top.

Step 1: Set Up the Class Structure
We start by defining a class to represent our priority queue. It will use an array to store the elements, and each element will be stored as an object with two properties:

priority (a number)
value (the actual data)
```typescript
class PriorityQueue<T> {
  private heap: { priority: number, value: T }[];

  constructor() {
    this.heap = [];
  }
}```
heap: This array will be our internal representation of the heap. Each element will be an object containing a priority and a value.
constructor: Initializes an empty heap.
Step 2: Helper Functions
We’ll need helper methods to perform heap operations. These include:

getParentIndex: Get the parent index of a node (used during insertions).
getLeftChildIndex & getRightChildIndex: Get the left and right child indices (used during deletions).
swap: Swap two elements in the heap (used in both insertion and deletion).
```typescript
private getParentIndex(childIndex: number): number {
  return Math.floor((childIndex - 1) / 2);
}

private getLeftChildIndex(parentIndex: number): number {
  return (2 * parentIndex) + 1;
}

private getRightChildIndex(parentIndex: number): number {
  return (2 * parentIndex) + 2;
}

private swap(index1: number, index2: number): void {
  const temp = this.heap[index1];
  this.heap[index1] = this.heap[index2];
  this.heap[index2] = temp;
}```
Explanation:
getParentIndex: This calculates the parent index in a heap array. If a node is at index i, its parent is at index (i-1)/2.
getLeftChildIndex & getRightChildIndex: These return the indices of the left and right children of a node. For any parent node at index i, the left child is at 2*i + 1 and the right child is at 2*i + 2.
swap: This swaps two elements in the heap array, which is useful during "bubble-up" and "bubble-down" operations.
Step 3: Insert (Enqueue) Operation
Now we’ll implement the enqueue operation. When inserting a new element, we’ll add it to the end of the heap and then “bubble it up” to maintain the heap order.

```typescript
enqueue(value: T, priority: number): void {
  this.heap.push({ priority, value });
  this.bubbleUp(this.heap.length - 1);
}

private bubbleUp(index: number): void {
  let parentIndex = this.getParentIndex(index);
  
  // Continue bubbling up until the heap property is satisfied
  while (index > 0 && this.heap[index].priority < this.heap[parentIndex].priority) {
    this.swap(index, parentIndex);
    index = parentIndex;
    parentIndex = this.getParentIndex(index);
  }
}```
Explanation:
enqueue: Adds a new element with a given priority to the end of the heap.
bubbleUp: Ensures the heap property (min-heap in our case) is maintained. It compares the priority of the newly added element with its parent. If the child’s priority is smaller than the parent’s, they are swapped, and the process continues until the heap property is satisfied.
Step 4: Dequeue Operation
The dequeue operation removes the element with the highest priority (in a min-heap, it’s the element at index 0). After removing the element, we need to move the last element to the root and "bubble it down" to maintain heap order.

```typescript

dequeue(): T | null {
  if (this.heap.length === 0) return null;

  // Swap the first element with the last
  this.swap(0, this.heap.length - 1);
  
  const poppedNode = this.heap.pop();
  
  // Restore the heap order by bubbling down the root element
  this.bubbleDown(0);
  
  return poppedNode?.value || null;
}

private bubbleDown(index: number): void {
  let smallest = index;
  const leftChildIndex = this.getLeftChildIndex(index);
  const rightChildIndex = this.getRightChildIndex(index);

  // Compare with left child
  if (leftChildIndex < this.heap.length && this.heap[leftChildIndex].priority < this.heap[smallest].priority) {
    smallest = leftChildIndex;
  }

  // Compare with right child
  if (rightChildIndex < this.heap.length && this.heap[rightChildIndex].priority < this.heap[smallest].priority) {
    smallest = rightChildIndex;
  }

  // If the smallest element is not the current node, swap and continue bubbling down
  if (smallest !== index) {
    this.swap(index, smallest);
    this.bubbleDown(smallest);
  }
}```
Explanation:
dequeue: Swaps the root (smallest element) with the last element, removes the last element, and then calls bubbleDown to restore the heap property.
bubbleDown: Starts from the root and compares the current node with its children. If one of the children has a smaller priority, it swaps with the smallest child and continues down the heap.
Step 5: Peek Operation
The peek operation allows us to view the element with the highest priority (without removing it).

```typescript
peek(): T | null {
  return this.heap.length > 0 ? this.heap[0].value : null;
}```
Explanation:
peek: Returns the element at the root of the heap (the element with the highest priority). If the heap is empty, it returns null.
Step 6: Size and isEmpty
To check if the priority queue is empty or get its size, we can add these helper methods:

```typescript

size(): number {
  return this.heap.length;
}

isEmpty(): boolean {
  return this.heap.length === 0;
}``
Final Code
Here’s the complete PriorityQueue implementation:

``typescript

class PriorityQueue<T> {
  private heap: { priority: number, value: T }[];

  constructor() {
    this.heap = [];
  }

  private getParentIndex(childIndex: number): number {
    return Math.floor((childIndex - 1) / 2);
  }

  private getLeftChildIndex(parentIndex: number): number {
    return (2 * parentIndex) + 1;
  }

  private getRightChildIndex(parentIndex: number): number {
    return (2 * parentIndex) + 2;
  }

  private swap(index1: number, index2: number): void {
    const temp = this.heap[index1];
    this.heap[index1] = this.heap[index2];
    this.heap[index2] = temp;
  }

  enqueue(value: T, priority: number): void {
    this.heap.push({ priority, value });
    this.bubbleUp(this.heap.length - 1);
  }

  private bubbleUp(index: number): void {
    let parentIndex = this.getParentIndex(index);
    
    while (index > 0 && this.heap[index].priority < this.heap[parentIndex].priority) {
      this.swap(index, parentIndex);
      index = parentIndex;
      parentIndex = this.getParentIndex(index);
    }
  }

  dequeue(): T | null {
    if (this.heap.length === 0) return null;

    this.swap(0, this.heap.length - 1);
    const poppedNode = this.heap.pop();
    this.bubbleDown(0);
    
    return poppedNode?.value || null;
  }

  private bubbleDown(index: number): void {
    let smallest = index;
    const leftChildIndex = this.getLeftChildIndex(index);
    const rightChildIndex = this.getRightChildIndex(index);

    if (leftChildIndex < this.heap.length && this.heap[leftChildIndex].priority < this.heap[smallest].priority) {
      smallest = leftChildIndex;
    }

    if (rightChildIndex < this.heap.length && this.heap[rightChildIndex].priority < this.heap[smallest].priority) {
      smallest = rightChildIndex;
    }

    if (smallest !== index) {
      this.swap(index, smallest);
      this.bubbleDown(smallest);
    }
  }

  peek(): T | null {
    return this.heap.length > 0 ? this.heap[0].value : null;
  }

  size(): number {
    return this.heap.length;
  }

  isEmpty(): boolean {
    return this.heap.length === 0;
  }
}```
Usage Example:
```typescript

const pq = new PriorityQueue<string>();

pq.enqueue("Task 1", 1);
pq.enqueue("Task 2", 2);
pq.enqueue("Task 3", 0);

console.log(pq.peek());  // Task 3 (smallest priority)
console.log(pq.dequeue());  // Task 3
console.log(pq.dequeue());  // Task 1
console.log(pq.isEmpty());  // false
```
This code sets up a fully functional min-heap-based priority queue in TypeScript! Let me know if you'd like to extend this with additional functionality.






