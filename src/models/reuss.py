"""
Reuss homogenization model (inverse rule of mixtures).
"""

def effective_modulus(matrix_modulus, inclusion_modulus, volume_fraction):
    """
    Calculate effective elastic modulus using Reuss model (lower bound).
    
    Parameters
    ----------
    matrix_modulus : float
        Elastic modulus of matrix material.
    inclusion_modulus : float
        Elastic modulus of inclusion material.
    volume_fraction : float
        Volume fraction of inclusions (0 <= volume_fraction <= 1).
    
    Returns
    -------
    float
        Effective elastic modulus.
    """
    if volume_fraction == 0:
        return matrix_modulus
    if volume_fraction == 1:
        return inclusion_modulus
    return 1 / ((1 - volume_fraction) / matrix_modulus + volume_fraction / inclusion_modulus)