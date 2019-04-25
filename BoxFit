using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
namespace DailyProgrammer
{
    class Program
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

            int fit3(int bigX, int bigY, int bigZ,
                int smallX, int smallY, int smallZ)
            {
                int attempt = 1;
                int[] bigDimensions = new int[3] {bigX, bigY, bigZ };
                int[] smallDimensions = new int[3] { smallX, smallY, smallZ };


            }
            int X = 10, Y = 10, Z = 10, x = 1, y = 1, z =1;
            
            System.Console.Write(fit(X, Y, x, y));
            System.Console.WriteLine();
            System.Console.Write(fit2(X, Y, x, y));
            System.Console.ReadKey();
        }
    }
}
