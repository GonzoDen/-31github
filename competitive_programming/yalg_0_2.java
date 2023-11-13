import java.util.Scanner;
import java.io.IOException;

public class b {
    static int gcd(int a, int b)
    {
        int i;
        if (a < b)
            i = a;
        else
            i = b;

        for (i = i; i > 1; i--) {

            if (a % i == 0 && b % i == 0)
                return i;
        }

        return 1;
    }

    public static void main(String[] args) throws IOException {
    	Scanner input = new Scanner(System.in);
    	int a = input.nextInt();
    	int b = input.nextInt();
    	int c = input.nextInt();
    	int d = input.nextInt();

    	int numerator = 0;
    	int denominator = 0;

    	if (b == d) {
    		numerator = a + c;
    		denominator = b;
    	}
    	else {
    		denominator = b * d;
    		numerator = (a * d) + (b * c);
    	}
    	int gcd = gcd(numerator, denominator);
    	int numerator_upd = numerator / gcd;
    	int denominator_upd = denominator / gcd;

    	System.out.printf("%d %d%n", numerator_upd, denominator_upd);
   	
   	}
}