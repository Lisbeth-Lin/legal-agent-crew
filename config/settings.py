import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Keys
    openai_api_key: Optional[str] = ""
    firecrawl_api_key: Optional[str] = ""
    qwen_api_key: Optional[str] = ""
    
    # Model Configuration
    llm_provider: str = "qwen"
    embedding_model: str = "BAAI/bge-large-en-v1.5"
    llm_model: str = "gpt-3.5-turbo"
    qwen_model: str = "qwen-plus"
    qwen_base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    vector_dim: int = 1024
    
    # Retrieval Configuration
    top_k: int = 3
    batch_size: int = 512
    rerank_top_k: int = 3
    
    # Database Configuration
    milvus_db_path: str = "./data/milvus_binary.db"
    collection_name: str = "paralegal_agent"
    
    # Data Configuration
    docs_path: str = "./data/raft.pdf"

    # Cache Configuration
    hf_cache_dir: str = "./cache/hf_cache"
    
    # LLM settings
    temperature: float = 0.6
    max_tokens: int = 1000
    
    class Config:
        env_file = ".env"
        case_sensitive = False
    
    def __post_init__(self):
        # Create necessary directories
        Path(self.milvus_db_path).parent.mkdir(parents=True, exist_ok=True)
        Path(self.hf_cache_dir).mkdir(parents=True, exist_ok=True)

# Global settings instance
settings = Settings()
