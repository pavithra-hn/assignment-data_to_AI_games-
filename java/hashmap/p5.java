//Access value using key

import java.util.HashMap;

public class p5 {
    public static void main(String[] args) {
        HashMap<String, Integer> age = new HashMap<>();
        age.put("Pavi", 22);

        System.out.println(age.get("Pavi"));
    }
}


//Output: 22