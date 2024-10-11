let num1 = parseInt(prompt("Dame el primer numero:"))
let num2 = parseInt(prompt("Dame el segundo numero:"))
let signo = prompt("Dame el signo:")
switch (signo) {
    case "+":
        alert("El resultado es: "+(num1+num2))
        break
    case "-":
        alert("El resultado es: "+(num1-num2))
        break
    case "*":
        alert("El resultado es: "+(num1*num2))
        break
    case "/":
        alert("El resultado es: "+(num1/num2))
        break
    default:
        alert("     ERROR     ")
}