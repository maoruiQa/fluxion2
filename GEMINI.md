# Project Overview

This project, Fluxion, is a security auditing and social-engineering research tool for WPA/WPA2 attacks. It is a shell script-based tool that provides a menu-driven interface for launching various attacks. The main script is `fluxion.sh`, which handles the user interaction and launches the selected attacks.

The project is structured with different attack vectors in the `attacks` directory. The two main attacks are:

*   **Captive Portal:** This attack creates a fake access point (rogue AP) and a captive portal to phish for WPA/WPA2 passwords. It uses a combination of tools like `hostapd` or `airbase-ng` to create the fake AP, `dnsspoof` for DNS redirection, and a web server to host the captive portal.
*   **Handshake Snooper:** This attack is used to capture WPA/WPA2 handshakes. It uses tools like `airodump-ng` to monitor the network and `aireplay-ng` or `mdk4` to deauthenticate clients, forcing them to re-authenticate and reveal the handshake.

The project also includes a library of shell scripts in the `lib` directory that provide various utility functions for network interface management, process control, and user interaction.

# Building and Running

Fluxion is a script-based tool and does not require compilation.

**To run the tool:**

1.  Make sure you have all the required dependencies installed. The script will attempt to install them automatically.
2.  Run the main script as root:

    ```bash
    ./fluxion.sh
    ```

**Dependencies:**

The script checks for the following dependencies:

*   aircrack-ng
*   bc
*   awk
*   curl
*   cowpatty
*   dhcpd
*   7zr
*   hostapd
*   lighttpd
*   iwconfig
*   macchanger
*   mdk4
*   dsniff
*   mdk3
*   nmap
*   openssl
*   php-cgi
*   xterm
*   rfkill
*   unzip
*   route
*   fuser
*   killall

# Development Conventions

*   The project is primarily written in `bash`.
*   The code is organized into modules, with each attack having its own directory containing the attack script and language files.
*   The `lib` directory contains shared utility scripts.
*   The `language` directory contains language files for internationalization.
*   The project uses `getopt` for command-line argument parsing.
*   The scripts use a consistent naming convention for variables and functions.
*   The project has a `CONTRIBUTING.md` file with guidelines for contributors.
