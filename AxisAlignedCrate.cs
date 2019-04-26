using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
namespace DailyProgrammer
{
    class AxisAlignedCrate
    {
        static void Main(string[] args)
        {
            int fit(int bigX, int bigY, int smallX, int smallY)
            {
                int totalX = bigX / smallX;
                int totalY = bigY / smallY;
                return totalX * totalY;
            }

            int fit2(int bigX, int bigY, int smallX, int smallY)
            {
                int fit1 = fit(bigX, bigY, smallX, smallY);
                int totalX = bigX / smallY;
                int totalY = bigY / smallX;
                return fit1 >= (totalX * totalY) ? fit1 : (totalX * totalY);
            }
            int[] permutate(int[] arr, int pSize = 0)
            {
                int arrLen = arr.Length;
                int[] tempArr = new int[arr.Length];
                int pLen = pSize != 0 ? pSize : arrLen;
                if(pLen > arrLen) { return tempArr; }
                System.Console.Write(arrLen + "\n" + pLen + "\n");
                return null;
            }

            IEnumerable<IEnumerable<T>> GetPermutationsWithRept<T>(IEnumerable<T> list, int length)
            {
                if (length == 1) return list.Select(t => new T[] { t });
                return GetPermutationsWithRept(list, length - 1)
                    .SelectMany(t => list,
                        (t1, t2) => t1.Concat(new T[] { t2 }));
            }
            int fit3(int bigX, int bigY, int bigZ,
                int smallX, int smallY, int smallZ)
            {
                int attempt = 1;
                int[] bigDimensions = new int[3] { bigX, bigY, bigZ };
                int[] smallDimensions = new int[3] { smallX, smallY, smallZ };

                return 0;
            }
            int X = 10, Y = 10, Z = 10, x = 1, y = 1, z = 1;
            int[] allPerms = GetPermutationsWithRept(new int[6] { X, Y, Z, x, y, z });
           


            System.Console.Write(GetPermutationsWithRept(new int[] {4, 5, 7, 9, 12}, 6) + "\n");
            System.Console.Write(fit(X, Y, x, y) + "\n");
            System.Console.Write(fit2(X, Y, x, y) + "\n");
            System.Console.ReadKey();
        }
    }
}
