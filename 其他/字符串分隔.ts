// 字符串分隔 - 提出 by安卓小哥
// "aa,,bbb,c,,d,,"
// ",,"
// ["aa", "bbb", "c"]

// 双指针 - 处理delimeter='' 情况
let split = (str: string, delimeter: string): string[] => {
  let ans: string[] = [];
  let jv = delimeter.length ? 0 : -1;
  let [i, j] = [0, jv];
  while (i < str.length) {
    if (str[i] === delimeter[j] || j === -1) {
      if (j === delimeter.length - 1) {
        ans.push(str.substr(0, i - j));
        str = str.substr(i + 1);
        i = 0;
        j = jv;
      } else {
        i++;
        j++;
      }
    } else {
      i++;
      j = jv;
    }
  }
  return ans;
};

// 双指针
let split = (str: string, delimeter: string): string[] => {
  let ans: string[] = [];
  let [i, j] = [0, 0];
  while (i < str.length) {
    if (str[i] === delimeter[j]) {
      if (j === delimeter.length - 1) {
        ans.push(str.substr(0, i - j));
        str = str.substr(i + 1);
        i = 0;
        j = 0;
      } else {
        i++;
        j++;
      }
    } else {
      i++;
      j = 0;
    }
  }
  return ans;
};

// builtin split函数
let split = (str, delimeter) => {
  return str.split(delimeter);
};
