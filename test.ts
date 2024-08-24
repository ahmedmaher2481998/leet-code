export const test = (
  { handler, result }: { result: number; handler: (...rest: any[]) => any },
  ...rest: any[]
) => {
  //@ts-ignore
  const res = handler(...rest);
  if (res !== result) {
    console.error("failed expected: " + result + " but recived " + res);
  } else {
    console.log("Passed");
  }
};
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

export function arrayToListNode(arr: number[]): ListNode | null {
  if (arr.length === 0) return null;

  const head = new ListNode(arr[0]); // Initialize the head with the first element
  let current = head;

  for (let i = 1; i < arr.length; i++) {
    current.next = new ListNode(arr[i]); // Create a new node and link it
    current = current.next; // Move to the next node
  }

  return head; // Return the head of the list
}
export function listNodeToArray(head: ListNode | null): number[] {
  const arr: number[] = [];
  let current = head;

  while (current !== null) {
    arr.push(current.val); // Push the value of the current node to the array
    current = current.next; // Move to the next node
  }

  return arr; // Return the array of values
}
