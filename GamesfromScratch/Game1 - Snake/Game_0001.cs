using System;
using System.Drawing;
using System.Threading;
using System.Windows.Forms;

namespace Game1
{   
    public class Window
    {
    	public Form window1;
	public Bitmap bm;
	public PictureBox picture;
	
	public Window()
	{
	   this.window1 = new Form();
	   this.bm = new Bitmap(1280, 720);
	   this.picture = new PictureBox{Name = "pictureBox", Size = new Size(1280, 720), Location = new Point(0,0)};
	}

	public void SetResolution()
	{
	   this.window1.Width = 1280;
	   this.window1.Height = 720;
	}

	public void editpixel(int start_x, int stop_x, int start_y, int stop_y)
	{
	   for(int i = start_x; i < stop_x; i++)
	   {
	   	for(int o = start_y; o < stop_y; o++)
		{
		   this.bm.SetPixel(i, o, Color.Black);
		}
	   }	

	   this.picture.Image = bm;
	}

	public void ShowWindow()
	{
	   this.window1.ShowDialog();
	}
    }

    class Program
    {

        static void Main(string[] args)
        {
           //Create a window
	   Window form1 = new Window();
	   form1.SetResolution();
	   
	   //Edit the pixels of the image
	   form1.editpixel(0, 100, 0, 100);
	   
	   //Add the picturebox to the window
           form1.window1.Controls.Add(form1.picture);
	   
	   //Adding Multithreading
	   Thread t = new Thread(form1.ShowWindow);
	   t.Start();

	   //Edit the bitmap movement
	   for(int i = 0; i < 200; i++)
	   {
	   	form1.editpixel(0, 100+i, 0, 100+i);

		if(i % 10 == 0)
		{
		   Thread.Sleep(1000);
		}
	   }
	}
    }
}
