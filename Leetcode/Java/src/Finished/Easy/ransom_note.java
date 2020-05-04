import java.util.*;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> table = new HashMap<>();
        for (int i = 0; i < magazine.length(); i++) {
            char key = magazine.charAt(i);
            if (table.containsKey(key)) {
                table.put(key, table.get(key) + 1);
            } else {
                table.put(key, 1);
            }
        }
        for (int i = 0; i < ransomNote.length(); i++) {
            char key = ransomNote.charAt(i);
            if (table.containsKey(key)) {
                table.put(key, table.get(key) - 1);
                if (table.get(key) < 0) {
                    return false;
                }
            } else {
                return false;
            }
        }
        return (true);
    }
}