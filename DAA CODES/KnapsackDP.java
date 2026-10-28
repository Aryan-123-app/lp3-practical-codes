import java.util.Scanner;

public class KnapsackDP {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        int[] value = new int[n];
        int[] weight = new int[n];

        System.out.println("Enter value and weight of each item:");

        for (int i = 0; i < n; i++) {

            System.out.print("Value of item " + (i + 1) + ": ");
            value[i] = sc.nextInt();

            System.out.print("Weight of item " + (i + 1) + ": ");
            weight[i] = sc.nextInt();
        }

        System.out.print("Enter knapsack capacity: ");
        int W = sc.nextInt();

        int[][] dp = new int[n + 1][W + 1];

        for (int i = 1; i <= n; i++) {

            for (int w = 0; w <= W; w++) {

                if (weight[i - 1] <= w) {

                    dp[i][w] = Math.max(
                            dp[i - 1][w],
                            value[i - 1] + dp[i - 1][w - weight[i - 1]]
                    );

                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        System.out.println("Maximum value = " + dp[n][W]);

        System.out.println("Selected items:");

        int w = W;

        for (int i = n; i > 0; i--) {

            if (dp[i][w] != dp[i - 1][w]) {

                System.out.println("Item " + i);
                w = w - weight[i - 1];
            }
        }

        sc.close();
    }
}