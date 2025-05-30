from pagerank import PageRank

links = [
    ("A", "B"),
    ("A", "C"), 
    ("B", "C"),
    ("C", "A"),
    ("B", "A")  # Added back-link to make it more interesting
]

print()
print("Graph links")
print("-" * 20)

for source, target in links:
    print(f"  {source} -> {target}")
    
pr = PageRank(damping_factor=0.85, tolerance=1e-6)
scores = pr.calculate_pagerank(links)
    
print("\nPageRank Scores:")
print("-" * 20)
    
sorted_pages = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for page, score in sorted_pages:
    print(f"{page}: {score:.6f}")

total_score = sum(scores.values())
print(f"\nTotal PageRank sum: {total_score:.1f}")
