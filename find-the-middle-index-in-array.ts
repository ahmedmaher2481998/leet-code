import { test } from "./test";

function findMiddleIndex(nums: number[]): number {
  let left = 0,
    right = 0;

  nums.forEach((int, index) => {});
}

const nums1 = [2, 3, -1, 8, 4]; // 3
const nums2 = [1, -1, 4]; //2
const nums3 = [2, 5]; // -1

test({ handler: findMiddleIndex, result: 3 }, nums1);
test({ handler: findMiddleIndex, result: 2 }, nums2);
test({ handler: findMiddleIndex, result: -1 }, nums3);
