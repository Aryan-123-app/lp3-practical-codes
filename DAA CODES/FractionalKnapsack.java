import java.util.*;

class Item {
    int value;
    int weight;
    double ratio;

    Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
        this.ratio = (double) value / weight;
    }
}

public class FractionalKnapsack {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        Item[] items = new Item[n];

        System.out.println("Enter value and weight of each item:");

        for (int i = 0; i < n; i++) {

            System.out.print("Item " + (i + 1) + " value: ");
            int value = sc.nextInt();

            System.out.print("Item " + (i + 1) + " weight: ");
            int weight = sc.nextInt();

            items[i] = new Item(value, weight);
        }

        System.out.print("Enter knapsack capacity: ");
        int capacity = sc.nextInt();

        // Sort according to value/weight ratio
        Arrays.sort(items, (a, b) ->
                Double.compare(b.ratio, a.ratio));

        double totalValue = 0;
        int remainingCapacity = capacity;

        System.out.println("\nSelected Items:");

        for (int i = 0; i < n; i++) {

            if (remainingCapacity == 0)
                break;

            if (items[i].weight <= remainingCapacity) {

                remainingCapacity -= items[i].weight;
                totalValue += items[i].value;

                System.out.println(
                        "Item " + (i + 1) +
                        " -> 100% selected"
                );

            } else {

                double fraction =
                        (double) remainingCapacity / items[i].weight;

                totalValue += items[i].value * fraction;

                System.out.printf(
                        "Item %d -> %.2f%% selected%n",
                        i + 1,
                        fraction * 100
                );

                remainingCapacity = 0;
            }
        }

        System.out.printf(
                "\nMaximum value = %.2f%n",
                totalValue
        );

        sc.close();
    }
}