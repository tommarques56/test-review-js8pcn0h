import java.util.*;

// Missing class documentation
public class DataProcessor {
    private List<Integer> data;
    
    public DataProcessor() {
        data = new ArrayList<>();
    }
    
    // Missing parameter validation
    public void addData(Integer value) {
        data.add(value);  // No null check
    }
    
    // Missing exception handling
    public int processData() {
        int sum = 0;
        for (Integer item : data) {
            sum += item;  // Potential NullPointerException
        }
        return sum;
    }
    
    // Resource not closed properly
    public void processFile(String filename) {
        try {
            File file = new File(filename);
            Scanner scanner = new Scanner(file);
            // Scanner not closed in finally block
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
    }
    
    // Missing @Override annotation
    public String toString() {
        return "DataProcessor with " + data.size() + " items";
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Starting Java application...");
        
        DataProcessor processor = new DataProcessor();
        processor.addData(1);
        processor.addData(2);
        processor.addData(3);
        
        int result = processor.processData();
        System.out.println("Result: " + result);
        
        // Potential null pointer
        String input = null;
        System.out.println(input.length());  // NullPointerException
        
        processor.processFile("test.txt");
    }
}
