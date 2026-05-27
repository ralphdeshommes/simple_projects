# this is for the gui
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

# symmetric encryption
from cryptography.fernet import Fernet

# asymmetric encryption
from cryptography.hazmat.primitives.asymmetric import rsa, padding as res_padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64  

rsa_private_key = None
rsa_public_key = None

# ============================
# NEW GLOBALS FOR SYMMETRIC PART
# ============================
selected_file_path = None
fernet_key_global = None


def fernet_key():
    global fernet_key_global
    # generate and store a single Fernet key for this session
    if fernet_key_global is None:
        fernet_key_global = Fernet.generate_key()
    return fernet_key_global


def fernet_encrypt():
    """
    Encrypt the selected file (e.g., an image) with Fernet
    and save it as <original_name>.enc.
    """
    global selected_file_path, fernet_key_global

    if not selected_file_path:
        messagebox.showerror("Error", "Please select a file first.")
        return

    # ensure we have a key
    key = fernet_key()
    f = Fernet(key)

    try:
        # read the original file bytes
        with open(selected_file_path, "rb") as f_in:
            data = f_in.read()

        # encrypt with Fernet
        ciphertext = f.encrypt(data)

        # save encrypted bytes as <filename>.enc
        enc_path = selected_file_path + ".enc"
        with open(enc_path, "wb") as f_out:
            f_out.write(ciphertext)

        symmetric_encrypt_textbox.delete("1.0", "end")
        symmetric_encrypt_textbox.insert(
            "1.0",
            f"File encrypted successfully!\nSaved as:\n{enc_path}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")


def fernet_decrypt():
    """
    Decrypt the selected encrypted file (.enc) with Fernet
    and save it as <original_name>.dec.
    """
    global selected_file_path, fernet_key_global

    if not selected_file_path:
        messagebox.showerror("Error", "Please select an encrypted file first.")
        return

    if fernet_key_global is None:
        messagebox.showerror(
            "Error",
            "No Fernet key in memory.\nYou must encrypt with this session first."
        )
        return

    f = Fernet(fernet_key_global)

    try:
        # read ciphertext from file
        with open(selected_file_path, "rb") as f_in:
            ciphertext = f_in.read()

        # decrypt
        plaintext = f.decrypt(ciphertext)

        # create output path: remove ".enc" if present, then add ".dec"
        if selected_file_path.endswith(".enc"):
            dec_path = selected_file_path[:-4] + ".dec"
        else:
            dec_path = selected_file_path + ".dec"

        with open(dec_path, "wb") as f_out:
            f_out.write(plaintext)

        symmetric_encrypt_textbox.delete("1.0", "end")
        symmetric_encrypt_textbox.insert(
            "1.0",
            f"File decrypted successfully!\nSaved as:\n{dec_path}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")


# ASYMMETRIC ENCRYPTION (RSA)

def generate_rsa_keypair(key_size_bits=2048):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size_bits,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def generate_and_show_keys():
    global rsa_private_key, rsa_public_key

    rsa_private_key, rsa_public_key = generate_rsa_keypair()
    # formatting the keys 
    private_pem = rsa_private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = rsa_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    key_window = tk.Toplevel(window)
    key_window.title("RSA Key Pair")
    key_window.geometry("700x500")

    pub_label = tk.Label(key_window, text="Public Key:", font=("Arial", 10, "bold"))
    pub_label.pack(pady=(10, 0))

    pub_text = tk.Text(key_window, height=10, wrap="word")
    pub_text.pack(fill="both", expand=False, padx=10, pady=(0, 10))
    pub_text.insert("1.0", public_pem.decode())
    pub_text.config(state="disabled")

    priv_label = tk.Label(key_window, text="Private Key:", font=("Arial", 10, "bold"))
    priv_label.pack(pady=(10, 0))

    priv_text = tk.Text(key_window, height=10, wrap="word")
    priv_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))
    priv_text.insert("1.0", private_pem.decode())
    priv_text.config(state="disabled")


