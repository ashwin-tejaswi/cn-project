# SNIST CN Project 3-1
**Subject:** Computer Networks  
**Language:** Python   
**Members:**  
-  Dinesh reddy 
- Ashwin tejaswi
- Bhavana reddy
- Kavya harge 

---

## 📌 Problem Statement
Using TCP/IP sockets, create a Client–Server program where:
- The **client sends a filename** to the server.
- The **server reads the file** (if it exists) and sends its **content back to the client**.

---

## 📘 Description
This project implements a simple **TCP-based File Request System**.

It contains:
- `server.py` → Waits for client connection, receives filename, sends file content.
- `client.py` → Sends filename to server and displays the server’s response.

The server will return:
- File content (if available)  
- “File not found”  
- Or an error message  

This project uses Python’s built-in **socket** module and demonstrates the basics of **TCP communication**.

---

## 🛠 How to Run the Project

 ✔ 1. Start the Server  
Open Terminal 1 in VS Code:

python server.py

 ✔ 2. Run the Client
Open Terminal 2 in VS Code:

python client.py

Enter the filename you want to retrieve, example:

sample.txt

<img width="868" height="82" alt="Screenshot 2025-11-30 213041" src="https://github.com/user-attachments/assets/1804bd69-3f52-49e5-8a4b-88e496c1c705" />




<img width="674" height="158" alt="Screenshot 2025-11-30 213119" src="https://github.com/user-attachments/assets/02489594-0545-406d-bf77-0a2dac535713" />


<img width="777" height="152" alt="Screenshot 2025-11-30 213134" src="https://github.com/user-attachments/assets/f4b02220-d4c8-40a4-b901-fb768164d2ab" />


