def voting_eligibility(name, age, country):
    status = "Eligible to vote" if (
        age >= 18 and country.lower() == "india"
    ) or (
        age >= 21 and country.lower() != "india"
    ) else "Not eligible to vote"

    result = (
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Country: {country}\n"
        f"Status: {status}"
    )
    return result


if __name__ == "__main__":
    name = "soujanya"
    age = 25
    country = "India"

    print(voting_eligibility(name, age, country))