using System;

// https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
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
        public static void Swap<T>(T[] intArr, int pos1, int pos2)
        {
            T temp = intArr[pos1];
            intArr[pos1] = intArr[pos2];
            intArr[pos2] = temp;
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
        static public void Permuations<T>(T[] toPerm, int startIdx, int endIdx, ref T[][]storageArr, ref int count)
        {
            // https://www.geeksforgeeks.org/c-program-to-print-all-permutations-of-a-given-string-2/            
            if (startIdx == endIdx)
            {
                for (int j = 0; j < toPerm.Length; j++)
                {
                    storageArr[count][j] = toPerm[j];
                }
                System.Console.Write("Current Perm: ");
                PrintElement(toPerm);
                System.Console.WriteLine("Count: " + count + "\n");
                count++;
            }
            else
            {
                for (int i = startIdx; i <= endIdx; i++)
                {
                    Swap(toPerm, startIdx, i);
                    Permuations(toPerm, startIdx + 1, endIdx, ref storageArr, ref count);
                    Swap(toPerm, startIdx, i);
                    
                }
            }
        }        
    }
    class Program
    {
        static void Main(string[] args)
        {
            int[] testArr = new int[] { 5, 4, 7 };
            int start = 0;
            int end = 2;
            int lenOfPerm = testArr.Length - start;
            int[][] permPool = PySharp.MakeJaggedForPerms(testArr.Length, lenOfPerm, true);
            int insertArr = 0;

            
            PySharp.Permuations<int>(testArr, start, lenOfPerm - 1, ref permPool, ref insertArr);

            foreach (int[] currentArr in permPool)
            {
                System.Console.Write("(");
                PySharp.PrintElement(currentArr);
                System.Console.WriteLine(")\n");
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
            
            // System.Console.WriteLine(Fit(X, Y, x, y));

            // System.Console.WriteLine(Fit2(X, Y, x, y));
            System.Console.ReadKey();
        }
    }
}
