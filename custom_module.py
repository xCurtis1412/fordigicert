#!/usr/bin/env python3
"""
Ansible custom module for math
"""
import math
from ansible.module_utils.basic import AnsibleModule

def ryansmath():
    module = AnsibleModule(
        argument_spec=dict(
            values=dict(type='list', elements='float', required=True),
        )
    )
    values = module.params['values']
    if not values:
        module.fail_json(msg="values list is empty/blank")
    mean = sum(values) / len(values)
    stddev = math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))    
        module.exit_json(changed=False, mean=round(mean, 4), stddev=round(stddev, 4))

if __name__ == '__main__':
    ryansmath()
