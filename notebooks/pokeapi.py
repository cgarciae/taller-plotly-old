#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x26264fca

# Compiled with Coconut version 1.2.2-post_dev3 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_tee, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

import requests
import json
import sys
import os
import errno
from IPython.display import Image
from IPython.display import display

BASE_API = "http://pokeapi.co/api/v2"

def _mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def render(pokemon):
    print("{}: #{}".format(pokemon["name"], pokemon["id"]))
    display(Image(pokemon["sprites"]["front_default"]))

class _Record(dict):

    def __init__(self, *args, **kwargs):
        super(_Record, self).__init__(*args, **kwargs)

        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = _Record(value)
            elif isinstance(value, list):
                self[key] = [_Record(elem) for elem in value if isinstance(elem, dict)]

    def __getattr__(self, attr):
        return self[attr]

    def load(self):
        return ((_Record)((_coconut.operator.methodcaller("json"))((requests.get)(self.url))))

class Pokemon(dict):
    """docstring for Pokemon."""

    API = BASE_API + "/pokemon"

    @classmethod
    def catch_on_internet(cls, id):
        return ((Pokemon)((_coconut.operator.methodcaller("json"))((requests.get)("{api}/{id}".format(api=Pokemon.API, id=id)))))

    @classmethod
    def catch(cls, id):
        local_path = "pokemons/{}.json".format(id)

        if os.path.isfile(local_path):
            with open(local_path, 'r') as f :
                return Pokemon(json.load(f))
        else:
            pkm = Pokemon.catch_on_internet(id)

            return pkm


class Species(_Record):
    """docstring for Pokemon."""

    API = BASE_API + "/pokemon-species"

    @classmethod
    def get(cls, id):
        return ((Pokemon)((_coconut.operator.methodcaller("json"))((requests.get)("{api}/{id}".format(api=Pokemon.API, id=id)))))
