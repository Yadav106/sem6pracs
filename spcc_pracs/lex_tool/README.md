If you are using kali, install lex/flex tool using

```
sudo apt install flex
```

then compiler the main.l file using

```
lex main.l
```

a lex.yy.c file will be generated, compile it using gcc or cc

```
cc lex.yy.c -o main -ll
```

then run the main file using

```
./main
```



then enter any code in input like

```
#include<stdio.h>
```

which'll fetch the output as
```
# - Symbol
include - Identifier
< - Symbol
stdio - Identifier
. - Symbol
h - Identifier
> - Symbol
```
