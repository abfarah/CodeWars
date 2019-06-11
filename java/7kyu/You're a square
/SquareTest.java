/*

By Abdullahi Farah

Unit Tests for codewars square problem

Dependencies: 
		junit-4.10.jar
		hamcrest-core-2.1-rc4.jar


To Test: javac -cp .:junit-4.10.jar SquareTest.java
To Rum: java -cp .:junit-4.10.jar:hamcrest-core-2.1-rc4.jar org.junit.runner.JUnitCore SquareTest.java
*/

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class SquareTest {

    @Test
    public void test() {
      assertEquals("negative numbers aren't square numbers", false, Square.isSquare(-1));
      assertEquals("0 is a square number (0 * 0)",    true,   Square.isSquare(0));
      assertEquals("3 isn't a square number", false,  Square.isSquare(3));
      assertEquals("4 is a square number (2 * 2)",    true,   Square.isSquare(4));
      assertEquals("25 is a square number (5 * 5)",   true,   Square.isSquare(25));
      assertEquals("26 isn't a square number",false,  Square.isSquare(26));
    }
    
}
