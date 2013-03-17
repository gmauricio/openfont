#!/usr/bin/python
# -*- coding: utf-8 -*-

# OpenFont - Font Packaging Format
# https://github.com/heynemann/openfont

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from pyvows import Vows, expect

from openfont import OpenFontFileLoader
import openfont.errors
from vows.helpers import fixture


@Vows.batch
class OpenFontFileLoaderVows(Vows.Context):

    class WhenProperPackage(Vows.Context):
        def topic(self):
            return OpenFontFileLoader(fixture("first"))

        def should_not_be_an_error(self, topic):
            expect(topic).not_to_be_an_error()
            expect(topic).not_to_be_null()

        def should_have_proper_font_name(self, topic):
            expect(topic.font_name).to_equal('first')

    class WhenInvalidPathPackage(Vows.Context):
        def topic(self):
            return OpenFontFileLoader("invalid-path")

        def should_be_an_error(self, topic):
            expect(topic).to_be_an_error()
            expect(topic).to_be_an_error_like(openfont.errors.InvalidPackageError)
            expect(topic.errno).to_equal(1)
            expect(topic.strerror).to_equal('Path "invalid-path" is not valid. No openfont package could be loaded.')
            expect(topic.filename).to_equal('invalid-path')
