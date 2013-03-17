#!/usr/bin/python
# -*- coding: utf-8 -*-

# OpenFont - Font Packaging Format
# https://github.com/heynemann/openfont

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from ujson import loads


class PackageLoaderAlgorithm1(object):
    @classmethod
    def load_from_json(cls, json):
        pkg = Package()

        pkg.meta_version = json['metaVersion']
        pkg.name = json['name']
        pkg.version = json['version']
        pkg.families = cls.parse_families(json)

        return pkg

    @classmethod
    def parse_families(cls, obj):
        return []


class Package(object):
    loaders = {
        "1.0": PackageLoaderAlgorithm1
    }

    @classmethod
    def load_from_json_string(cls, json):
        obj = loads(json)

        loader = cls.loaders.get(obj.get('metaVersion', "1.0"), PackageLoaderAlgorithm1)

        return loader.load_from_json(obj)
