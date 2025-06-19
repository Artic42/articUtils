# articUtils
Set of utilities design to live as executable in my $HOME/bin folder. 

## Utilities

### isGit

It returns True if the current directory is inside of a git repo. Used to determine how to colore the shell prompt for example.

### fileRamote

fileRemote is an aplication that check for a folder in a especific path and executes certain system commands. Can be used to execute very specific commands from a docker container or by a user with limited privileges.

#### config

Configuration is set on $HOME/.config/articUtils/fileRemote.yaml file.

| Parameter | Description | Default |
| --- | --- | --- |
| refreshRate | Time between checkups of the file in miliseconds | 1000 |
| monPath | Path where the command files will appear | $HOME/.fileRemote |

#### commands

List of commands builtin commands

| File | Command description |
| --- | --- |
| REBOOT | Reboots the system |
