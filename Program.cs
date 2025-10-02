using System;
using System.Collections.Generic;

namespace TestApp
{
    // Missing XML documentation
    public class DataProcessor
    {
        private List<int> data;
        
        public DataProcessor()
        {
            data = new List<int>();
        }
        
        // Missing parameter validation
        public void AddData(int value)
        {
            data.Add(value);  // No null check or validation
        }
        
        // Missing exception handling
        public int ProcessData()
        {
            int sum = 0;
            foreach (var item in data)
            {
                sum += item;
            }
            return sum;
        }
        
        // Resource not disposed properly
        public void ProcessFile(string filename)
        {
            var file = System.IO.File.OpenRead(filename);  // Not disposed
            // Process file...
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting C# application...");
            
            var processor = new DataProcessor();
            processor.AddData(1);
            processor.AddData(2);
            processor.AddData(3);
            
            int result = processor.ProcessData();
            Console.WriteLine($"Result: {result}");
            
            // Potential null reference
            string input = null;
            Console.WriteLine(input.Length);  // NullReferenceException
        }
    }
}
