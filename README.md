# Multi-threaded-Port-Scanner
# Multithreaded TCP Port Scanner

## Overview

This project is a Python-based Multithreaded TCP Port Scanner that scans a specified range of ports on a target host and identifies which ports are open. The scanner uses multiple threads to improve scanning speed and supports both IP addresses and hostnames.

## Features

* Scans a user-defined range of TCP ports.
* Supports both IP addresses and domain names.
* Uses multithreading for faster scanning.
* Displays open and closed ports during the scan.
* Provides a summary of all open ports after completion.
* Handles invalid hostnames and connection errors gracefully.

## Requirements

### Python Version

* Python 3.8 or higher

### Required Modules

Install the required package:

```bash
pip install IPy
```

### Built-in Modules Used

* socket
* threading
* queue

## Project Structure

```text
port-scanner/
│
├── scan.py
└── README.md
```

## How It Works

1. The user enters a target IP address or hostname.
2. The user specifies a port range to scan.
3. The program validates the target host.
4. A queue is created containing all ports in the specified range.
5. Multiple threads are launched to scan ports concurrently.
6. Each thread attempts to establish a TCP connection to a port.
7. Open ports are recorded and displayed.
8. After all threads finish, a summary of open ports is shown.

## Running the Program

Open a terminal in the project directory and run:

```bash
python scan.py
```

## Example

### Input

```text
Enter the target host IP or hostname: 127.0.0.1
Enter the range of ports to scan (eg. 1-200): 20-100
```

### Output

```text
Port 22: Open
Port 80: Open
Port 21: Closed
Port 23: Closed

Summary:
Port 22: Open
Port 80: Open
```

## Code Components

### scan_ports()

This function:

* Retrieves ports from the queue.
* Attempts a TCP connection to each port.
* Identifies whether the port is open or closed.
* Stores open ports in a list.

### main()

This function:

* Accepts user input.
* Validates the target host.
* Creates the port queue.
* Launches worker threads.
* Displays scanning results.

## Error Handling

The program handles:

* Invalid hostnames.
* Network connection errors.
* Invalid port ranges.
* User interruption using Ctrl + C.

## Limitations

* Scans only TCP ports.
* Does not perform service detection.
* May be slower on networks with high latency.
* Results depend on firewall and network configurations.

## Educational Purpose

This project is intended for educational purposes to demonstrate:

* Socket programming
* Multithreading in Python
* Queue management
* Basic network scanning concepts

Always scan only systems and networks that you own or have explicit permission to test.

## Author

Created as a Python networking and multithreading project for learning port scanning concepts.
