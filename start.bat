@echo off
chcp 65001 >nul
echo 🚀 启动 EduMind Docker 容器...

REM 检查Docker是否安装
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker 未安装，请先安装 Docker Desktop
    pause
    exit /b 1
)

REM 检查Docker Compose是否可用
docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker Compose 未安装，请先安装 Docker Compose
    pause
    exit /b 1
)

REM 进入docker目录
cd /d %~dp0

REM 创建必要的目录
if not exist "..\data" mkdir ..\data
if not exist "..\logs" mkdir ..\logs

REM 检查环境变量文件
if not exist "..\.env" (
    echo ⚠️  未找到 .env 文件，请复制 ..\env.example 为 ..\.env 并配置相关参数
    echo    copy ..\env.example ..\.env
    echo    然后编辑 .env 文件配置 API 密钥等参数
    pause
    exit /b 1
)

REM 构建并启动容器
echo 🔨 构建 Docker 镜像...
docker-compose build

echo 🌟 启动服务...
docker-compose up -d

REM 等待服务启动
echo ⏳ 等待服务启动...
timeout /t 10 /nobreak >nul

REM 检查服务状态
docker-compose ps | findstr "Up" >nul
if %errorlevel% equ 0 (
    echo ✅ EduMind 启动成功！
    echo 🌐 访问地址: http://localhost:8501
    echo 📊 查看日志: docker-compose logs -f
    echo 🛑 停止服务: docker-compose down
) else (
    echo ❌ 服务启动失败，请检查日志:
    docker-compose logs
)

pause 