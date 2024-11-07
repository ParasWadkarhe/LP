import java.util.*;
public class deadlock {

    public static void main(String[] args) {
 
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the no. of processes");
        int numProcess = sc.nextInt();
        System.out.print("Enter the number of resource types: ");
        int numResources = sc.nextInt();
        int[][] max = new int[numProcess][numResources];
        int[][] allocation = new int[numProcess][numResources];
        int[][] need = new int[numProcess][numResources];
        int[] available = new int[numResources];
        boolean[] finished = new boolean[numProcess];
        int[] safeSequence = new int[numProcess];
        System.out.println("Enter Max matrix");
        for(int i=0;i<numProcess;i++){
            for(int j=0;j<numResources;j++){
                max[i][j] = sc.nextInt();
            }
        }
        System.out.println("Enter Allocation matrix: ");
        for (int i = 0; i < numProcess; i++) {
            for (int j = 0; j < numResources; j++) {
                allocation[i][j] = sc.nextInt();
            }
        }
        System.out.println("Enter Available matrix;");
        for(int i=0;i<numResources;i++){
            available[i] = sc.nextInt();
        }
        for(int i=0;i<numProcess;i++){
            for(int j=0;j<numResources;j++){
                need[i][j]=max[i][j]-allocation[i][j];
            }
        }
                System.out.println("\nMAX matrix:");
        for (int i = 0; i < numProcess; i++) {
            for (int j = 0; j < numResources; j++) {
                System.out.print(max[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("\nAllocation matrix:");
        for (int i = 0; i < numProcess; i++) {
            for (int j = 0; j < numResources; j++) {
                System.out.print(allocation[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("\nNeed Matrix");
        for(int i=0;i<numProcess;i++){
            for(int j=0;j<numResources;j++){
                System.out.println(need[i][j]+"");
            }
            System.out.println();
        }
        System.out.println("\nAvailable Matrix");
        for(int i=0;i<numResources;i++){
            System.out.println(available[i]+"");
        }
            System.out.println();
        
            int count = 0;
            while(count<numProcess){
                boolean found = false;
                for(int p=0;p<numProcess;p++){
                    if(!finished[p]){
                        int j;
                        for(j=0;j<numResources;j++){
                            if(need[p][j]>available[j]){
                                break;
                            }
                        }
                        if(j==numResources){
                            for(int k=0;k<numResources;k++){
                                available[k]+=allocation[p][k];
                            }
                            safeSequence[count++]=p;
                            finished[p]=true;
                            found=true;
                        }
                    }
                }
                if(!found){
                    System.out.println("The system is in an unsafe state(deadlock)");
                    return;
                }
            }
            System.out.println("Safe Sequence:");
            for(int i=0;i<numProcess;i++){
                System.out.println("P"+safeSequence[i]);
                if(i != numProcess-1){
                    System.out.println("->");
                }
            }
            System.out.println();
            sc.close();
    }
    
}
