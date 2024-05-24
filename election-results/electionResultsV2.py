party_names = {
    "C": "Conservative",
    "L": "Labour",
    "UKIP": "UKIP",
    "LD": "Liberal Democrats",
    "G": "Green Party",
    "Ind": "Independent",
    "SNP": "SNP"
}

file_path = "sample_results.txt"


def process_results(nameOfFile):
    with open(nameOfFile, "r") as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split(',')
        constituency_name = parts[0].strip()

        # Initialize total votes and store party votes
        total_votes = 0
        party_votes = []

        print(parts)

        try:
            for i in range(1, len(parts), 2):
                party_code = parts[i + 1].strip()  # Swap the indices to get the correct elements
                votes = int(float(parts[i].strip()))  # Correctly parse the votes first
                total_votes += votes
                party_votes.append((party_code, votes))
        except ValueError as e:
            print("Error with formatting")
            print(e)

        # Print the results
        print(f"\nConstituency: {constituency_name}")
        for party_code, votes in party_votes:
            party_name = party_names.get(party_code, party_code)
            vote_share = (votes / total_votes) * 100
            print(f"{party_name}: {vote_share:.2f}%")


process_results(file_path)
