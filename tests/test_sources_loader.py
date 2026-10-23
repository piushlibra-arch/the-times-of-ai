import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.shared.config.sources_loader import get_sources_loader


def test_get_sources_by_category_accepts_hyphenated_alias():
    loader = get_sources_loader()
    sources = loader.get_sources_by_category("open-source")
    assert sources
    assert "huggingface_blog" in sources


def test_get_categories_uses_canonical_names():
    categories = get_sources_loader().get_categories()
    assert "open-source" in categories
    assert "open_source" not in categories
