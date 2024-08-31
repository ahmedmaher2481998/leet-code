function trap(height: number[]): number {
  if (height.length === 0) return 0;

  let n = height.length;
  let left = new Array(n).fill(0);
  let right = new Array(n).fill(0);

  let l = 0,
    r = height.length - 1;

  for (let i = 0; i < height.length; i++) {
    left[l] = Math.max(height[i], l === 0 ? 0 : left[l - 1]);
    l++;

    right[r] = Math.max(height[i], r + 1 >= height.length ? 0 : right[r + 1]);
    r--;
  }

  // (left = [0, ...left, 0]), (right = [0, ...right, 0]);
  let trapped = 0;
  for (let i = 0; i < height.length; i++) {
    const water = Math.min(left[i], right[i]) - height[i];
    if (water > 0) {
      trapped += water;
    }
  }
  console.log(`left ${left.length},right: ${right.length}`);
  return trapped;
}

console.log("result : ", trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
console.log("result : ", trap([4, 2, 0, 3, 2, 5]));
