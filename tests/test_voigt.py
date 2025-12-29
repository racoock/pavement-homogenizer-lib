"""
Test Voigt homogenization model.
"""
import sys
sys.path.insert(0, 'src')
from models.voigt import effective_modulus

def test_voigt_effective_modulus():
    """Test Voigt rule of mixtures."""
    # Case 1: pure matrix
    assert effective_modulus(10.0, 100.0, 0.0) == 10.0
    # Case 2: pure inclusion
    assert effective_modulus(10.0, 100.0, 1.0) == 100.0
    # Case 3: 50% volume fraction
    assert effective_modulus(10.0, 100.0, 0.5) == 55.0
    # Case 4: floating point
    result = effective_modulus(2.5, 7.5, 0.3)
    expected = (1 - 0.3) * 2.5 + 0.3 * 7.5
    assert abs(result - expected) < 1e-12