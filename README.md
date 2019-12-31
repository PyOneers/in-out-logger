# InOutLogger

Decorator based utility to implement Entry-Exit logs for methods

## Getting Started

### Prerequisites

```
python>=3.6
```

### Installing

```
pip install inoutlogger
```

### A Simple Example

```
from inoutlogger.utils import InOutLogger, Logger
from inoutlogger.decorators import entry_exit_log

# With Single Logger
LOGGER # Your Application Logger
logger1 = Logger(log_handler ="LOGGER",  name="application_logger")

InOutLogger(logger1)

@in_out_log
def test():
  print("Demo Single log handler")
  
# With Multiple Logger
LOGGER1 # Your Application Logger
LOGGER2 # Other Logger
logger1 = Logger(log_handler ="LOGGER1",  name="application_logger")
logger2 = Logger(log_handler ="LOGGER2",  name="Other")

InOutLogger([logger1, logger2])

@in_out_log
def test(handler_name="Other"):
  print("Demo Multiple log handler")
  
```



## Authors

* **Pankaj Suthar** - *Initial work* - [PankajSuthar](https://github.com/PanksSuthar)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](https://github.com/PanksSuthar/InOutLogger/blob/master/LICENSE) file for details
