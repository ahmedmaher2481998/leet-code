function numIslands(map: string[][]): number {
  const visited: Record<string, boolean> = {};
  const rows = map.length,
    cols = map[0].length,
    q: number[][] = [];
  let islands = 0;
  const getPos = (row: number, col: number) => row * cols + (col + 1);

  function addToQ(row: number, col: number) {
    const pos = getPos(row, col);
    if (
      row === rows ||
      col === cols ||
      visited[pos + ""] ||
      row < 0 ||
      col < 0 ||
      map[row][col] === "0"
    ) {
      return;
    } else {
      q.push([row, col]);
      visited[pos] = true;
    }
  }
  for (let i = 0; i < rows; i++) {
    const r = map[i];
    for (let j = 0; j < cols; j++) {
      const node = r[j];
      const pos = getPos(i, j);
      if (node === "1" && !visited[pos + ""]) {
        visited[pos + ""] = true;
        islands++;
        q.push([i, j]);
        while (q.length) {
          let node = q.shift();
          if (node?.length) {
            const [cr, cc] = node as number[];
            addToQ(cr + 1, cc);
            addToQ(cr - 1, cc);
            addToQ(cr, cc - 1);
            addToQ(cr, cc + 1);
          }
        }
      } else {
        visited[pos] = true;
      }
    }
  }
  console.log("islands", islands);
  return islands;
}
const grid1 = [
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"],
];
const grid2 = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"],
];
numIslands(grid1);
numIslands(grid2);
