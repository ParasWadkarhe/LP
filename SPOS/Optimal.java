import java.util.Scanner;
public class Optimal{
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
System.out.print("Enter the length of the reference string: ");
int refLength = scanner.nextInt();
System.out.print("Enter the number of frames: ");
int frames = scanner.nextInt();
int[] reference = new int[refLength];
int[] buffer = new int[frames];
int hit = 0, fault = 0;
for (int i = 0; i < frames; i++) {
buffer[i] = -1;
}
System.out.print("Enter the reference string: ");
for (int i = 0; i < refLength; i++) {
reference[i] = scanner.nextInt();
}
System.out.print("Strings \t");
for (int i = 0; i < frames; i++) {
System.out.print("Frame " + (i + 1) + "\t\t");
}
System.out.println();
for (int i = 0; i < refLength; i++) {
int currentPage = reference[i];
boolean pageFound = false;
for (int j = 0; j < frames; j++) {
if (buffer[j] == currentPage) {
pageFound = true;
hit++;
break;
}
}
if (!pageFound) {
int replaceIndex = getOptimalPageIndex(buffer, reference, i);
buffer[replaceIndex] = currentPage;
fault++;
}
System.out.print(currentPage + "\t\t");
for (int j = 0; j < frames; j++) {
if (buffer[j] != -1) {
System.out.print(buffer[j] + "\t\t");
} else {
System.out.print("-\t\t");
}
}
System.out.println();
}
System.out.println("\nTotal Hits: " + hit);
System.out.println("Total Faults: " + fault);
scanner.close();
}
private static int getOptimalPageIndex(int[] buffer, int[] reference, int currentIndex) {
int farthest = currentIndex;
int replaceIndex = 0;
for (int i = 0; i < buffer.length; i++) {
int j;
for (j = currentIndex + 1; j < reference.length; j++) {
if (buffer[i] == reference[j]) {
if (j > farthest) {
farthest = j;
replaceIndex = i;
}
break;
}
}
if(j == reference.length){
    return i;
}
}
return replaceIndex;
}
}