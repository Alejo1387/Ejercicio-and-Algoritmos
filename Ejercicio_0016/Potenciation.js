function potencia(x, y) {
    let result = x;
    if (x == 0) {
        if (y == 0) {
            result = 1;
        } else {
            result = 0;
        }
    } else if (y == 0) {
        result = 0;
    } else {
        let i = 1;
        while (i < y) {
            result *= x;
            i++;
        }
    }
    alert(`
      ${y}
    ${x}        es igual a ${result}
    `);
}

let num1 = parseInt(prompt("\nDame el numero de la base de la potencia:\n"));

while (num1 < 0) {
    num1 = parseInt(prompt("\nSolo numero natural para base de la potencia:\n"));
}

let num2 = parseInt(prompt("\nDame el numero de la potencia:\n"));

while (num2 < 0) {
    num2 = parseInt(prompt("\nSolo numero natural para de la potencia:\n"));
}

potencia(num1, num2)