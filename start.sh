#!/bin/bash

# EduMind Docker 启动脚本

echo "🚀 启动 EduMind Docker 容器..."

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    exit 1
fi

# 检查Docker Compose是否安装
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose 未安装，请先安装 Docker Compose"
    exit 1
fi

# 进入docker目录
cd "$(dirname "$0")"

# 创建必要的目录
mkdir -p ../data ../logs

# 检查环境变量文件
if [ ! -f "../.env" ]; then
    echo "⚠️  未找到 .env 文件，请复制 ../env.example 为 ../.env 并配置相关参数"
    echo "   cp ../env.example ../.env"
    echo "   然后编辑 .env 文件配置 API 密钥等参数"
    exit 1
fi

# 构建并启动容器
echo "🔨 构建 Docker 镜像..."
docker-compose build

echo "🌟 启动服务..."
docker-compose up -d

# 等待服务启动
echo "⏳ 等待服务启动..."
sleep 10

# 检查服务状态
if docker-compose ps | grep -q "Up"; then
    echo "✅ EduMind 启动成功！"
    echo "🌐 访问地址: http://localhost:8501"
    echo "📊 查看日志: docker-compose logs -f"
    echo "🛑 停止服务: docker-compose down"
else
    echo "❌ 服务启动失败，请检查日志:"
    docker-compose logs
fi 