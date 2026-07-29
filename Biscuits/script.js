const flatArray = (arr = [], initialValue) =>
  arr.reduce((memo, elem) => {
    if (!Array.isArray(elem)) {
      memo.push(elem);
    } else {
      const res = flatArray(elem, memo);
      return res;
    }
    return memo;
  }, initialValue || []);

const arr = [1, 2, [3, 4, [5, [6, 7, 8]], [5, 6, [7, 8]]]];

console.log(flatArray(arr));
console.log("flatArrayTwo = ", flatArray(arr));