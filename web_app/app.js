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

const analyze = function () {
  const rawInput = document.getElementById("input-text").value;
  const allLower = rawInput.toLowerCase();
  const inputAsArray = allLower.split(" ");
  const noNumbers = [];
  const noSymbols = [];

  // remove any number strings
  console.log("Cleaning text of numbers");
  for (let i = 0; i < inputAsArray.length; i++) {
    if (isNaN(parseInt(inputAsArray[i]))) {
      noNumbers.push(inputAsArray[i]);
    }
  }

  // remove any words that contain symbols
  console.log("Cleaning text of special symbols");
  for (let i = 0; i < noNumbers.length; i++) {
    if (noNumbers[i].search(/[.|,|$|%|&|:|;|(|)|!|-|_]/g) === -1) {
      noSymbols.push(noNumbers[i]);
    }
  }

  // need to get this file with ajax call to webserver
  console.log("Importing word map");
  let wordMap = null;
  // const request = axios.get("http://192.168.178.43:8000/automation");
  const request = axios({
    method: "get",
    // port must be the same as locahost port!
    url: "http://192.168.178.43:8080/automation",
    headers: {
      accept: "application/json",
    },
  });
  request.then((response) => {
    // wordMap = JSON.parse(response.data);
    wordMap = response.data;
    // console.log(wordMap["a"]);
  });
  console.log(wordMap);
};
