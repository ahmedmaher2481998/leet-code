class Stack {
  private data = [];
  constructor() {}

  get top() {
    return this.data[this.data.length - 1];
  }
  get isEmpty() {
    return this.data.length === 0;
  }
  get bottom() {
    return data[0];
  }

  pop() {
    if (this.isEmpty) return false;
    else return this.data.pop();
    return true;
  }
  push(v) {
    if (this.isEmpty) return false;
    else return this.data.push(v);
    return true;
  }
}