def rsa_encrypt():
    """
    Read plaintext from the encryption textbox,
    encrypt it with the RSA public key (OAEP + SHA-256),
    and put base64 ciphertext into the decryption textbox.
    """
    global rsa_public_key

    # 1) Make sure we have a public key
    if rsa_public_key is None:
        messagebox.showerror("Error", "Generate the RSA key pair first.")
        return

    # 2) Get plaintext from textbox
    plaintext = encryption_textbox.get("1.0", "end-1c")  # remove trailing newline

    if not plaintext.strip():
        messagebox.showerror("Error", "Please enter some text to encrypt.")
        return

    # 3) Convert plaintext string -> bytes
    plaintext_bytes = plaintext.encode("utf-8")

    # 4) Encrypt with RSA using OAEP padding (with SHA-256)
    ciphertext_bytes = rsa_public_key.encrypt(
        plaintext_bytes,
        res_padding.OAEP(
            mgf=res_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 5) Convert ciphertext bytes -> base64 string so we can display it in a textbox
    ciphertext_b64 = base64.b64encode(ciphertext_bytes).decode("utf-8")

    # 6) Show ciphertext in the decryption textbox
    decryption_textbox.delete("1.0", "end")
    decryption_textbox.insert("1.0", ciphertext_b64)


def rsa_decrypt():
    """
    Read base64 ciphertext from the decryption textbox,
    decode + decrypt it with the RSA private key,
    and put the recovered plaintext back into the encryption textbox.
    """
    global rsa_private_key

    # 1) Make sure we have a private key
    if rsa_private_key is None:
        messagebox.showerror("Error", "Generate the RSA key pair first.")
        return

    # 2) Get ciphertext (base64 string) from textbox
    ciphertext_b64 = decryption_textbox.get("1.0", "end-1c")

    if not ciphertext_b64.strip():
        messagebox.showerror("Error", "Please enter ciphertext to decrypt.")
        return

    try:
        # 3) Convert base64 string -> raw ciphertext bytes
        ciphertext_bytes = base64.b64decode(ciphertext_b64)
    except Exception:
        messagebox.showerror("Error", "Invalid base64 ciphertext.")
        return

    try:
        # 4) Decrypt with RSA using same OAEP parameters
        plaintext_bytes = rsa_private_key.decrypt(
            ciphertext_bytes,
            res_padding.OAEP(
                mgf=res_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except Exception:
        messagebox.showerror("Error", "Decryption failed. Wrong ciphertext or key.")
        return

    # 5) Convert bytes -> string
    plaintext = plaintext_bytes.decode("utf-8", errors="replace")

    # 6) Show plaintext back in the encryption textbox
    encryption_textbox.delete("1.0", "end")
    encryption_textbox.insert("1.0", plaintext)


def select_file():
    global selected_file_path

    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    selected_file_path = file_path

    # try to preview only if it's an image
    try:
        img = Image.open(file_path)
        img = img.resize((300, 300))
        tk_img = ImageTk.PhotoImage(img)

        image_preview.config(image=tk_img, text="")
        image_preview.image = tk_img
    except Exception:
        # not an image or cannot preview
        image_preview.config(image="", text="No image preview available.")
        image_preview.image = None


window = tk.Tk()
window.title("Cryptography Project")
window.geometry("600x600")

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill='both')

asymmetric_tab = ttk.Frame(notebook)
notebook.add(asymmetric_tab, text='Asymmetric Encryption')

asymmetric_label = ttk.Label(asymmetric_tab, text="Text Encryption (RSA)")
asymmetric_label.pack(pady=10)

public_key_button = ttk.Button(
    asymmetric_tab,
    text="Generate Key Pair",
    command=generate_and_show_keys
)
public_key_button.pack(pady=5)

encryption_textbox = tk.Text(asymmetric_tab, height=10)
encryption_textbox.pack(pady=5)

encryption_button = ttk.Button(
    asymmetric_tab,
    text="Encrypt Text",
    command=rsa_encrypt
)
encryption_button.pack(pady=5)

decryption_textbox = tk.Text(asymmetric_tab, height=10)
decryption_textbox.pack(pady=5)

decryption_button = ttk.Button(
    asymmetric_tab,
    text="Decrypt Text",
    command=rsa_decrypt
)
decryption_button.pack(pady=5)

symmetric_tab = ttk.Frame(notebook)
notebook.add(symmetric_tab, text='Symmetric Encryption')

symmetric_label = ttk.Label(symmetric_tab, text="File Encryption (Fernet)")
symmetric_label.pack(pady=10)

insert_file_button = tk.Button(symmetric_tab, text="File Browse", command=select_file)
insert_file_button.pack(pady=10)

image_preview = tk.Label(symmetric_tab, text="No image selected")
image_preview.pack(pady=10)

symmetric_encrypt_textbox = tk.Text(symmetric_tab, height=10)
symmetric_encrypt_textbox.pack(pady=10)

symmetric_encrypt_button = tk.Button(
    symmetric_tab,
    text="Encrypt File",
    command=fernet_encrypt
)
symmetric_encrypt_button.pack(pady=10)

symmetric_decrypt_button = tk.Button(
    symmetric_tab,
    text="Decrypt File",
    command=fernet_decrypt
)
symmetric_decrypt_button.pack(pady=10)

window.mainloop()
