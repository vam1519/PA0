import tkinter as tk

FONT = ("calbri", 20, "bold")


class Assignment:
    def __init__(self, master):
        master.title("PA0")
        self.plaintext = tk.StringVar(master, value="")
        self.ciphertext = tk.StringVar(master, value="")
 
       
        self.plain_label = tk.Label(master, text="Plaintext", fg="green", font=FONT).grid(row=0, column=0)
        self.plain_entry = tk.Entry(master,
        textvariable=self.plaintext, width=50, font=FONT)
        self.plain_entry.grid(row=0, column=1, padx=20)
        self.encrypt_button = tk.Button(master, text="Encrypt",
        command=lambda: self.encrypt_callback(), font=FONT).grid(row=0, column=2)
        self.plain_clear = tk.Button(master, text="Clear",
        command=lambda: self.clear('plain'), font=FONT).grid(row=0, column=3)

       

      
        self.cipher_label = tk.Label(master, text="Ciphertext", fg="red", font=FONT).grid(row=2, column=0)
        self.cipher_entry = tk.Entry(master,
        textvariable=self.ciphertext, width=50, font=FONT)
        self.cipher_entry.grid(row=2, column=1, padx=20)
        self.decrypt_button = tk.Button(master, text="Decrypt",
        command=lambda: self.decrypt_callback(), font=FONT).grid(row=2, column=2)
        self.cipher_clear = tk.Button(master, text="Clear",
        command=lambda: self.clear('cipher'), font=FONT).grid(row=2, column=3)

    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        elif str_val == 'plain':
            self.plain_entry.delete(0, 'end')

   

    def encrypt_callback(self):
        
        ciphertext = encrypt(self.plain_entry.get())
        self.cipher_entry.delete(0, tk.END)
        self.cipher_entry.insert(0, ciphertext)

    def decrypt_callback(self):
        
        plaintext = decrypt(self.cipher_entry.get())
        self.plain_entry.delete(0, tk.END)
        self.plain_entry.insert(0, plaintext)


def encrypt(plaintext):
    reverse = "zyxwvutsrqponmlkjihgfedcba"
    l = len(plaintext)
     
    
    answer = ""
                 
    for i in range(0, l):
        answer = (answer +
        reverse[ord(plaintext[i]) - ord('a')]);
         
    return answer;


def decrypt(plaintext):
    reverse = "zyxwvutsrqponmlkjihgfedcba"
    l = len(plaintext)
     
    
    answer = ""
                 
    for i in range(0, l):
        answer = (answer +
        reverse[ord(plaintext[i]) - ord('a')]);
         
    return answer;


if __name__ == "__main__":
    root = tk.Tk()
    caesar = Assignment(root)
    root.mainloop()