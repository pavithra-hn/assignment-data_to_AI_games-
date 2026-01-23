// Check key existence

import java.util.HashMap;

public class p6 {
    public static void main(String[] args) {
        HashMap<String, String> map = new HashMap<>();
        map.put("India", "Delhi");

        System.out.println(map.containsKey("India"));
    }
}

//output: true