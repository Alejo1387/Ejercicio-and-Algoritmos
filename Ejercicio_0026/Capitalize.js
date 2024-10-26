function solvee(s) {
    s += " ";
    let mesage = "";
    let texto = "";

    for (let i = 0; i < s.length; i++) {
        if (s[i] === " "){
            mesage += texto.charAt(0).toUpperCase() + texto.slice(1).toLowerCase() + " ";
            texto = "";
        } else {
            texto += s[i];
        }
    }

    alert("\nResultado:  " + mesage + "\n")
}

let s = prompt("\nEscribe la cadena:\n")

solvee(s)