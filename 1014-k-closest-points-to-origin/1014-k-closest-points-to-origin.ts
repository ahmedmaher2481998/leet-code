function d(p: number[]) {
    const dist = (p[0] * p[0]) + (p[1] * p[1]);
    return dist;
}
function heapify(arr: number[][], i: number) {
    const n = arr.length
    while (true) {
        let min = i * 2 + 1
        const n = arr.length
        if (min + 1 < n && d(arr[min]) > d(arr[min + 1])) {
            min = min + 1
        }
        if (min < n && d(arr[i]) > d(arr[min])) {
            const temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
            i = min
        }
       
        else break;
    }
    return arr
}
function heap(arr: number[][]) {
    let mid = (arr.length - 1 ) >> 1;
    for (let i = mid; i >= 0; i--) {

        heapify(arr, i)
    }
    return arr
}

function kClosest(points: number[][], k: number): number[][] {
    const h = heap(points)
    const result = []
    for (let i = 0; i < k; i++) {
        result.push(h.shift())
        h.unshift(h.pop())
        heapify(h,0)
    }

    return result

};