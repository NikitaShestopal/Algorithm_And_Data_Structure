var scanf = require('scanf');


var n = scanf('%d');

var matrix = [];
for (let i = 0; i < n; i++) {
    matrix.push(scanf(('%d '.repeat(n)).trim()));
}

function hasCycle(n, matrix) {
    const visited = Array(n).fill(0);

    function dfs(v) {
        visited[v] = 1;
        for (let u = 0; u < n; u++) {
            if (matrix[v][u]) {
                if (visited[u] === 1) return true;
                if (visited[u] === 0 && dfs(u)) return true;
            }
        }
        visited[v] = 2;
        return false;
    }

    for (let i = 0; i < n; i++) {
        if (visited[i] === 0 && dfs(i)) {
            console.log(1);
            return;
        }
    }
    console.log(0);
}

hasCycle(n, matrix);