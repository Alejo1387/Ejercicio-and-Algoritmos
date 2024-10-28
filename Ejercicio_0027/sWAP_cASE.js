function swap_case(s) {
    const array_min = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    const array_may = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

    let new_tex = "";

    for (let i = 0; i < s.length; i++) {
        let found = false;
        
        for (let j = 0; j < array_min.length; j++) {
            if (s[i] === array_min[j]) {
                new_tex += array_may[j];
                found = true;
                break;
            } else if (s[i] === array_may[j]) {
                new_tex += array_min[j];
                found = true;
                break;
            }
        }
        if (!found) {
            new_tex += s[i];
        }
    }

    alert(`
    Cadena normal:
    ${texto}

    Cadena modificada:
    ${new_tex}
    `)
}

const texto = prompt("\nDime la cadena de texto:\n");
swap_case(texto)