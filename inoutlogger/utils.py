# -*- coding: utf-8 -*-
"""
    utils.py
    ~~~~~~~~~~~~~
    Author: Pankaj Suthar
"""

class Logger:
    def __init__(self, log_handler, name, entry_identifier=">>>>", exit_identifier="<<<<", log_time=False):
        self.log_handler = log_handler
        self.name = name
        self.entry_identifier = entry_identifier
        self.exit_identifier = exit_identifier
        self.log_time = log_time

    def __str__(self):
        return "Logger Name : {}".format(self.name)

class InOutLogger:

    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getResources():
        """ Static access method. """
        if InOutLogger.__instance is None:
            raise Exception("InOutLogger configuration is not defined. Initialize InOutLogger first.")
        return InOutLogger.__instance

    def __init__(self, LOGGERS, supress_warings = False):
        """
        LOGGERS: Dictinary of Loggers
        """
        if InOutLogger.__instance is not None:
            raise Exception("Already initailized the InOutLogger")
        else:
            if isinstance(LOGGERS, list):
                self.LOGGERS = LOGGERS
                InOutLogger.__instance = self
            elif isinstance(LOGGERS, Logger):
                self.LOGGERS = [LOGGERS]
                InOutLogger.__instance = self
            else:
                raise Exception("LOGGERS must be list of [ InOutLogger.Logger ]")

            self.supress_warings = supress_warings
        InOutLogger.__instance = self


