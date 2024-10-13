let X = parseFloat(prompt("Dime el numero de X:\n"))
while (X==0) {
    X = parseFloat(prompt("Dime el numero distinto a 0:\n"))
}

let Y = parseFloat(prompt("Dime el numero de Y:\n"))
while (Y==0) {
    Y = parseFloat(prompt("Dime el numero distinto a 0:\n"))
}

if (X>0 && Y>0) {
    alert("\nLos datos ("+X+", "+Y+") estan en el cuadrante 1");
} else if (X<0 && Y>0) {
    alert("\nLos datos ("+X+", "+Y+") estan en el cuadrante 2");
} else if (X<0 && Y<0) {
    alert("\nLos datos ("+X+", "+Y+") estan en el cuadrante 3");
} else {
    alert("\nLos datos ("+X+", "+Y+") estan en el cuadrante 3");
}