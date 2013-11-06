/*
 * NOTE: This solution works, but it is very slow. It will take ~ 13 days running on both of my processors to complete; the last time I tried to run it my machine crashed 4 days in to it the job. Still don't have a solution.
 *
 */

import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class P433Threads implements Runnable {

    private int n;
    private int start;
    private int end;

    public static void main(String[] args) {
	// Argument 1: N
	// Argument 2: # of Threads
	
	int n = Integer.parseInt(args[0]);
	int numThreads = Integer.parseInt(args[1]);
	for (int i = 0; i < numThreads; i ++)
	    (new Thread(new P433Threads(n, 1 + (i * (n/numThreads)), ((i+1) * (n/numThreads))))).start();
    }

    public void run() {
	System.out.println(countEmQuick());
    }

    public P433Threads(int n, int start, int end) {
	this.n = n;
	this.start = start;
	this.end = end;
    }

    public BigInteger countEmQuick() {
	BigInteger sum = new BigInteger("0");
	int numTween;
	int count;
	int st;
	for (int i = start; i <= end; i ++) {
	    st = i*2;
	    if (st > n)
		st = n;
	    //System.out.println(i);
	    for (int j = st; j > i; j --) {
		count = countEuler(i, j);
		numTween = numTween(i, j, n);
		sum = sum.add(new BigInteger("" + ((numTween * count) + (numTween * (count-1)))));
	    }
	}
	//System.out.println();
	// Ident
	sum = sum.add(new BigInteger("" + (end - start + 1)));;
	
	try {
	    String outName = "benis_" + start + "_" + end;
	    PrintStream pStream = new PrintStream(new FileOutputStream(outName, false));
	    pStream.print(sum);
	    pStream.println();
	    pStream.close();
	} catch (Exception e) {
	    System.out.println(e);
	}
	return sum;
    }

    private int numTween(int mult, int start, int end) {
	return ((end - start) / mult) + 1;
    }

    private int countEuler(int x, int y) {
	int sum = 0;
	int tmp;
	while (y != 0) {
	    tmp = x;
	    x = y;
	    y = tmp % y;
	    sum = sum + 1;
	}
	return sum;
    }
}
