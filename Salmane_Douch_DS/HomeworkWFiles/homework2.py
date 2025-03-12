def clean_data(input_filename, output_filename):
    with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
        next(infile)  # Skip header line
        for line in infile:
            parts = line.strip().split(",")
            if len(parts) < 5:
                print(f"Skipped malformed lines: {line.strip()}")
                continue
            try:
                rank = parts[0].strip()
                company = parts[1].strip()
                revenue = float(parts[2].strip())
                employees = int(parts[3].strip())
                country = parts[4].strip()
                outfile.write(f"{rank}>{company}>{revenue}>{employees}>{country}\n")
            except ValueError:
                print(f"Skipping invalid data: {line.strip()}")

def load_data(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(">")
            if len(parts) < 5:
                print(f"Skipping invalid data: {line.strip()}")
                continue
            try:
                data.append({
                    "rank": int(parts[0]),
                    "company": parts[1],
                    "revenue": float(parts[2]),
                    "employees": int(parts[3]),
                    "country": parts[4]
                })
            except ValueError:
                print(f"Skipping invalid data: {line.strip()}")
    return data

def print_clean_data(data):
    for entry in data:
        print(f"{entry['rank']} {entry['company']} | {entry['revenue']}B | {entry['employees']} employees | {entry['country']}")

def update_revenue(data, company_name, new_revenue):
    try:
        new_revenue = float(new_revenue)
        closest_matches = []
        for entry in data:
            if entry["company"].lower() == company_name.lower():
                entry["revenue"] = new_revenue
                print(f"Updated {company_name} revenue to {new_revenue} B")
                return True
            if company_name.lower() in entry['company'].lower():
                closest_matches.append(entry["company"])

        if closest_matches:
            print(f"Company not found. Did you mean: {', '.join(closest_matches)}?")
        else:
            print("Company not found.")

    except ValueError:
        print("Invalid revenue value. Please enter a valid number.")

    return False

def bubble_sort(data):
    n = len(data)
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j]["company"] > data[j+1]["company"]:
                data[j], data[j+1] = data[j+1], data[j]

def selection_sort(data, key="employees"):
    if not all(key in entry for entry in data):
        print(f"Invalid key: '{key}'. Sorting by default key 'employees'.")
        key = "employees"

    n = len(data)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if data[j][key] < data[min_index][key]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

def search_for_company(data, company_name):
    for entry in data:
        if entry["company"].lower() == company_name.lower():
            return entry
    return None

def top_3_companies(data):
    sorted_data = sorted(data, key=lambda x: x["revenue"], reverse=True)
    print("The top three companies by revenue:")
    for i in range(min(3, len(sorted_data))):
        print(f"{i+1}. {sorted_data[i]['company']} - {sorted_data[i]['revenue']}B")
