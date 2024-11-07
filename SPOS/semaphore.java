import java.util.*;
import java.util.concurrent.Semaphore;

public class semaphore {

        static Semaphore mutex = new Semaphore(1);
        static Semaphore wrt = new Semaphore(1);
        static int readcount = 0;
        static String message = "hello";
        static Scanner sc = new Scanner(System.in);
        static class Reader implements Runnable{
            public void run(){
                try{
                    mutex.acquire();
                    readcount++;
                    if(readcount==1){
                        wrt.acquire();
                    }
                    mutex.release();
                    System.out.println("Thread "+Thread.currentThread().getName()+"is Reading :"+message);
                    System.out.println("Thread"+Thread.currentThread().getName() + "has finished Reading");
                    mutex.acquire();
                    readcount--;
                    if(readcount==0){
                        wrt.release();
                    }
                    mutex.release();
                   }   
                catch(Exception e){
                    System.out.println(e.getMessage());
                }
            }
        }
        static class Writer implements Runnable{
            public void run(){
                try{
                    wrt.acquire();
                    message = "Good Night";
                    System.out.println("Thread"+Thread.currentThread().getName()+"is waiting:"+message);
                    Thread.sleep(1000);
                    System.out.println("Thread"+Thread.currentThread().getName()+"has finished Writing:");
                    wrt.release();
                }
                catch(Exception e){
                    System.out.println(e.getMessage());
                }
            }
        }
        
    public static void main(String[] args) {
        Reader read = new Reader();
        Writer write = new Writer();
        Thread r1 = new Thread(read);
        r1.setName("Reader1");
        Thread r2 = new Thread(read);
        r2.setName("Reader2");
        Thread r3= new Thread(read);
        r3.setName("Reader3");
        Thread w1 = new Thread(write);
        w1.setName("Writer1");
        Thread w2= new Thread(write);
	w2.setName("Writer2");
	Thread w3= new Thread(write);
	w3.setName("Writer 3");
	w1.start();
        r1.start();
	w2.start();
	r2.start();
	w3.start();
	r3.start();

    }
    
}
