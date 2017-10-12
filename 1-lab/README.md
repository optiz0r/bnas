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

Access to the Lab is via one of the VIRL management containers. Since the hosts
are not directly reachable, connection needs to be proxied through a jump host.
This config is tested against ansible 2.4.

`./lab.hosts`
```
[core]
core1 ios=nxos ansible_host=10.255.0.1

[access]
access1 os=ios ansible_host=10.255.0.2

[all:vars]
ansible_ssh_common_args='-o ProxyCommand="ssh -i ~/.ssh/virl -W %h:%p -q guest@losdtestncore1 -p 10001"'
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

Like with the lab, access to the production network is via a jump host, since
the managed devices are not directly reachable. The only difference to the lab
environment is the `ProxyCommand` parameters.
This config is tested against ansible 2.4.

`./production.hosts`
```
#...

[all:vars]
ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -q production.jump.host"'
```
