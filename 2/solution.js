var sum = 0;
var currentNumber = 1;
var lastNumber = 0;
while(currentNumber < 4000000){
    if(currentNumber % 2 == 0){
        sum += currentNumber;
    }
    var nextNumber = currentNumber + lastNumber;
    lastNumber = currentNumber;
    currentNumber = nextNumber;
}
console.log(sum);
