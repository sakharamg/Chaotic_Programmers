import java.util.regex.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class q3 {
    public boolean fun1(String myStr) 
    {
	// write your code here
	 if (myStr.length()<=6)
	 {
      return (Pattern.matches("[a]+[b[c]]*[.a]", myStr));
    }
    else{
        return false;
    }
    }
        
    public String fun2(String myStr, String patt) 
    {
	// write your code here
	
	List<String> matchedGroups = new ArrayList<>();
	Pattern compiledPattern = Pattern.compile(patt);
	Matcher m = compiledPattern.matcher(myStr);
	while (m.find()) {
		matchedGroups.add(m.group());
	}
	Collections.sort(matchedGroups);
	String maxString = "#";
	int length = 0;
		for (int i = 0; i < matchedGroups.size(); i++) {
		String t = matchedGroups.get(i);
		if (length < t.length()) {
			length = t.length();
			maxString = t;
		}
	}
	return maxString;
   }
}  


