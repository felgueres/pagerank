import graphviz
import os

def visualize_pagerank(links, scores, filename="pagerank_graph"):
    dot = graphviz.Digraph(comment='PageRank Graph')
    dot.attr(rankdir='TB', size='8,8', dpi='400')
    dot.attr('node', shape='circle', style='filled', fontname='Arial')
    dot.attr('edge', fontname='Arial')
    min_score = min(scores.values())
    max_score = max(scores.values())
    score_range = max_score - min_score if max_score != min_score else 1
    
    for page, score in scores.items():
        normalized_score = (score - min_score) / score_range
        node_size = 1.0 + 2.0 * normalized_score
        dot.node(page, 
                label=f"{page}\\n{score:.3f}",
                width=str(node_size),
                height=str(node_size),
                fillcolor="black",
                fontcolor="white",
                fontsize="14",
                penwidth="2")
    
    for source, target in links:
        dot.edge(source, target, 
                color='darkgray', 
                arrowsize='1.0',
                penwidth="1.5")
    
    try:
        dot.render(filename, format='png', cleanup=True)
        print(f"Graph saved as {filename}.png")
        os.system(f"open {filename}.png")
        
    except Exception as e:
        print(f"Error: {e}")
    
    return dot