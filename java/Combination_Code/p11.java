// Product Prices

import java.util.*;

public class p11 {
    public static void main(String[] args) {
        LinkedList<String> products = new LinkedList<>();
        products.add("Laptop");
        products.add("Mobile");

        HashMap<String, Integer> prices = new HashMap<>();
        prices.put("Laptop", 50000);
        prices.put("Mobile", 20000);

        for (String p : products) {
            System.out.println(p + " costs " + prices.get(p));
        }
    }
}

//Output:
//Laptop costs 50000
//Mobile costs 20000
