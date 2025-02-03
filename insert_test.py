import os
from supabase import create_client

# Fetch credentials from environment variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
client = create_client(url, key)

# Attempt to insert a row into a test table called "test3"
response = client.table("test3").insert({"name": "Example"}).execute()
print("Initial insert response:", response.data)

# If the insert returned empty data, try a select query
if not response.data:
    response = client.table("test3").select("*").eq("name", "Example").execute()
    print("Select response after insert:", response.data)

