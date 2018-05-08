import socket
import msvcrt

# def getch():
#   myInput = msvcrt.getch()
#   return myInput

UDP_IP = "172.16.27.2"
UDP_PORT = 9999

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("")
print("W, A, S, D - Move mouse")
print("Space      - Click")
print("Q          - Quit")


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while True:
    # key = ord(getch())
    key = ord(msvcrt.getch())
    print("执行Key编码： >  ",key)
    if key == 119: # W
        sock.sendto('0', (UDP_IP, UDP_PORT))
    elif key == 97: # A
        # print 'left'
        sock.sendto('2', (UDP_IP, UDP_PORT))
    elif key == 115: # S
        # print 'down'
        sock.sendto('1', (UDP_IP, UDP_PORT))
    elif key == 100: # D
        # print 'right'
        sock.sendto('3', (UDP_IP, UDP_PORT))
    elif key == 113: # Q
        break
    elif key == 32: # Space
        # print 'click'
        sock.sendto('4', (UDP_IP, UDP_PORT))


