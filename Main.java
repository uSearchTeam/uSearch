import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        ReadFile file = new ReadFile();
        Scanner scanner = new Scanner(System.in);
        String string = scanner.next();
        System.out.print("Enter File Name");
        try{ 
            file.scan(string);
        }
        catch (FileNotFoundException e){
            System.out.println("File Not Found" + e.getMessage());
        }
        scanner.close();
    }
}

