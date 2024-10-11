const texto = prompt("Escribe la cadena:");

const polish = {
    "ą" : "a",
    "ć" : "c",
    "ę" : "e",
    "ł" : "l",
    "ń" : "n",
    "ó" : "o",
    "ś" : "s",
    "ź" : "z"
}

let new_texto = "";

let l = 1;

for (let i = 0; i < texto.length; i++) {

    let caracter = texto[i];

    if (polish[caracter]) {
        new_texto = new_texto + polish[caracter];
    } else {
        new_texto = new_texto + caracter;
    }
}

alert("Resultado:\n\n" + new_texto);