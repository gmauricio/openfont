#!/usr/bin/python
# -*- coding: utf-8 -*-

# OpenFont - Font Packaging Format
# https://github.com/heynemann/openfont

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from os.path import exists, join

from openfont.loaders.base import Loader
from openfont.models import Package
from openfont.errors import InvalidPackageError, BrokenPackageError


class OpenFontFileLoader(Loader):
    def __init__(self, path):
        self.path = path
        self.valid_formats = ['woff', 'eot', 'svg', 'ttf']

        self.load()

    def load(self):
        if not exists(self.path):
            raise InvalidPackageError(1, 'Path "invalid-path" is not valid. No openfont package could be loaded.', self.path)

        pkg_file_path = join(self.path, 'package.json')

        if not exists(pkg_file_path):
            msg = 'Path "%s" does not contain a package.json file. No openfont package could be loaded.' % self.path
            raise InvalidPackageError(2, msg, self.path)

        with open(pkg_file_path) as pkg_file:
            pkg = Package.load_from_json_string(pkg_file.read())

        self.package = pkg

        self.validate_package()

    def validate_package(self):
        for weight in self.package.weights:
            for font_format in self.valid_formats:
                filepath = join(self.path, "%s.%s" % (weight.filename, font_format))
                if not exists(filepath):
                    msg = 'Package at "%s" is broken. Missing %s weight file (%s.%s) for format %s.' % (
                        self.path,
                        weight.name,
                        weight.filename,
                        font_format,
                        font_format
                    )

                    raise BrokenPackageError(3, msg, self.path)
