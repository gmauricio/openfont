#!/usr/bin/python
# -*- coding: utf-8 -*-

# OpenFont - Font Packaging Format
# https://github.com/heynemann/openfont

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from pyvows import Vows, expect

from openfont.models import Package


@Vows.batch
class PackageVows(Vows.Context):

    class CanLoadFromJSON(Vows.Context):
        def topic(self):
            return Package.load_from_json_string("""{
    "metaVersion": "1.0",
    "name": "test1",
    "version": "1.1",

    "weights": {

    }
}""")

        def should_not_be_an_error(self, topic):
            expect(topic).not_to_be_an_error()
            expect(topic).not_to_be_null()

        def should_have_proper_name(self, topic):
            expect(topic.name).to_equal('test1')

        def should_have_proper_meta_version(self, topic):
            expect(topic.meta_version).to_equal('1.0')

        def should_have_proper_version(self, topic):
            expect(topic.version).to_equal('1.1')

        def should_have_no_weights(self, topic):
            expect(topic.weights).to_be_empty()

    class CanLoadweights(Vows.Context):
        def topic(self):
            return Package.load_from_json_string("""{
    "metaVersion": "1.0",
    "name": "SourceSansPro",
    "version": "1.1",

    "weights": {
        "Black": "SourceSansPro-Black-webfont",
        "Black It": "SourceSansPro-BlackIt-webfont",
        "Bold": "SourceSansPro-Bold-webfont",
        "Bold It": "SourceSansPro-BoldIt-webfont",
        "Extra Light": "SourceSansPro-ExtraLight-webfont",
        "Extra Light It": "SourceSansPro-ExtraLightIt-webfont",
        "Regular": "SourceSansPro-Regular-webfont",
        "Regular It": "SourceSansPro-It-webfont",
        "Light": "SourceSansPro-Light-webfont",
        "Light It": "SourceSansPro-LightIt-webfont",
        "Semibold": "SourceSansPro-Semibold-webfont",
        "Semibold It": "SourceSansPro-SemiboldIt-webfont"
    }
}""")

        def should_have_weights(self, topic):
            expect(topic.weights).to_length(12)
