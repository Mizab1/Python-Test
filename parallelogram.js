let str = "";
let totalStars = 5;

for (i = 0; i < totalStars; i++) {
  str += " ".repeat(i).concat("*".repeat(totalStars)).concat("\n");
}

console.log(str);
