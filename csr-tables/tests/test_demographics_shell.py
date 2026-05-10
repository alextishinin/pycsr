from csr_tables.demographics_shell import (
    create_demographics_shell,
    write_demographics_shell,
)


def test_demographics_shell_structure() -> None:
    shell = create_demographics_shell()

    assert shell.columns == ["row", "treatment_a", "treatment_b", "total"]
    assert shell.height == 59
    assert shell["row"][1] == "Age (years)"
    assert shell["row"][14] == "Sex, n (%)"
    assert shell["row"][18] == "Race, n (%)"
    assert shell["row"][53] == "Body Mass Index (kg/m2)"
    assert shell["treatment_a"][15] == "xx (xx.x)"
    assert shell["total"][48] == "xx"


def test_write_demographics_shell(tmp_path) -> None:
    output_path = tmp_path / "demographics_shell.rtf"

    result = write_demographics_shell(output_path)

    assert result == output_path
    assert output_path.exists()
    assert output_path.stat().st_size > 0
