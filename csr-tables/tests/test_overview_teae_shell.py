from csr_tables.overview_teae_shell import (
    create_overview_teae_shell,
    write_overview_teae_shell,
)


def test_overview_teae_shell_structure() -> None:
    shell = create_overview_teae_shell()

    assert shell.columns == ["row", "treatment_a", "treatment_b", "total"]
    assert shell.height == 25
    assert shell["row"][1] == "Any Treatment-Emergent Adverse Events (TEAE)"
    assert shell["row"][6] == "Any Serious TEAE"
    assert shell["row"][10] == "      Congenital Anomaly or Birth Defect"
    assert shell["row"][15] == "Any TEAE Leading to Dose Modification of Study Drug"
    assert shell["row"][23] == "Any Fatal TEAE"
    assert shell["treatment_a"][1] == "xx (xx.x) xx"
    assert shell["total"][23] == "xx (xx.x) xx"


def test_write_overview_teae_shell(tmp_path) -> None:
    output_path = tmp_path / "overview_teae_shell.rtf"

    result = write_overview_teae_shell(output_path)

    assert result == output_path
    assert output_path.exists()
    assert output_path.stat().st_size > 0
