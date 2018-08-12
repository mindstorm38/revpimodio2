# -*- coding: utf-8 -*-
"""Bildet die Summary-Sektion von piCtory ab."""
__author__ = "Sven Sager"
__copyright__ = "Copyright (C) 2018 Sven Sager"
__license__ = "LGPLv3"


class Summary(object):

    """Bildet die Summary-Sektion der config.rsc ab."""

    def __init__(self, summary):
        """Instantiiert die RevPiSummary-Klasse.
        @param summary piCtory Summaryinformationen"""
        self.inptotal = summary["inpTotal"]
        self.outtotal = summary["outTotal"]
