let numbers = "(";

let n = 0;

let num = parseInt(prompt("\nDame el 1 numero:\n"));
if (num > 0) {
    n += 1;
}
numbers += num.toString() + ", ";

num = parseInt(prompt("\nDame el 2 numero:\n"));
if (num > 0) {
    n += 1;
}
numbers += num.toString() + ", ";

num = parseInt(prompt("\nDame el 1 numero:\n"));
if (num > 0) {
    n += 1;
}
numbers += num.toString() + ")";

if (n === 2) {
    alert(numbers + "  ->  True")
} else {
    alert(numbers + "  ->  False")
}