# -*- coding: utf-8 -*-
"""
    decorators.py
    ~~~~~~~~~~~~~~~~~~~~~
    Author : Pankaj Suthar
"""
import datetime
from .utils import InOutLogger


def in_out_log(*args, **kwargs):
    # Name of Log Handler
    handler_name = None
    if "handler_name" in kwargs.keys():
        handler_name = kwargs["handler_name"]

    def decorator(func):
        def inner(*args, **kwargs):
            log_handler, entry_identifier, exit_identifier, log_time = None, None, None, False
            pass_handeler_name_check = False            
            # Get Log Handlers
            handlers = InOutLogger.getResources().LOGGERS
            if handler_name is None and len(handlers) > 1:
                raise Exception(
                        "Multiple Logger(inoutlogger.utils.Logger) found. Specify handler_name in decorator arguments to select which logger to be used")
            elif handler_name is None and len(handlers) == 1:
                pass_handeler_name_check = True

            for hndlr in handlers:
                if pass_handeler_name_check:
                    log_handler = hndlr.log_handler
                    entry_identifier = hndlr.entry_identifier
                    exit_identifier = hndlr.exit_identifier
                    log_time = hndlr.log_time

                elif hndlr.name == handler_name:
                    log_handler = hndlr.log_handler
                    entry_identifier = hndlr.entry_identifier
                    exit_identifier = hndlr.exit_identifier
                    log_time = hndlr.log_time

            if log_handler is None:
                raise Exception("No Logger(inoutlogger.utils.Logger)  found with name [ {} ]".format(handler_name))
            # Entry
            start_time = datetime.datetime.now()
            start_time_microsec = datetime.datetime.now().microsecond
            log_handler.info(
                    "{} Entered [ {} ] method with args [ {} ] and kwargs [ {} ] at [ {} ] time".format(
                            entry_identifier,
                            func.__name__,
                            args,
                            kwargs,
                            str(start_time)))

            # Executing Method
            return_value = func(*args, **kwargs)

            # End Method
            end_time = datetime.datetime.now()
            end_time_microsec = datetime.datetime.now().microsecond

            # Log execution time
            if log_time:
                log_handler.info(
                        "Time taken to execute method is [ {} ]".format(str(end_time_microsec - start_time_microsec)))

            # Exit
            log_handler.info(
                    "{} Exited [ {} ] method with return value [ {} ] at [ {} ] time".format(
                            exit_identifier,
                            func.__name__,
                            return_value,
                            str(end_time)))

            return return_value

        return inner

    return decorator
