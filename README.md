# InOutLogger

Decorator based utility to implement Entry-Exit logs for methods

## Getting Started

### Prerequisites

```python
python>=3.6
```

### Installing

```bash
pip install inoutlogger
```

### A Simple Example

```python
from inoutlogger.utils import InOutLogger, Logger
from inoutlogger.decorators import entry_exit_log

# With Single Logger
LOGGER # Your Application Logger
logger1 = Logger(log_handler =LOGGER,  name="application_logger")

InOutLogger(logger1)

@in_out_log()
def test():
  print("Demo Single log handler")
  
test() # See Log file for output

# With Multiple Logger
LOGGER1 # Your Application Logger
LOGGER2 # Other Logger
logger1 = Logger(log_handler =LOGGER1,  name="application_logger")
logger2 = Logger(log_handler =LOGGER2,  name="Other")

InOutLogger([logger1, logger2])

@in_out_log(handler_name="Other")
def test():
  print("Demo Multiple log handler")
  
test() # See Log file for output  
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/PyOneers/in-out-logger/blob/master/LICENSE) file for details
