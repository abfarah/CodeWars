public class Dubstep {
  public static String SongDecoder (String song)
  {
     String[] arr = song.split("WUB");
     String result = arr[0];
     
     for(int i = 1; i < arr.length; i++){
         result = result + " " + arr[i];
     }
     result = result.trim().replaceAll(" +", " ");
     return result;
   }
}
