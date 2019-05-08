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
            int X = 12, Y = 34, Z = 56, x = 7, y = 8, z = 9;
 
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
                int permCount = 0, total = 0, tempTotal;
                PySharp.Permuations(smallBoxes, 0, 2, boxPool, ref permCount);
                for (int i = 0; i < boxPool.Length; i++)
                {
                    int totalX = bigX / boxPool[i][0];
                    int totalY = bigY / boxPool[i][1];
                    int totalZ = bigZ / boxPool[i][2];
                    tempTotal = totalX * totalY * totalZ;
                    total = total > tempTotal ? total : tempTotal;
                }

                return total;
            }
            int FitN(int[] largeBox, int[] smallBox)
            {
                int permCount = 0, total = 0, tempTotal;
                if (largeBox.Length != smallBox.Length)
                {
                    System.Console.WriteLine("Error: Arrays are not the same same");
                    return total;
                }
                
                int[][] boxPool = PySharp.MakeJaggedForPerms(smallBox.Length, smallBox.Length);
                PySharp.Permuations(smallBox, 0, smallBox.Length - 1, boxPool, ref permCount);
                int i = 0;
                while (i < boxPool.Length)
                {
                    tempTotal = 1;
                    for (int j = 0; j < largeBox.Length; j++)
                        tempTotal *= largeBox[j] / boxPool[i][j];
                    total = total > tempTotal ? total : tempTotal;
                    i++;
                }
                return total;
            }

            System.Console.WriteLine("Fit 1: " + Fit(X, Y, x, y));
            System.Console.WriteLine("Fit 2: " + Fit2(X, Y, x, y));
            System.Console.WriteLine("Fit 3: " + Fit3(X, Y, Z, x, y, z));
            System.Console.WriteLine("Fit N: " + FitN(new int[] { 123, 456, 789, 1011, 1213, 1415 }, 
                new int[] { 16, 17, 18, 19, 20, 21 }));
            System.Console.ReadKey();
        }
    }
}
