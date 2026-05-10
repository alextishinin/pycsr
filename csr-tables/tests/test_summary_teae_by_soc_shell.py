from csr_tables.summary_teae_by_soc_shell import (
    create_summary_teae_by_soc_shell,
    write_summary_teae_by_soc_shell,
)


def test_summary_teae_by_soc_shell_structure() -> None:
    shell = create_summary_teae_by_soc_shell()

    assert shell.columns == ["row", "treatment_a", "treatment_b", "total"]
    assert shell.height == 15
    assert shell["row"][1] == (
        "Subjects with at Least One Treatment-Emergent Adverse Event"
    )
    assert shell["row"][3] == "System Organ Class #1"
    assert shell["row"][4] == "   Preferred Term #1.1"
    assert shell["row"][9] == "System Organ Class #2"
    assert shell["row"][14] == "..."
    assert shell["treatment_a"][1] == "xx (xx.x) xx"
    assert shell["total"][13] == "xx (xx.x) xx"


def test_write_summary_teae_by_soc_shell(tmp_path) -> None:
    output_path = tmp_path / "summary_teae_by_soc_shell.rtf"

    result = write_summary_teae_by_soc_shell(output_path)

    assert result == output_path
    assert output_path.exists()
    assert output_path.stat().st_size > 0
