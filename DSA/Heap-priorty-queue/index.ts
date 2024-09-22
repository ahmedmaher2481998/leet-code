// Min Heap-based Priority Queue
class PriorityQueue<T> {
  private heap: { priority: number, value: T }[]
  constructor(getPriority: (t: T) => number) {
    this.heap = []
    this.getPriority = getPriority
  }

  private orderUp(i: number) {
    let parent = this.getParentIndex(i)
    while (i > 0 && this.heap[i].priority < this.heap[parent].priority) {
      this.swap(i, parent)
      i = parent
      parent = this.getParentIndex(i)
    }

  }
  private orderDown(i: number) {
    while (true) {

      let smallest = this.getLeftChildIndex(i),
        right = this.getRightChildIndex(i)
      // smallest = i
      if (right < this.heap.length && this.heap[smallest].priority < this.heap[right].priority) {
        smallest = right
      }
      if (smallest < this.heap.length && this.heap[i].priority > this.heap[smallest].priority) {
        this.swap(i, smallest)
        // this.orderDown(smallest)
        i = smallest
      } else break
    }
  }

  enqueue(e: T) {
    this.heap.push({
      priority: this.getPriority(e),
      value: e,
    })
    // reorder the elements from the bottom up 
    this.orderUp(this.heap.length - 1)
  }


  dequeue(): T | null {
    if (this.heap.length === 0) return null;
    this.swap(0, this.heap.length - 1);
    const popNode = this.heap.pop()
    this.orderDown(0)
    return popNode?.value || null;

  }
  peek(): T | null {
    return this.heap.length > 0 ? this.heap[0].value : null;
  }

  print() {
    console.log(this.heap.map(({ value, priority }) => ({ value, priority })))
  }

  private getPriority(element: T): number {
    return 0
  }
  getLeftChildIndex(i: number) {
    return 2 * i + 1

  }
  getRightChildIndex(i: number) {
    return 2 * i + 2
  }
  getParentIndex(i: number): number {
    return Math.floor((i - 1) / 2)
  }
  private swap(index1: number, index2: number): void {
    const temp = this.heap[index1]
    this.heap[index1] = this.heap[index2]
    this.heap[index2] = temp
  }
  size(): number {
    return this.heap.length;
  }

  isEmpty(): boolean {
    return this.heap.length === 0;
  }

}


// const pq = new PriorityQueue<number>((number) => number)
const pq = new PriorityQueue<string>((s: string) => {
  return Number(s.split(' ')[1])
});

pq.enqueue("Task 1");
pq.enqueue("Task 2");
pq.enqueue("Task 0");

console.log(pq.peek());  // Task 0 (smallest priority)
console.log(pq.dequeue());  // Task 0
console.log(pq.dequeue());  // Task 1
console.log(pq.isEmpty());  // false
