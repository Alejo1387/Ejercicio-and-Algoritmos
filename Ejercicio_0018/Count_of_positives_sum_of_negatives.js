function numeros() {
    let can_pos = 0;
    let neg = 0;
    for (let i = 0; i < cantidad_array; i++) {
        if (array[i] > 0){
            can_pos += 1;
        }
        if (array[i] < 0) {
            neg += array[i];
        }
    }
    let array_Cadena = `[${array.join(', ')}]`;
    alert(`Array:
    ${array_Cadena}

    Cantidad de positivos:  ${can_pos}

    Suma de negativos:  ${neg}
    `);
}

const cantidad_array = parseInt(prompt("\nCantidad de numeros:\n"));

let array = [];

for (let i = 0; i < cantidad_array; i++) {
    let num = parseInt(prompt("\nDime el "+(i+1)+" elemento del array:\n"))
    array.push(num)
}

numeros()