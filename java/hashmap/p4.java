//Store roll number and name

import java.util.HashMap;

public class p4 {
    public static void main(String[] args) {
        HashMap<Integer, String> students = new HashMap<>();
        students.put(1, "Pavi");
        students.put(2, "Anu");

        System.out.println(students);
    }
}


//output : {1=Pavi, 2=Anu}