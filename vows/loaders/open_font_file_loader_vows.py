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
            expect(topic.package).not_to_be_null()
            expect(topic.package.name).to_equal('first')
            expect(topic.package.meta_version).to_equal('1.0')
            expect(topic.package.version).to_equal('2.0')

        class HasProperWeights(Vows.Context):
            def topic(self, topic):
                return topic.package

            def should_have_twelve_weights(self, topic):
                expect(topic.weights).to_length(12)

    class WhenInvalidPathPackage(Vows.Context):
        def topic(self):
            return OpenFontFileLoader("invalid-path")

        def should_be_an_error(self, topic):
            expect(topic).to_be_an_error()
            expect(topic).to_be_an_error_like(openfont.errors.InvalidPackageError)
            expect(topic.errno).to_equal(1)
            expect(topic.strerror).to_equal('Path "invalid-path" is not valid. No openfont package could be loaded.')
            expect(topic.filename).to_equal('invalid-path')

    class WhenValidPathButNoPackageFile(Vows.Context):
        def topic(self):
            return OpenFontFileLoader(fixture('no-package-file'))

        def should_be_an_error(self, topic):
            expect(topic).to_be_an_error()
            expect(topic).to_be_an_error_like(openfont.errors.InvalidPackageError)
            expect(topic.errno).to_equal(2)
            fixture_path = fixture('no-package-file')
            msg = 'Path "%s" does not contain a package.json file. No openfont package could be loaded.' % fixture_path
            expect(topic.strerror).to_equal(msg)
            expect(topic.filename).to_equal(fixture_path)

    class WhenValidPathButMissingFonts(Vows.Context):
        def topic(self):
            errored = 0
            valid_formats = ['woff', 'eot', 'svg', 'ttf']
            for font_format in valid_formats:
                try:
                    OpenFontFileLoader(fixture('missing-fonts-%s' % font_format))
                except Exception, err:
                    errored += 1
                    yield (font_format, err)

            if errored != len(valid_formats):
                raise RuntimeError("Should have errored %d times" % len(valid_formats))

        def should_be_an_error(self, (font_format, topic)):
            expect(topic).to_be_an_error()
            expect(topic).to_be_an_error_like(openfont.errors.BrokenPackageError)
            expect(topic.errno).to_equal(3)
            fixture_path = fixture('missing-fonts-%s' % font_format)
            msg = u'Package at "%s" is broken. Missing Black weight file (SourceSansPro-Black-webfont.%s) for format %s.' % (
                fixture_path,
                font_format,
                font_format
            )
            expect(topic.strerror).to_equal(msg)
            expect(topic.filename).to_equal(fixture_path)
