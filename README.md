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
| UPDATE | Update config from reading file |

#### docker

List of commands builtin docker module

| File | Command description |
| --- | --- |
| UP_DOCKER_CONTAINER| Put up a docker container with docker compose |
| DOWN_DOCKER_CONTAINER | Put down a docker container with coker compose |
| CREATE_DOCKER_CONTAINER | Create a docker image using the file as a dockerfile |
| REMOVE_DOCKER_CONTAINER | Remove a docker image from the system |

### systemStatus

This application will save a series of status variables on a yaml file to be read by other software. There will be a option to point to a MongoDB database where the info will be stored. Two refresh rate can be configured for slow and fast data.

#### config

Configuration is set on $HOME/.config/articUtils/systemStatus.yaml file.

| Parameter | Description | Default |
| --- | --- | --- |
| refreshRateFast | Time between checkups of the file in miliseconds | 10 |
| refreshRateSlow | Time between checkups of the file in miliseconds | 1000 |
| reportPath | Path where the command files will appear | $HOME/.fileRemote |
| alertsEnable | Enable the alert system using ntfy | False |
| ntfyServer | Path to the ntfy server for the alerts | NoServer |

#### Slow data 
- System docker images
- Running containers and status
- Disk drive usage

#### Fast data
- RAM usages
- CPU usage
- Temperature

#### Alert system
This module will allow to create HH, HL, LH, and LL limits for any value on the data. And send a ntfy notification if needed.
Also it creates alert if containers stop for some reason.
