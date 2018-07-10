# is-valid-hashtag

> Check if a hashtag is valid

## Usage

Pick the appropriate script for your language, import it, and call `is_valid_hashtag(hashtag)` and check the boolean result. Checking is case-insensitive.

### Examples

```python
# Python, but all versions work the same way

from is_valid_hashtag import *

is_valid_hashtag("#HelloWorld")  # True
is_valid_hashtag("#Hello_World")  # True
is_valid_hashtag("#0day")  # True
is_valid_hashtag("#000")  # False
```

## Contributing

If you would like to contribute to this project, such as adding another language, feel free to do so!

### Currently available languages

* Python 3.6+
* JavaScript (ES6 module)
* PHP

## License

2018 Caleb Ely

[Unlicense](LICENSE)
