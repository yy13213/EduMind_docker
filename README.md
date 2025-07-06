# EduMind Docker 容器化部署

<div align="center">

![EduMind Logo](https://img.shields.io/badge/EduMind-多模态AI教育平台-blue?style=for-the-badge)

[![Docker](https://img.shields.io/badge/Docker-20.10+-blue?style=flat&logo=docker)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.46+-red?style=flat&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-green?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

*一键部署 EduMind 多模态大数据与生成式模型赋能高校学生全周期成长管理平台*

</div>

## 🔥 最新更新

### v1.1.0 (2025-07-07)
- ✅ **重要修复**: 解决了 "File does not exist: app.py" 错误
- 🔧 **Docker优化**: 修复了构建上下文配置问题
- 📦 **完整文件**: 现在包含所有必要的应用文件（app.py、HelloWeb.py等）
- 🎯 **即开即用**: 克隆后可直接运行，无需额外配置

> **注意**: 如果您之前遇到 app.py 文件找不到的错误，请重新克隆本仓库并重新部署。

## 🌟 项目简介

EduMind 是一个基于 Streamlit 开发的多模态教育管理平台，集成了：

- 📊 **学业发展分析** - 智能学习轨迹追踪与预测
- 🧠 **心理特质评估** - 多维度心理健康监测
- 📈 **行为规律挖掘** - 学生行为模式识别与分析
- 🌐 **社交网络分析** - 校园社交关系图谱构建
- 🚀 **发展潜能评估** - AI驱动的个性化成长建议
- 🛡️ **安全管理系统** - 智能风险预警与干预

## 🚀 快速开始

### 📋 环境要求

- **Docker**: 20.10 或更高版本
- **Docker Compose**: 1.29 或更高版本
- **系统要求**: 2GB+ RAM, 5GB+ 磁盘空间

### ⚡ 一键部署

#### 1. 克隆仓库

```bash
git clone https://github.com/yy13213/EduMind_docker.git
cd EduMind_docker
```

#### 2. 快速启动

**Linux/Mac 用户:**
```bash
chmod +x start.sh
./start.sh
```

**Windows 用户:**
```cmd
start.bat
```

#### 3. 访问应用

🌐 打开浏览器访问: http://127.0.0.1:8501

## 📚 详细部署指南

### 🔧 手动部署

```bash
# 1. 构建镜像
docker-compose build

# 2. 启动服务
docker-compose up -d

# 3. 查看状态
docker-compose ps
```

### 🎛️ 配置选项

#### 端口配置
```yaml
ports:
  - "127.0.0.1:8501:8501"  # 仅本地访问
  # - "8501:8501"          # 外部访问（不推荐生产环境）
```

#### 环境变量
```yaml
environment:
  - STREAMLIT_SERVER_HEADLESS=true
  - STREAMLIT_SERVER_PORT=8501
  - STREAMLIT_SERVER_ADDRESS=0.0.0.0
  # 添加您的 API 密钥
  - OPENAI_API_KEY=${OPENAI_API_KEY}
```

#### 数据持久化
```yaml
volumes:
  - ./data:/app/data      # 应用数据
  - ./logs:/app/logs      # 日志文件
```

## 📊 服务管理

### 常用命令

```bash
# 启动服务
docker-compose up -d

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 查看日志
docker-compose logs -f

# 查看资源使用
docker stats

# 进入容器
docker-compose exec edumind bash
```

### 健康检查

容器内置健康检查机制：
- ✅ **检查间隔**: 30秒
- ⏱️ **超时时间**: 10秒
- 🔄 **重试次数**: 3次
- 🚀 **启动等待**: 40秒

## 🛠️ 故障排除

### 常见问题

<details>
<summary>🔴 端口冲突</summary>

```bash
# 检查端口占用
netstat -ano | findstr :8501  # Windows
lsof -i :8501                 # Linux/Mac

# 杀死占用进程
taskkill /PID <PID> /F        # Windows
kill -9 <PID>                 # Linux/Mac
```
</details>

<details>
<summary>🔴 容器启动失败</summary>

```bash
# 查看详细日志
docker-compose logs edumind

# 重新构建镜像
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```
</details>

<details>
<summary>🔴 权限问题</summary>

```bash
# Linux/Mac 修复权限
sudo chown -R $USER:$USER ./data ./logs

# 确保启动脚本可执行
chmod +x start.sh
```
</details>

### 性能优化

```bash
# 清理未使用的资源
docker system prune -f

# 查看镜像大小
docker images

# 限制内存使用
docker-compose up -d --scale edumind=1 --memory=2g
```

## 📁 项目结构

```
EduMind_docker/
├── 📄 README.md              # 本文档
├── 🐳 Dockerfile             # Docker镜像构建文件
├── 🔧 docker-compose.yml     # Docker Compose配置
├── 📋 requirements.txt       # Python依赖清单
├── 🚫 .dockerignore          # Docker构建忽略文件
├── 🐧 start.sh               # Linux/Mac启动脚本
├── 🪟 start.bat              # Windows启动脚本
├── 📁 data/                  # 数据目录
├── 📁 logs/                  # 日志目录
├── 🐍 app.py                 # 主应用文件
├── 🌐 HelloWeb.py            # Web组件
├── 🧪 test.py                # 测试文件
├── 📝 homework.py            # 作业模块
└── 🎨 *.ttf, *.png, *.jpg    # 资源文件
```

## 🔐 安全说明

- 🏠 **本地访问**: 默认绑定到 `127.0.0.1`，仅本地访问
- 🔑 **API密钥**: 请妥善保管您的API密钥，不要提交到代码仓库
- 🛡️ **防火墙**: 生产环境请配置适当的防火墙规则
- 📝 **日志管理**: 定期清理日志文件，避免敏感信息泄露

## 📦 依赖包清单

本项目包含37个Python依赖包：

### 核心框架
- **streamlit** >= 1.28.0 - Web应用框架
- **pandas** >= 1.5.0 - 数据处理
- **numpy** >= 1.21.0 - 数值计算

### 可视化组件
- **matplotlib** >= 3.5.0 - 图表绘制
- **seaborn** >= 0.11.0 - 统计图表
- **plotly** >= 5.0.0 - 交互式图表
- **pyecharts** >= 1.9.0 - 中文图表库

### AI & ML
- **openai** >= 1.0.0 - OpenAI API
- **faker** >= 15.0.0 - 模拟数据生成

### Streamlit扩展
- **streamlit-extras** >= 0.3.0 - 扩展组件
- **streamlit-echarts** >= 0.4.0 - ECharts集成
- **streamlit-avatar** >= 0.1.0 - 头像组件
- **streamlit-card** >= 1.0.0 - 卡片组件

完整依赖列表请查看 [requirements.txt](requirements.txt)

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. 🍴 Fork 本仓库
2. 🌿 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 💬 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 📤 推送分支 (`git push origin feature/AmazingFeature`)
5. 🔄 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 技术支持

- 🐛 **Bug 报告**: [Issues](https://github.com/yy13213/EduMind_docker/issues)
- 💡 **功能请求**: [Issues](https://github.com/yy13213/EduMind_docker/issues)
- 📧 **联系我们**: yy13213@example.com

## 🔄 更新日志

### v1.0.0 (2025-01-06)
- 🚀 初始版本发布
- ✅ 支持Docker一键部署
- ✅ 包含完整的Streamlit应用配置
- ✅ 仅本地访问安全配置
- ✅ 跨平台启动脚本支持

## 🙏 致谢

感谢所有为 EduMind 项目做出贡献的开发者和用户！

---

<div align="center">

**[⬆ 回到顶部](#edumind-docker-容器化部署)**

Made with ❤️ by EduMind Team

</div> 