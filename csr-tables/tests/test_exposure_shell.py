from csr_tables.exposure_shell import create_exposure_shell, write_exposure_shell


def test_exposure_shell_structure() -> None:
    shell = create_exposure_shell()

    assert shell.columns == ["row", "treatment_a", "treatment_b", "total"]
    assert shell.height == 25
    assert shell["row"][1] == (
        "Duration of Exposure During the Randomized Treatment Period (unit)"
    )
    assert shell["row"][4] == (
        "Duration of Exposure During the Randomized Treatment Period, n (%)"
    )
    assert shell["row"][10] == "Total Amount of Dose Received (unit)"
    assert shell["row"][13] == "Total Number of Dose/Injection Received, n (%)"
    assert shell["row"][19] == (
        "Exposure Gap Due to Interruption < applicable if defined in SAP >"
    )
    assert shell["treatment_a"][2] == "xx"
    assert shell["total"][14] == "xx (xx.x)"


def test_write_exposure_shell(tmp_path) -> None:
    output_path = tmp_path / "exposure_shell.rtf"

    result = write_exposure_shell(output_path)

    assert result == output_path
    assert output_path.exists()
    assert output_path.stat().st_size > 0
