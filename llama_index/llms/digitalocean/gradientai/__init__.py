"""DigitalOcean Gradient AI LLM integration for LlamaIndex."""

from llama_index.llms.digitalocean.gradientai.base import GradientAI

# Backward compatibility alias
DigitalOceanGradientAILLM = GradientAI

__all__ = ["GradientAI", "DigitalOceanGradientAILLM"]
