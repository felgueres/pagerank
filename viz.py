import graphviz
import os

def visualize_pagerank(links, scores, filename="pagerank_graph"):
    dot = graphviz.Digraph(comment='PageRank Graph')
    dot.attr(rankdir='TB', size='8,6')
    dot.attr('node', shape='circle', style='filled')
    min_score = min(scores.values())
    max_score = max(scores.values())
    score_range = max_score - min_score if max_score != min_score else 1
    for page, score in scores.items():
        normalized_score = (score - min_score) / score_range
        node_size = 0.5 + 1.5 * normalized_score
        dot.node(page, 
                label=f"{page}\\n{score:.2f}",
                width=str(node_size),
                height=str(node_size),
                fontsize="12",)
    
    for source, target in links:
        dot.edge(source, target, color='gray', arrowsize='0.8')
    
    try:
        dot.render(filename, format='png', cleanup=True)
        print(f"Graph saved as {filename}.png")
        os.system(f"open {filename}.png")
        
    except Exception as e:
        print(f"Error: {e}")
    
    return dot