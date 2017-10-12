# Building Network Automation Systems - Compliance Reporting

## Problem

A number of existing switches in the network don't have consistent config
with regards to SNMP, Syslog etc. A report showing which devices don't match
the baseline will help us correct the errors and have a consistent network.

## Report format

Produce a list of issues for each device in the format `hostname: issue description`
When everything is good, the report will be empty.

```
tstncore1: 10.0.0.1 is not configured as Syslog host
tstnaccess1: 10.0.0.100 is not configured as SNMP trap host
```

## Playbook

This playbook is split so that each check (syslog, snmp etc) is a separate task file.
When the report is run, each task is run in sequence. For each task, there is a
default version, but this can be overridden per switch platform in case there are
differences in the way we need to retrieve or process the information.

The report is constructed using a jinja2 template.

The required configuration is described by variables. The defaults are located in
`group_vars/all.yml`, and they can be overridden in case different switches need
non-standard configurations.

## Usage

For the lab environment:

```
ansible-playbook check.yml
less outputs/compliance/report.txt
```

For a production environment:

```
ansible-playbook -i ~/ansible/production/inventory --vault-password-file ~/ansible/production/scripts/openvault.sh
less outputs/compliance/report.txt
```

## Checks

### Syslog

Checks that switches have exactly the correct set of syslog servers configured.
The required list of servers is defined by the `syslog_servers` variable, which
takes a list of IP addresses

```
syslog_servers:
  - 10.0.0.1
```

### SNMP Traps

Checks that switches have exactly the correct set of syslog trap hosts configured.
The required list of servers is defined by the `snmp_servers` variable, which takes
a list of IP addresses

```
snmp_servers:
  - 10.0.0.100
  - 10.0.0.200
```

