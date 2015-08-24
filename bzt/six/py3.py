"""
Module for reporting into http://www.blazemeter.com/ service

Copyright 2015 BlazeMeter Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# pylint: skip-file
import io
import operator
import collections
import urllib
from io import IOBase

import urllib.error
import urllib.request
import urllib.parse
import tkinter
import configparser
from tkinter import font
from http import server
import socketserver
import tempfile

string_types = str,
integer_types = int,
class_types = type,
text_type = str
binary_type = bytes
file_type = IOBase

configparser = configparser
tkinter = tkinter
tkfont = font
UserDict = collections.UserDict

StringIO = io.StringIO
BytesIO = io.BytesIO

request = urllib.request
parse = urllib.parse
urlopen = request.urlopen
urlencode = parse.urlencode
build_opener = request.build_opener
install_opener = request.install_opener
ProxyHandler = request.ProxyHandler
Request = request.Request
HTTPError = urllib.error.HTTPError
BaseHTTPServer = server
socketserver = socketserver
SimpleHTTPRequestHandler = BaseHTTPServer.SimpleHTTPRequestHandler

viewvalues = operator.methodcaller("values")


def iteritems(dictionary, **kw):
    return iter(dictionary.items(**kw))


def b(string):
    return string.encode("latin-1")


def u(string):
    return string
