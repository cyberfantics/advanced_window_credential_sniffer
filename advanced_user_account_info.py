# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 19:07:15 2024

@author: Mansoor
"""

import os
import wmi

# Initialize WMI connection
w = wmi.WMI()

# Function to get list of Administrator accounts
def get_administrator_accounts():
    admins = []
    for group in w.Win32_Group():
        if group.Name == "Administrators":
            admins = [a.Name for a in group.associators(wmi_result_class="Win32_UserAccount")]
    return admins

# Function to print user account details and save to file
def print_user_account_details(user, admins, output_file):
    output_file.write(f"Username: {user.Name}\n")
    output_file.write(f"Administrator: {'Yes' if user.Name in admins else 'No'}\n")
    output_file.write(f"Disabled: {user.Disabled}\n")
    output_file.write(f"Local Account: {user.LocalAccount}\n")
    output_file.write(f"Password Changeable: {user.PasswordChangeable}\n")
    output_file.write(f"Password Expires: {user.PasswordExpires}\n")
    output_file.write(f"Password Required: {user.PasswordRequired}\n")
    output_file.write("\n")

# Function to print Windows password policy and save to file
def print_password_policy(output_file):
    output_file.write("Password Policy:\n")
    output_file.flush()  # Ensure previous writes are flushed before executing external command
    os.system("net accounts >> output.txt")  # Append output to file

# Main function to list user accounts and details
def list_user_accounts(output_file_path):
    admins = get_administrator_accounts()
    with open(output_file_path, 'w') as output_file:
        for user in w.Win32_UserAccount():
            print_user_account_details(user, admins, output_file)
        print_password_policy(output_file)

if __name__ == "__main__":
    output_file_path = "user_accounts_details.txt"
    list_user_accounts(output_file_path)
    print(f"User account details saved to: {output_file_path}")
