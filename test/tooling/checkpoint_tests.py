#TO RUN: joey2 project_operation_tests.py
import os
import sys
import unittest
import mock
import shutil
sys.path.append('../')
sys.path.append('../../')
import lib.mm_util as mm_util
import test_util as util
from test_helper import MavensMateTest
import mm    

base_test_directory = os.path.dirname(os.path.dirname(__file__))

class CheckpointTests(MavensMateTest):
    # @classmethod    
    # def setUpClass(self):
    #     pass
    #     #setup project

    def create_project(self):
        stdin = {
            "project_name"  : "unit test tooling project",
            "username"      : "mm@force.com",
            "password"      : "force",
            "org_type"      : "developer",
            "action"        : "new",
            "package"       : {
                "ApexClass" : "*"
            } 
        }
        mm_util.get_request_payload = mock.Mock(return_value=stdin)
        sys.argv = ['mm.py', '-o', 'new_project']
        mm.main()
        

    def test_01_new_debug_log(self): 
        self.create_project()
        commandOut = self.redirectStdOut()
        stdin = {
            "project_name"      : "unit test tooling project",
            "type"              : "user",
            "debug_categories"  : {
                "ApexCode"      : "DEBUG",
                "Visualforce"   : "FOO"
            }
        }
        mm_util.get_request_payload = mock.Mock(return_value=stdin)
        sys.argv = ['mm.py', '-o', 'new_log']
        mm.main()
        mm_response = commandOut.getvalue()
        sys.stdout = self.saved_stdout
        print mm_response
        mm_json_response = util.parse_mm_response(mm_response)
        self.assertTrue(mm_json_response['success'] == True)
        self.assertTrue('id' in mm_json_response and len(mm_json_response['id']) is 18)

    def test_02_new_apex_checkpoint(self): 
        self.create_project()
        commandOut = self.redirectStdOut()
        stdin = {
            "project_name"      : "unit test tooling project",
            "type"              : "user",
            "debug_categories"  : {
                "ApexCode"      : "DEBUG",
                "Visualforce"   : "FOO"
            }
        }
        mm_util.get_request_payload = mock.Mock(return_value=stdin)
        sys.argv = ['mm.py', '-o', 'new_log']
        mm.main()
        mm_response = commandOut.getvalue()
        sys.stdout = self.saved_stdout
        print mm_response
        mm_json_response = util.parse_mm_response(mm_response)
        self.assertTrue(mm_json_response['success'] == True)
        self.assertTrue('id' in mm_json_response and len(mm_json_response['id']) is 18)


    @classmethod    
    def tearDownClass(self):
        if os.path.exists(os.path.join(base_test_directory,"test_workspace","unit test tooling project")):
            shutil.rmtree(os.path.join(base_test_directory,"test_workspace","unit test tooling project"))

if __name__ == '__main__':
    if os.path.exists(os.path.join(base_test_directory,"test_workspace","unit test tooling project")):
        shutil.rmtree(os.path.join(base_test_directory,"test_workspace","unit test tooling project"))
    unittest.main()