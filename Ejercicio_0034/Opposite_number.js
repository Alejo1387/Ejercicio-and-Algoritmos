function contraparte(n) {
    let num2 = parseFloat(n);
    if (num2 === 0) {
        alert("\nEl 0 no tiene contraparte\n");
    } else if (num2 > 0) {
        alert("\nNumero: " + num2 + "\n\nContraparte: " + -num2 + "\n");
    } else {
        alert("\nNumero: " + num2 + "\n\nContraparte: " + Math.abs(num2) + "\n");
    }
}

const num = prompt("\nEscribe el numero:\n");
contraparte(num);
