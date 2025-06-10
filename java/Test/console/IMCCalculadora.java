package Test.console;

public class IMCCalculadora {
    
    // Método 1 - calcularIMC(Pessoa pessoa)
    public static double calcularIMC(Pessoa pessoa) {
        return pessoa.getPeso() / (pessoa.getAltura() * pessoa.getAltura());
    }

    // Método 2 - classificarIMC(double imc)
    public static String classificarIMC(double imc) {
        if (imc < 18.5) return "Abaixo do peso";
        else if (imc < 25) return "Peso normal";
        else if (imc < 30) return "Sobrepeso";
        else return "Obesidade";
    }
}
