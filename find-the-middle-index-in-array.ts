import { test } from "./test";
function findMiddleIndex(nums: number[]): number {
  let right = nums.reduce((acc, i) => (acc += i), 0);
  let left = 0;

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (i === 0) {
      left = 0;
      right -= nums[i];
    } else if (i === nums.length - 1) {
      right = 0;
      left += nums[i - 1];
    } else {
      right -= nums[i];
      left += nums[i - 1];
    }

    if (right === left) return i;
  }
  return -1;
}

const nums1 = [2, 3, -1, 8, 4]; // 3
const nums2 = [1, -1, 4]; //2
const nums3 = [2, 5]; // -1

test({ handler: findMiddleIndex, result: 3 }, nums1);
test({ handler: findMiddleIndex, result: 2 }, nums2);
test({ handler: findMiddleIndex, result: -1 }, nums3);
