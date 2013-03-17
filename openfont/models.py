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
        pkg.weights = cls.parse_weights(json)

        return pkg

    @classmethod
    def parse_weights(cls, obj):
        weights = []
        for name, filename in obj['weights'].iteritems():
            weights.append(FontWeight(name, filename))

        return weights


class FontWeight(object):
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


class Package(object):
    loaders = {
        "1.0": PackageLoaderAlgorithm1
    }

    @classmethod
    def load_from_json_string(cls, json):
        obj = loads(json)

        loader = cls.loaders.get(obj.get('metaVersion', "1.0"), PackageLoaderAlgorithm1)

        return loader.load_from_json(obj)
