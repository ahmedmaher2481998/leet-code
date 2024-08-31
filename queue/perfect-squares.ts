function numSquares(n: number): number {
  if (n <= 0) return 0;
  let squares: number[] = [];
  let seen = new Set<number>();
  let q: { sum: number; step: number }[] = [];
  for (let i = 1; i * i <= n; i++) {
    let s = i * i;
    if (n === s) return 1;

    squares.push(s);
    let sum = n - s;
    q.push({ sum, step: 1 });
    seen.add(sum);
  }
  while (q.length) {
    const { sum, step } = q.shift()!;
    for (let i = 0; i < squares.length; i++) {
      let result = sum - squares[i];
      console.log("step " + step + 1, result);
      if (result === 0) {
        return step + 1;
      } else if (result > 0 && !seen.has(result)) {
        q.push({ sum: result, step: step + 1 });
        seen.add(result);
      }
    }
  }
  return n;
}

numSquares(4703);
numSquares(7168);
