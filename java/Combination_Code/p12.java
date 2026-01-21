// City Population

import java.util.*;

public class p12 {
    public static void main(String[] args) {
        LinkedList<String> cities = new LinkedList<>();
        cities.add("Bangalore");
        cities.add("Chennai");

        HashMap<String, Integer> population = new HashMap<>();
        population.put("Bangalore", 120);
        population.put("Chennai", 100);

        for (int i = 0; i < cities.size(); i++) {
            String city = cities.get(i);
            System.out.println(city + " Population: " + population.get(city));
        }
    }
}

//Output:
//Bangalore Population: 120
//Chennai Population: 100