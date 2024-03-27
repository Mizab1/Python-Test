let str = "aaabbcccds";
let count = 0;
let holder = [];

for (let i = 0; i < str.length; i++) {
  count++;
  if (str[i + 1] != str[i]) {
    holder.push(str[i] + count);
    count = 0;
  }
}

console.log(holder.join(""));
