Hybrid Cryptography GUI – Architecture Overview

This project implements a graphical application that demonstrates both symmetric and asymmetric cryptography inside a single Python interface. The GUI is built using Tkinter, and all cryptographic operations are powered by the cryptography library. Pillow (PIL) is used for file previewing.

📌 High-Level Architecture

The program is structured into three core layers:

User Interface Layer (Tkinter GUI)

Asymmetric Encryption Module (RSA – text encryption)

Symmetric Encryption Module (Fernet – file encryption)

A ttk.Notebook organizes the GUI into two tabs—one for RSA text encryption and one for Fernet-based file encryption.

Several global variables store session-wide cryptographic state such as the RSA keypair, the selected file, and the active Fernet key.

🖥️ User Interface Layer (Tkinter)

The GUI is implemented using Tkinter components:

window: The root application window

ttk.Notebook: Provides two separate tabs:

Asymmetric Encryption — RSA key generation, text encryption, and decryption

Symmetric Encryption — file selection, image preview, and Fernet encryption/decryption

The program uses Label, Button, and Text widgets to gather and display user input.
Error handling is performed using messagebox.showerror().

🔐 Asymmetric Encryption Module (RSA)

This module handles public-key encryption using 2048-bit RSA.
Keys are stored in two global variables:

rsa_public_key

rsa_private_key

Key Generation

generate_rsa_keypair() creates a 2048-bit RSA key pair using exponent 65537.
generate_and_show_keys():

Generates keys

Serializes them to PEM format

Displays them inside a separate window

RSA Encryption Workflow

rsa_encrypt():

Reads plaintext from the GUI text box

Encodes it to bytes

Encrypts using the public key + OAEP (SHA-256)

Base64-encodes the ciphertext

Outputs it to the decryption textbox

RSA Decryption Workflow

rsa_decrypt():

Reads base64 ciphertext

Decodes to raw bytes

Decrypts using the private key + OAEP (SHA-256)

Converts to UTF-8 text

Displays the recovered plaintext

This module demonstrates secure asymmetric text encryption within the GUI.

🔐 Symmetric Encryption Module (Fernet)

This module performs file encryption using the Fernet authenticated encryption scheme.

Globals

selected_file_path – path of chosen file

fernet_key_global – session-wide Fernet key

File Selection

select_file():

Opens a file chooser dialog

Stores the file path

Attempts to display a 300×300 image preview using PIL

File Encryption

fernet_encrypt():

Ensures a Fernet key exists (generates once per session)

Reads raw file bytes

Encrypts with Fernet(key)

Saves output as <filename>.enc

Displays the new path in the GUI

File Decryption

fernet_decrypt():

Reads ciphertext from the selected .enc file

Decrypts using the same Fernet key

Writes plaintext to <filename>.dec

Displays path in output box

This module demonstrates modern authenticated symmetric encryption on arbitrary files.

🧩 Summary

This hybrid cryptography application cleanly separates GUI interaction from cryptographic logic:

RSA (asymmetric) securely encrypts/decrypts text

Fernet (symmetric) encrypts/decrypts full files

A simple, tab-based Tkinter interface organizes the two systems

Image preview enhances usability when encrypting image files

