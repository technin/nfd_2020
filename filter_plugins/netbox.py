import json
import yaml


def cleanup_site_data(value):
    site = {}
    for each in value:
        site["name"] = each["name"]
    
    return site

# ##################################################################
# ### format the return of GET dcim/devices/?slug={{ site_name }}
# ###   into an object that can be easily called by the jinja2
# ###   template the json used to create a device's config in Mist
# ##################################################################
def netbox_to_mist_devices(value):
    '''
    example payload:
      - config_context: {}
        device_role:
          slug: switch-l2
        device_type:
          slug: ex
        display_name: Magnolia-sw1
        name: Magnolia-sw1
        platform:
          slug: ex2300-c-12p
        serial: HW0216520055
        site:
          slug: magnolia
        status:
          value: active
        tags:
        - switch
        tenant:
          slug: redtail
    '''
    devices = []
    network_device = {}
    for each in value:
        network_device["config_context"] = each["config_context"]
        network_device["device_role"] = each["device_role"]["slug"]
        network_device["device_type"] = each["device_type"]["slug"]
        network_device["name"] = each["display_name"]
        network_device["platform"] = each["platform"]["slug"]
        network_device["serial"] = each["serial"]
        network_device["site"] = each["site"]["slug"]
        network_device["site_url"] = each["site"]["url"]
        network_device["status"] = each["status"]["value"]
        network_device["tags"] = each["tags"]
        if each["tenant"] is not None:
          network_device["tenant"] = each["tenant"]["slug"]
        else:
          network_device["tenant"] = "not_found"

        devices.append(network_device)
    return devices

class FilterModule(object):
    ''' 
    20200912: @packetferret
    Netbox Jinja2 filter plugins
    '''

    def filters(self):
        return {
            # jinja2 overrides
            'netbox_to_mist_devices': netbox_to_mist_devices,

        }
