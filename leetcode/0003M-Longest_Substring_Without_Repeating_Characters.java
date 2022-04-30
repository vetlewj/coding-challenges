public class Solution {
    public int lengthOfLongestSubstring(String s) {
        StringBuilder currentSubstring = new StringBuilder();
        StringBuilder maxSubstring = new StringBuilder();
        for (int i = 0; i < s.length(); i ++){
            boolean hasFoundRepChar = false;
            int index = i;
            while (!hasFoundRepChar){
                String currentChar = String.valueOf(s.charAt(index));
                if (!currentSubstring.toString().contains(currentChar)){
                    currentSubstring.append(currentChar);
                    if (currentSubstring.toString().length() > maxSubstring.toString().length()){
                        maxSubstring = new StringBuilder();
                        maxSubstring.append(currentSubstring);
                    }
                }
                else {
                    currentSubstring = new StringBuilder();
                    hasFoundRepChar = true;
                }
                if (index+1 < s.length()){
                    index++;}
                else{
                    hasFoundRepChar = true;
                }
            }
        }
        return maxSubstring.toString().length();
    }
}