from vote import voting_eligibility

def test_eligible_india():
    expected_output = (
        "Name: Soujanya\n"
        "Age: 25\n"
        "Country: India\n"
        "Status: Eligible to vote"
    )
    assert voting_eligibility("Soujanya", 25, "India") == expected_output