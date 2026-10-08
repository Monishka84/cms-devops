def submit_complaint(title, description):
    return {
        "title": title,
        "description": description,
        "status": "pending"
    }

print("Complaint Management System")

complaint = submit_complaint(
    "Water Leakage",
    "There is water leakage in the college corridor."
)

print("Complaint:", complaint["title"])
print("Description:", complaint["description"])
print("Status:", complaint["status"])
