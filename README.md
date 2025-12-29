# pavement-homogenizer-lib

Python library for homogenization of pavement composites.

## Installation

```bash
pip install pavement-homogenizer-lib
```

Or clone the repository and install in development mode:

```bash
git clone https://github.com/racoock/pavement-homogenizer-lib
cd pavement-homogenizer-lib
pip install -e .
```

## Available Models

Currently implemented homogenization models:

- **Voigt model** (upper bound): rule of mixtures.
- **Reuss model** (lower bound): inverse rule of mixtures.

## Usage

```python
from models import voigt_effective_modulus, reuss_effective_modulus

matrix_modulus = 3.0  # GPa (asphalt binder)
inclusion_modulus = 30.0  # GPa (aggregate)
volume_fraction = 0.4  # 40% aggregate

voigt_result = voigt_effective_modulus(matrix_modulus, inclusion_modulus, volume_fraction)
reuss_result = reuss_effective_modulus(matrix_modulus, inclusion_modulus, volume_fraction)

print(f"Voigt effective modulus: {voigt_result:.2f} GPa")
print(f"Reuss effective modulus: {reuss_result:.2f} GPa")
```

## Testing

Run the test suite with pytest:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue to discuss proposed changes or submit a pull request.

## License

MIT