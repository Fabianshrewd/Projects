using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

namespace Game1
{
    public class Form1 : Form
    {
        public Form1()
        {
            Bitmap bm = new Bitmap(1280, 720);
            PictureBox picture = new PictureBox { Name = "pictureBox", Size = new Size(1280, 720), Location = new Point(0, 0), Image = bm };
            this.Controls.Add(picture);

            bm = editpixel(100, 200, 100, 200, bm);
            bm = editpixel(0, 100, 0, 100, bm);
        }

        static Bitmap editpixel(int start_x, int stop_x, int start_y, int stop_y, Bitmap bm)
        {
            for (int i = start_x; i < stop_x; i++)
            {
                for (int o = start_y; o < stop_y; o++)
                {
                    bm.SetPixel(i, o, Color.Black);
                }
            }

            return bm;
        }

        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.Run(new Form1());
        }
    }
}