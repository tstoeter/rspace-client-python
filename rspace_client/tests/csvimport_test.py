#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:11:08 2022

@author: richardadams
"""

import pytest,json, io

import rspace_client.tests.base_test as base
from rspace_client.inv import importer

class CSVImportest(base.BaseApiTest):
    def setUp(self):
        """
        Skips tests if aPI client credentials are missing
        """
        self.assertClientCredentials()
        self.api = importer.Importer(self.rspace_url, self.rspace_apikey)

    def test_create_sample_from_file(self):
        col_map= importer.ContainerColumnMap("Name")
        mappings = col_map.description_column("Alternative name").id_column("Import Id").parent_id_ref_column("Parent container").build()
        
        
        f = base.get_datafile("container_basic.csv")
        with open(f, 'r')as container:
            resp = self.api.import_container_csv(container, mappings)
            self.assertTrue(resp.is_ok())
            self.assertEqual(5, resp.containers_imported())
            
    def test_names_only(self):
        f = io.StringIO("CName\nC1\nC2\n")
        colmap= importer.ContainerColumnMap("CName").build()
        resp = self.api.import_container_csv(f, colmap)
        self.assertEqual(2, resp.containers_imported())
        
        
        
            
            
    
            
        
        