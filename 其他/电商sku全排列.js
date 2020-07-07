// 前端电商 sku 的全排列算法很难吗？学会这个套路，彻底掌握排列组合。
// https://juejin.im/post/5ee6d9026fb9a047e60815f1

let names = ["iPhone X", "iPhone XS"];
let colors = ["黑色", "白色"];
let storages = ["64g", "256g"];
let chunks = [names, colors, storages];

let [lst0, lst1, lst2] = chunks;

// 2. 通用法 - 函数组装
// todo

// 1. 简单法
ans = lst0.reduce((ac0, x0) => {
  return ac0.concat(...lst1.map((x1) => lst2.map((x2) => [x0, x1, x2])));
}, []);
