import java.io.*;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;
import java.lang.Thread;
class q4 extends Thread {
    public void run()
    {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH:mm:ss");
   	while(1==1)
   	{
   		LocalDateTime now = LocalDateTime.now();
   		System.out.println(dtf.format(now));
   		try 
		{
    			Thread.sleep(1000);
		} 
		catch(InterruptedException e)
		{
     			// this part is executed when an exception (in this example InterruptedException) occurs
		}
   	}
    }
    public static void main(String[] args)
    {
        q4 g = new q4(); // creating thread
        g.start(); // starting thread
    }
}
