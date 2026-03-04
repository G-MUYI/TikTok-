#!/bin/bash
# 会话持久化功能快速测试脚本

echo "========================================="
echo "  会话持久化功能测试"
echo "========================================="
echo ""

# 切换到项目目录
cd "d:/AI导航网站及资源网站/AI编程小工具/TikTok-爆款文案生成器/TikTok-"

echo "📁 1. 检查状态文件是否存在..."
echo "-----------------------------------"
if [ -f ".ai/session-state.json" ]; then
    echo "✅ session-state.json 存在"
else
    echo "❌ session-state.json 不存在"
fi

if [ -f ".ai/user-profile.json" ]; then
    echo "✅ user-profile.json 存在"
else
    echo "❌ user-profile.json 不存在"
fi

if [ -f ".ai/work-history.json" ]; then
    echo "✅ work-history.json 存在"
else
    echo "❌ work-history.json 不存在"
fi
echo ""

echo "📄 2. 查看session-state.json内容..."
echo "-----------------------------------"
cat .ai/session-state.json
echo ""
echo ""

echo "📄 3. 查看user-profile.json内容..."
echo "-----------------------------------"
cat .ai/user-profile.json
echo ""
echo ""

echo "📄 4. 查看work-history.json内容..."
echo "-----------------------------------"
cat .ai/work-history.json
echo ""
echo ""

echo "🕐 5. 检查文件修改时间..."
echo "-----------------------------------"
ls -lh .ai/*.json
echo ""

echo "📊 6. 检查测试文案..."
echo "-----------------------------------"
if [ -d "tests/fixtures" ]; then
    echo "✅ 测试文案目录存在"
    ls -lh tests/fixtures/
else
    echo "❌ 测试文案目录不存在"
fi
echo ""

echo "========================================="
echo "  测试完成"
echo "========================================="
echo ""
echo "💡 下一步："
echo "1. 使用测试文案进行实际测试"
echo "2. 查看详细测试指南：tests/SESSION_PERSISTENCE_TEST.md"
echo ""
