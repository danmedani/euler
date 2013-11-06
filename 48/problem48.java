import java.math.BigInteger;
public class problem48 {
    public static void main(String[] args) {
	BigInteger sum = new BigInteger("0");
	BigInteger[] ints = new BigInteger[1000];
	for (int i = 0; i < 1000; i ++) {
	    ints[i] = new BigInteger(Integer.toString(i+1));
	    sum = sum.add(ints[i].pow(i+1));
	}
	System.out.println(sum);
    }
}
