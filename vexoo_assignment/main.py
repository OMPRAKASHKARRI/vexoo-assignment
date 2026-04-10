from ingestion import sliding_window, KnowledgeBase
from retrieval import format_output
from router import route_query

# Sample document
text = """
Artificial Intelligence systems process large documents.
Sliding window techniques help retain context.
Knowledge pyramids organize raw text into structured insights.
Errors in data pipelines can affect model performance.
"""

# Step 1: Chunking
chunks = sliding_window(text)

# Step 2: Build Knowledge Base
kb = KnowledgeBase()
kb.add_documents(chunks)

# Step 3: Query
query = input("Enter your query: ")

# Step 4: Routing
route = route_query(query)
print(f"\n[Router] Query routed to: {route}")

# Step 5: Retrieval
result = kb.search(query)

# Step 6: Output
output = format_output(result)

print("\n🔍 Result:")
print("Summary:", output["summary"])
print("Category:", output["category"])
print("Keywords:", output["keywords"])