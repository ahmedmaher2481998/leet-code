import { test } from "../test";

/*
 * MyCircularQueue(k) Initializes the object with the size of the queue to be k.
 * int Front() Gets the front item from the queue. If the queue is empty, return -1.
 * int Rear() Gets the last item from the queue. If the queue is empty, return -1.
 * boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
 * boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
 * boolean isEmpty() Checks whether the circular queue is empty or not.
 * boolean isFull() Checks whether the circular queue is full or not.
 */
class MyCircularQueue {
  private start: number = -1;
  private end: number = -1;
  private q: number[] | null[] = [];
  private size = 0;
  private k: number = 0;

  constructor(k: number) {
    this.size = 0;
    this.start = 0;
    this.end = 0;
    this.k = k;
    this.q = new Array(k).fill(null);
  }

  enQueue(value: number): boolean {
    if (this.isFull()) return false;
    this.q[this.end] = value;
    this.end = (this.end + 1) % this.k;
    this.size++;
    return true;
  }

  deQueue(): boolean {
    if (this.isEmpty()) return false;
    else if (this.start === this.end) {
      this.start = -1;
      this.end = -1;
      return true;
    }
    this.q[this.start] = null;
    this.size--;
    this.start = (this.start + 1) % this.k;
    return true;
  }

  Front(): number {
    if (this.isEmpty()) return -1;
    return this.q[this.start] as number;
  }

  Rear(): number {
    if (this.isEmpty()) return -1;
    return this.q[(this.end + this.k - 1) % this.k] as number;
  }

  isEmpty(): boolean {
    return this.size === 0;
  }

  isFull(): boolean {
    return this.size === this.k;
  }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */
const myCircularQueue = new MyCircularQueue(3);

console.log(myCircularQueue.enQueue(1)); // return True
console.log(myCircularQueue.enQueue(2)); // return True
console.log(myCircularQueue.enQueue(3)); // return True
console.log(myCircularQueue.enQueue(4)); // return False
console.log(myCircularQueue.Rear()); // return 3
console.log(myCircularQueue.isFull()); // return True
console.log(myCircularQueue.deQueue()); // return True
console.log(myCircularQueue.enQueue(4)); // return True
console.log(myCircularQueue.Rear()); // return 4
