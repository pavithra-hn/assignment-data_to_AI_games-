// Player Scores

import java.util.*;

public class p14 {
    public static void main(String[] args) {
        LinkedList<String> players = new LinkedList<>();
        players.add("Alex");
        players.add("Blake");
        players.add("Casey");

        HashMap<String, Integer> scores = new HashMap<>();
        scores.put("Alex", 150);
        scores.put("Blake", 120);
        scores.put("Casey", 180);

        for (String player : players) {
            System.out.println(player + " Score: " + scores.get(player));
        }
    }
}

//Output:
//Alex Score: 150
//Blake Score: 120
//Casey Score: 180
