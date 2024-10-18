function bisiesto() {
    let texto = false;
    if ((year % 4 === 0 && year & 100 !== 0) || (year % 400 === 0)) {
        texto = true;
    }
    alert(texto)
}

const year = parseInt(prompt("\nEscribe al año:\n"))

bisiesto()