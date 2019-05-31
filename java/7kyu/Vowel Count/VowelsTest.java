/*

By Abdullahi Farah

Unit Tests for codewars vowel problem

Dependencies: 
		junit-4.10.jar
		hamcrest-core-2.1-rc4.jar


To Test: javac -cp .:junit-4.10.jar VowelsTest.java
To Rum: java -cp .:junit-4.10.jar:hamcrest-core-2.1-rc4.jar org.junit.runner.JUnitCore VowelsTest.java
*/

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class VowelsTest {

    @Test
    public void testCase1() {
      assertEquals("Nope!", 5, Vowels.getCount("abracadabra"));
    }
    
}
