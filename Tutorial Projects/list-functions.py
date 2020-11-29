numbers = [4, 8, 15, 16, 23, 42]
companies = ["Google", "Youtube", "Microsoft", "Apple", "AMD", "Intel", "Aram Services", "Giraffe Academy",
             "Marhaba & Co.", "HOP Partner Network"]
companies[0] = "Google G-Suite"
companies.insert(1, "Hewlett Packard")
companies.append("JetBrains")
companies.extend(numbers)
print(companies)
