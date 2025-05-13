public class App {
    public static void main(String[] args) throws Exception {
     int numero = 10000;
        long numeroLargo = numero; // Conversión implícita

        double numeroDecimal = numeroLargo; // También implícita

        float flotante = (float) numeroDecimal; // Conversión explícita
        short numeroCorto = (short) numero;     // Explícita, aunque sin decimales

        System.out.println("int: " + numero);
        System.out.println("long: " + numeroLargo);
        System.out.println("double: " + numeroDecimal);
        System.out.println("float: " + flotante);
        System.out.println("short: " + numeroCorto);      
        }
}
