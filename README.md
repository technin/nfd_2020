# ansible_for_juniper_mist

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/3/31/Juniper_Networks_logo.svg)](https://www.juniper.net/us/en/products-services/sdn/contrail/contrail-service-orchestration/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

`Ansible for Juniper Mist` is a demonstration to showcase the ease of automation within Juniper's portfolio, specifically focusing on the following:

- manage 100% of your firewall, switches, and access point configurations as code
- integration with 3rd party APIs
- proactive messaging by leveraging webhooks

## Dependencies

This project will be hosted within Ansible Tower and will therefore have that obvious requirement. In regards to packages, we require nothing more than the default modules shipped with Ansible.

## Very Important

Please make sure to create your own `secrets.yml` file and store it in `group_vars/all` directory. This file hosts many variables necessary to complete the ansible playbook, without this file all of your plans for automation are destroyed.

The `secrets_example.yml` file from the root directory of this project will get you started, simply update the variables with the values appropriate for your environment and move it to `group_vars/all` directory, overwriting the current file there.

This should do the trick nicely

```sh
mv secrets_example.yml ./group_vars/all/secrets.yml
```

### Optional

> Leverage Ansible-Vault to encrypt the `secrets.yml` file before hosting on the public internet

```sh
ansible-vault encrypt secrets.yml
```

## Development

Want to contribute? Great!

Submit a PR and let's work on this together :D

...wait a minute. this is a private repository, you shouldn't be able to access any of this. Sir, this is an Arby's
