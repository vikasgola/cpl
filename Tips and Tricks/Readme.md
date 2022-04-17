# General

## Common built-in Linux tools:

*   chmod +x <filename>

  Makes a file runnable - chmod changes permissions of a file.

*    ./<filename>

    Run a file.

*    file <filename>

    View file type and information.

*    strings <filename>

    Print all printable strings in a file.

*    nc <host> <port>

    Use netcat to connect to a remote host. This is very common in the pwn category and other remote challenges.

*    xxd <filename>

    View the hex dump of a file using xxd.

*    base64 -d <filename>

    Decode a Base64-encoded file.

## Web

*    Browser developer tools

    Found in most browsers by pressing [F12].
    Here you can view the network traffic, cookies, page source code and more.

*    robots.txt

    Most web pages has this file, located at www.example.com/robots.txt. This is to prevent web crawlers from traversing certain places of a web page.
    Hidden paths and information may be found here.

# Binary

* Some common disassembly and debugging tools:

    gdb

    The Gnu debugger, built into most Linux systems.

    OllyDbg

    IDA Pro

    radare2

    ghidra

## Scripting

Sometimes you have to write short scripts to solve certain challenges.
We recommend using your favourite language.

* Common languages include:

    Python

    C/C++

    bash

    perl

    ruby

    PHP

It is strongly recommended to learn how to script over a TCP connection.