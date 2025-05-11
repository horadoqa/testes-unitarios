function adicionar(a, b) {
    return a + b;
}

function subtrair(a, b) {
    return a - b;
}

function multiplicar(a, b) {
    return a * b;
}

function dividir(a, b) {
    if (b === 0) throw new Error("Divisão por zero não é permitida.");
    return a / b;
}

function potencia(a, b) {
    return a ** b;
}

function raizQuadrada(a) {
    if (a < 0) throw new Error("Raiz de número negativo não é permitida.");
    return Math.sqrt(a);
}

function porcentagem(a, b) {
    return (a / 100) * b;
}

module.exports = {
    adicionar,
    subtrair,
    multiplicar,
    dividir,
    potencia,
    raizQuadrada,
    porcentagem
};
