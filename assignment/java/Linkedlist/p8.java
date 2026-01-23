// Add elements at first and last

import java.util.LinkedList;

public class p8 {
    public static void main(String[] args) {
        LinkedList<Integer> numbers = new LinkedList<>();
        numbers.add(20);
        numbers.addFirst(10);
        numbers.addLast(30);

        System.out.println(numbers);
    }
}

//Output: [10, 20, 30]