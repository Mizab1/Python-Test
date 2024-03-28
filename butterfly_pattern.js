const createButterfly = (numOfPoints) => {
  let str = "";

  const drawPattern = (i) => {
    str += "*"
      .repeat(i)
      .concat(" ".repeat((numOfPoints - i) * 2))
      .concat("*".repeat(i))
      .concat("\n");
  };

  for (let i = 1; i <= numOfPoints; i++) {
    drawPattern(i);
  }
  for (let i = numOfPoints; i >= 1; i--) {
    drawPattern(i);
  }

  return str;
};

console.log(createButterfly(9));
