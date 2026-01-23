//  Employee Salary Lookup

import java.util.*;

public class p10 {
    public static void main(String[] args) {
        LinkedList<Integer> empIds = new LinkedList<>();
        empIds.add(101);
        empIds.add(102);

        HashMap<Integer, Integer> salary = new HashMap<>();
        salary.put(101, 30000);
        salary.put(102, 35000);

        for (int id : empIds) {
            System.out.println("Employee " + id + " Salary: " + salary.get(id));
        }
    }
}


//Output:
//Employee 101 Salary: 30000
//Employee 102 Salary: 35000