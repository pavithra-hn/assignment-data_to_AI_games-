//Course Duration

import java.util.*;

public class p13 {
    public static void main(String[] args) {
        LinkedList<String> courses = new LinkedList<>();
        courses.add("Java");
        courses.add("Python");

        HashMap<String, Integer> duration = new HashMap<>();
        duration.put("Java", 60);
        duration.put("Python", 45);

        for (String c : courses) {
            System.out.println(c + " Duration: " + duration.get(c) + " days");
        }
    }
}


//Output:
//Java Duration: 60 days    
//Python Duration: 45 days
