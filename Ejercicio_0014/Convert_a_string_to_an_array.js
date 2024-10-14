const texto = prompt("Dime el String:");
let texto1 = texto + " ";

let textoarray = "";
let array = [];

for (let i = 0; i < texto1.length; i++) {
    if (texto1[i] !== " ") {
        textoarray = textoarray + texto1[i];
    } else {
        if (textoarray !== "") {
            array.push(textoarray);
        }
        textoarray = "";
    }
}

alert("Texto: " + texto + "\nArray: " + JSON.stringify(array));