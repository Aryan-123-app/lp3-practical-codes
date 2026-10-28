import java.util.*;

public class GreedyHuffmanEncoding {

    static class Node {
        char ch;
        int freq;
        Node left, right;

        Node(char ch, int freq) {
            this.ch = ch;
            this.freq = freq;
        }

        Node(int freq, Node left, Node right) {
            this.freq = freq;
            this.left = left;
            this.right = right;
        }
    }

    static Node root;
    static Map<Character, String> codes = new HashMap<>();
    static String originalText = "";

    // Build Huffman Tree
    static void buildTree(String text) {

        Map<Character, Integer> freq = new HashMap<>();

        for (char c : text.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        PriorityQueue<Node> pq =
                new PriorityQueue<>(Comparator.comparingInt(n -> n.freq));

        for (Map.Entry<Character, Integer> entry : freq.entrySet()) {
            pq.add(new Node(entry.getKey(), entry.getValue()));
        }

        // Special case: only one unique character
        if (pq.size() == 1) {
            Node only = pq.poll();
            root = new Node(only.freq, only, null);
        } else {
            while (pq.size() > 1) {

                Node left = pq.poll();
                Node right = pq.poll();

                Node parent = new Node(
                        left.freq + right.freq,
                        left,
                        right
                );

                pq.add(parent);
            }

            root = pq.poll();
        }

        codes.clear();
        generateCodes(root, "");
    }

    // Generate Huffman Codes
    static void generateCodes(Node node, String code) {

        if (node == null)
            return;

        if (node.left == null && node.right == null) {
            codes.put(node.ch, code.length() == 0 ? "0" : code);
            return;
        }

        generateCodes(node.left, code + "0");
        generateCodes(node.right, code + "1");
    }

    // Encode Text
    static String encode(String text) {

        StringBuilder encoded = new StringBuilder();

        for (char c : text.toCharArray()) {
            encoded.append(codes.get(c));
        }

        return encoded.toString();
    }

    // Decode Text
    static String decode(String encoded) {

        StringBuilder decoded = new StringBuilder();

        Node current = root;

        for (char bit : encoded.toCharArray()) {

            if (bit == '0')
                current = current.left;
            else
                current = current.right;

            if (current.left == null && current.right == null) {
                decoded.append(current.ch);
                current = root;
            }
        }

        return decoded.toString();
    }

    // Display Huffman Codes
    static void displayCodes() {

        System.out.println("\nHuffman Codes:");

        for (Map.Entry<Character, String> entry : codes.entrySet()) {

            char c = entry.getKey();

            if (c == ' ')
                System.out.println("[space] : " + entry.getValue());
            else
                System.out.println(c + " : " + entry.getValue());
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter text: ");
        originalText = sc.nextLine();

        if (originalText.isEmpty()) {
            System.out.println("Text cannot be empty.");
            sc.close();
            return;
        }

        buildTree(originalText);

        int choice;

        do {
            System.out.println("\n----- HUFFMAN ENCODING -----");
            System.out.println("1. Build Huffman Tree");
            System.out.println("2. Encode the Text");
            System.out.println("3. Decode the Text");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {

                case 1:
                    buildTree(originalText);
                    System.out.println("\nHuffman Tree built successfully.");
                    displayCodes();
                    break;

                case 2:
                    String encoded = encode(originalText);

                    System.out.println("\nOriginal Text : " + originalText);
                    System.out.println("Encoded Text : " + encoded);

                    displayCodes();
                    break;

                case 3:
                    String encodedText = encode(originalText);
                    String decodedText = decode(encodedText);

                    System.out.println("\nEncoded Text : " + encodedText);
                    System.out.println("Decoded Text : " + decodedText);
                    break;

                case 4:
                    System.out.println("Program terminated.");
                    break;

                default:
                    System.out.println("Invalid choice.");
            }

        } while (choice != 4);

        sc.close();
    }
}