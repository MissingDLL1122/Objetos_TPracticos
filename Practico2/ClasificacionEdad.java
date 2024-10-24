package Practico2;

import java.util.Scanner;

public class ClasificacionEdad {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicitar la edad al usuario
        System.out.print("Por favor, ingresa tu edad: ");
        int edad = scanner.nextInt();

        // Clasificar al usuario según su edad
        if (edad < 13) {
            System.out.println("Eres un niño.");
        } else if (edad >= 13 && edad <= 17) {
            System.out.println("Eres un adolescente.");
        } else if (edad >= 18 && edad <= 64) {
            System.out.println("Eres un adulto.");
        } else {
            System.out.println("Eres un adulto mayor.");
        }

        // Cerrar el scanner
        scanner.close();
    }
}
