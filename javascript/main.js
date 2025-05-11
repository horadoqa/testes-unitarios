const readline = require('readline');
const {
    adicionar, subtrair, multiplicar, dividir,
    potencia, raizQuadrada, porcentagem
} = require('./calculadora');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function obterNumero(pergunta) {
    return new Promise(resolve => {
        rl.question(pergunta, resposta => {
            const numero = parseFloat(resposta);
            if (isNaN(numero)) {
                console.log("❌ Entrada inválida. Tente novamente.");
                resolve(obterNumero(pergunta)); // recursão para repetir
            } else {
                resolve(numero);
            }
        });
    });
}

function exibirMenu() {
    console.log(`
📘 CALCULADORA MODERNA
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz quadrada
7. Porcentagem
8. Sair
`);
}

async function main() {
    while (true) {
        exibirMenu();
        const escolha = await obterNumero("Escolha uma opção (1-8): ");

        try {
            switch (escolha) {
                case 1: {
                    const a = await obterNumero("Digite o primeiro número: ");
                    const b = await obterNumero("Digite o segundo número: ");
                    console.log(`Resultado: ${adicionar(a, b)}`);
                    break;
                }
                case 2: {
                    const a = await obterNumero("Digite o primeiro número: ");
                    const b = await obterNumero("Digite o segundo número: ");
                    console.log(`Resultado: ${subtrair(a, b)}`);
                    break;
                }
                case 3: {
                    const a = await obterNumero("Digite o primeiro número: ");
                    const b = await obterNumero("Digite o segundo número: ");
                    console.log(`Resultado: ${multiplicar(a, b)}`);
                    break;
                }
                case 4: {
                    const a = await obterNumero("Digite o primeiro número: ");
                    const b = await obterNumero("Digite o segundo número: ");
                    console.log(`Resultado: ${dividir(a, b)}`);
                    break;
                }
                case 5: {
                    const a = await obterNumero("Digite a base: ");
                    const b = await obterNumero("Digite o expoente: ");
                    console.log(`Resultado: ${potencia(a, b)}`);
                    break;
                }
                case 6: {
                    const a = await obterNumero("Digite o número: ");
                    console.log(`Resultado: ${raizQuadrada(a)}`);
                    break;
                }
                case 7: {
                    const a = await obterNumero("Digite a porcentagem (%): ");
                    const b = await obterNumero("Digite o número base: ");
                    console.log(`Resultado: ${porcentagem(a, b)}`);
                    break;
                }
                case 8:
                    console.log("👋 Encerrando a calculadora.");
                    rl.close();
                    return;
                default:
                    console.log("⚠️ Opção inválida. Tente novamente.");
            }
        } catch (e) {
            console.log(`❗ Erro: ${e.message}`);
        }
    }
}

main();
