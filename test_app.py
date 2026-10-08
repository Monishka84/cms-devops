from app import submit_complaint

def test_submit_complaint():
    complaint = submit_complaint(
        "Water Leakage",
        "There is water leakage in the college corridor."
    )

    assert complaint["title"] == "Water leakage"
    assert complaint["description"] == "There is water leakage in the college corridor."
    assert complaint["status"] == "pending"
