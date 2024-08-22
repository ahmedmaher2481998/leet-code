// works but exceeded limit
// function maxProfit(prices: number[]) {
//   if (prices.length < 2) return 0;
//   // min can be
//   let max = 0;
//   let min = Infinity;

import { test } from "./test";

//   let max_profit = 0;
//   prices.forEach((price, index) => {
//     // we move max
//     // we update window based on max profit
//     // we move min only if newMaxProfit is larger then maxProfit
//     // we also move max only if it increase the maxProfit
//     for (let i = index; i < prices.length; i++) {
//       const price2 = prices[i];
//       if (max_profit < price2 - price) {
//         max_profit = price2 - price;
//       }
//     }
//   });

//   return max_profit;
// }
// solution using sliding window
function maxProfit(prices: number[]): number {
  let buy = prices[0],
    sell = prices[1],
    profit = 0;

  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > buy) {
      sell = prices[i];
      if (sell - buy > profit) {
        profit = sell - buy;
      }
    } else {
      buy = prices[i];
    }
  }
  return profit;
}

const p1 = [7, 1, 5, 3, 6, 4]; //5
const p2 = [7, 6, 4, 3, 1]; // 0
const p3 = [2, 4, 1];
const p4 = [3, 2, 6, 5, 0, 3];

test({ handler: maxProfit, result: 5 }, p1);
test({ result: 0, handler: maxProfit }, p2);
test({ result: 2, handler: maxProfit }, p3);
test({ result: 4, handler: maxProfit }, p4);
