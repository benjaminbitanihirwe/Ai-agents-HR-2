import os
from typing import List, Dict, Any

class CompanyKnowledgeGraph:
    """
    RAG Setup / Vector Store for Company Policies.
    Provides agents with access to policy documents for compliance and culture matching.
    """
    def __init__(self, data_dir: str = "data/policies"):
        self.data_dir = data_dir
        self._load_knowledge_base()

    def _load_knowledge_base(self):
        """Mock loading of Faiss or Vector DB for company policies"""
        # In a real setup, we would load PDF/Markdown policies, chunk them, 
        # generate embeddings using openclaw.embeddings or sentence_transformers, 
        # and store in a faiss index.
        self.policies = {
            "code_of_conduct": "All employees must act with integrity...",
            "payroll_schedule": "Salaries are paid on the 25th of each month.",
            "remote_work": "Employees may work remotely 2 days a week.",
            "termination": "Offboarding requires 2 weeks notice and physical asset return."
        }

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, str]]:
        """
        Query the company knowledge graph. 
        Returns relevant text chunks and document sources.
        """
        # Mock semantic search
        results = []
        query_lower = query.lower()
        
        for doc_name, content in self.policies.items():
            if any(keyword in query_lower for keyword in doc_name.split("_")):
                results.append({"source": doc_name, "content": content})
        
        # Fallback if no specific match
        if not results:
            results.append({"source": "general_handbook", "content": "Please refer to the HR handbook for standard procedures."})
            
        return results[:top_k]

# Singleton instance for agents to share
knowledge_store = CompanyKnowledgeGraph()
