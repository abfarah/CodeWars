/*

By Abdullahi Farah

Unit Tests for codewars mutiply problem

Dependencies: 
		junit-4.10.jar
		hamcrest-core-2.1-rc4.jar


To Test: javac -cp .:junit-4.10.jar MultiplyTest.java
To Rum: java -cp .:junit-4.10.jar:hamcrest-core-2.1-rc4.jar org.junit.runner.JUnitCore MultiplyTest.java
*/

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MultiplyTest {
    
    @Test
    public void testCase1() {
      assertEquals("Nope!", 25, Multiply.multiply(5,5));
    }
    
}
