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

        static public void PrintElement<T>(T[] arr)
        {
            foreach (T elem in arr)
            {
                Console.WriteLine(elem);
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
        static public IEnumerable<int> Permutations(int[] iterable, int pLen = 0)
        {
            List<int> pool = new List<int>(iterable);
            List<int> perms = new List<int>();
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
            perms.Add(temp);
            yield return perms;
            // Console.WriteLine(permLen.ToString());

            yield break;
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
            List<int> permTest = new List<int>(PySharp.Permutations(new int[] { 7, 8, 2, -2, 90 }, 2));
            Console.WriteLine(permTest[0]);
            foreach (int num in permTest)
            {
                Console.WriteLine(num);
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
                int[] bigDimensions = new int[3] {bigX, bigY, bigZ };
                int[] smallDimensions = new int[3] { smallX, smallY, smallZ };

                return 0;
            }
            int X = 10, Y = 10, Z = 10, x = 1, y = 1, z =1;
            
            // System.Console.WriteLine(Fit(X, Y, x, y));

            // System.Console.WriteLine(Fit2(X, Y, x, y));
            System.Console.ReadKey();
        }
    }
}
