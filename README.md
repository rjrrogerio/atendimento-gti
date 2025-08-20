# User Creation System for Active Directory

This is a web application written in Python using the Django framework. It is used to generate PowerShell scripts for creating and managing users in Active Directory.

## Features

- **User-friendly web interface:** Easily create, modify, and manage users through a simple web form.
- **PowerShell script generation:** Automatically generates PowerShell scripts for various Active Directory tasks, including:
    - Creating new users
    - Modifying user attributes
    - Disabling user accounts
    - Managing group memberships
- **Customizable templates:** The generated scripts can be easily customized to fit specific organizational needs.
- **Secure password handling:** Includes options for setting temporary passwords and forcing a password change on the first logon.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Navigate to the Django project directory:**
    ```bash
    cd atendimentosistema
    ```

5.  **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

### Production

For production environments, it is recommended to use a WSGI server like Gunicorn.

```bash
gunicorn --bind 0.0.0.0:8000 atendimentosistema.wsgi:application
```

## Usage

Once the application is running, open your web browser and navigate to `http://127.0.0.1:8000/`. The web interface will guide you through the process of generating PowerShell scripts for user management.

### Debug Mode

To run the application in debug mode, you need to edit the `atendimentosistema/atendimentosistema/settings.py` file and set the `DEBUG` variable to `True`.

```python
DEBUG = True
```

## PowerShell Commands

A list of PowerShell commands and their functions.

| Command | Function |
| :--- | :--- |
| **-Name** | **Full Name** |
| **-GivenName** | **First Name** |
| **-Surname** | **Last Name** |
| **-UserPrincipalName** | **User Logon Name** |
| **-SamAccountName** | **User Logon Name (pre-Windows 2000)** |
| **-DisplayName** | **Display Name** |
| **-Description**| **Description** |
| **-Office** | **Office** |
| **-Company** | **Company** |
| **-EmailAddress**| **Email** |
| **-AccountPassword** | **Password** |
| **-ChangePasswordAtLogon $true** | **Change password at next logon** |
| **-AccountExpirationDate** | **Account expiration date** |
| **-Department** | **Department** |
| **-City** | **City** |
| **-State** | **State** |
| **-Path** | **Canonical object location** |

### Add ProxyAddresses

`Set-ADUser email -add @{ProxyAddresses="smtp:email@sede.sescsp.org.br,SMTP:email@sescsp.org.br" -split ","}`

### Add Groups

`Add-ADGroupMember -Identity group_name -Members email1, email2`

### Complete Syntax Example

```powershell
New-ADUser -Name "Name Surname1 Surname2" -GivenName "Name" -Surname "Surname1 Surname2" -SamAccountName "name.surname2" -UserPrincipalName "name.surname2@sescsp.org.br" -EmailAddress "name.surname2@sescsp.org.br" -DisplayName "Name Surname1 Surname2" -Company "SESCSP" -Description "Bertioga - temporary" -Office "SESC Bertioga" -Department "Bertioga" -City "Bertioga" -State "SP" -AccountPassword (ConvertTo-SecureString -AsPlainText “978_Nss#71” -Force) -ChangePasswordAtLogon $True -Path "OU=Usuarios,OU=71-Bertioga,OU=UNIDADES,DC=sescsp,DC=local" -AccountExpirationDate "30/12/2023" -Enabled $True;
Set-ADUser name.surname2 -add @{ProxyAddresses="smtp:name.surname2@sede.sescsp.org.br,SMTP:name.surname2@sescsp.org.br" -split ","};
Add-ADGroupMember -Identity "group_name1" -Members name.surname2;
Add-ADGroupMember -Identity "group_name2" -Members name.surname2;
Add-DistributionGroupMember -Identity "Grupo Geral Unidades SescSP" -Members name.surname2;
Add-DistributionGroupMember -Identity "Grupo Geral Unidades do Interior SescSP" -Members name.surname2;
Add-ADGroupMember -Identity "LIC-A3-TEMPORARIOS_SG" -Members name.surname2;
```
