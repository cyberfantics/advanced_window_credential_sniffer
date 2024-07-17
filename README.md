# Advanced User Account Info

**Developer:** Syed Mansoor ul Hassan Bukhari  
**GitHub:** [cyberfantics](https://github.com/cyberfantics)

## Overview

`advanced_user_account_info.py` is a Python script designed to retrieve detailed information about user accounts on a Windows machine. It lists user account details, including administrator status, password policies, and more. Additionally, it saves the retrieved information to a text file for easy access and analysis.

## Features

- Lists all user accounts on the device.
- Identifies whether each user account has administrator privileges.
- Displays various account properties such as:
  - Disabled status
  - Local account status
  - Password changeable status
  - Password expiration status
  - Password requirement status
- Retrieves and displays the current Windows password policy.
- Saves all retrieved information to a text file.

## Requirements

- Python 3.x
- `wmi` package

You can install the required package using pip:

```sh
pip install WMI
```

## Usage

   ```bash
     git clone https://github.com/cyberfantics/advanced_window_credential_sniffer.git
     cd advanced_window_credential_sniffer
     python advanced_user_account_info.py
  ```
- **The script will generate an output file named user_accounts_details.txt in the same directory, containing all the retrieved information.**

## Script Details

The script performs the following main tasks:
1. **Retrieve Administrator Accounts:** Identifies and lists all user accounts with administrator privileges.
2. **List User Accounts:** Gathers detailed information about each user account on the system.
3. **Display Password Policy:** Retrieves and displays the current Windows password policy.
4. **Save to File:** Writes all retrieved information to user_accounts_details.txt.

## Contributing
**Contributions are welcome! Please open an issue or submit a pull request on GitHub.**

## Contact
[cyberfantics](https://github.com/cyberfantics)
[LinkedIn](https://www.linkedin.com/in/mansoor-bukhari-77549a264/)
