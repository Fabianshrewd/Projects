using System;
using System.Drawing;
using System.Windows.Forms;

namespace Game1
{
    class Program
    {
	static void WindowSetup()
	{
		
	}
	    
        static void Main(string[] args)
        {
           //Create a window
	   Form window1 = new Form();
	   
	   //Show the window
	   window1.ShowDialog();

	   //Show button
	   Button mybutton = new Button()
            {
                Text = "Hello",
                Location = new System.Drawing.Point(10, 10)
            };
            mybutton.Click += (o, s) =>
            {
                MessageBox.Show("world");
            };

            window1.Controls.Add(mybutton);
            window1.ShowDialog();        }
    }
}
