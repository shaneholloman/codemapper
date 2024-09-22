# shaneholloman.iptables

This markdown document provides a comprehensive overview of the directory structure and file contents. It aims to give viewers (human or AI) a complete view of the codebase in a single file for easy analysis.

## Document Table of Contents

The table of contents below is for navigational convenience and reflects this document's structure, not the actual file structure of the repository.

<!-- TOC -->

- [shaneholloman.iptables](#shaneholloman.iptables)
  - [Document Table of Contents](#document-table-of-contents)
  - [Repo File Tree](#repo-file-tree)
  - [Repo File Contents](#repo-file-contents)
    - [README.md](#readmemd)
    - [.gitignore](#gitignore)
    - [.ansible-lint](#ansible-lint)
    - [.editorconfig](#editorconfig)
    - [.gitattributes](#gitattributes)
    - [.github\FUNDING.yml](#github\fundingyml)
    - [.github\workflows\ci.yml](#github\workflows\ciyml)
    - [.github\workflows\release.yml](#github\workflows\releaseyml)
    - [.github\workflows\remove.yml](#github\workflows\removeyml)
    - [.github\workflows\stale.yml](#github\workflows\staleyml)
    - [.vscode\settings.json](#vscode\settingsjson)
    - [.yamllint](#yamllint)
    - [ansible-role-iptables.code-workspace](#ansible-role-iptablescode-workspace)
    - [defaults\main.yml](#defaults\mainyml)
    - [handlers\main.yml](#handlers\mainyml)
    - [kickstart.sh](#kickstartsh)
    - [LICENSE](#license)
    - [meta\.galaxy_install_info](#meta\galaxy_install_info)
    - [meta\main.yml](#meta\mainyml)
    - [molecule\default\cleanup.yml](#molecule\default\cleanupyml)
    - [molecule\default\converge.yml](#molecule\default\convergeyml)
    - [molecule\default\molecule.yml](#molecule\default\moleculeyml)
    - [molecule\default\prepare.yml](#molecule\default\prepareyml)
    - [molecule\default\side_effect.yml](#molecule\default\side_effectyml)
    - [molecule\default\verify.yml](#molecule\default\verifyyml)
    - [tasks\disable-other-firewalls.yml](#tasks\disable-other-firewallsyml)
    - [tasks\main.yml](#tasks\mainyml)
    - [templates\firewall.bash.j2](#templates\firewallbashj2)
    - [templates\firewall.init.j2](#templates\firewallinitj2)
    - [templates\firewall.unit.j2](#templates\firewallunitj2)
    - [tests\inventory](#tests\inventory)
    - [tests\test.yml](#tests\testyml)
    - [vars\main.yml](#vars\mainyml)

<!-- /TOC -->

## Repo File Tree

This file tree represents the actual structure of the repository. It's crucial for understanding the organization of the codebase.

```tree
.
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── release.yml
│   │   ├── remove.yml
│   │   └── stale.yml
│   └── FUNDING.yml
├── .vscode/
│   └── settings.json
├── defaults/
│   └── main.yml
├── handlers/
│   └── main.yml
├── meta/
│   ├── .galaxy_install_info
│   └── main.yml
├── molecule/
│   └── default/
│       ├── cleanup.yml
│       ├── converge.yml
│       ├── molecule.yml
│       ├── prepare.yml
│       ├── side_effect.yml
│       └── verify.yml
├── tasks/
│   ├── disable-other-firewalls.yml
│   └── main.yml
├── templates/
│   ├── firewall.bash.j2
│   ├── firewall.init.j2
│   └── firewall.unit.j2
├── tests/
│   ├── inventory
│   └── test.yml
├── vars/
│   └── main.yml
├── .ansible-lint
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .yamllint
├── LICENSE
├── README.md
├── ansible-role-iptables.code-workspace
└── kickstart.sh

12 directories, 33 files
```

## Repo File Contents

The following sections present the content of each file in the repository.

### .ansible-lint

```txt
skip_list:
  - 'yaml'
  - 'role-name'
```

### .editorconfig

```txt
# .editorconfig
root = true

[*]
end_of_line = lf
```

### .gitattributes

```txt
* text=auto eol=lf
```

### .gitignore

```ini
*.retry
*/__pycache__
*.pyc
.cache
*.cfg
```

### .yamllint

```txt
---
extends: default

rules:
  line-length:
    max: 120
    level: warning

ignore: |
  .github/workflows/stale.yml
```

### ansible-role-iptables.code-workspace

```txt
{
	"folders": [
		{
			"path": "."
		}
	],
	"settings": {
		"ansible.python.interpreterPath": "/bin/python3"
	}
}
```

### kickstart.sh

```bash
#!/bin/bash

# Define the GitHub account or organization name
githubAccount="shaneholloman"  # Change this to your personal account name if needed

# Initialize a new git repository
git init -b main

# Get the name of the current repository from the top-level directory
repoName=$(basename "$(git rev-parse --show-toplevel)")

# Create a new repository on GitHub using the gh CLI
gh repo create "$repoName" --public -y

# Add the remote repository
git remote add origin https://github.com/$githubAccount/"$repoName".git

# Add all files in the current directory to the git repository
git add .

# Commit the changes
git commit -m "Initial commit"

# Push the changes to GitHub
git push -u origin main

# Define an associative array where the key is the name of the secret and the value is the secret value
declare -A secrets
secrets=(
  ["DOCKERHUB_TOKEN"]="$DOCKERHUB_TOKEN"
  ["DOCKERHUB_USERNAME"]="$DOCKERHUB_USERNAME"
  ["GALAXY_API_KEY"]="$GALAXY_API_KEY"
  # Add more secrets here as needed
)

# Check if environment variables exist
missingVars=()
for key in "${!secrets[@]}"
do
  if [ -z "${secrets[$key]}" ]; then
    missingVars+=("$key")
  fi
done

if [ ${#missingVars[@]} -ne 0 ]; then
  echo ""
  echo ""
  echo "The following environment variables are missing:"
  for var in "${missingVars[@]}"
  do
    echo "$var"
  done
  echo "Please add them to your .bashrc file and run 'source ~/.bashrc'"
  exit 1
fi

# Loop through each secret to set it for the current repository
for key in "${!secrets[@]}"
do
  value=${secrets[$key]}
  command="echo -n $value | gh secret set $key --repo=$githubAccount/$repoName"
  eval "$command"
done

# Tag and push after setting the secrets
commitMessage="tagging first version"
tagVersion="2.0.0"
tagMessage="An Ansible role for iptables"

git commit --allow-empty -m "$commitMessage"
git tag -a $tagVersion -m "$tagMessage"

# Ask the user if the current git tag and message are correct
echo ""
echo ""
echo "The current git tag is $tagVersion with the message '$tagMessage'. Is this correct? (yes/no)"
read -r answer

if [ "$answer" != "${answer#[Yy]}" ] ;then
  git push origin $tagVersion
else
  echo "Please edit the git tag and message in this script."
fi
```

### LICENSE

```txt
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
```

### README.md

````markdown
# Ansible Role: `iptables`

[![CI](https://github.com/shaneholloman/ansible-role-iptables/actions/workflows/ci.yml/badge.svg)](https://github.com/shaneholloman/ansible-role-iptables/actions/workflows/ci.yml) [![Release](https://github.com/shaneholloman/ansible-role-iptables/actions/workflows/release.yml/badge.svg)](https://github.com/shaneholloman/ansible-role-iptables/actions/workflows/release.yml)

Installs an iptables-based firewall for Linux.
Supports both IPv4 (`iptables`) and IPv6 (`ip6tables`).

This firewall aims for simplicity over complexity, and only opens a few specific ports for incoming traffic (configurable through Ansible variables). If you have a rudimentary knowledge of `iptables` and/or firewalls in general, this role should be a good starting point for a secure system firewall.

After the role is run, a `firewall` init service will be available on the server.
You can use `service firewall [start|stop|restart|status]` to control the firewall.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yml
iptables_state: started
iptables_enabled_at_boot: true
```

Controls the state of the firewall service; whether it should be running (`iptables_state`) and/or enabled on system boot (`iptables_enabled_at_boot`).

```yml
iptables_flush_rules_and_chains: true
```

Whether to flush all rules and chains whenever the firewall is restarted. Set this to `false` if there are other processes managing iptables (e.g. Docker).

```yml
iptables_allowed_tcp_ports:
  - "22"
  - "80"
  ...
iptables_allowed_udp_ports: []
```

A list of TCP or UDP ports (respectively) to open to incoming traffic.

```yml
iptables_forwarded_tcp_ports:
  - { src: "22", dest: "2222" }
  - { src: "80", dest: "8080" }
iptables_forwarded_udp_ports: []
```

Forward `src` port to `dest` port, either TCP or UDP (respectively).

```yml
iptables_additional_rules: []
iptables_ip6_additional_rules: []
```

Any additional (custom) rules to be added to the firewall (in the same format you would add them via command line, e.g. `iptables [rule]`/`ip6tables [rule]`).

A couple of examples of how this could be used:

```yml
# Allow only the IP 167.89.89.18 to access port 4949 (Munin).
iptables_additional_rules:
  - "iptables -A INPUT -p tcp --dport 4949 -s 167.89.89.18 -j ACCEPT"
```

```yml
# Allow only the IP 214.192.48.21 to access port 3306 (MySQL).
iptables_additional_rules:
  - "iptables -A INPUT -p tcp --dport 3306 -s 214.192.48.21 -j ACCEPT"
```

See [Iptables Essentials: Common Firewall Rules and Commands](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands) for more examples.

```yml
iptables_log_dropped_packets: true
```

Whether to log dropped packets to syslog (messages will be prefixed with "Dropped by firewall: ").

```yml
iptables_disable_firewalld: false
iptables_disable_ufw: false
```

Set to `true` to disable firewalld (installed by default on RHEL/CentOS) or ufw (installed by default on Ubuntu), respectively.

```yml
iptables_enable_ipv6: true
```

Set to `false` to disable configuration of ip6tables (for example, if your `GRUB_CMDLINE_LINUX` contains `ipv6.disable=1`).

## Dependencies

None.

## Example Playbook

```yml
- hosts: server
  vars_files:
    - vars/main.yml
  roles:
    - { role: shaneholloman.iptables }
```

*Inside `vars/main.yml`*:

```yml
iptables_allowed_tcp_ports:
  - "22"
  - "25"
  - "80"
```

TODO:

  - [ ] Make outgoing ports more configurable.
  - [ ] Make other firewall features (like logging) configurable.

## License

Unlicense

## Author Information

Shane Holloman 2023
````

### .github\FUNDING.yml

```yml
# These are supported funding model platforms
---
github: shaneholloman
patreon: none
```

### .github\workflows\ci.yml

```yml
---
name: CI
"on":
  pull_request:
  push:
    branches:
      - main
  schedule:
    - cron: "0 1 * * 1"

defaults:
  run:
    working-directory: "shaneholloman.iptables"

jobs:
  lint:
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - name: Check out the codebase.
        uses: actions/checkout@v4
        with:
          path: "shaneholloman.iptables"

      - name: Set up Python 3.
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      - name: Install test dependencies.
        run: pip3 install yamllint

      - name: Lint code.
        run: |
          yamllint .

  molecule:
    name: Molecule
    runs-on: ubuntu-latest
    strategy:
      matrix:
        distro:
          - rockylinux9
          - ubuntu2204
          - debian12

    steps:
      - name: Check out the codebase.
        uses: actions/checkout@v4
        with:
          path: "shaneholloman.iptables"

      - name: Set up Python 3.
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      - name: Install test dependencies.
        run: pip3 install ansible molecule molecule-plugins[docker] docker

      - name: Upgrade Molecule and Docker Driver
        run: |
          pip install --upgrade molecule
          pip install --upgrade molecule-docker

      - name: Run Molecule tests.
        run: molecule test
        env:
          PY_COLORS: "1"
          ANSIBLE_FORCE_COLOR: "1"
          MOLECULE_DISTRO: ${{ matrix.distro }}
```

### .github\workflows\release.yml

```yml
---
# This workflow requires a GALAXY_API_KEY secret present in the GitHub
# repository or organization.
# See: https://github.com/marketplace/actions/publish-ansible-role-to-galaxy
# See: https://github.com/ansible/galaxy/issues/46

name: Release
'on':
  push:
    tags:
      - '*'
  workflow_dispatch:

defaults:
  run:
    working-directory: 'shaneholloman.iptables'

jobs:

  release:
    name: Release
    runs-on: ubuntu-latest
    steps:
      - name: Check out the codebase.
        uses: actions/checkout@v4
        with:
          path: 'shaneholloman.iptables'

      - name: Set up Python 3.
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install Ansible.
        run: pip3 install ansible-core

      - name: Trigger a new import on Galaxy.
        run: >-
          ansible-galaxy role import --api-key ${{ secrets.GALAXY_API_KEY }}
          $(echo ${{ github.repository }} | cut -d/ -f1)
          $(echo ${{ github.repository }} | cut -d/ -f2)
```

### .github\workflows\remove.yml

```yml
---
# Delete Repo from Ansible Galaxy
name: Remove
'on':
  workflow_dispatch:

defaults:
  run:
    working-directory: 'shaneholloman.iptables'

jobs:

  release:
    name: Remove from Galaxy
    runs-on: ubuntu-latest
    steps:
      - name: Check out the codebase.
        uses: actions/checkout@v4
        with:
          path: 'shaneholloman.iptables'

      - name: Set up Python 3.
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install Ansible.
        run: pip3 install ansible-core

      - name: Trigger a removal from Galaxy.
        run: >-
          ansible-galaxy role delete --api-key ${{ secrets.GALAXY_API_KEY }}
          $(echo ${{ github.repository }} | cut -d/ -f1)
          $(echo ${{ github.repository }} | cut -d/ -f2)
```

### .github\workflows\stale.yml

```yml
---
name: Close inactive issues
'on':
  schedule:
    - cron: "55 4 * * 0"  # semi-random time

jobs:
  close-issues:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write
    steps:
      - uses: actions/stale@v8
        with:
          days-before-stale: 120
          days-before-close: 60
          exempt-issue-labels: bug,pinned,security,planned
          exempt-pr-labels: bug,pinned,security,planned
          stale-issue-label: "stale"
          stale-pr-label: "stale"
          stale-issue-message: |
            This issue has been marked 'stale' for lack of recent activity.<br>
            If there's no further activity:<br>
            Issue closes in 30 days.<br>
            Thank you for your contribution!
          close-issue-message: |
            This issue has been closed for inactivity.<br>
            If you feel this is in error:<br>
            Please reopen issue or file new issue with relevant details.
          stale-pr-message: |
            This pr has been marked 'stale' for lack of recent activity.<br>
            If there is no further activity:<br>
            Issue closes in 30 days.<br>
            Thank you for your contribution!
          close-pr-message: |
            This PR has been closed for inactivity.<br>
            If you feel this is in error:<br>
            Please reopen issue or file new issue with relevant details.
          repo-token: ${{ secrets.GITHUB_TOKEN }}
```

### .vscode\settings.json

```json
{
    "ansible.python.interpreterPath": "c:\\Python310\\python.exe"
}
```

### defaults\main.yml

```yml
---
iptables_state: started
iptables_enabled_at_boot: true

iptables_flush_rules_and_chains: true

iptables_allowed_tcp_ports:
  - "22"
  - "25"
  - "80"
  - "443"
iptables_allowed_udp_ports: []
iptables_forwarded_tcp_ports: []
iptables_forwarded_udp_ports: []
iptables_additional_rules: []
iptables_enable_ipv6: true
iptables_ip6_additional_rules: []
iptables_log_dropped_packets: true

# Set to true to ensure other firewall management software is disabled.
iptables_disable_firewalld: false
iptables_disable_ufw: false
```

### handlers\main.yml

```yml
---
- name: Restart firewall
  ansible.builtin.service:
    name: firewall
    state: restarted
```

### meta\.galaxy_install_info

```txt
install_date: Thu 25 Jan 2024 01:46:48
version: 2.2.0
```

### meta\main.yml

```yml
---
galaxy_info:
  role_name: iptables
  author: shaneholloman
  description: Simple iptables firewall for most Unix-like systems.
  company: "shaneholloman"
  license: "license (Unlicense)"
  min_ansible_version: "2.12"

  platforms:
    - name: Debian
      versions:
        - all
    - name: Ubuntu
      versions:
        - all

  galaxy_tags:
    - networking
    - system
    - security
    - firewall
    - iptables
    - tcp

dependencies: []
```

### molecule\default\cleanup.yml

```yml
---
- name: Cleanup
  hosts: all
  gather_facts: false
  tasks: []
```

### molecule\default\converge.yml

```yml
---
# This will hold the build and we can `molecule login` to the docker image
- name: Converge
  hosts: all
  become: true

  vars:
    # Added to prevent test failures in CI.
    iptables_enable_ipv6: false

    # Added for a test.
    iptables_allowed_tcp_ports:
      - "9123"

  pre_tasks:
    - name: Update apt cache.
      ansible.builtin.apt:
        update_cache: true
        cache_valid_time: 1200
      when: ansible_os_family == 'Debian'
      changed_when: false

  roles:
    - role: shaneholloman.iptables
```

### molecule\default\molecule.yml

```yml
---
role_name_check: 1
dependency:
  name: galaxy
driver:
  name: docker
platforms:
  - name: instance
    image: "shaneholloman/docker-${MOLECULE_DISTRO:-rockylinux9}-ansible:latest"
    command: ${MOLECULE_DOCKER_COMMAND:-""}
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    cgroupns_mode: host
    privileged: true
    pre_build_image: true
provisioner:
  name: ansible
  playbooks:
    converge: ${MOLECULE_PLAYBOOK:-converge.yml}
scenario:
  test_sequence:
    - destroy
    - dependency
    - syntax
    - create
    - prepare
    - converge
    - idempotence
    - check
    - side_effect
    - verify
    - destroy
```

### molecule\default\prepare.yml

```yml
---
- name: Prepare
  hosts: all
  gather_facts: false
  tasks: []
```

### molecule\default\side_effect.yml

```yml
---
- name: Side Effect
  hosts: all
  gather_facts: false
  tasks: []
```

### molecule\default\verify.yml

```yml
---
- name: Verify
  hosts: all
  gather_facts: false
  tasks: []
```

### tasks\disable-other-firewalls.yml

```yml
---
- name: Gather package facts (on RHEL).
  ansible.builtin.package_facts:
    manager: auto
  when: ansible_os_family == "RedHat"

- name: Check if firewalld package is installed (on RHEL).
  ansible.builtin.set_fact:
    firewalld_installed: "'firewalld' in ansible_facts.packages"
  when:
    - ansible_os_family == "RedHat"
    - iptables_disable_firewalld

- name: Disable the firewalld service (on RHEL, if configured).
  ansible.builtin.service:
    name: firewalld
    state: stopped
    enabled: false
  when:
    - ansible_os_family == "RedHat"
    - iptables_disable_firewalld
    - firewalld_installed.rc == 0

- name: Gather facts about all services (on Ubuntu).
  ansible.builtin.service_facts:
  when: ansible_distribution == "Ubuntu"

- name: Check if ufw service is running (on Ubuntu).
  ansible.builtin.set_fact:
    ufw_service_running: "'ufw' in ansible_facts.services and ansible_facts.services['ufw'].state == 'running'"
  when:
    - ansible_distribution == "Ubuntu"
    - iptables_disable_ufw

- name: Disable the ufw firewall (on Ubuntu, if configured).
  ansible.builtin.service:
    name: ufw
    state: stopped
    enabled: false
  when:
    - ansible_distribution == "Ubuntu"
    - iptables_disable_ufw
    - ufw_installed.rc == 0

- name: Check if ufw package is installed (on ArchLinux).
  ansible.builtin.command: pacman -Q ufw
  register: ufw_installed
  ignore_errors: true
  changed_when: false
  when:
    - ansible_distribution == "ArchLinux"
    - iptables_disable_ufw
  check_mode: false

- name: Disable the ufw firewall (on ArchLinux, if configured).
  ansible.builtin.service:
    name: ufw
    state: stopped
    enabled: false
  when:
    - ansible_distribution == "ArchLinux"
    - iptables_disable_ufw
    - ufw_installed.rc == 0
```

### tasks\main.yml

```yml
---
- name: Ensure iptables is present.
  ansible.builtin.package:
    name: iptables
    state: present

- name: Flush iptables the first time playbook runs.
  ansible.builtin.command: >
    iptables -F
    creates=/etc/firewall.bash

- name: Copy firewall script into place.
  ansible.builtin.template:
    src: firewall.bash.j2
    dest: /etc/firewall.bash
    owner: root
    group: root
    mode: 0744
  notify: Restart firewall

- name: Copy firewall init script into place.
  ansible.builtin.template:
    src: firewall.init.j2
    dest: /etc/init.d/firewall
    owner: root
    group: root
    mode: 0755
  when: "ansible_service_mgr != 'systemd'"

- name: Copy firewall systemd unit file into place (for systemd systems).
  ansible.builtin.template:
    src: firewall.unit.j2
    dest: /etc/systemd/system/firewall.service
    owner: root
    group: root
    mode: 0644
  when: "ansible_service_mgr == 'systemd'"

- name: Configure the firewall service.
  ansible.builtin.service:
    name: firewall
    state: "{{ iptables_state }}"
    enabled: "{{ iptables_enabled_at_boot }}"

- name: Disable other firewalls if necessary
  ansible.builtin.import_tasks: disable-other-firewalls.yml
  when: iptables_disable_firewalld or iptables_disable_ufw
```

### templates\firewall.bash.j2

```jinja2
#!/bin/bash
# iptables firewall.
#
# This file should be located at /etc/firewall.bash, and is meant to work with
# the `shaneholloman.iptables` Ansible role.
#
# Common port reference:
#   22: SSH
#   25: SMTP
#   80: HTTP
#   123: NTP
#   443: HTTPS
#   2222: SSH alternate
#   8080: HTTP alternate
#
# @author Shane Holloman

# No spoofing.
if [ -e /proc/sys/net/ipv4/conf/all/rp_filter ]
then
for filter in /proc/sys/net/ipv4/conf/*/rp_filter
do
echo 1 > $filter
done
fi

# Set the default rules.
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

{% if iptables_flush_rules_and_chains %}
# Remove all rules and chains.
iptables -t nat -F
iptables -t mangle -F
iptables -F
iptables -X
{% endif %}

# Accept traffic from loopback interface (localhost).
iptables -A INPUT -i lo -j ACCEPT

# Forwarded ports.
{# Add a rule for each forwarded port #}
{% for forwarded_port in iptables_forwarded_tcp_ports %}
iptables -t nat -I PREROUTING -p tcp --dport {{ forwarded_port.src }} -j REDIRECT --to-port {{ forwarded_port.dest }}
iptables -t nat -I OUTPUT -p tcp -o lo --dport {{ forwarded_port.src }} -j REDIRECT --to-port {{ forwarded_port.dest }}
{% endfor %}
{% for forwarded_port in iptables_forwarded_udp_ports %}
iptables -t nat -I PREROUTING -p udp --dport {{ forwarded_port.src }} -j REDIRECT --to-port {{ forwarded_port.dest }}
iptables -t nat -I OUTPUT -p udp -o lo --dport {{ forwarded_port.src }} -j REDIRECT --to-port {{ forwarded_port.dest }}
{% endfor %}

# Open ports.
{# Add a rule for each open port #}
{% for port in iptables_allowed_tcp_ports %}
iptables -A INPUT -p tcp -m tcp --dport {{ port }} -j ACCEPT
{% endfor %}
{% for port in iptables_allowed_udp_ports %}
iptables -A INPUT -p udp -m udp --dport {{ port }} -j ACCEPT
{% endfor %}

# Accept icmp ping requests.
iptables -A INPUT -p icmp -j ACCEPT

# Allow NTP traffic for time synchronization.
iptables -A OUTPUT -p udp --dport 123 -j ACCEPT
iptables -A INPUT -p udp --sport 123 -j ACCEPT

# Additional custom rules.
{% for rule in iptables_additional_rules %}
{{ rule }}
{% endfor %}

# Allow established connections:
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Log EVERYTHING (ONLY for Debug).
# iptables -A INPUT -j LOG

{% if iptables_log_dropped_packets %}
# Log other incoming requests (all of which are dropped) at 15/minute max.
iptables -A INPUT -m limit --limit 15/minute -j LOG --log-level 7 --log-prefix "Dropped by firewall: "
{% endif %}

# Drop all other traffic.
iptables -A INPUT -j DROP

{% if iptables_enable_ipv6 %}
# Configure IPv6 if ip6tables is present.
if [ -x "$(which ip6tables 2>/dev/null)" ]; then

{% if iptables_flush_rules_and_chains %}
  # Remove all rules and chains.
  ip6tables -F
  ip6tables -X
{% endif %}

  # Accept traffic from loopback interface (localhost).
  ip6tables -A INPUT -i lo -j ACCEPT

  # Open ports.
{# Add a rule for each open port #}
{% for port in iptables_allowed_tcp_ports %}
  ip6tables -A INPUT -p tcp -m tcp --dport {{ port }} -j ACCEPT
{% endfor %}
{% for port in iptables_allowed_udp_ports %}
  ip6tables -A INPUT -p udp -m udp --dport {{ port }} -j ACCEPT
{% endfor %}

  # Accept icmp ping requests.
  ip6tables -A INPUT -p icmpv6 -j ACCEPT

  # Allow NTP traffic for time synchronization.
  ip6tables -A OUTPUT -p udp --dport 123 -j ACCEPT
  ip6tables -A INPUT -p udp --sport 123 -j ACCEPT

  # Additional custom rules.
{% for rule in iptables_ip6_additional_rules %}
  {{ rule }}
{% endfor %}

  # Allow established connections:
  ip6tables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

  # Log EVERYTHING (ONLY for Debug).
  # ip6tables -A INPUT -j LOG

{% if iptables_log_dropped_packets %}
  # Log other incoming requests (all of which are dropped) at 15/minute max.
  ip6tables -A INPUT -m limit --limit 15/minute -j LOG --log-level 7 --log-prefix "Dropped by firewall: "
{% endif %}

  # Drop all other traffic.
  ip6tables -A INPUT -j DROP

fi
{% endif %}
```

### templates\firewall.init.j2

```jinja2
#! /bin/sh
# /etc/init.d/firewall
#
# Firewall init script, to be used with /etc/firewall.bash by Shane Holloman.
#
# @author Shane Holloman

### BEGIN INIT INFO
# Provides:          firewall
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start firewall at boot time.
# Description:       Enable the firewall.
### END INIT INFO

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting firewall."
    /etc/firewall.bash
    ;;
  stop)
    echo "Stopping firewall."
    iptables -F
    if [ -x "$(which ip6tables 2>/dev/null)" ]; then
        ip6tables -F
    fi
    ;;
  restart)
    echo "Restarting firewall."
    /etc/firewall.bash
    ;;
  status)
    echo -e "`iptables -L -n`"
    EXIT=4 # program or service status is unknown
    NUMBER_OF_RULES=$(iptables-save | grep '^\-' | wc -l)
    if [ 0 -eq $NUMBER_OF_RULES ]; then
        EXIT=3 # program is not running
    else
        EXIT=0 # program is running or service is OK
    fi
    exit $EXIT
    ;;
  *)
    echo "Usage: /etc/init.d/firewall {start|stop|status|restart}"
    exit 1
    ;;
esac

exit 0
```

### templates\firewall.unit.j2

```jinja2
[Unit]
Description=Firewall
After=syslog.target network.target

[Service]
Type=oneshot
ExecStart=/etc/firewall.bash
ExecStop=/sbin/iptables -F
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

### tests\inventory

```txt
localhost
```

### tests\test.yml

```yml
---
- hosts: localhost
  remote_user: root
  roles:
    - firewall
```

### vars\main.yml

```yml
---
# vars file for firewall
```

> This concludes the repository's file contents. Please review thoroughly for a comprehensive understanding of the codebase.
