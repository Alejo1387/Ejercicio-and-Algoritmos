function array_cuadrado() {
    let min = array[0];
    let max = array[0];
    for (let i = 0; i < cantidad_array; i++) {
        if (array[i] < min) {
            min = array[i];
        }
        if (array[i] > max) {
            max = array[i];
        }
    }
    let array_Cadena = `[${array.join(', ')}]`;
    alert(`Array:
    ${array_Cadena}

    Numero minimo:
    ${min}

    Numero maximo:
    ${max}`)
}


const cantidad_array = parseInt(prompt("\nDime la cantidad de numeros en el array:\n"));

let array = [];

for (let i = 0; i < cantidad_array; i++) {
    let num = parseInt(prompt("\nDime el "+(i+1)+" elemento del array:\n"));
    array.push(num);
}

array_cuadrado()