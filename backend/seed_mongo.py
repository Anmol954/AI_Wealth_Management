from pymongo import MongoClient

uri = "mongodb+srv://anmolmadhav2004:S%40ndw1ch@cluster0.tjovtzu.mongodb.net/portfolio-db?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["portfolio-db"]
collection = db["clients"]

# Clear existing data first
collection.delete_many({})
print("Cleared existing data.")

documents = [
    # C001-C010 (matching MySQL transactions data)
    {"client_id": "C001", "name": "Arjun Kapoor",        "address": "Mumbai",           "risk_appetite": "high",   "investment_preferences": ["Equity", "Stocks"],          "relationship_manager": "Ashima Sharma"},
    {"client_id": "C002", "name": "Priya Sharma",        "address": "Delhi",            "risk_appetite": "medium", "investment_preferences": ["Mutual Funds", "SIP"],       "relationship_manager": "Ravi Kapoor"},
    {"client_id": "C003", "name": "Rohit Verma",         "address": "Bangalore",        "risk_appetite": "high",   "investment_preferences": ["Stocks", "Crypto"],          "relationship_manager": "Ashima Sharma"},
    {"client_id": "C004", "name": "Sneha Gupta",         "address": "Hyderabad",        "risk_appetite": "low",    "investment_preferences": ["FD", "Savings"],             "relationship_manager": "Sneha Roy"},
    {"client_id": "C005", "name": "Vikas Mehta",         "address": "Chennai",          "risk_appetite": "high",   "investment_preferences": ["Equity", "Startups"],        "relationship_manager": "Ravi Kapoor"},
    {"client_id": "C006", "name": "Kavya Nair",          "address": "Pune",             "risk_appetite": "medium", "investment_preferences": ["Gold", "Mutual Funds"],      "relationship_manager": "Ashima Sharma"},
    {"client_id": "C007", "name": "Sameer Khan",         "address": "Kolkata",          "risk_appetite": "low",    "investment_preferences": ["Govt Bonds", "PPF"],         "relationship_manager": "Sneha Roy"},
    {"client_id": "C008", "name": "Deepika Rao",         "address": "Ahmedabad",        "risk_appetite": "high",   "investment_preferences": ["Crypto", "Stocks"],          "relationship_manager": "Ravi Kapoor"},
    {"client_id": "C009", "name": "Ankit Joshi",         "address": "Jaipur",           "risk_appetite": "medium", "investment_preferences": ["SIP", "REITs"],              "relationship_manager": "Ashima Sharma"},
    {"client_id": "C010", "name": "Meera Pillai",        "address": "Kochi",            "risk_appetite": "low",    "investment_preferences": ["FD", "Savings"],             "relationship_manager": "Sneha Roy"},
    # C011-C030 (from original data.py)
    {"client_id": "C011", "name": "Rohit Mehra",         "address": "Chandigarh",       "risk_appetite": "medium", "investment_preferences": ["Mutual Funds", "REITs"],     "relationship_manager": "Aisha Gupta"},
    {"client_id": "C012", "name": "Priya Sinha",         "address": "Bhopal",           "risk_appetite": "low",    "investment_preferences": ["PPF", "FD"],                 "relationship_manager": "Sneha Roy"},
    {"client_id": "C013", "name": "Kunal Verma",         "address": "Nagpur",           "risk_appetite": "high",   "investment_preferences": ["Crypto", "Stocks"],          "relationship_manager": "Ravi Kapoor"},
    {"client_id": "C014", "name": "Neha Rathi",          "address": "Surat",            "risk_appetite": "medium", "investment_preferences": ["Gold", "SIPs"],              "relationship_manager": "Aisha Gupta"},
    {"client_id": "C015", "name": "Manoj Nair",          "address": "Thiruvananthapuram","risk_appetite": "low",   "investment_preferences": ["Savings", "Govt Bonds"],     "relationship_manager": "Sneha Roy"},
    {"client_id": "C016", "name": "Divya Aggarwal",      "address": "Lucknow",          "risk_appetite": "high",   "investment_preferences": ["Startups", "Crypto"],        "relationship_manager": "Ravi Kapoor"},
    {"client_id": "C017", "name": "Aditya Malhotra",     "address": "Guwahati",         "risk_appetite": "medium", "investment_preferences": ["SIP", "Mutual Funds"],       "relationship_manager": "Aisha Gupta"},
    {"client_id": "C018", "name": "Meera Iyer",          "address": "Chennai",          "risk_appetite": "low",    "investment_preferences": ["FD", "Savings"],             "relationship_manager": "Sneha Roy"},
    {"client_id": "C019", "name": "Tanishq Arora",       "address": "Jaipur",           "risk_appetite": "high",   "investment_preferences": ["Stocks", "Equity"],          "relationship_manager": "Ravi Kapoor"},
    {"client_id": "C020", "name": "Riya Das",            "address": "Bhubaneswar",      "risk_appetite": "medium", "investment_preferences": ["REITs", "Gold"],             "relationship_manager": "Aisha Gupta"},
    {"client_id": "C021", "name": "Amit Trivedi",        "address": "Rajkot",           "risk_appetite": "low",    "investment_preferences": ["PPF", "FD"],                 "relationship_manager": "Sneha Roy"},
    {"client_id": "C022", "name": "Sneha Kulkarni",      "address": "Aurangabad",       "risk_appetite": "high",   "investment_preferences": ["Crypto", "Startups"],        "relationship_manager": "Ravi Kapoor"},
    {"client_id": "C023", "name": "Zoya Khan",           "address": "Patna",            "risk_appetite": "medium", "investment_preferences": ["Mutual Funds", "Gold"],      "relationship_manager": "Aisha Gupta"},
    {"client_id": "C024", "name": "Nikhil Bansal",       "address": "Udaipur",          "risk_appetite": "low",    "investment_preferences": ["Govt Bonds", "FD"],          "relationship_manager": "Sneha Roy"},
    {"client_id": "C025", "name": "Ananya Reddy",        "address": "Vijayawada",       "risk_appetite": "high",   "investment_preferences": ["Stocks", "Equity"],          "relationship_manager": "Ravi Kapoor"},
    {"client_id": "C026", "name": "Harshita Sen",        "address": "Agra",             "risk_appetite": "medium", "investment_preferences": ["SIP", "REITs"],              "relationship_manager": "Aisha Gupta"},
    {"client_id": "C027", "name": "Saurav Pandey",       "address": "Varanasi",         "risk_appetite": "low",    "investment_preferences": ["PPF", "Savings"],            "relationship_manager": "Sneha Roy"},
    {"client_id": "C028", "name": "Ishaan Bhatt",        "address": "Amritsar",         "risk_appetite": "high",   "investment_preferences": ["Crypto", "Startups"],        "relationship_manager": "Ravi Kapoor"},
    {"client_id": "C029", "name": "Kritika Shah",        "address": "Coimbatore",       "risk_appetite": "medium", "investment_preferences": ["Mutual Funds", "Gold"],      "relationship_manager": "Aisha Gupta"},
    {"client_id": "C030", "name": "Dev Mehta",           "address": "Mysore",           "risk_appetite": "low",    "investment_preferences": ["FD", "Savings"],             "relationship_manager": "Sneha Roy"},
]

result = collection.insert_many(documents)
print(f"✅ Successfully inserted {len(result.inserted_ids)} documents into 'clients' collection.")
print(f"Total documents now: {collection.count_documents({})}")
print("\nSample document:")
print(collection.find_one({"client_id": "C001"}, {"_id": 0}))
