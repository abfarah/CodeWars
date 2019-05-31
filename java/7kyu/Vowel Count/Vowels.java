public class Vowels {

  public static int getCount(String str) {
    int vowelsCount = 0;
    char[] str2 = str.toCharArray();
    char[] vowels = {'a', 'e', 'i', 'o', 'u'};
    int count = 0;
    for(int i =0; i < str2.length; i++){
      count = 0;
      while(count <= 4){
        if(str2[i] == vowels[count]){
          vowelsCount++;
        }
        count++;
      }
    }
    return vowelsCount;
  }

}
