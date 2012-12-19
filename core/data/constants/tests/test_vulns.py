'''
test_vulns.py

Copyright 2006 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''
import os
import re
import unittest

from core.data.constants.vulns import VULNS


class TestVulnsConstants(unittest.TestCase):
    
    LOCATION = os.path.join('core', 'data', 'constants', 'vulns.py')
    
    def test_no_duplicated_ids(self):
        # Just skip the entire license header
        vulns_file = file(self.LOCATION) 
        for _ in xrange(21):
            vulns_file.readline()
            
        vuln_id_list = re.findall('\d+', vulns_file.read())
        filtered = set()
        dups = set()
        
        for vuln_id in vuln_id_list:
            if vuln_id in filtered:
                dups.add(vuln_id)
            
            filtered.add(vuln_id)
            
        self.assertEquals( set([]), dups )
    
    def test_no_empty(self):
        items = VULNS.items()
        empty_values = [(key, val) for (key, val) in items if not val]
        self.assertEqual(set([]), empty_values)