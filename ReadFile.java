import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class ReadFile {
    public String scan(String strFileName) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(strFileName));
        StringBuilder stringBuilder = new StringBuilder();

        // Read each line from the file and append it to the StringBuilder
        while (scanner.hasNextLine()) {
            stringBuilder.append(scanner.nextLine()).append("\n");
        }

        // Close the scanner
        scanner.close();

        // Get the content as a String
        String fileContent = stringBuilder.toString();

        // Now fileContent contains the content of the file
        return fileContent;
    }
}
