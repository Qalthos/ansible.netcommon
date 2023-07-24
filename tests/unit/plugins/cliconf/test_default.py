#
# (c) 2016 Red Hat Inc.
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function


__metaclass__ = type

import json

from unittest.mock import MagicMock

import pytest

from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import cliconf_loader


@pytest.fixture(name="cliconf")
def plugin_fixture(monkeypatch):
    pc = PlayContext()

    cliconf = cliconf_loader.get("ansible.netcommon.default", pc, "/dev/null")
    return cliconf


def test_get_device_info(cliconf):
    info = cliconf.get_device_info()
    assert info == dict(network_os="default")


def test_get_capabilities(cliconf):
    cap = cliconf.get_capabilities()
    assert cap == dict(
        device_operations={
            "supports_diff_replace": False,
            "supports_commit": False,
            "supports_rollback": False,
            "supports_defaults": False,
            "supports_onbox_diff": False,
            "supports_commit_comment": False,
            "supports_multiline_delimiter": False,
            "supports_diff_match": False,
            "supports_diff_ignore_lines": False,
            "supports_generate_diff": False,
            "supports_replace": False,
        },
    )
