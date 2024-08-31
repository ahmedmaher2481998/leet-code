import { arrayToListNode, listNodeToArray } from "./test";
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  let curr = new ListNode(-1);

  const preVHead = curr;
  let l1 = list1,
    l2 = list2;
  while (l1 && l2) {
    if (l1.val <= l2.val) {
      const t = l1.next;
      l1.next = null;
      curr.next = l1;

      l1 = t;
    } else {
      const t = l2.next;
      l2.next = null;
      curr.next = l2;

      l2 = t;
    }
    curr = curr.next;
  }
  if (!l1) curr.next = l2;
  if (!l2) curr.next = l1;
  return preVHead.next;
}

console.log(
  "result 1",
  listNodeToArray(
    mergeTwoLists(arrayToListNode([1, 2, 4]), arrayToListNode([1, 3, 4]))
  )
);
console.log(
  "result 2",
  listNodeToArray(mergeTwoLists(arrayToListNode([]), arrayToListNode([])))
);
console.log(
  "result 3",
  listNodeToArray(mergeTwoLists(arrayToListNode([]), arrayToListNode([0])))
);
