using System;
using System.Drawing;
using System.Windows.Forms;

namespace Game1
{
    class Program
    {
        static void Main(string[] args)
        {
           //Create a window
	   Form window1 = new Form();
	   
	   //Set length
           window1.Width = 1280;	   
	   window1.Height = 720;

	   //Show the window
	   window1.ShowDialog();
	}
    }
}
