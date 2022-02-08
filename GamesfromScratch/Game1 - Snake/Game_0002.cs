using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using System.Threading;

namespace Game1
{
    public class Form1 : Form
    {
        public Button button1;
        public Button button2;
	public Bitmap bm;
	public PictureBox picture;
	//Main Method
        public Form1()
        {
            	//Creating the surface
		bm = new Bitmap(1280, 720);
            	picture = new PictureBox { Name = "pictureBox", Size = new Size(1280, 720), Location = new Point(0, 100), Image = bm };
            	this.Controls.Add(picture);

		button1 = new Button();
            	button1.Size = new Size(40, 40);
            	button1.Location = new Point(30, 30);
            	button1.Text = "Click me";
            	this.Controls.Add(button1);
            	button1.Click += new EventHandler(button1_Click);
            	
            	button2 = new Button();
            	button2.Size = new Size(40, 40);
            	button2.Location = new Point(90, 30);
            	button2.Text = "Click me";
            	this.Controls.Add(button2);
            	button2.Click += new EventHandler(button2_Click);    
	}
	
	private void button1_Click(object sender, EventArgs e)
        {
        	Thread t1 = new Thread(Action1);
        	Thread t2 = new Thread(Action2);
        	t1.Start();
        	t2.Start();
        	
        }
        
        private void button2_Click(object sender, EventArgs e)
        {
        	
        }
        
        private void Action1()
        {
        	for(int i = 0; i < 5; i++)
		{
			bm = editpixel(i*256,(i+1)*256, 0, 256, bm);
			picture.Refresh();
			Thread.Sleep(1000);
		}
        }
        
        private void Action2()
        {
        	for(int i = 0; i < 5; i++)
		{
			bm = editpixel(i*256,(i+1)*256, 256, 512, bm);
			picture.Refresh();
			Thread.Sleep(2000);
		}
        }
        
	//Function - Sets the pixel
        static Bitmap editpixel(int start_x, int stop_x, int start_y, int stop_y, Bitmap bm)
        {
	    //Makes the pixel full
            for (int i = start_x; i < stop_x; i++)
            {
                for (int o = start_y; o < stop_y; o++)
                {   
		    //Sets the pixel
                    bm.SetPixel(i, o, Color.Black);
                }
            }
	    
	    //Return the solution
            return bm;
        }
	
	//Start Method
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new Form1());
        }
    }
}
