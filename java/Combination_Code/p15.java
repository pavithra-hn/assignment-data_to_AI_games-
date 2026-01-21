// Game Levels and Difficulty

import java.util.*;

public class p15 {
    public static void main(String[] args) {
        LinkedList<String> levels = new LinkedList<>();
        levels.add("Level 1");
        levels.add("Level 2");
        levels.add("Level 3");

        HashMap<String, String> difficulty = new HashMap<>();
        difficulty.put("Level 1", "Easy");
        difficulty.put("Level 2", "Medium");
        difficulty.put("Level 3", "Hard");

        for (int i = 0; i < levels.size(); i++) {
            String level = levels.get(i);
            System.out.println(level + " Difficulty: " + difficulty.get(level));
        }
    }
}

//Output:
//Level 1 Difficulty: Easy
//Level 2 Difficulty: Medium
//Level 3 Difficulty: Hard
