// console.log(generateChildren("0099"));
function openLock(locked: string[], target: string): number {
  let init = "0000";

  const seen = new Set(locked);
  function addChar(c: string): string {
    let res = (Number(c) + 1) % 10;
    return `${res}`;
  }
  function minusChar(c: string): string {
    let result = (Number(c) - 1 + 10) % 10;
    return `${result}`;
  }
  function generateChildren(currentLock: string): string[] {
    let s = currentLock.split("");
    const genArrayVariation = (index: number): string[] => {
      let a = [...s];
      let b = [...s];
      a[index] = addChar(a[index]);
      b[index] = minusChar(b[index]);
      return [a.join(""), b.join("")];
    };
    const [a1, b1] = genArrayVariation(0),
      [a2, b2] = genArrayVariation(1),
      [a3, b3] = genArrayVariation(2),
      [a4, b4] = genArrayVariation(3);
    const res = [a1, b1, a2, b2, a3, b3, a4, b4];
    // console.log("🚀 ~ generateChildren ~ res:", res);
    return res;
  }
  if (target === init) return 0;
  if (seen.has(target)) return -1;

  let q: { lock: string; step: number }[] = [];

  q.push({ lock: init, step: 0 });

  while (q.length) {
    if (!q.length) break;
    if (target === "8888") console.log(q.length);

    const { lock, step } = q.shift()!;

    if (lock === target) {
      return step;
    }
    let currStep = step + 1;
    const children = generateChildren(lock);
    for (let i = 0; i < children.length; i++) {
      const currLock = children[i];
      if (!seen.has(currLock)) {
        seen.add(currLock);
        if (currLock === target) return currStep;
        else
          q.push({
            lock: currLock,
            step: currStep,
          });
      }
    }
  }
  return -1;
}

const deaden1 = ["0201", "0101", "0102", "1212", "2002"],
  target1 = "0202";

const deaden2 = ["8888"],
  target2 = "0009";
const deaden3 = [
    "8887",
    "8889",
    "8878",
    "8898",
    "8788",
    "8988",
    "7888",
    "9888",
  ],
  target3 = "8888";

// console.log("steps", openLock(deaden1, target1));
// console.log("steps", openLock(deaden2, target2));
console.log("steps", openLock(deaden3, target3));
