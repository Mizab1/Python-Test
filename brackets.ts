const groupBrackets = (input: string): Array<String> => {
  let stack: Array<String> = [];
  let result: Array<String> = [];
  let group: string = "";
  for (let char of input) {
    if (char !== "(" && char !== ")") {
      continue;
    }
    if (char === "(") {
      stack.push(char);
      group += char;
    }
    if (char === ")") {
      group += char;
      stack.pop();
      if (stack.length === 0) {
        result.push(group);
        group = "";
      }
    }
  }

  return result;
};

console.log(
  groupBrackets("( (  ( ) ) ( )  ( ( ) ) ) ( (  ) ( )   ) ( ) ( ( ( ) ( ) )) ")
);
