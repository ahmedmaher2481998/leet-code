import { test } from "./test";

/**
 * Definition for singly-linked list.
 *
 */
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
function hasCycle(head: ListNode | null): boolean {
  let slow = head;
  let fast = head;

  while (slow?.next && fast?.next?.next) {
    slow = slow.next;
    fast = fast?.next?.next;
    if (fast === slow) return true;
  }
  return false;
}
