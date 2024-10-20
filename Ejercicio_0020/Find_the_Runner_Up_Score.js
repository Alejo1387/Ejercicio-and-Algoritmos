function second() {
    let min = array[0]
    for (let i = 0; i < n; i++) {
        if (array[i] < min) {
            min = array[i]
        }
    }
    let max2 = min;
    let max = array[0];
    for (let j = 0; j < n; j++) {
        if (array[j] > max) {
            max2 = max;
            max = array[j];
        } else if (array[j] >= max2 && array[j] < max) {
            max2 = array[j]
        }
    }
    let array_Cadena = `[${array.join(', ')}]`;
    alert(`Array:
        ${array_Cadena}
    
        Segundo lugar:  ${max2}
        `);
}

const n = parseInt(prompt("\nDime la cantidad de numeros en el array:\n"));

let array = [];

for (let i = 0; i < n; i++) {
    let num = parseInt(prompt("\nDime el "+(i+1)+" elemento del array:\n"))
    array.push(num)
}

second()