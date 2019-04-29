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
            foreach (T elem in arr)
            {
                Console.Write(elem + " ");
            }
        }
        // a C# version of Python's range()
        static public IEnumerable<int> Range(int stop, int start = 0, int step = 1)
        {
            if (stop > start && step > 0)
            {
                for (int i = start; i < stop; i += step)
                {
                    yield return i;
                }
            }
            else if (stop < start && step < 0)
            {
                for (int i = start; i > stop; i += step)
                {
                    yield return i;
                }
            }
            yield break;
        }
        // a C# version of Python's itertools.permutations() for int arrays
        // struglling between using arrays and lists
        /*
        static public IEnumerable<int[]> Permutations(int[] iterable, int pLen = 0)
        
        {
            int[] pool = new int[iterable.Length];
            pool = iterable;
            int iterLen = iterable.Length;
            int permLen = pLen != 0 ? pLen : iterLen;

            if (permLen > iterLen)
            {
                Console.WriteLine("Error: Permutation length is larger the the iterable's length");
                yield break;
            }
            // indices = list(range(n))
            List<int> indices = new List<int>();
            foreach (int num in Range(iterLen))
            {
                indices.Add(num);
            }
            // cycles = list(range(n, n-r, -1))
            List<int> cycles = new List<int>();
            foreach (int num in Range(iterLen, iterLen - permLen, -1))
            {
                cycles.Add(num);
            }
            // yield tuple(pool[i] for i in indices[:r])
            List<int> temp = new List<int>();
            for (int i = 0; i < permLen; i++)
            {
                temp.Add(pool[i]);
            }
            int[] tempArr = temp.ToArray();
            yield return tempArr;
            while (iterLen < 0)
            {
                List<int> rangeList = new List<int>();
                foreach (int i in Range(0, permLen, -1))
                {
                    rangeList.Add(i);
                }
                foreach (int i in rangeList)
                {
                    cycles[i] -= 1;
                    if (cycles[i] == 0)
                    {
                        //List<int> tempIndices = indices.Skip(i)
                    }
                    else
                    {
                        int j = cycles[i];
                        int tempValue = indices[i];
                        indices[i] = indices[indices.Count - 1 - j];
                        indices[indices.Count - 1 - j] = tempValue;
                        List<int[]> yList = new List<int[]>();
                        /*
                        foreach (int[] h in indices.Skip(permLen))
                        {
                            yList.Add(h);
                        }
                        yield return yList;
                        
                        yield break;

                    }
                }
            }
            // Console.WriteLine(permLen.ToString());

            yield break;
        }*/

        // second attempt at permutations
        static public int[][] Permuations(int[] toPerm, int pLen=0)
        {   
            // creating the jagged array that will hold all fof the perms
            int permLen;
            if (pLen == 0)
            {
                permLen = toPerm.Length;
            }
            else
            {
                permLen = pLen;
            }

            int tempArrLen = toPerm.Length;
            int tempPermLen = permLen;
            int rows = Factorial(toPerm.Length) / ((permLen != toPerm.Length) ? Factorial(toPerm.Length - permLen) : 1);
            /*
            int rows = tempArrLen;
            while (tempPermLen > 1)
            {
                tempArrLen -= 1;
                tempPermLen -= 1;
                rows *= tempArrLen;
                System.Console.WriteLine(rows);
            }
            */
            System.Console.WriteLine(rows);
            int[][] pool = new int[rows][];
            for (int j = 0; j < rows; j++)
            {
                pool[j] = new int[permLen];
            }

            int i = 0;

            for (int x = 0; x < rows; x++)
            {
                for (int y = 0; y < permLen; y++)
                {
                    pool[x][y] = i;
                    i++;
                }
            }
            // trying to rewrite python's itertools.permutations() in C#
            int n = toPerm.Length;  // to save time, these should probably be higher up
            int r = permLen;
            if (r > n)
            {
                System.Console.WriteLine("Error: The desired permutation length is longer than the array length");
                return null;
            }


            return pool;
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
            int [][] pytest = PySharp.Permuations(new int[] { 5, 4, 7, 5, 12 }, 3);
            for (int i = 0; i < pytest.Length; i++)
            {
                PySharp.PrintElement(pytest[i]);
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
