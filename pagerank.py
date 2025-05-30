from typing import Dict, List, Tuple
import numpy as np

class PageRank:
    """Models a random surfer that either:
    1. Follows a random outbound link with probability 'damping_factor'
    2. Jumps to a random page with probability '1 - damping_factor'
    """
    
    def __init__(self, damping_factor: float = 0.85, tolerance: float = 1e-6, max_iterations: int = 100):
        """
        damping_factor: Probability of following links (typically 0.85)
        tolerance: Convergence threshold
        max_iterations: Maximum number of iterations
        """
        self.damping_factor = damping_factor
        self.tolerance = tolerance
        self.max_iterations = max_iterations
    
    def build_graph(self, links: list[tuple[str, str]]):
        pages = set()
        for source, target in links:
            pages.add(source)
            pages.add(target)
        
        page_to_index = {page: i for i, page in enumerate(sorted(pages))}
        n_pages = len(pages)
        adjacency = np.zeros((n_pages, n_pages))
        for source, target in links:
            source_idx = page_to_index[source]
            target_idx = page_to_index[target]
            adjacency[source_idx][target_idx] = 1
        return page_to_index, adjacency
    
    def calculate(self, links: List[Tuple[str, str]]) -> Dict[str, float]:
        """Calculate PageRank scores for all pages.
        """
        if not links: return {}
        page_to_index, adjacency = self.build_graph(links)
        n_pages = len(page_to_index)
        
        pagerank = np.ones(n_pages) / n_pages # init uniformly
        outbound_counts = np.sum(adjacency, axis=1) # get number outbound links per page
        
        for iteration in range(self.max_iterations):
            new_pagerank = np.zeros(n_pages)
            new_pagerank += (1 - self.damping_factor) / n_pages
            
            # Add contributions from incoming links
            for source_idx in range(n_pages):
                if outbound_counts[source_idx] > 0:
                    contribution = self.damping_factor * pagerank[source_idx] / outbound_counts[source_idx]
                    for target_idx in range(n_pages):
                        if adjacency[source_idx][target_idx] == 1:
                            new_pagerank[target_idx] += contribution
                else:
                    # Means it's a dangling node, distribute rank equally to all pages
                    contribution = self.damping_factor * pagerank[source_idx] / n_pages
                    new_pagerank += contribution
            
            max_delta = np.max(np.abs(new_pagerank - pagerank))
            self.show_iteration_results(iteration, new_pagerank, max_delta, page_to_index)
            pagerank = new_pagerank
            if max_delta < self.tolerance:
                print(f"Converged after {iteration + 1} iterations")
                break
        
        index_to_page = {i: page for page, i in page_to_index.items()}
        return {index_to_page[i]: score for i, score in enumerate(pagerank)}

    def show_iteration_results(self, iteration, new_pagerank, max_delta, page_to_index, verbose=True):
        """Print PageRank values for current iteration."""
        if verbose:
            print(f"Iteration {iteration + 1}:")
            index_to_page = {i: page for page, i in page_to_index.items()}
            for i, score in enumerate(new_pagerank):
                print(f"  {index_to_page[i]}: {score:.6f}")
            print(f"  Max change: {max_delta:.3f}\n\n")