from subject_disposition.subjdisp import create_subject_disposition_shell


def test_subject_disposition_shell_structure() -> None:
    shell = create_subject_disposition_shell()

    assert shell.columns == ["row", "treatment_a", "treatment_b", "total"]
    assert shell.height == 46
    assert shell["row"][1].startswith("Screened [1]")
    assert shell["row"][15] == "Randomized Population [1]"
    assert shell["total"][15] == "xx"
    assert shell["row"][44] == "   Other"
