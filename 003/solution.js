var getPrime = function(number){
    for(var x = 1; x >= number; x++){
        if(number % x == 0){
            primeFactors.append(x)
            number = number / x
            console.log(number)
            console.log(x)
            return [number,x]
        }
    }
}

var primeFactors = []
var number = 600851475143
while(number > 2){
    values = getPrime(number)
    console.log(values)
    //number = values[1]
    //primeFactors.append(values[1])
    console.log(number)
}
console.log(primeFactors)
