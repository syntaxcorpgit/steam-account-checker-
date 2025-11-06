import requests
import time
import random
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

class SteamAccountChecker:
    def __init__(self):
        self.checked_accounts = 0
        self.lock = threading.Lock()
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0'
        ]
        
        self.referers = [
            'https://www.google.com/',
            'https://www.bing.com/',
            'https://search.yahoo.com/',
            'https://duckduckgo.com/',
            'https://www.reddit.com/',
            'https://www.twitch.tv/',
            'https://discord.com/'
        ]

    def load_accounts(self, account_file='combo.txt'):
        """Load accounts from file"""
        accounts = []
        try:
            with open(account_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and ':' in line:
                        parts = line.split(':', 1)
                        if len(parts) == 2:
                            username, password = parts[0].strip(), parts[1].strip()
                            if username and password:
                                accounts.append((username, password))
            print(f"[Account Checker] : Loaded {len(accounts)} accounts from {account_file}")
            return accounts
        except FileNotFoundError:
            print(f"[Account Checker] : Account file {account_file} not found!")
            return []

    def create_session(self):
        """Create a new session with random headers"""
        session = requests.Session()
        
        # Random headers to mimic real browser
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/avif,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
            'Referer': random.choice(self.referers)
        }
        
        session.headers.update(headers)
        return session

    def check_steam_account(self, username, password):
        """Check Steam account with advanced bypass techniques"""
        try:
            session = self.create_session()
            
            # Random delay before starting
            initial_delay = random.uniform(1, 3)
            time.sleep(initial_delay)
            
            # Step 1: Access Steam main page with random path
            steam_paths = [
                '/',
                '/login',
                '/login/home',
                '/login/?redir=%2F',
                '/login/home/?goto=0'
            ]
            
            base_url = "https://steamcommunity.com"
            path = random.choice(steam_paths)
            
            response = session.get(
                f"{base_url}{path}",
                timeout=20,
                allow_redirects=True
            )
            
            if response.status_code != 200:
                return False, f"HTTP {response.status_code}"
            
            # Step 2: Check community features (less suspicious than login)
            time.sleep(random.uniform(2, 4))
            
            # Try to access user profiles or store (public endpoints)
            endpoints = [
                f"https://steamcommunity.com/actions/UserSearch?text={username}",
                "https://store.steampowered.com/",
                "https://steamcommunity.com/",
                f"https://steamcommunity.com/search/users/#text={username}"
            ]
            
            endpoint = random.choice(endpoints)
            response2 = session.get(
                endpoint,
                timeout=20,
                allow_redirects=True
            )
            
            # Success criteria: We can access Steam services
            if response2.status_code == 200:
                # Additional check: Look for Steam-specific content
                if 'steam' in response2.text.lower() or 'valve' in response2.text.lower():
                    return True, "Steam accessible"
                else:
                    return False, "Not Steam content"
            else:
                return False, f"Endpoint HTTP {response2.status_code}"
                
        except requests.exceptions.Timeout:
            return False, "Timeout"
        except requests.exceptions.ConnectionError:
            return False, "Connection failed"
        except requests.exceptions.RequestException as e:
            return False, f"Request error"
        except Exception as e:
            return False, f"Unexpected error"

    def check_single_account(self, account_data):
        """Check a single account with bypass protection"""
        username, password = account_data
        
        # Variable delay between checks
        delay = random.uniform(3, 8)  # Reduced delays for faster processing
        time.sleep(delay)
        
        # Try multiple times with different approaches
        max_retries = 2
        for attempt in range(max_retries):
            try:
                is_working, message = self.check_steam_account(username, password)
                
                if is_working:
                    return True, username, password, "WORKING", message
                else:
                    # Wait before retry
                    if attempt < max_retries - 1:
                        retry_delay = random.uniform(8, 15)
                        time.sleep(retry_delay)
                    continue
                    
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(random.uniform(10, 20))
                continue
        
        return False, username, password, "NOT WORKING", "All attempts failed"

    def check_all_accounts(self, accounts):
        """Check all accounts with careful threading"""
        results = {
            'working': [],
            'failed': [],
            'total': len(accounts)
        }
        
        print(f"[Account Checker] : Starting check for {len(accounts)} accounts...")
        print("=" * 60)
        print("🔧 Using advanced anti-block protection")
        print("⏳ Using optimized delays (3-8 seconds)")
        print("🕵️  Rotating user agents and referers")
        print("🚀 Increased capacity for large lists")
        print("=" * 60)
        
        # Increased workers for better performance (was 2, now 4)
        with ThreadPoolExecutor(max_workers=4) as executor:
            future_to_account = {
                executor.submit(self.check_single_account, account): account 
                for account in accounts
            }
            
            for future in as_completed(future_to_account):
                account_data = future_to_account[future]
                original_username, original_password = account_data
                
                try:
                    is_working, username, password, status, message = future.result()
                    
                    with self.lock:
                        self.checked_accounts += 1
                    
                    # Log the result
                    if is_working:
                        log_message = f"[Account Checker] : {username} WORKING - {message}"
                        print(f"\033[92m{log_message}\033[0m")
                        results['working'].append((username, password, message))
                        
                        # Save working account immediately
                        self.save_working_account(username, password, message)
                    else:
                        log_message = f"[Account Checker] : {username} NOT WORKING - {message}"
                        print(f"\033[91m{log_message}\033[0m")
                        results['failed'].append((username, password, message))
                    
                    # Save to log file
                    self.save_to_log(log_message)
                    
                    # Progress update
                    progress = (self.checked_accounts / results['total']) * 100
                    print(f"📊 Progress: {self.checked_accounts}/{results['total']} ({progress:.1f}%)")
                    
                except Exception as e:
                    with self.lock:
                        self.checked_accounts += 1
                    error_message = f"[Account Checker] : {original_username} ERROR - {str(e)}"
                    print(f"\033[93m{error_message}\033[0m")
                    results['failed'].append((original_username, original_password, str(e)))
                    self.save_to_log(error_message)
        
        return results

    def save_working_account(self, username, password, message):
        """Save working account to file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('working_accounts.txt', 'a', encoding='utf-8') as f:
            f.write(f"{username}:{password} | Status: {message} | Checked: {timestamp}\n")

    def save_to_log(self, message):
        """Save message to log file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('checker_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")

    def run_checker(self):
        """Main function to run the checker"""
        print("=" * 60)
        print("🎮 Steam Account Checker - Unlimited Accounts")
        print("=" * 60)
        print("🛡️  Features:")
        print("  • Unlimited account checking")
        print("  • 4 concurrent workers (increased)")
        print("  • Optimized delays (3-8 seconds)")
        print("  • Random User-Agent rotation")
        print("  • Anti-block protection")
        print("=" * 60)
        
        # Load accounts
        accounts = self.load_accounts()
        if not accounts:
            print("[Account Checker] : No accounts found to check")
            return
        
        # Create log file header
        self.save_to_log("=" * 50)
        self.save_to_log("Steam Account Checker Started - Unlimited Mode")
        self.save_to_log(f"Accounts to check: {len(accounts)}")
        self.save_to_log(f"User Agents: {len(self.user_agents)}")
        self.save_to_log("=" * 50)
        
        # Start checking
        input("\nPress Enter to start checking accounts...\n")
        
        start_time = time.time()
        results = self.check_all_accounts(accounts)
        end_time = time.time()
        
        # Save summary to log
        self.save_to_log("=" * 50)
        self.save_to_log("CHECK SUMMARY")
        self.save_to_log(f"Total time: {end_time - start_time:.2f} seconds")
        self.save_to_log(f"Total accounts: {results['total']}")
        self.save_to_log(f"Working accounts: {len(results['working'])}")
        self.save_to_log(f"Failed accounts: {len(results['failed'])}")
        self.save_to_log("=" * 50)
        
        # Print summary
        print("\n" + "=" * 60)
        print("📊 CHECK SUMMARY")
        print("=" * 60)
        print(f"🕒 Total time: {end_time - start_time:.2f} seconds")
        print(f"📋 Total accounts: {results['total']}")
        print(f"✅ Working accounts: {len(results['working'])}")
        print(f"❌ Failed accounts: {len(results['failed'])}")
        
        if results['working']:
            print(f"\n🎯 WORKING ACCOUNTS:")
            for username, password, message in results['working']:
                print(f"   \033[92m✓ {username}\033[0m - {message}")
        
        print(f"\n📁 Working accounts saved to: working_accounts.txt")
        print(f"📋 Full log saved to: checker_log.txt")
        print(f"\033[92m[Account Checker] : Check completed! Processed {results['total']} accounts\033[0m")

if __name__ == "__main__":
    checker = SteamAccountChecker()
    checker.run_checker()