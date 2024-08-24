import { arrayToListNode, listNodeToArray } from "./test";
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
function reorderList(head: ListNode | null): void {
  if (!head) return;
  console.log("now is: ", listNodeToArray(head));
  // locating the middle element
  let slow = head,
    fast = head;
  while (fast.next && fast.next.next) {
    slow = slow.next!;
    fast = fast.next.next;
  }
  let right = slow.next;
  console.log("🚀middle:", slow.val);
  slow.next = null;
  // reversing everything after the middle element (right list)
  let curr = right,
    prev = null;
  while (curr) {
    const t = curr.next;
    curr.next = prev;
    prev = curr;
    curr = t;
  }
  right = prev;
  let left: ListNode | null = head;
  // merging right list with left list
  // [1,2,3] [4,5]
  // l 2, r 5 ,1-4-5
  while (right && left) {
    const l: ListNode | null = left.next;
    const r = right.next;

    //merging
    left.next = right;
    right.next = l;
    right = r;

    left = l;
  }
}

const firList = arrayToListNode([1, 2, 3, 4]);
const secondList = arrayToListNode([1, 2, 3, 4, 5]);
const thirdList = arrayToListNode([1, 2, 3]);
const p1 = reorderList(firList);
const p2 = reorderList(secondList);
const p3 = reorderList(thirdList);
// console.log(listNodeToArray(reorderList(firList)));
// console.log(listNodeToArray(reorderList(secondList)));
// console.log(listNodeToArray(reorderList(thirdList)));
