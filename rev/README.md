# Rev

## Complilation Instructions

All the binaries are compiled considering 32( add -m32 tag to instruct compiler to compile using 32 bit libraries) bit machines. By default gcc compiler adds stack protector to prevent stack smashing.

To Disable Canary:
	`gcc vuln.c -o vuln_disable_canary -fno-stack-protector`
To Disable DEP:
	`gcc vuln.c -o vuln_disable_dep -z execstack`
To Disable PIE(Position Independent Execution):
	`gcc vuln.c -o vuln_disable_pie -no-pie`
To Disable all protection Mechanisms:
	`gcc vuln.c -o vuln_disable_all -fno-stack-protector -z execstack -no-pie`

## Scenario Descriptions

**Scenario 1**: During an CPL Cricket Match is going on, generally speaking outsiders(i.e people other than team players and their staff)
are not allowed to enter the Playing ground while the game is still going on but sometimes some hardcore fans forcefully enter 
the playing ground while the match is still going on. In similar fashion, there is a Outsider present in this challenge and 
he has a special power. Can you find that special power and use it to your advantage?

WriteUp: An environment variable with the name `OUTSIDER` is being imported and copied onto a variable without a limit on the
length of the content inside the env variable. This can be used as an buffer Overflow exploit to modify the variable `to_be_modded` to desired value.

Exploit code used present in `exploit.sh` file. 
