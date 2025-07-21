# =================================================================
# AUTHOR: hubter125
# DATE: 7/21/2025
# PROGRAM: Port Scanner
# PURPOSE: Practice my coding and learn network programming
# =================================================================
import socket

class Bcolors:
    HIGHLIGHT = '\033[93m'
    ENDC = '\033[0m'

# Get IP and Port

def target_details():
    """
    prompt user for ip and port
    :return: string ip address and port list
    """
    port_list = []
    ip = input("Enter ip address: ")
    port = int(input("Enter port, type 99999 to quit: "))
    while port != 99999:
        if port < 0 or port > 65535:
            print("Enter a real port this time... ")
            port = int(input("Enter port, type 99999 to quit: "))
        else:
            port_list.append(port)
            port = int(input("Enter port: "))
    return ip, port_list

def port_test(ip, port):
    """
    Takes an ip and port and attempts to connect to it
    :param ip: ipv4 standard notation
    :param port: any port
    :return: return server response
    """

    response = None # If connection fails, it returns response but only inside try block
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(4)
        client_socket.connect((ip, port))
        client_socket.send(b"GET / HTTP/1.0\r\n\r\n")
        response = client_socket.recv(1024).decode().strip()
        client_socket.close()
        print(f"Server response from {Bcolors.HIGHLIGHT}{ip}:{port}{Bcolors.ENDC}: ", response)
    except socket.error:
        print("Connection refused by the server")
    return response

# Split this port_test function into two parts, open_ports and service_detection, add threading for speed


def main():
    ip, port_list = target_details()
    # Looping through port list and testing each port, should look into threading
    for port in port_list:
        response = port_test(ip, port)

if __name__ == '__main__':
    main()
