import socket
import argparse

def find_subdomain(domain, wordlist_path, verbose=False):
    """
    指定されたドメインのサブドメインを検索する関数。
    
    Args:
        domain (str): ターゲットのドメイン（例：example.com）
        wordlist_path (str): サブドメイン候補が記載された辞書ファイルのパス
        verbose (bool): 詳細なエラーメッセージを表示するかどうか
        
    Returns:
        list: 有効なサブドメインのリスト
    """
    discovered_subdomains = []
    hidden_errors = 0
    
    print(f"[*] Scanning subdomains for: {domain}")
    print(f"[*] Using wordlist: {wordlist_path}\n")
    
    try:
        with  open(wordlist_path, 'r', encoding='utf-8') as file:
            for line in file:
                subdomain_candidate = line.strip()
                if not subdomain_candidate:
                    continue
                
                full_domain = f"{subdomain_candidate}.{domain}"
                
                try:
                    # DNS解決を試みる
                    ip_address = socket.gethostbyname(full_domain)
                    print(f"[+] Found: {full_domain} (IP:{ip_address})")
                    discovered_subdomains.append(full_domain)
                except socket.gaierror as e:
                    # DNS解決に失敗した場合
                    if verbose:
                        print(f"[-] Error resolving {full_domain}: {e}")
                    else:
                        hidden_errors += 1
                except UnicodeError:
                    if verbose:
                        print(f"[-] Skipping invlalid subdomain: {subdomain_candidate}")
                    else:
                        hidden_errors += 1
                except Exception as e:
                    # その他の予期しないエラー
                    if verbose:
                        print(f"[-] Unexpected error with {full_domain}: {e}")
                    else:
                        hidden_errors += 1
                        
    except FileNotFoundError:
        print(f"[!] Error: Wordlist file not found: {wordlist_path}")
        return [] # 空のリストを返す
    except Exception as e:
        print(f"[!] Unexpected error reading wordlist: {hidden_errors}")
        return []
    
    if not verbose and hidden_errors > 0:
        print(f"\n[*] Note: {hidden_errors} errors occurred during the scan. Use -v for more details.")
    
    return discovered_subdomains

def main():
    parser = argparse.ArgumentParser(description="Simple Subdomain Scanner")
    parser.add_argument("domain", help="Target domain(e.g., example.com)")
    parser.add_argument("wordlist", help="Path to the subdomain wordlist file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed error messages")
    parser.add_argument("-o", "--output", help="Output file to save discovered subdomains")
    
    args = parser.parse_args()
    
    found_subdomains = find_subdomain(args.domain, args.wordlist, args.verbose)
    
    if found_subdomains:
        print("\n[*] Discovered subdomains:")
        for subdomain in found_subdomains:
            print(f"  - {subdomain}")
        
        if args.output:
            try:
                with open(args.output, 'w', encoding='utf-8') as output_file:
                    for subdomain in found_subdomains:
                        output_file.write(f"{subdomain}\n")
                print(f"\n[*] Results saved to: {args.output}")
            except Exception as e:
                print(f"[!] Error saving results: {e}")
    else:
        print("\n[*] No subdomains found or an error occurred during the scan.")

if __name__ == "__main__":
    main()
# This script is a simple subdomain scanner that takes a target domain and a wordlist file,