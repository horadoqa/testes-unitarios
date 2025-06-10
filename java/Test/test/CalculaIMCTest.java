package Test.test;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import Test.console.IMCCalculadora;
import Test.console.Pessoa;

public class CalculaIMCTest {

    @Test
    public void testCalculoIMC() {
        Pessoa pessoa = new Pessoa("João", 25, 1.87, 55);
        double imc = IMCCalculadora.calcularIMC(pessoa);
        assertEquals(15.72, imc, 0.01); // margem de erro de 0.01
    }

    @Test
    public void testClassificacaoAbaixoPeso() {
        assertEquals("Abaixo do peso", IMCCalculadora.classificarIMC(17.0));
    }

    @Test
    public void testClassificacaoPesoNormal() {
        assertEquals("Peso normal", IMCCalculadora.classificarIMC(22.0));
    }

    @Test
    public void testClassificacaoSobrepeso() {
        assertEquals("Sobrepeso", IMCCalculadora.classificarIMC(28.0));
    }

    @Test
    public void testClassificacaoObesidade() {
        assertEquals("Obesidade", IMCCalculadora.classificarIMC(35.0));
    }
}
