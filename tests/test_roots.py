from gan_nomenclature.generator import combine_roots, join_two_roots


def test_join_two_roots_protected_suffix():
    assert join_two_roots("micro", "aero") == "microaero"


def test_join_two_roots_vowel_collision():
    assert join_two_roots("hydro", "aero") == "hydraero"


def test_combine_roots_capitalisation():
    assert combine_roots(("micro", "spora")) == "Microspora"
