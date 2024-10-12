# GUTS Hackathon CTF

Welcome to the CTF! Each of the challenges have been outlined below along with links to information which you may find helpful.

All flags take the format of `flag{secret_phrase_here}`

## Prerequisites

- python if you'd like to run the example code below

# Part 1 - ctf-server

Navigate to `bin/`, run the executable which matches your platform (windows/linux/mac), and take a look at the output.

You may need to click "Yes" or "Allow" to permit the binary from running and allow it through your antivirus and firewall programs.

You should see the following two lines:

```
...
4:39PM INF Listening on HTTPS '127.0.0.1:8080'
4:39PM INF Listening on TCP '127.0.0.1:8888'
...
```

If you see these lines then it means the server is ready to go and you can proceed to the next section.
You can start with task 1 or task 2, they don't depend on each other.

## Task 1

In this task you'll need to write a program to connect to the server using the TCP protocol.
The server will ask you a series of questions and you will need to anwser them.
If you get them right then the server will tell you the flag.

IP Address: 127.0.0.1
Port: 8888

Below is some example python code to get you started:

```python
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(('127.0.0.1', 8888))

# Receive data
data = s.recv(1024)

# Print the received data
print('Received = ', data.decode())

# Send data "abc" and send a newline "\n" to simulate pressing enter
s.sendall(b'abc\n')

# Receive more data
data = s.recv(1024)

# Print the received data
print('Received = ', data.decode())

# Close the connection
s.close()
```

You can also use a tool like "netcat" or "putty" to connect to the server without the need to write any code.

## Task 2

This task can be completed in your web browser. Access the website by visiting `https://127.0.0.1:8080/`.

> Note: make sure you access the webpage over `https://`.
> If your browser shows a warning about an insecure webpage you'll need
> to ignore it (in chrome you can do this by clicking `Advanced`)

You may want to read up on the following topics to help you with this challange:
- How to open the web browser developer tools
- How to read HTML source code of a website
- How cookies work
- What "base64" encoding is (you can play around with it here https://gchq.github.io/CyberChef/)

Hacking the website will reveal a flag. 

There is a secret third flag hidden in this website, see if you can find it! 
If you need a hint, you can use what you learned in hacking the website to reveal the hint below:

`UmVzZWFyY2ggSFRUUFMgKyBUTFMgYW5kIGhvdyBjZXJ0aWZpY2F0ZXMgd29yaw==`

# Part 2 - cryptography

In this section there are 6 cryptography challenges to solve.
The challenge files contain a cipher (sometimes a key and hint included) and in one case an image that you need to decode or decipher.

The flags that you will find after a successful attempt will be in the format: `flag{\<some text\>}`, with the exception of the 2 flags in the 6th challenge.
