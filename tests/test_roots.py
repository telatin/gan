import pytest

from gan_nomenclature.generator import combine_roots, join_two_roots


def test_join_two_roots_protected_suffix():
    assert join_two_roots("micro", "aero") == "microaero"


def test_join_two_roots_vowel_collision():
    assert join_two_roots("hydro", "aero") == "hydraero"


def test_combine_roots_capitalisation():
    assert combine_roots(("micro", "spora")) == "Microspora"


# Additional edge case tests
def test_join_two_roots_no_vowel_collision():
    """Test joining roots where no vowels collide."""
    assert join_two_roots("lacto", "bacillus") == "lactobacillus"


def test_join_two_roots_consonant_ending():
    """Test joining roots ending with consonants."""
    assert join_two_roots("strept", "coccus") == "streptcoccus"


def test_join_two_roots_all_protected_suffixes():
    """Test all protected suffixes don't trigger vowel elision."""
    protected = ["bio", "geo", "neo", "mega", "micro", "allo", "amphi",
                 "extra", "hetero", "iso", "iuxta", "meso", "peri", "quasi", "ultra"]
    for suffix in protected:
        result = join_two_roots(suffix, "organism")
        assert result == suffix + "organism", f"Failed for {suffix}"


def test_join_two_roots_with_digits():
    """Test that digits are stripped from roots."""
    assert join_two_roots("hydro1", "aero2") == "hydraero"
    assert join_two_roots("micro3", "bio4") == "microbio"


def test_join_two_roots_empty_strings():
    """Test handling of empty strings."""
    assert join_two_roots("", "aero") == "aero"
    assert join_two_roots("hydro", "") == "hydro"
    assert join_two_roots("", "") == ""


def test_join_two_roots_single_vowel():
    """Test joining single vowel roots."""
    assert join_two_roots("a", "e") == "e"
    assert join_two_roots("o", "i") == "i"


def test_combine_roots_two_roots():
    """Test combining exactly two roots."""
    assert combine_roots(("lacto", "cola")) == "Lactocola"


def test_combine_roots_three_roots():
    """Test combining three roots."""
    assert combine_roots(("hydro", "geo", "bacter")) == "Hydrogeobacter"


def test_combine_roots_with_vowel_elision():
    """Test root combination with multiple vowel elisions."""
    assert combine_roots(("aero", "endo", "opsis")) == "Aerendopsis"


def test_combine_roots_empty_list():
    """Test that empty list raises ValueError."""
    with pytest.raises(ValueError, match="No roots provided"):
        combine_roots([])
