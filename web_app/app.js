const makePerfectSquareList = function (textArray) {
  let value = null;
  let outputArray = textArray;
  const sr = Math.sqrt(textArray.length);

  if (sr - Math.floor(sr) !== 0) {
    value = Math.floor(sr) + 1;

    perfectSquare = value ** 2;
    for (let i = 0; i < perfectSquare - textArray.length; i++) {
      outputArray.push("luman");
    }
  } else {
    value = sr;
    outputArray = textArray;
  }

  return [value, outputArray];
};

const cleanInput = function () {
  const rawInput = document.getElementById("input-text").value;
  const allLower = rawInput.toLowerCase();
  const inputAsArray = allLower.split(" ");

  console.log("Cleaning text of numbers");
};
