import hashlib
import os
import shutil
import time

# --- [ CONFIGURATION ] ---
SECRET_SALT = "ohmygod@123"
# run.py က သိမ်းတဲ့ နေရာအတိုင်း အတိအကျ သတ်မှတ်ထားခြင်း
LICENSE_PATH = os.path.join(os.path.expanduser("~"), ".turbo_license")
KEYS_LOG = "keys.txt"

# --- [ UI COLORS ] ---
C_CYAN, C_GREEN, C_YELLOW, C_WHITE, C_RED, C_RESET, C_BOLD = '\033[96m', '\033[92m', '\033[93m', '\033[97m', '\033[91m', '\033[0m', '\033[1m'

def print_banner():
    os.system('clear')
    w = shutil.get_terminal_size().columns
    logo = f"""
{C_GREEN}{C_BOLD} ██████╗███╗   ███╗███╗   ██╗███████╗
██╔════╝████╗ ████║████╗  ██║██╔════╝
╚█████╗ ██╔████╔██║██╔██╗ ██║███████╗
 ╚═══██╗██║╚██╔╝██║██║╚██╗██║╚════██║
██████╔╝██║ ╚═╝ ██║██║ ╚████║███████║
╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝{C_RESET}"""
    for line in logo.split('\n'):
        print(line.center(w))
    print(f"{C_YELLOW}{C_BOLD}{'SMNS ADMIN KEY GENERATOR'.center(w)}{C_RESET}")
    print(f"{C_CYAN}{'━' * (w-4)}{C_RESET}".center(w))

def make_key():
    print_banner()
    print(f"{C_WHITE}[*] Enter Device ID (Example: SMNS-49417534BE)")
    did = input(f"{C_YELLOW}[?] Device ID: {C_WHITE}").strip()
    if not did: return
    
    print(f"\n{C_WHITE}[*] Enter Expiry (Example: 202704131225)")
    expiry = input(f"{C_YELLOW}[?] Expiry Date: {C_WHITE}").strip()
    if not expiry: return
    
    # Key Generation Logic (SHA256)
    raw = f"{did}{expiry}{SECRET_SALT}"
    auth_hash = hashlib.sha256(raw.encode()).hexdigest()
    # ရှေ့ ၁၂ လုံး + Expiry ၁၂ လုံး ပေါင်းခြင်း
    final_key = f"{auth_hash[:12].upper()}{expiry}"
    
    # keys.txt ထဲမှာ မှတ်တမ်းသိမ်းခြင်း
    with open(KEYS_LOG, "a") as f:
        f.write(f"Device: {did} | Key: {final_key} | Exp: {expiry}\n")
    
    print(f"\n{C_GREEN}[✔] SUCCESS! KEY GENERATED!{C_RESET}")
    print(f"{C_CYAN}┌──────────────────────────────────────────┐")
    print(f"│ {C_YELLOW}DEVICE ID : {C_WHITE}{did:<24}{C_CYAN} │")
    print(f"│ {C_YELLOW}KEY       : {C_GREEN}{C_BOLD}{final_key:<24}{C_CYAN} │")
    print(f"└──────────────────────────────────────────┘{C_RESET}")
    input(f"\n{C_WHITE}Press Enter to go back...")

def delete_all_data():
    """System ထဲက License ဖိုင်နဲ့ keys.txt ကို အပြတ်ရှင်းခြင်း"""
    print_banner()
    print(f"{C_RED}{C_BOLD}[!] WARNING: THIS WILL RESET ALL SYSTEM ACCESS{C_RESET}")
    confirm = input(f"{C_YELLOW}[?] Confirm Reset? (y/n): {C_WHITE}").lower()
    
    if confirm == 'y':
        # ၁။ keys.txt ကို ဖျက်ခြင်း
        if os.path.exists(KEYS_LOG):
            os.remove(KEYS_LOG)
            print(f"{C_GREEN}[*] Deleted: {KEYS_LOG}{C_RESET}")
            
        # ၂။ .turbo_license ကို ဖျက်ခြင်း (ဒါမှ user ဆီမှာ Key ပြန်တောင်းမှာပါ)
        if os.path.exists(LICENSE_PATH):
            os.remove(LICENSE_PATH)
            print(f"{C_GREEN}[*] Deleted: System License File (.turbo_license){C_RESET}")
            print(f"{C_YELLOW}[!] All access has been reset successfully!{C_RESET}")
        else:
            print(f"{C_RED}[!] No active license found in system.{C_RESET}")
            
        time.sleep(2.5)
    else:
        print(f"{C_CYAN}[*] Operation cancelled.{C_RESET}")
        time.sleep(1)

if __name__ == "__main__":
    while True:
        print_banner()
        print(f"{C_WHITE}[1] {C_GREEN}GENERATE NEW SMNS KEY")
        print(f"{C_WHITE}[2] {C_RED}FULL SYSTEM RESET (DELETE ALL)")
        print(f"{C_WHITE}[3] {C_YELLOW}EXIT")
        
        opt = input(f"\n{C_CYAN}root@smns_admin:~# {C_WHITE}").strip()
        if opt == '1':
            make_key()
        elif opt == '2':
            delete_all_data()
        elif opt == '3':
            print(f"{C_GREEN}Goodbye!{C_RESET}")
            break
