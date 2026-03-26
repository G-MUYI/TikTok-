#!/usr/bin/env python3
"""Simple test for sample_index.py functions"""

import sys
from pathlib import Path

# Execute the script to load functions
exec(open("tools/sample_index.py").read(), globals())

# Test case_id_from_filename
p1 = Path("sample-016-产品名.md")
assert _case_id_from_filename(p1) == "sample-016", "Test 1 failed"

p2 = Path("sample-006.md")
assert _case_id_from_filename(p2) == "sample-006", "Test 2 failed"

# Test product extraction
p3 = Path("sample-016-脚蹬拉力器.md")
assert _product_from_filename(p3) == "脚蹬拉力器", "Test 3 failed"

# Test tag extraction
md = """
## 标签
#个护 #清洁 #耳垢
"""
tags = _extract_tags(md)
assert tags == ["个护", "清洁", "耳垢"], "Test 4 failed"

print("✓ All tests passed!")
