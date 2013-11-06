public class problem49 {

    boolean[] primes;

    public static void main(String[] args) {
	problem49 gen = new problem49(20000);
	gen.run();
    }

    public problem49(int primeListSize) {
	primes = new boolean[primeListSize];
	for (int i = 0; i < primeListSize; i ++)
	    primes[i] = true;
	
	primes[1] = false;
	for (int i = 2; i < primes.length; i ++) {
	    if (primes[i]) {
		// Prime. Baboom it.
		for (int j = i * 2; j < primes.length; j = j + i) {
		    primes[j] = false;
		}
	    }
	}
    }

    private boolean isSame(int a, int b, int c) {
	String as = "" + a;
	String bs = "" + b;
	String cs = "" + c;
	
	if (as.length() == bs.length() && bs.length() == cs.length()) {
	    int[] digitsA = new int[10];
	    int[] digitsB = new int[10];
	    int[] digitsC = new int[10];
	    for (int i = 0; i < 10; i ++) {
		digitsA[i] = 0;
		digitsB[i] = 0;
		digitsC[i] = 0;
	    }
	    
	    for (int i = 0; i < as.length(); i ++) {
		digitsA[Integer.parseInt(as.substring(i, i + 1))] += 1;
	    }
	    for (int i = 0; i < bs.length(); i ++) {
		digitsB[Integer.parseInt(bs.substring(i, i + 1))] += 1;
	    }
	    for (int i = 0; i < cs.length(); i ++) {
		digitsC[Integer.parseInt(cs.substring(i, i + 1))] += 1;
	    }

	    for (int i = 0; i < 10; i ++) {
		if (digitsA[i] != digitsB[i] || digitsB[i] != digitsC[i]) {
		    return false;
		}
	    }
	} else {
	    return false;
	}
	
	return true;
    }

    public void run() {
	int i = 3330;
	for (int n = 1000; (n+1) < 10000; n ++) {
	    if (primes[n] && primes[n+i] && primes[n+(2*i)]) {
		if (isSame(n, n+i, n+(2*i))) {
		    System.out.println(n);
		    System.out.println(n+i);
		    System.out.println(n+(2*i));
		    System.out.println("!!!");
		}
	    }
	}
    }
}