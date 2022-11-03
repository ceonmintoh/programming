
namespace MALAMI
{
    partial class entryForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.yesAdmin = new System.Windows.Forms.Button();
            this.noAdmin = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Wolfpack Free Personal Use", 24F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline))), System.Drawing.GraphicsUnit.Point);
            this.label1.ForeColor = System.Drawing.Color.Blue;
            this.label1.Location = new System.Drawing.Point(38, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(344, 48);
            this.label1.TabIndex = 0;
            this.label1.Text = "Are You an Admin?";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // yesAdmin
            // 
            this.yesAdmin.Font = new System.Drawing.Font("Segoe UI", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.yesAdmin.ForeColor = System.Drawing.Color.Lime;
            this.yesAdmin.Location = new System.Drawing.Point(48, 82);
            this.yesAdmin.Name = "yesAdmin";
            this.yesAdmin.Size = new System.Drawing.Size(135, 54);
            this.yesAdmin.TabIndex = 1;
            this.yesAdmin.Text = "Yes";
            this.yesAdmin.UseVisualStyleBackColor = true;
            this.yesAdmin.Click += new System.EventHandler(this.yesAdmin_Click);
            // 
            // noAdmin
            // 
            this.noAdmin.Font = new System.Drawing.Font("Segoe UI", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.noAdmin.ForeColor = System.Drawing.Color.Red;
            this.noAdmin.Location = new System.Drawing.Point(209, 82);
            this.noAdmin.Name = "noAdmin";
            this.noAdmin.Size = new System.Drawing.Size(123, 53);
            this.noAdmin.TabIndex = 2;
            this.noAdmin.Text = "No";
            this.noAdmin.UseVisualStyleBackColor = true;
            // 
            // entryForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(406, 162);
            this.Controls.Add(this.noAdmin);
            this.Controls.Add(this.yesAdmin);
            this.Controls.Add(this.label1);
            this.Name = "entryForm";
            this.Text = "Welcome To Malami POS System";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button yesAdmin;
        private System.Windows.Forms.Button noAdmin;
    }
}

