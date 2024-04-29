first we'll have to open a port on the computer we wanna attack
we can do that by running

```
python3 -m http.server {port number}
```

port number can be any port number you want
we are using 80 here(check the code, line 9)

then from the attacker system, run this file by providing 2 arguments, ip address, and any path(for ease, just use `\\`, but you can use any existing path on the target's system)

```
python3 dos.py 192.168.0.10 \\
```
