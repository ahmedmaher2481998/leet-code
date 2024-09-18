
function heapify(arr: number[], i: number, p: (number) => number) {
    while (true) {
        let min = i * 2 + 1
        const n = arr.length;
        if (min + 1 < n && p(min) < p(min + 1)) {
            min = min + 1
        }
        if (min < n && p(i) < p(min)) {
            [arr[min], arr[i]] = [arr[i], arr[min]]
            i = min

        } else break;
    }
}
function topKFrequent(nums: number[], k: number): number[] {
    const m = new Map<number, number>()
    nums.forEach(n => {
        if (m.get(n)) {
            m.set(n, m.get(n) + 1)
        } else {
            m.set(n, 1)
        }
    })
    // console.log('map',m)
    const arr = Array.from(m.keys())
    const p = (i) => m.get(arr[i])
    for (let i = (arr.length - 1 ) >> 1; i >= 0; i--) {
        heapify(arr, i, p)
    }
    const result = []
    // console.log(arr)
    for (let i =0; i <k; i++) {
        result.push(arr.shift())
        arr.unshift(arr.pop())
        heapify(arr,0,p)
        // console.log('after pop',i,arr)
    }
    return result
};