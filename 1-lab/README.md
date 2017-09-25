# Building Network Automation Systems Lab

## Development Lab

The development lab will be used for testing configuration changes
during the BNAS course.

### Network Environment

The Lab environment is Cisco VIRL running on a VMware cluster. The lab
contain a Cisco Nexus "core" switch, and a Cisco IOS "access" switch.

### Ansible Host

The Ansible host is a Fedora 26 workstation. Code is developed using
PyCharm with additional plugins:
- YAML/Ansible support

To get a recent version of ansible, virtualenv is used with the system
copy of Python.

To setup the right environment:

```bash
cd ~/ansible/bnas
source env/bin/activate
```

Access to the Lab is via one of the VIRL management containers. A bit
of SSH config is required to allow ansible to tunnel SSH through to the
network devices.

`./ansible.cfg`
```ini
[defaults]
transport=ssh
[ssh_connection]
ssh_args = -F ./ssh_config -o ControlMaster=auto -o ControlPersist=30m
control_path = ~/.ssh/ansible-%%r@%%h:%%p
```

`./ssh_config`
```
# Lab devices sit in 10.255.0.0/16
# virl and virl.local both refer to the virl host
Host 10.255.*
  ProxyCommand ssh -W %h:%p guest@virl -i ~/.ssh/virl -p 10001

Host virl.local
  Hostname virl.local
  Port 10001
  User guest
  IdentityFile ~/.ssh/virl
  ControlMaster auto
  ControlPath ~/.ssh/ansible-%r@%h:%p
  ControlPersist 5m
```

`./inventory`
```
[core]
core1 ios=nxos ansible_host=10.255.0.1

[access]
access1 os=ios ansible_host=10.255.0.2

[all:vars]
ansible_ssh_user=cisco
ansible_ssh_pass=******
```

## Production

Production hosts will be used for any read-only activities in the BNAS
course to allow fetching real world data.

### Network Environment

The production network is a mixed-vendor network with a range of devices
including:

- Cisco ASA
- Cisco IOS
- Cisco Nexus
- Arista EOS
- VMware

Access to production devices is managed by TACACS+. There is a user
account for ansible to access all devices, and a policy which permits
it to run only show-commands, and commands for basic functionality
such as enable, disabling the pager etc.

Credentials for the ansible account is stored in ansible vault. The
vault passphrase is stored on disk in a GPG-encrypted file which can be
decrypted only by network operators. This setup was adapted from
Vallard Benincosa's setup described here:
[Secrets with Ansible: Ansible Vault and GPG](https://benincosa.com/?p=3235)

### Ansible Host

Ansible is running on a bastion host able to connect to all devices in
the network. The host is running CentOS 6 and so to get recent versions,
a copy of Python from the SCL is being used, with ansible installed from
pypi in a virtualenv.

To setup the right environment for using ansible:

```bash
cd ~/ansible/netops
source /opt/rh/python27/enable
source env/bin/activate
```
