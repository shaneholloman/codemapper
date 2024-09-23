# ansible-role-apache

This markdown document provides a comprehensive overview of the directory structure and file contents. It aims to give viewers (human or AI) a complete view of the codebase in a single file for easy analysis.

## Document Table of Contents

The table of contents below is for navigational convenience and reflects this document's structure, not the actual file structure of the repository.

<!-- TOC -->

- [ansible-role-apache](#ansible-role-apache)
  - [Document Table of Contents](#document-table-of-contents)
  - [Repo File Tree](#repo-file-tree)
  - [Repo File Contents](#repo-file-contents)
    - [README.md](#readmemd)
    - [.gitignore](#gitignore)
    - [.ansible-lint](#ansible-lint)
    - [.gitattributes](#gitattributes)
    - [.github/FUNDING.yml](#githubfundingyml)
    - [.github/workflows/ci.yml](#githubworkflowsciyml)
    - [.github/workflows/release.yml](#githubworkflowsreleaseyml)
    - [.github/workflows/remove.yml](#githubworkflowsremoveyml)
    - [.github/workflows/stale.yml](#githubworkflowsstaleyml)
    - [.yamllint](#yamllint)
    - [defaults/main.yml](#defaultsmainyml)
    - [handlers/main.yml](#handlersmainyml)
    - [LICENSE](#license)
    - [meta/main.yml](#metamainyml)
    - [molecule/default/converge.yml](#moleculedefaultconvergeyml)
    - [molecule/default/molecule.yml](#moleculedefaultmoleculeyml)
    - [tasks/configure-Debian.yml](#tasksconfigure-debianyml)
    - [tasks/configure-RedHat.yml](#tasksconfigure-redhatyml)
    - [tasks/configure-Solaris.yml](#tasksconfigure-solarisyml)
    - [tasks/configure-Suse.yml](#tasksconfigure-suseyml)
    - [tasks/main.yml](#tasksmainyml)
    - [tasks/setup-Debian.yml](#taskssetup-debianyml)
    - [tasks/setup-RedHat.yml](#taskssetup-redhatyml)
    - [tasks/setup-Solaris.yml](#taskssetup-solarisyml)
    - [tasks/setup-Suse.yml](#taskssetup-suseyml)
    - [templates/vhosts.conf.j2](#templatesvhostsconfj2)
    - [vars/AmazonLinux.yml](#varsamazonlinuxyml)
    - [vars/apache-22.yml](#varsapache-22yml)
    - [vars/apache-24.yml](#varsapache-24yml)
    - [vars/Debian.yml](#varsdebianyml)
    - [vars/RedHat.yml](#varsredhatyml)
    - [vars/Solaris.yml](#varssolarisyml)
    - [vars/Suse.yml](#varssuseyml)

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
├── defaults/
│   └── main.yml
├── handlers/
│   └── main.yml
├── meta/
│   └── main.yml
├── molecule/
│   └── default/
│       ├── converge.yml
│       └── molecule.yml
├── tasks/
│   ├── configure-Debian.yml
│   ├── configure-RedHat.yml
│   ├── configure-Solaris.yml
│   ├── configure-Suse.yml
│   ├── main.yml
│   ├── setup-Debian.yml
│   ├── setup-RedHat.yml
│   ├── setup-Solaris.yml
│   └── setup-Suse.yml
├── templates/
│   └── vhosts.conf.j2
├── vars/
│   ├── AmazonLinux.yml
│   ├── Debian.yml
│   ├── RedHat.yml
│   ├── Solaris.yml
│   ├── Suse.yml
│   ├── apache-22.yml
│   └── apache-24.yml
├── .ansible-lint
├── .gitattributes
├── .gitignore
├── .yamllint
├── LICENSE
└── README.md

10 directories, 33 files
```

## Repo File Contents

The following sections present the content of each file in the repository. Large binary files are acknowledged but their contents are not displayed.

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

### .gitignore

```ini
*.retry
*/__pycache__
*.pyc
.cache
```

### .gitattributes

```txt
* text=auto eol=lf
```

### README.md

````markdown
[Binary file detected. File Type: text/markdown, Size: 8379 bytes]
````

### .ansible-lint

```txt
skip_list:
  - 'yaml'
  - 'role-name'
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

### molecule/default/converge.yml

```yml
---
- name: Converge
  hosts: all
  become: true

  vars:
    apache_listen_port_ssl: 443
    apache_create_vhosts: true
    apache_vhosts_filename: "vhosts.conf"
    apache_vhosts:
      - servername: "example.com"
        documentroot: "/var/www/vhosts/example_com"

  pre_tasks:
    - name: Update apt cache.
      ansible.builtin.apt: update_cache=yes cache_valid_time=600
      when: ansible_os_family == 'Debian'
      changed_when: false

  roles:
    - role: shaneholloman.apache
```

### molecule/default/molecule.yml

```yml
---
role_name_check: 1
dependency:
  name: galaxy
driver:
  name: docker
platforms:
  - name: instance
    image: "shaneholloman/docker-${MOLECULE_DISTRO:-centos8}-ansible:latest"
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
```

### tasks/setup-Suse.yml

```yml
---
- name: Ensure Apache is installed on Suse.
  community.general.zypper:
    name: "{{ apache_packages }}"
    state: "{{ apache_packages_state }}"
```

### tasks/setup-Solaris.yml

```yml
---
- name: Ensure Apache is installed on Solaris.
  community.general.pkg5:
    name: "{{ apache_packages }}"
    state: "{{ apache_packages_state }}"
```

### tasks/configure-Suse.yml

```yml
---

- name: Configure Apache.
  ansible.builtin.lineinfile:
    dest: "{{ apache_server_root }}/listen.conf"
    regexp: "{{ item.regexp }}"
    line: "{{ item.line }}"
    state: present
    mode: '0644'
  with_items: "{{ apache_ports_configuration_items }}"
  notify: Restart apache

- name: Check whether certificates defined in vhosts exist.
  ansible.builtin.stat:
    path: "{{ item.certificate_file }}"
  register: apache_ssl_certificates
  with_items: "{{ apache_vhosts_ssl }}"

- name: Add apache vhosts configuration.
  ansible.builtin.template:
    src: "{{ apache_vhosts_template }}"
    dest: "{{ apache_conf_path }}/{{ apache_vhosts_filename }}"
    owner: root
    group: root
    mode: '0644'
  notify: Restart apache
  when: apache_create_vhosts | bool
```

### tasks/main.yml

```yml
---
# Include variables and define needed variables.
- name: Include OS-specific variables.
  ansible.builtin.include_vars: "{{ ansible_os_family }}.yml"

- name: Include variables for Amazon Linux.
  ansible.builtin.include_vars: "AmazonLinux.yml"
  when:
    - ansible_distribution == "Amazon"
    - ansible_distribution_major_version == "NA"

- name: Define apache_packages.
  ansible.builtin.set_fact:
    apache_packages: "{{ __apache_packages | list }}"
  when: apache_packages is not defined

# Setup/install tasks.
- name: Include OS-specific setup tasks
  ansible.builtin.include_tasks: "setup-{{ ansible_os_family }}.yml"

# Figure out what version of Apache is installed.
- name: Get installed version of Apache.
  ansible.builtin.command: "{{ apache_daemon_path }}{{ apache_daemon }} -v"
  changed_when: false
  check_mode: false
  register: _apache_version

- name: Create apache_version variable.
  ansible.builtin.set_fact:
    apache_version: "{{ _apache_version.stdout.split()[2].split('/')[1] }}"

- name: Include Apache 2.2 variables.
  ansible.builtin.include_vars: apache-22.yml
  when: "apache_version.split('.')[1] == '2'"

- name: Include Apache 2.4 variables.
  ansible.builtin.include_vars: apache-24.yml
  when: "apache_version.split('.')[1] == '4'"

# Configure Apache.
- name: Configure Apache.
  ansible.builtin.include_tasks: "configure-{{ ansible_os_family }}.yml"

- name: Ensure Apache has selected state and enabled on boot.
  ansible.builtin.service:
    name: "{{ apache_service }}"
    state: "{{ apache_state }}"
    enabled: "{{ apache_enabled }}"
```

### tasks/configure-RedHat.yml

```yml
---
- name: Configure Apache.
  ansible.builtin.lineinfile:
    dest: "{{ apache_server_root }}/conf/{{ apache_daemon }}.conf"
    regexp: "{{ item.regexp }}"
    line: "{{ item.line }}"
    state: present
    mode: '0644'
  with_items: "{{ apache_ports_configuration_items }}"
  notify: Restart apache

- name: Check whether certificates defined in vhosts exist.
  ansible.builtin.stat:
    path: "{{ item.certificate_file }}"
  register: apache_ssl_certificates
  with_items: "{{ apache_vhosts_ssl }}"

- name: Enable Apache mods.
  ansible.builtin.copy:
    dest: "{{ apache_server_root }}/conf.modules.d/99-ansible-{{ item }}.conf"
    content: |
      LoadModule {{ item }}_module modules/mod_{{ item }}.so
    mode: '0644'
  with_items: "{{ apache_mods_enabled }}"
  notify: Restart apache

- name: Disable Apache mods
  ansible.builtin.file:
    path: "{{ apache_server_root }}/conf.modules.d/99-ansible-{{ item }}.conf"
    state: absent
  with_items: "{{ apache_mods_disabled }}"
  notify: Restart apache

- name: Add apache vhosts configuration.
  ansible.builtin.template:
    src: "{{ apache_vhosts_template }}"
    dest: "{{ apache_conf_path }}/{{ apache_vhosts_filename }}"
    owner: root
    group: root
    mode: '0644'
  notify: Restart apache
  when: apache_create_vhosts | bool

- name: Ensure localhost certificate exists for RHEL 8 and later
  when: ansible_distribution_major_version | int >= 8
  block:
    - name: Check if localhost cert exists (RHEL 8 and later).
      ansible.builtin.stat:
        path: /etc/pki/tls/certs/localhost.crt
      register: localhost_cert

    - name: Ensure httpd certs are installed (RHEL 8 and later).
      ansible.builtin.command: /usr/libexec/httpd-ssl-gencerts  # noqa no-changed-when
      when: not localhost_cert.stat.exists
```

### tasks/configure-Solaris.yml

```yml
---
- name: Configure Apache.
  ansible.builtin.lineinfile:
    dest: "{{ apache_server_root }}/{{ apache_daemon }}.conf"
    regexp: "{{ item.regexp }}"
    line: "{{ item.line }}"
    state: present
    mode: '0644'
  with_items: "{{ apache_ports_configuration_items }}"
  notify: Restart apache

- name: Add apache vhosts configuration.
  ansible.builtin.template:
    src: "{{ apache_vhosts_template }}"
    dest: "{{ apache_conf_path }}/{{ apache_vhosts_filename }}"
    owner: root
    group: root
    mode: '0644'
  notify: Restart apache
  when: apache_create_vhosts | bool
```

### tasks/setup-Debian.yml

```yml
---
- name: Update apt cache.
  ansible.builtin.apt:
    update_cache: true
    cache_valid_time: 3600

- name: Ensure Apache is installed on Debian.
  ansible.builtin.apt:
    name: "{{ apache_packages }}"
    state: "{{ apache_packages_state }}"
```

### tasks/configure-Debian.yml

```yml
---
- name: Configure Apache.
  ansible.builtin.lineinfile:
    dest: "{{ apache_server_root }}/ports.conf"
    regexp: "{{ item.regexp }}"
    line: "{{ item.line }}"
    state: present
    mode: '0644'
  with_items: "{{ apache_ports_configuration_items }}"
  notify: Restart apache

- name: Enable Apache mods.
  ansible.builtin.file:
    src: "{{ apache_server_root }}/mods-available/{{ item }}.load"
    dest: "{{ apache_server_root }}/mods-enabled/{{ item }}.load"
    state: link
    mode: '0644'
  with_items: "{{ apache_mods_enabled }}"
  notify: Restart apache

- name: Disable Apache mods.
  ansible.builtin.file:
    path: "{{ apache_server_root }}/mods-enabled/{{ item }}.load"
    state: absent
  with_items: "{{ apache_mods_disabled }}"
  notify: Restart apache

- name: Check whether certificates defined in vhosts exist.
  ansible.builtin.stat:
    path: "{{ item.certificate_file }}"
  register: apache_ssl_certificates
  with_items: "{{ apache_vhosts_ssl }}"

- name: Add apache vhosts configuration.
  ansible.builtin.template:
    src: "{{ apache_vhosts_template }}"
    dest: "{{ apache_conf_path }}/sites-available/{{ apache_vhosts_filename }}"
    owner: root
    group: root
    mode: '0644'
  notify: Restart apache
  when: apache_create_vhosts | bool

- name: Add vhost symlink in sites-enabled.
  ansible.builtin.file:
    src: "{{ apache_conf_path }}/sites-available/{{ apache_vhosts_filename }}"
    dest: "{{ apache_conf_path }}/sites-enabled/{{ apache_vhosts_filename }}"
    state: link
    mode: '0644'
  notify: Restart apache
  when: apache_create_vhosts | bool

- name: Remove default vhost in sites-enabled.
  ansible.builtin.file:
    path: "{{ apache_conf_path }}/sites-enabled/{{ apache_default_vhost_filename }}"
    state: absent
  notify: Restart apache
  when: apache_remove_default_vhost
```

### tasks/setup-RedHat.yml

```yml
---
- name: Ensure Apache is installed on RHEL.
  ansible.builtin.package:
    name: "{{ apache_packages }}"
    state: "{{ apache_packages_state }}"
    enablerepo: "{{ apache_enablerepo | default(omit, true) }}"
```

### handlers/main.yml

```yml
---

- name: Restart apache
  ansible.builtin.service:
    name: "{{ apache_service }}"
    state: "{{ apache_restart_state }}"
```

### .github/FUNDING.yml

```yml
# These are supported funding model platforms
---
github: shaneholloman
patreon: none
```

### .github/workflows/release.yml

```yml
---
# Release Repo to Ansible Galaxy
name: Release
'on':
  push:
    tags:
      - '*'
  workflow_dispatch:

defaults:
  run:
    working-directory: 'shaneholloman.apache'

jobs:

  release:
    name: Release
    runs-on: ubuntu-latest
    steps:
      - name: Check out the codebase.
        uses: actions/checkout@v4
        with:
          path: 'shaneholloman.apache'

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

### .github/workflows/stale.yml

```yml
---
name: Close inactive issues
'on':
  schedule:
    - cron: "55 19 * * 6"  # semi-random time
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

### .github/workflows/ci.yml

```yml
---
name: CI
'on':
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - main
  schedule:
    - cron: "0 5 * * 0"

defaults:
  run:
    working-directory: 'shaneholloman.apache'

jobs:

  lint:
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - name: Check out the codebase.
        uses: actions/checkout@v4
        with:
          path: 'shaneholloman.apache'

      - name: Set up Python 3.
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

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
          path: 'shaneholloman.apache'

      - name: Set up Python 3.
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install test dependencies.
        run: pip3 install ansible molecule molecule-plugins[docker] docker

      - name: Run Molecule tests.
        run: molecule test
        env:
          PY_COLORS: '1'
          ANSIBLE_FORCE_COLOR: '1'
          MOLECULE_DISTRO: ${{ matrix.distro }}
```

### .github/workflows/remove.yml

```yml
---
# This workflow requires a GALAXY_API_KEY secret present in the GitHub
# repository or organization.
#
# See: https://github.com/marketplace/actions/publish-ansible-role-to-galaxy
# See: https://github.com/ansible/galaxy/issues/46

name: Remove
'on':
  workflow_dispatch:

defaults:
  run:
    working-directory: 'shaneholloman.apache'

jobs:

  release:
    name: Remove from Galaxy
    runs-on: ubuntu-latest
    steps:
      - name: Check out the codebase.
        uses: actions/checkout@v4
        with:
          path: 'shaneholloman.apache'

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

### vars/apache-24.yml

```yml
---
apache_vhosts_version: "2.4"
apache_default_vhost_filename: 000-default.conf
apache_ports_configuration_items:
  - {
    regexp: "^Listen ",
    line: "Listen {{ apache_listen_port }}"
  }
```

### vars/RedHat.yml

```yml
---
apache_service: httpd
apache_daemon: httpd
apache_daemon_path: /usr/sbin/
apache_server_root: /etc/httpd
apache_conf_path: /etc/httpd/conf.d

apache_vhosts_version: "2.2"

__apache_packages:
  - httpd
  - httpd-devel
  - mod_ssl
  - openssh

apache_ports_configuration_items:
  - regexp: "^Listen "
    line: "Listen {{ apache_listen_port }}"
  - regexp: "^#?NameVirtualHost "
    line: "NameVirtualHost {{ apache_listen_ip }}:{{ apache_listen_port }}"
```

### vars/Solaris.yml

```yml
---
apache_service: apache24
apache_daemon: httpd
apache_daemon_path: /usr/apache2/2.4/bin/
apache_server_root: /etc/apache2/2.4/
apache_conf_path: /etc/apache2/2.4/conf.d

apache_vhosts_version: "2.4"

__apache_packages:
  - web/server/apache-24
  - web/server/apache-24/module/apache-ssl
  - web/server/apache-24/module/apache-security

apache_ports_configuration_items:
  - regexp: "^Listen "
    line: "Listen {{ apache_listen_port }}"
  - regexp: "^#?NameVirtualHost "
    line: "NameVirtualHost {{ apache_listen_ip }}:{{ apache_listen_port }}"
```

### vars/Debian.yml

```yml
---
apache_service: apache2
apache_daemon: apache2
apache_daemon_path: /usr/sbin/
apache_server_root: /etc/apache2
apache_conf_path: /etc/apache2

__apache_packages:
  - apache2
  - apache2-utils

apache_ports_configuration_items:
  - regexp: "^Listen "
    line: "Listen {{ apache_listen_port }}"
```

### vars/AmazonLinux.yml

```yml
---
apache_service: httpd
apache_daemon: httpd
apache_daemon_path: /usr/sbin/
apache_server_root: /etc/httpd
apache_conf_path: /etc/httpd/conf.d

apache_vhosts_version: "2.4"

__apache_packages:
  - httpd24
  - httpd24-devel
  - mod24_ssl
  - openssh

apache_ports_configuration_items:
  - regexp: "^Listen "
    line: "Listen {{ apache_listen_port }}"
```

### vars/apache-22.yml

```yml
---
apache_vhosts_version: "2.2"
apache_default_vhost_filename: 000-default
apache_ports_configuration_items:
  - {
    regexp: "^Listen ",
    line: "Listen {{ apache_listen_port }}"
  }
  - {
    regexp: "^#?NameVirtualHost ",
    line: "NameVirtualHost {{ apache_listen_ip }}:{{ apache_listen_port }}"
  }
```

### vars/Suse.yml

```yml
---
apache_service: apache2
apache_daemon: httpd2
apache_daemon_path: /usr/sbin/
apache_server_root: /etc/apache2
apache_conf_path: /etc/apache2/conf.d

apache_vhosts_version: "2.2"

__apache_packages:
  - apache2
  - openssh

apache_ports_configuration_items:
  - regexp: "^Listen "
    line: "Listen {{ apache_listen_port }}"
  - regexp: "^#?NameVirtualHost "
    line: "NameVirtualHost {{ apache_listen_ip }}:{{ apache_listen_port }}"
```

### meta/main.yml

```yml
---
galaxy_info:
  role_name: apache
  author: shaneholloman
  description: Apache 2.x for Linux.
  company: "shaneholloman"
  license: "license (Unlicense)"
  min_ansible_version: "2.12"

  platforms:
    - name: Fedora
      versions:
        - all
    - name: Amazon
      versions:
        - all
    - name: Debian
      versions:
        - all
    - name: Ubuntu
      versions:
        - trusty
        - xenial
        - bionic
    - name: Solaris
      versions:
        - "11.3"

  galaxy_tags:
    - web
    - apache
    - webserver
    - html
    - httpd

allow_duplicates: true

dependencies: []
```

### defaults/main.yml

```yml
---
apache_enablerepo: ""

apache_listen_ip: "*"
apache_listen_port: 80
apache_listen_port_ssl: 443

apache_create_vhosts: true
apache_vhosts_filename: "vhosts.conf"
apache_vhosts_template: "vhosts.conf.j2"

# On Debian/Ubuntu, a default virtualhost is included in Apache's configuration.
# Set this to `true` to remove that default.
apache_remove_default_vhost: false

apache_global_vhost_settings: |
  DirectoryIndex index.php index.html

apache_vhosts:
  # Additional properties:
  # 'serveradmin, serveralias, allow_override, options, extra_parameters'.
  - servername: "local.dev"
    documentroot: "/var/www/html"

apache_allow_override: "All"
apache_options: "-Indexes +FollowSymLinks"

apache_vhosts_ssl: []
# Additional properties:
# 'serveradmin, serveralias, allow_override, options, extra_parameters'.
# - servername: "local.dev",
#   documentroot: "/var/www/html",
#   certificate_file: "/path/to/certificate.crt",
#   certificate_key_file: "/path/to/certificate.key",
#   # Optional.
#   certificate_chain_file: "/path/to/certificate_chain.crt"

apache_ignore_missing_ssl_certificate: true

apache_ssl_protocol: "All -SSLv2 -SSLv3"
apache_ssl_cipher_suite: "AES256+EECDH:AES256+EDH"

# Only used on Debian/Ubuntu/Redhat.
apache_mods_enabled:
  - rewrite
  - ssl
apache_mods_disabled: []

# Set initial apache state. Recommended values: `started` or `stopped`
apache_state: started

# Set initial apache service status. Recommended values: `true` or `false`
apache_enabled: true

# Set apache state when configuration changes are made. Recommended values:
# `restarted` or `reloaded`
apache_restart_state: restarted

# Apache package state; use `present` to make sure it's installed, or `latest`
# if you want to upgrade or switch versions using a new repo.
apache_packages_state: present
```

### templates/vhosts.conf.j2

```jinja2
{{ apache_global_vhost_settings }}

{# Set up VirtualHosts #}
{% for vhost in apache_vhosts %}
<VirtualHost {{ apache_listen_ip }}:{{ apache_listen_port }}>
  ServerName {{ vhost.servername }}
{% if vhost.serveralias is defined %}
  ServerAlias {{ vhost.serveralias }}
{% endif %}
{% if vhost.documentroot is defined %}
  DocumentRoot "{{ vhost.documentroot }}"
{% endif %}

{% if vhost.serveradmin is defined %}
  ServerAdmin {{ vhost.serveradmin }}
{% endif %}
{% if vhost.documentroot is defined %}
  <Directory "{{ vhost.documentroot }}">
    AllowOverride {{ vhost.allow_override | default(apache_allow_override) }}
    Options {{ vhost.options | default(apache_options) }}
{% if apache_vhosts_version == "2.2" %}
    Order allow,deny
    Allow from all
{% else %}
    Require all granted
{% endif %}
  </Directory>
{% endif %}
{% if vhost.extra_parameters is defined %}
{{ vhost.extra_parameters | indent(width=2, first=True) }}
{% endif %}
</VirtualHost>

{% endfor %}

{# Set up SSL VirtualHosts #}
{% for vhost in apache_vhosts_ssl %}
{% if apache_ignore_missing_ssl_certificate or apache_ssl_certificates.results[loop.index0].stat.exists %}
<VirtualHost {{ apache_listen_ip }}:{{ apache_listen_port_ssl }}>
  ServerName {{ vhost.servername }}
{% if vhost.serveralias is defined %}
  ServerAlias {{ vhost.serveralias }}
{% endif %}
{% if vhost.documentroot is defined %}
  DocumentRoot "{{ vhost.documentroot }}"
{% endif %}

  SSLEngine on
  SSLCipherSuite {{ apache_ssl_cipher_suite }}
  SSLProtocol {{ apache_ssl_protocol }}
  SSLHonorCipherOrder On
{% if apache_vhosts_version == "2.4" %}
  SSLCompression off
{% endif %}
  SSLCertificateFile {{ vhost.certificate_file }}
  SSLCertificateKeyFile {{ vhost.certificate_key_file }}
{% if vhost.certificate_chain_file is defined %}
  SSLCertificateChainFile {{ vhost.certificate_chain_file }}
{% endif %}

{% if vhost.serveradmin is defined %}
  ServerAdmin {{ vhost.serveradmin }}
{% endif %}
{% if vhost.documentroot is defined %}
  <Directory "{{ vhost.documentroot }}">
    AllowOverride {{ vhost.allow_override | default(apache_allow_override) }}
    Options {{ vhost.options | default(apache_options) }}
{% if apache_vhosts_version == "2.2" %}
    Order allow,deny
    Allow from all
{% else %}
    Require all granted
{% endif %}
  </Directory>
{% endif %}
{% if vhost.extra_parameters is defined %}
{{ vhost.extra_parameters | indent(width=2, first=True) }}
{% endif %}
</VirtualHost>

{% endif %}
{% endfor %}
```

> This concludes the repository's file contents. Please review thoroughly for a comprehensive understanding of the codebase.
