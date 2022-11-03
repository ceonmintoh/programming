using System;
using System.Data;
using System.Windows.Forms;
using System.Data.SQLite;

namespace Login
{
    public partial class login_form : Form
    {
        public login_form()
        {
            InitializeComponent();
        }

        private void login_form_Load(object sender, EventArgs e)
        {

        }

        private void btnLogin_Click(object sender, EventArgs e)
        {
            if(username.Text.Trim() =="" && password.Text.Trim() == "")
            {
                MessageBox.Show("Username and Password cannot be empty");
            }
            else
            {
                string query = "SELECT * FROM admin WHERE username = @username AND password =@password";
                string connectionString = @"URI=Data Source = myLogin.db; Version = 3;";
                SQLiteConnection conn = new SQLiteConnection(connectionString);
                conn.Open();
                SQLiteCommand cmd = new SQLiteCommand(query,conn);
                cmd.Parameters.AddWithValue("@username", username.Text);
                cmd.Parameters.AddWithValue("@password", password.Text);
                SQLiteDataAdapter da = new SQLiteDataAdapter(cmd);
                DataTable dt = new DataTable();
                da.Fill(dt);

                if(dt.Rows.Count>0)
                {
                    MessageBox.Show("You're Now Logged In!");
                }
                else
                {
                    MessageBox.Show("Invalid Username or Password!");
                }
            }
        }
    }
}
