using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
namespace DailyProgrammer
{
    static class PySharp
    {
        static public void Display<T>(string msg, T value)
        {
            Console.WriteLine("{0}:{1}", msg, value);
        }

        static public int Factorial(int num)
        {
            int i = 2;
            int factor = 2;
            while (i < num)
            {
                i++;
                factor *= i;
            }
            return factor;
        }

        static public void PrintElement<T>(T[] arr)
        {
            if (arr == null)
                System.Console.Write("null ");
            else
                foreach (T elem in arr)
                    Console.Write(elem + " ");            
        }
        // function mainly meant for permutations code
        private static int[] Swap(int[] arr, int pos1, int pos2)
        {
            int temp;
            int[] intArr = arr;
            temp = intArr[pos1];
            intArr[pos1] = intArr[pos2];
            intArr[pos2] = temp;
            return intArr;
        }
        // function for creating creating empyty jagged array to hold perms
        public static int[][] MakeJaggedForPerms(int arrLength, int permLength, bool bPrintRowNum=false)
        {
            int rows = Factorial(arrLength) / ((permLength != arrLength) ? Factorial(arrLength - permLength) : 1);
            
            if (bPrintRowNum)
                System.Console.WriteLine("# of permutations: " + rows);
            return new int[rows][];
        }
        // second attempt at permutations. A more simple one, not the one from Python.
        static public void Permuations(int[] toPerm, int[][] storage, int startIdx=0, int endIdx=0)
        {
            // https://www.geeksforgeeks.org/c-program-to-print-all-permutations-of-a-given-string-2/
            int i = startIdx;
            if (startIdx == endIdx)
            {
                storage[startIdx] = toPerm;                
            }
            else
            {
                for (i = startIdx; i <= endIdx; i++)
                {
                    toPerm = Swap(toPerm, startIdx, i);
                    Permuations(toPerm, storage, startIdx + 1, endIdx);
                    toPerm = Swap(toPerm, startIdx, i);
                }
            }
        }        
    }
    class Program
    {
        static void Main(string[] args)
        {
            // PySharp py = new PySharp();
            /*
            py.Display<int>("Int", 467);
            py.Display<char>("Char", 'A');
            py.Display<double>("Double", 45.67);
            
            string ham = "HAM";
            char[] hamArr = ham.ToCharArray();
            py.PrintElement<char>(hamArr);
            
            foreach (int num in PySharp.Range(-20, 3, -5))
            {
                Console.Write(num.ToString() + " ");
            }
            
            */
            // List<int> permTest = new List<int>(PySharp.Permutations(new int[] { 7, 8, 2, -2, 90 }, 2));
            int[] testArr = new int[] { 5, 4, 7, 5, 12 };
            int start = 0;
            int end = 2;
            int lenOfPerm = end - start;
            int[][] permPool = PySharp.MakeJaggedForPerms(testArr.Length, lenOfPerm, true);
            PySharp.Permuations(testArr, permPool, start, end - 1);
            for (int i = 0; i < permPool.Length; i++)
            {
                PySharp.PrintElement(permPool[i]);
                System.Console.WriteLine();
            }

            int Fit(int bigX, int bigY, int smallX, int smallY)
            {
                int totalX = bigX / smallX;
                int totalY = bigY / smallY;
                return totalX * totalY;
            }

            int Fit2(int bigX, int bigY, int smallX, int smallY)
            {
                int fit1 = Fit(bigX, bigY, smallX, smallY);
                int totalX = bigX / smallY;
                int totalY = bigY / smallX;
                return fit1 >= (totalX * totalY) ? fit1 : (totalX * totalY);
            }

            int Fit3(int bigX, int bigY, int bigZ,
                int smallX, int smallY, int smallZ)
            {
                int attempt = 1;
                int[] bigDimensions = new int[3] { bigX, bigY, bigZ };
                int[] smallDimensions = new int[3] { smallX, smallY, smallZ };

                return 0;
            }
            int X = 10, Y = 10, Z = 10, x = 1, y = 1, z = 1;

            // System.Console.WriteLine(Fit(X, Y, x, y));

            // System.Console.WriteLine(Fit2(X, Y, x, y));
            System.Console.ReadKey();
        }
    }
}
