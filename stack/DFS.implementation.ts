// Define the graph as an adjacency list
const graph: { [key: string]: string[] } = {
  A: ["B", "C"],
  B: ["D", "E"],
  C: ["F"],
  D: [],
  E: ["F"],
  F: [],
};

// DFS function
function dfs(node: string, visited: Set<string>): void {
  // Mark the current node as visited
  visited.add(node);
  console.log(node); // Process the current node (e.g., print it)

  // Recursively visit all the adjacent nodes
  for (const neighbor of graph[node]) {
    if (!visited.has(neighbor)) {
      dfs(neighbor, visited);
    }
  }
}

// Starting DFS from node 'A'
const visited = new Set<string>();
dfs("A", visited);
