# -*- coding: UTF-8 -*-
# This file is part of the jetson_stats package (https://github.com/rbonghi/jetson_stats or http://rnext.it).
# Copyright (c) 2019-2023 Raffaello Bonghi.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import pytest
from jtop import jtop
from .conftest import emulate_all_devices


def test_fan(setup_jtop_server):
    with jtop() as jetson:
        print("Running test with parameter:", setup_jtop_server)
        if jetson.ok():
            # Read fan status
            fan = jetson.fan
            # Status fan
            print("Fan output: {fan}".format(fan=fan))
            # Check depend of parameter
            if setup_jtop_server in ['simple', 'tk']:
                assert len(fan) == 0
            else:
                assert len(fan) > 0


test_fan = pytest.mark.parametrize("setup_jtop_server", emulate_all_devices(), indirect=True)(test_fan)
# EOF
