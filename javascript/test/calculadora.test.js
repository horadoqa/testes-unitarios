const {
    adicionar,
    subtrair,
    multiplicar,
    dividir,
    potencia,
    raizQuadrada,
    porcentagem
} = require('../calculadora');

describe('Funções da Calculadora', () => {

    test('Adição: 2 + 3 deve retornar 5', () => {
        expect(adicionar(2, 3)).toBe(5);
    });

    test('Subtração: 10 - 4 deve retornar 6', () => {
        expect(subtrair(10, 4)).toBe(6);
    });

    test('Multiplicação: 3 * 7 deve retornar 21', () => {
        expect(multiplicar(3, 7)).toBe(21);
    });

    test('Divisão: 10 / 2 deve retornar 5', () => {
        expect(dividir(10, 2)).toBe(5);
    });

    test('Divisão por zero deve lançar erro', () => {
        expect(() => dividir(5, 0)).toThrow('Divisão por zero não é permitida.');
    });

    test('Potência: 2^3 deve retornar 8', () => {
        expect(potencia(2, 3)).toBe(8);
    });

    test('Raiz quadrada: raiz quadrada de 25 deve retornar 5', () => {
        expect(raizQuadrada(25)).toBe(5);
    });

    test('Raiz quadrada de número negativo deve lançar erro', () => {
        expect(() => raizQuadrada(-9)).toThrow('Raiz de número negativo não é permitida.');
    });

    test('Porcentagem: 10% de 200 deve retornar 20', () => {
        expect(porcentagem(10, 200)).toBe(20);
    });
});
