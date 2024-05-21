print("Election Results \n")

constituencyNames = {
        "C": "Conservative",
        "L": "Labour",
        "UKIP": "UKIP",
        "LD": "Liberal Democrats",
        "G": "Green Party",
        "Ind": "Independent",
        "SNP": "SNP"
    }

"""results = open("sample_results.txt", "r")
listOfResults = []

for x in results:
    listOfResults.append([x.strip()])

for i in listOfResults:
    print(i)"""

with open("sample_results.txt", "r") as filestream:
    lines = filestream.readlines()

print(lines)

print("\n")

for line in lines:
    parts = line.split(",")
    print(parts)
    constituency_name = parts[0]

    print(constituency_name)

    totalVotes = 0
    party_votes = []

    for i in range(1, len(parts),2):
        party_code = parts[i].strip()
        votes = parts[i+1].strip()
        totalVotes = totalVotes + votes
        party_votes.append((party_code, votes))

    print(f"\nConstituency: {constituency_name}")
    for party_code, votes in party_votes:
        party_name = constituencyNames.get(party_code, party_code)
        vote_share = (votes / totalVotes) * 100
        print(f"{party_name}: {vote_share:.2f}%")




"""    for item in x.split(","):
        if item.isdigit():
            listOfResults.append(int(item))
        else:
            listOfResults.append(item)"""
