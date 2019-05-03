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
        public static int[][] MakeJaggedForPerms(int arrLength, int permLength, bool bPrintRowNum = false)
        {
            int rows = Factorial(arrLength) / ((permLength != arrLength) ? Factorial(arrLength - permLength) : 1);

            if (bPrintRowNum)
                System.Console.WriteLine("# of permutations: " + rows);
            int[][] returnArr = new int[rows][];
            for (int i = 0; i < rows; i++)
                returnArr[i] = new int[permLength];

            return returnArr;
        }
        // second attempt at permutations. A more simple one, not the one from Python.
        static public void Permuations<T>(T[] toPerm, int startIdx, int endIdx, T[][] storageArr, ref int count)
        {
            // https://www.geeksforgeeks.org/c-program-to-print-all-permutations-of-a-given-string-2/            
            if (startIdx == endIdx)
            {
                for (int j = 0; j < toPerm.Length; j++)
                    storageArr[count][j] = toPerm[j];
                count++;
            }
            else
            {
                for (int i = startIdx; i <= endIdx; i++)
                {
                    Swap(toPerm, startIdx, i);
                    Permuations(toPerm, startIdx + 1, endIdx, storageArr, ref count);
                    Swap(toPerm, startIdx, i);
                }
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            int X=5, Y=7, Z=3, x=1, y=3, z=1;
            /*
            int[] testArr = new int[] { 5, 4, 7, 12, 15, 4 };            
            int[][] permPool = PySharp.MakeJaggedForPerms(testArr.Length, testArr.Length, true);
            int insertArr = 0;

            PySharp.Permuations(testArr, 0, testArr.Length - 1, permPool, ref insertArr);

            foreach (int[] currentArr in permPool)
            {
                System.Console.Write("( ");
                PySharp.PrintElement(currentArr);
                System.Console.WriteLine(")");
            }
            */
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
            int Fit3(int bigX, int bigY, int bigZ, int smallX, int smallY, int smallZ) // we're gonna permutate this b****
            {
                int[] smallBoxes = new int[] { smallX, smallY, smallZ };
                int[][] boxPool = PySharp.MakeJaggedForPerms(3, 3);
                int permCount = 0, total=0, tempTotal;
                PySharp.Permuations(smallBoxes, 0, 2, boxPool, ref permCount);
                for (int i = 0; i < boxPool.Length; i++)
                {

                }

                return 0;
            }

            System.Console.WriteLine("Fit 1: " + Fit(X, Y, x, y));
            System.Console.WriteLine("Fit 2: " + Fit2(X, Y, x, y));
            System.Console.WriteLine("Fit 3: " + Fit3(X, Y, Z, x, y, z));
            System.Console.ReadKey();
        }
    }
}
