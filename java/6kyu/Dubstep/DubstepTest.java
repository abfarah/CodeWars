/*

By Abdullahi Farah

Unit Tests for codewars dubstep problem

Dependencies: 
		junit-4.10.jar
		hamcrest-core-2.1-rc4.jar


To Test: javac -cp .:junit-4.10.jar DubstepTest.java
To Rum: java -cp .:junit-4.10.jar:hamcrest-core-2.1-rc4.jar org.junit.runner.JUnitCore DubstepTest.java
*/

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class DubstepTest {
    @Test
    public void Test1() {
      assertEquals("ABC", new Dubstep().SongDecoder("WUBWUBABCWUB"));
    }
    @Test
    public void Test2()
    {
       assertEquals("R L", new Dubstep().SongDecoder("RWUBWUBWUBLWUB"));
    }
}
