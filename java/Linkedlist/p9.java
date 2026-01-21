// Remove an element

import java.util.LinkedList;

public class p9 {
    public static void main(String[] args) {
        LinkedList<String> cities = new LinkedList<>();
        cities.add("Bangalore");
        cities.add("Chennai");
        cities.add("Delhi");

        cities.remove("Chennai");
        System.out.println(cities);
    }
}

//Output: [Bangalore, Delhi]