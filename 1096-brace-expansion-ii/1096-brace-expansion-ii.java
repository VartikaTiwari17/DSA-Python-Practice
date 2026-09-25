import java.util.*;

class Solution {

    Set<String> parse(String s, int[] i) {

        Set<String> result = new TreeSet<>();
        Set<String> current = new TreeSet<>();
        current.add("");

        while (i[0] < s.length() &&
               s.charAt(i[0]) != '}' &&
               s.charAt(i[0]) != ',') {

            Set<String> part = new TreeSet<>();

            if (s.charAt(i[0]) == '{') {
                i[0]++; // skip {

                part = parse(s, i);

                i[0]++; // skip }
            } 
            else {
                part.add(String.valueOf(s.charAt(i[0])));
                i[0]++;
            }

            // Concatenation
            Set<String> temp = new TreeSet<>();

            for (String a : current) {
                for (String b : part) {
                    temp.add(a + b);
                }
            }

            current = temp;
        }

        result.addAll(current);

        // Union
        while (i[0] < s.length() && s.charAt(i[0]) == ',') {
            i[0]++;

            Set<String> next = parse(s, i);
            result.addAll(next);
        }

        return result;
    }

    public List<String> braceExpansionII(String expression) {
        int[] i = {0};

        Set<String> ans = parse(expression, i);

        return new ArrayList<>(ans);
    }
}