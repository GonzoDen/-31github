import java.util.Scanner;
import java.io.IOException;

public class first_a {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();

        int[] array = new int[n];

        for (int i = 0; i < n; i++) {
            array[i] = input.nextInt();
        }

        int x = input.nextInt();

        int count_small = 0;
        int count_other = 0;

        for (int j = 0; j < n; j++) {
            if (array[j] < x) {
                count_small++;
            } else {
                count_other++;
            }
        }

        System.out.println(count_small);
        System.out.println(count_other);
        input.close();

    }
}