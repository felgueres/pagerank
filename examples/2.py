from pagerank import PageRank
import viz

links = [
    ("Home", "Products"),
    ("Home", "About"),
    ("Home", "Blog"),
    ("Products", "Product1"),
    ("Products", "Product2"),
    ("Products", "Home"),  # Back to home
    ("Product1", "Product2"),
    ("Product2", "Product1"),
    ("Product1", "Home"),
    ("About", "Home"),
    ("About", "Contact"),
    ("Blog", "BlogPost1"),
    ("Blog", "BlogPost2"),
    ("Blog", "Home"),
    ("BlogPost1", "BlogPost2"),
    ("BlogPost1", "Products"),  # Blog mentions products
    ("BlogPost1", "Home"),
    ("BlogPost2", "BlogPost1"),
    ("BlogPost2", "About"),
    ("BlogPost2", "Contact"),
    ("Contact", "Home"),
    ("Contact", "About"),
    ("Authority", "Home"),
    ("Authority", "Products"),
]

print("Graph links")
print("-" * 20 + "\n")

for source, target in links:
    print(f"  {source} -> {target}")
    
pr = PageRank(damping_factor=0.85, tolerance=1e-3)
scores = pr.calculate(links)
    
print("\nPageRank Scores:")
print("-" * 20)
    
sorted_pages = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for page, score in sorted_pages:
    print(f"{page}: {score:.6f}")

total_score = sum(scores.values())
print(f"\nTotal PageRank sum: {total_score:.1f}")

viz.visualize_pagerank(links, scores, "pagerank_example")