import socket
from queue import Queue
import threading
from IPy import IP

# number of threads to be used
NUM_THREADS = 200
def scan_ports(target, port_queue,open_ports):
    while not port_queue.empty():
        port = port_queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1) # in seconds
            if s.connect_ex((target, port)) == 0:
                print(f"Port {port}: Open")
                open_ports.append(port)
            else:
                print(f"Port {port}: Closed")
                s.close()
        except socket.gaierror:
            print("Hostname could not be resolved")
            break
        except socket.error:
            print("Couldn't connect to the server")
            break
        except Exception as e:
            print(f"Error while scanning this port {port}: {e}")
def main():
    print("Program started")
    try:
        # get the target host IP/hostname & the ports to scan
        target_host = input("Enter the target host IP or hostname:")
        target_ports = input("Enter the range of ports to scan(eg. 1-200):")

        # parse the ports range
        start_port , end_port = map(int, target_ports.split('-'))
        port_range = range(start_port, end_port + 1)
        try:
            IP(target_host)
            target_ip = target_host
        except ValueError:
            target_ip = socket.gethostbyname(target_host)
        port_queue = Queue()
        for port in port_range:
            port_queue.put(port)
        open_ports = []
        thread_list = []
        for _ in range(min(NUM_THREADS, len(port_range))):
            thread = threading.Thread(target=scan_ports,args=(target_ip,port_queue,open_ports))
            thread_list.append(thread)
            thread.start()
        for thread in thread_list:
            thread.join()
        if open_ports:
            print("\nSummary:")
            for port in open_ports:
                print(f"Port {port}: Open")
        else:
            print("No open ports found.") 
    except KeyboardInterrupt:
        print("\nPort Scanning Interrupted")
    except ValueError:
        print("Invalid input ,please enter a valid IP address/hostname and port range:")
if __name__ == "__main__":
    main()
    
 


