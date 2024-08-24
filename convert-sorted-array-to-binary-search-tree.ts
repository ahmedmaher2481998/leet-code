class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function sortedArrayToBST(nums: number[]): TreeNode | null {
  let l = 0,
    r = nums.length;
  const helper = (l: number, r: number) => {
    if (l > r) return null;
    const m = Math.floor((r + l) * 0.5);
    console.log(`called with l:${l} , r:${r},while m is :${m}`);
    const root = new TreeNode(nums[m]);
    root.left = helper(l, m - 1);
    root.right = helper(m + 1, nums.length - 1);
    return root;
  };
  return helper(l, r);
}
const p1 = [-10, -3, 0, 5, 9];

console.log(sortedArrayToBST(p1));
