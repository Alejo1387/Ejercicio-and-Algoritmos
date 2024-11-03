let num = parseInt(prompt("\nDime la cantidad de me gusta:\n"));

let array_like = [];

for (let i = 0; i < num; i++) {
    let name = prompt("\nDime el " + (i+1) + " me gusta:  ").trim();
    array_like.push(name)
}

if (num < 0) {
    alert("\nError\n");
} else if (num == 0) {
    alert("\nNo one likes this\n");
} else if (num >= 1 && num <= 3) {
    if (num == 1) {
        alert("\n" + array_like[0] + " likes this\n");
    } else if (num == 2) {
        alert("\n" + array_like[0] + " and " + array_like[1] + " likes this\n");
    } else {
        alert("\n" + array_like[0] + ", " + array_like[1] + " and " + array_like[2] + " likes this\n");
    }
} else {
    alert("\n" + array_like[0] + ", " + array_like[1] + " and " + (num - 2) + " likes this\n");
}