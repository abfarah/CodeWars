import java.lang.Math;
public class Square {    
    public static boolean isSquare(int n) {    
        if(n < 0){
          return false;
        }
        int a = (int) Math.sqrt(n);
        if(a*a != n){
          return false;
        }
        return true;
    }
}
