const opcion_machina = Math.floor(Math.random() * 3) + 1;

let opcion_machina2 = "";

switch (opcion_machina) {
    case 1: opcion_machina2 = "Tijera"; break;
    case 2: opcion_machina2 = "Papel"; break;
    case 3: opcion_machina2 = "Piedra"; break;
}

let mensaje = `Vamos a jugar Piedra, Papel y Tijera, estas son las opciones:

    1. Piedra
    2. Papel
    3. Tijera

Elige la opción numérica:`;

let opcion_person = parseInt(prompt(mensaje));

let opcion_person2 = "";

switch (opcion_person) {
    case 1: opcion_person2 = "Piedra"; break;
    case 2: opcion_person2 = "Papel"; break;
    case 3: opcion_person2 = "Tijera"; break;
}

if (opcion_machina2 === opcion_person2) {
    alert(`
    Maquina:    ${opcion_machina2}
    Tú:         ${opcion_person2}
    Resultado:  Empate!!
    `);
} else if (opcion_machina2 === "Papel") {
    if (opcion_person2 === "Tijera") {
        alert(`
            Maquina:    ${opcion_machina2}
            Tú:         ${opcion_person2}
            Resultado:  Ganaste!!
            `);
    } else if (opcion_person2 === "Piedra") {
        alert(`
            Maquina:    ${opcion_machina2}
            Tú:         ${opcion_person2}
            Resultado:  Perdiste!!
            `);
    }
} else if (opcion_machina2 === "Piedra") {
    if (opcion_person2 === "Papel") {
        alert(`
            Maquina:    ${opcion_machina2}
            Tú:         ${opcion_person2}
            Resultado:  Ganaste!!
            `);
    } else if (opcion_person2 === "Tijera") {
        alert(`
            Maquina:    ${opcion_machina2}
            Tú:         ${opcion_person2}
            Resultado:  Perdiste!!
            `);
    }
} else if (opcion_machina2 === "Tijera") {
    if (opcion_person2 === "Piedra") {
        alert(`
            Maquina:    ${opcion_machina2}
            Tú:         ${opcion_person2}
            Resultado:  Ganaste!!
            `);
    } else if (opcion_person2 === "Papel") {
        alert(`
            Maquina:    ${opcion_machina2}
            Tú:         ${opcion_person2}
            Resultado:  Perdiste!!
            `);
    }
}