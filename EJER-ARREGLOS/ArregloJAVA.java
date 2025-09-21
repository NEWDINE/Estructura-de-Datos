import java.util.Scanner;

public class ArregloJAVA {
    static String[] meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
    static String[] departamentos = {"Ropa", "Deportes", "Juguetería"};
    static int[][] ventas = new int[12][3];
    static Scanner sc = new Scanner(System.in);

    public static void insertarVenta() {
        System.out.print("Ingresa el número de mes (1-12): ");
        int mes = sc.nextInt() - 1;
        System.out.print("Ingresa el departamento (1=Ropa, 2=Deportes, 3=Juguetería): ");
        int depto = sc.nextInt() - 1;
        System.out.print("Ingresa el valor de la venta: ");
        int valor = sc.nextInt();
        ventas[mes][depto] = valor;
        System.out.println("Venta registrada.\n");
    }

    public static void buscarVenta() {
        System.out.print("Ingresa el número de mes (1-12): ");
        int mes = sc.nextInt() - 1;
        System.out.print("Ingresa el departamento (1=Ropa, 2=Deportes, 3=Juguetería): ");
        int depto = sc.nextInt() - 1;
        System.out.println("Venta encontrada: " + ventas[mes][depto] + "\n");
    }

    public static void eliminarVenta() {
        System.out.print("Ingresa el número de mes (1-12): ");
        int mes = sc.nextInt() - 1;
        System.out.print("Ingresa el departamento (1=Ropa, 2=Deportes, 3=Juguetería): ");
        int depto = sc.nextInt() - 1;
        ventas[mes][depto] = 0;
        System.out.println("Venta eliminada.\n");
    }

    public static void mostrarTabla() {
        System.out.printf("%-12s", "Mes");
        for (String dep : departamentos) {
            System.out.printf("%-12s", dep);
        }
        System.out.println();
        for (int i = 0; i < meses.length; i++) {
            System.out.printf("%-12s", meses[i]);
            for (int j = 0; j < departamentos.length; j++) {
                System.out.printf("%-12d", ventas[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        while (true) {
            System.out.println("--- Menú de Ventas ---");
            System.out.println("1. Insertar venta");
            System.out.println("2. Buscar venta");
            System.out.println("3. Eliminar venta");
            System.out.println("4. Mostrar tabla completa");
            System.out.println("5. Salir");
            System.out.print("Selecciona una opción: ");
            int opcion = sc.nextInt();

            if (opcion == 1) {
                insertarVenta();
            } else if (opcion == 2) {
                buscarVenta();
            } else if (opcion == 3) {
                eliminarVenta();
            } else if (opcion == 4) {
                mostrarTabla();
            } else if (opcion == 5) {
                break;
            } else {
                System.out.println("Opción no válida.\n");
            }
        }
    }
}
