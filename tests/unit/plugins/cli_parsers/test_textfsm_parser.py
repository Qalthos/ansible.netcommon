# (c) 2020 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import textfsm
import os

from ansible_collections.ansible.netcommon.tests.unit.compat import unittest
from ansible_collections.ansible.netcommon.plugins.cli_parsers.textfsm_parser import (
    CliParser,
)


class TestTextfsmParser(unittest.TestCase):
    def test_textfsm_parser(self):
        nxos_cfg_path = os.path.join(os.path.dirname(__file__), "fixtures", "nxos_show_version.cfg")
        nxos_template_path = os.path.join(os.path.dirname(__file__), "fixtures", "nxos_show_version.textfsm")

        with open(nxos_cfg_path) as f:
            nxos_show_version_output = f.read()

        task_args = {"text": nxos_show_version_output,
                     "parser": 
                        {"name": "ansible.netcommon.textfsm", "command": "show version", "template_path": nxos_template_path}
                    }
        parser = CliParser(task_args=task_args, task_vars=[], debug=False)

        result = parser.parse()
        parsed_output = [{'BOOT_IMAGE': 'bootflash:///nxos.7.0.3.I7.1.bin', 
                        'LAST_REBOOT_REASON': 'Unknown',
                        'OS': '7.0(3)I7(1)',
                        'PLATFORM': '9000v',
                        'UPTIME': '12 day(s), 23 hour(s), 48 minute(s), 10 second(s)'}]
        self.assertEqual(result, {"parsed": parsed_output})
