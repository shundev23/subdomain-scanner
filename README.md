[日本語](#japanese) | [English](#english)

---
<a name="japanese"></a>

# シンプルサブドメインスキャナー (Simple Subdomain Scanner)

指定されたドメインのサブドメインを、単語リスト（辞書ファイル）を使用して発見するためのシンプルなPython製ツールです。このツールはDNSルックアップを実行し、アクティブなサブドメインを特定します。

## 機能

* 提供された単語リストに基づいてサブドメインを発見
* 発見されたサブドメインのIPアドレスを解決
* カスタム単語リストファイルのサポート
* 詳細なログ出力のための冗長モード（解決エラーも表示）
* 発見されたサブドメインをファイルに保存するオプション

## 要件

* Python 3.7以降

（基本的な機能については、Python標準ライブラリ以外の外部ライブラリは不要です。）

## インストール

1. リポジトリをクローンします:
    ```bash
    git clone [https://github.com/your-username/subdomain-scanner.git](https://github.com/your-username/subdomain-scanner.git)
    ```
2. プロジェクトディレクトリに移動します:
    ```bash
    cd subdomain-scanner
    ```
    *（もし外部ライブラリを使用する場合、通常ここで `pip install -r requirements.txt` を実行してインストールします。）*

## 使い方

スキャナーを実行するには、以下のコマンド構造を使用します:

```bash
python subdomain_scanner.py <ターゲットドメイン> <単語リストファイルのパス> [オプション]
```

### 引数

* <ターゲットドメイン>: スキャンしたいドメイン (例: example.com)
* <単語リストファイルのパス>: サブドメイン候補が1行に1つずつ記載されたファイルへのパス

### オプション

* -h, --help: ヘルプメッセージを表示して終了します。
* -v, --verbose: 詳細な出力を有効にし、すべてのDNS解決試行とエラーを表示します。
* -o OUTPUT, --output OUTPUT: 発見されたサブドメインのリストを指定されたファイルに保存します。

### 実行例

* example.com を wordlists/common_subdomains.txt を使ってスキャン
```bash
python subdomain_scanner.py example.com wordlists/common_subdomains.txt
```
* example.com を冗長モードでスキャンし、結果を found_subdomains.txt に保存
```bash
python subdomain_scanner.py example.com wordlists/large_wordlist.txt -v -o found_subdomains.txt
```
## 単語リスト（辞書ファイル）について
このツールには、各行に潜在的なサブドメイン名（メインドメイン部分を含まない）が記述された単語リストファイルが必要です。
```
www
mail
blog
dev
test
```
独自の単語リストを作成するか、以下のような公開されているコレクションから包括的なものを見つけることができます。

[SecLists (Discovery/DNS)](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)

単語リストファイルは wordlists/ ディレクトリに配置するか、ファイルへのフルパスを指定してください。

## ⚠️ 免責事項
このツールは、教育および研究目的でのみ提供されています。
本ツールの使用にあたっては、利用者がすべての適用される地方、州、連邦の法律および規制を遵守する責任を負います。

システム所有者から明示的かつ事前の書面による許可を得ていないシステムに対して、本ツールを使用することは固く禁じられています。 

システムへの不正なスキャンは敵対行為とみなされ、法的結果を招く可能性があります。

本ツールの開発者および貢献者は、本プログラムの誤用またはそれによって引き起こされたいかなる損害についても一切の責任を負いません。自己責任において使用してください。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています - 詳細は LICENSE ファイルをご覧ください。


# Simple Subdomain Scanner
A simple Python tool to discover subdomains of a given domain using a wordlist. This tool performs DNS lookups to identify active subdomains.

## Features
* Discovers subdomains based on a provided wordlist.
* Resolves IP addresses for discovered subdomains.
* Support for custom wordlist files.
* Verbose mode for detailed logging (shows resolution errors).
* Option to save discovered subdomains to an output file.

## Requirements
* Python 3.7+

(No external libraries are required for the basic functionality beyond the Python standard library.)

## Installation
1. Clone the repository
```bash
git clone [https://github.com/your-username/subdomain-scanner.git](https://github.com/your-username/subdomain-scanner.git)
```

2. Navigate to the project directory
```bash
cd subdomain-scanner
```

## Usage
To run the scanner, use the following command structure
```bash
python subdomain_scanner.py <target_domain> <wordlist_path> [options]
```

### Arguments
* <target_domain>: The domain you want to scan (e.g., example.com).
* <wordlist_path>: Path to the file containing subdomain candidates (one per line).

### Options
* -h, --help: Show the help message and exit.
* -v, --verbose: Enable verbose output, showing all DNS resolution attempts and errors.
* -o OUTPUT, --output OUTPUT: Save the list of discovered subdomains to the specified file.

### Examples
* Scan example.com using wordlists/common_subdomains.txt
```bash
python subdomain_scanner.py example.com wordlists/common_subdomains.txt
```
* Scan example.com with verbose output and save results to found_subdomains.txt
```bash
python subdomain_scanner.py example.com wordlists/large_wordlist.txt -v -o found_subdomains.txt
```

## Wordlists
This tool requires a wordlist file where each line contains a potential subdomain name (without the main domain part). For example
```
www
mail
blog
dev
test
```
You can create your own wordlists or find comprehensive ones in publicly available collections such as

[SecLists (Discovery/DNS)](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)

Place your wordlist files in the wordlists/ directory or provide the full path to your wordlist file.

## ⚠️ Disclaimer
This tool is provided for educational and research purposes only.

The user is solely responsible for ensuring that they are in compliance with all applicable local, state, and federal laws and regulations before using this tool.

Under no circumstances should this tool be used to scan, test, or interact with systems for which you do not have explicit, prior, written permission from the system owner. Unauthorized scanning of systems can be considered a hostile act and may lead to legal consequences.

The developers and contributors of this tool assume no liability and are not responsible for any misuse or damage caused by this program. Use at your own risk.

## License
This project is licensed under the MIT License - see the LICENSE file for details.