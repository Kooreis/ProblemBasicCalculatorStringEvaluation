```C#
using System;
using System.Collections.Generic;
using System.Data;

namespace BasicCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a mathematical expression:");
            string expression = Console.ReadLine();
            Console.WriteLine("Result: " + Evaluate(expression));
        }

        public static double Evaluate(string expression)
        {
            DataTable table = new DataTable();
            table.Columns.Add("expression", string.Empty.GetType(), expression);
            DataRow row = table.NewRow();
            table.Rows.Add(row);
            return double.Parse((string)row["expression"]);
        }
    }
}
```