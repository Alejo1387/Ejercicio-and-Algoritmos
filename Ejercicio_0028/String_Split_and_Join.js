const entrada = prompt("\nIntroduce el texto:\n");

const space = entrada.split(" ");

const result = space.join("-");

alert(`
    Texto:
    ${entrada}

    Resultado:
    ${result}
`)