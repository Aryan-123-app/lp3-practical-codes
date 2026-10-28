import java.util.Scanner;

public class NQueens {

    static int[][] board;
    static int n;

    // Check whether a position is safe
    static boolean isSafe(int row, int col) {

        // Check column above
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1)
                return false;
        }

        // Check upper-left diagonal
        for (int i = row - 1, j = col - 1;
             i >= 0 && j >= 0; i--, j--) {

            if (board[i][j] == 1)
                return false;
        }

        // Check upper-right diagonal
        for (int i = row - 1, j = col + 1;
             i >= 0 && j < n; i--, j++) {

            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    // Solve using backtracking
    static boolean solveNQueens(int row) {

        if (row == n)
            return true;

        // First queen is already placed
        if (row == 0)
            return solveNQueens(row + 1);

        for (int col = 0; col < n; col++) {

            if (isSafe(row, col)) {

                board[row][col] = 1;

                if (solveNQueens(row + 1))
                    return true;

                // Backtrack
                board[row][col] = 0;
            }
        }

        return false;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the value of N: ");
        n = sc.nextInt();

        if (n < 1) {
            System.out.println("N must be at least 1.");
            sc.close();
            return;
        }

        board = new int[n][n];

        // Place the first queen at (0, 0)
        board[0][0] = 1;

        if (solveNQueens(0)) {

            System.out.println("Solution Matrix:");

            for (int i = 0; i < n; i++) {

                for (int j = 0; j < n; j++) {
                    System.out.print(board[i][j] + " ");
                }

                System.out.println();
            }

        } else {
            System.out.println(
                    "No solution exists with the first queen at (0, 0)."
            );
        }

        sc.close();
    }
}