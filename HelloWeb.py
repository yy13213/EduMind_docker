import datetime
import seaborn as sns
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties
from streamlit.components.v1 import html
import random
import matplotlib.pyplot as plt
from PIL import Image
from streamlit_extras.metric_cards import style_metric_cards
import json
from streamlit_lottie import st_lottie
from plotly.subplots import make_subplots
import requests
from faker import Faker
import plotly.graph_objects as go
import time
from faker import Faker
import re
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud
from datetime import datetime, timedelta
import hashlib
from streamlit_extras.colored_header import colored_header
import streamlit as st
from docx import Document
from openai import OpenAI
from streamlit_extras.stylable_container import stylable_container
from typing import Optional
fake = Faker('zh_CN')
# 指定本地字体文件的路径
font_path = './仿宋_GB2312.ttf'
# 使用font_manager加载本地字体
font_prop = font_manager.FontProperties(fname=font_path)
# 设置全局字体属性
plt.rcParams['font.family'] = font_prop.get_name()
def Hello():
    # 设置页面配置

    # 自定义CSS样式
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&family=Roboto:wght@300;400;500;700&display=swap');

        * {
            font-family: 'Noto Sans SC', 'Roboto', sans-serif;
        }

        .main-container {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%);
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }

        .title {
            font-size: 3rem !important;
            color: #2c3e50 !important;
            font-weight: 700 !important;
            text-align: center;
            margin-bottom: 1rem !important;
            background: linear-gradient(90deg, #3498db, #9b59b6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: fadeIn 1.5s ease-in-out;
            position: relative;
            padding-bottom: 15px;
        }

        .title:after {
            content: "";
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 4px;
            background: linear-gradient(90deg, #3498db, #9b59b6);
            border-radius: 2px;
        }

        .subtitle {
            font-size: 1.2rem !important;
            color: #7f8c8d !important;
            text-align: center;
            margin-bottom: 2rem !important;
            animation: slideUp 1s ease-in-out;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.6;
        }

        .feature-card {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            margin-bottom: 1.5rem;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border-top: 4px solid #3498db;
            position: relative;
            overflow: hidden;
        }

        .feature-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
        }

        .feature-card:before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(52, 152, 219, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .feature-card:hover:before {
            opacity: 1;
        }

        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #3498db;
        }

        .link-section {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            margin-top: 2rem;
            position: relative;
            overflow: hidden;
        }

        .link-section:before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(to bottom, #3498db, #9b59b6);
        }

        .link-item {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 0.8rem;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            background: rgba(245, 247, 250, 0.5);
            position: relative;
            overflow: hidden;
        }

        .link-item:before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 0;
            height: 100%;
            background: linear-gradient(90deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.1));
            transition: width 0.3s ease;
        }

        .link-item:hover {
            transform: translateX(10px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }

        .link-item:hover:before {
            width: 100%;
        }

        .link-icon {
            margin-right: 15px;
            font-size: 1.5rem;
            color: #3498db;
        }

        .contact-section {
            text-align: center;
            margin-top: 3rem;
            padding: 2rem;
            background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%);
            border-radius: 15px;
            color: white;
            box-shadow: 0 10px 30px rgba(52, 152, 219, 0.3);
            position: relative;
            overflow: hidden;
        }

        .contact-section:before {
            content: "";
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0) 70%);
            animation: pulse 8s infinite linear;
        }

        .stats-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin: 2rem 0;
        }

        .stat-item {
            text-align: center;
            padding: 1.5rem;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
            min-width: 150px;
            margin: 0.5rem;
            transition: all 0.3s ease;
        }

        .stat-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }

        .stat-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #3498db;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            font-size: 0.9rem;
            color: #7f8c8d;
        }

        .floating {
            animation: floating 4s ease-in-out infinite;
        }

        .testimonial {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
            margin: 1rem;
            position: relative;
        }

        .testimonial:before {
            content: """ """;
            font-size: 5rem;
            position: absolute;
            top: 10px;
            left: 10px;
            color: rgba(52, 152, 219, 0.1);
            font-family: serif;
        }

        .testimonial-author {
            display: flex;
            align-items: center;
            margin-top: 1rem;
        }

        .author-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #3498db;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 10px;
            font-weight: bold;
        }

        @keyframes floating {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
            100% { transform: translateY(0px); }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes pulse {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .particle {
            position: absolute;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            pointer-events: none;
        }
    </style>
    """, unsafe_allow_html=True)

    html("""
        <!-- 引入particles.js库 -->
        <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>

        <script>
        document.addEventListener('DOMContentLoaded', function() {
            // 存储粒子实例
            let particlesInstance = null;

            // 初始化粒子效果
            function initParticles() {
                // 创建粒子容器
                const particlesDiv = document.createElement('div');
                particlesDiv.id = 'particles-js';
                document.body.insertBefore(particlesDiv, document.body.firstChild);

                // 初始化粒子系统
                particlesInstance = particlesJS('particles-js', {
                    "particles": {
                        "number": {
                            "value": 100,  // 初始设置为100个粒子
                            "density": {
                                "enable": true,
                                "value_area": 800
                            }
                        },
                        "color": {
                            "value": ["#3498db", "#9b59b6", "#2ecc71", "#e74c3c", "#f1c40f"]
                        },
                        "shape": {
                            "type": "circle"
                        },
                        "opacity": {
                            "value": 0.5,
                            "random": true,
                            "anim": {
                                "enable": true,
                                "speed": 1,
                                "opacity_min": 0.1,
                                "sync": false
                            }
                        },
                        "size": {
                            "value": 5,
                            "random": true,
                            "anim": {
                                "enable": true,
                                "speed": 2,
                                "size_min": 1,
                                "sync": false
                            }
                        },
                        "line_linked": {
                            "enable": true,
                            "distance": 150,
                            "color": "#3498db",
                            "opacity": 0.3,
                            "width": 1
                        },
                        "move": {
                            "enable": true,
                            "speed": 1,
                            "direction": "none",
                            "random": true,
                            "straight": false,
                            "out_mode": "out",
                            "bounce": false,
                            "attract": {
                                "enable": true,
                                "rotateX": 600,
                                "rotateY": 1200
                            }
                        }
                    },
                    "interactivity": {
                        "detect_on": "window",
                        "events": {
                            "onhover": {
                                "enable": true,
                                "mode": "grab"
                            },
                            "onclick": {
                                "enable": true,
                                "mode": "push"
                            },
                            "resize": true
                        },
                        "modes": {
                            "grab": {
                                "distance": 140,
                                "line_linked": {
                                    "opacity": 0.8
                                }
                            },
                            "push": {
                                "particles_nb": 4
                            }
                        }
                    },
                    "retina_detect": true
                });

                const maxParticles = 10;
                const reductionInterval = setInterval(() => {
                    if (!particlesInstance?.pJS?.particles?.array) return;

                    const currentParticles = particlesInstance.pJS.particles.array;
                    if (currentParticles.length > maxParticles) {
                        // 更安全的减少方式 - 从数组末尾移除
                        const particlesToRemove = currentParticles.length - maxParticles;
                        particlesInstance.pJS.particles.array.splice(maxParticles, particlesToRemove);

                        // 强制刷新画布
                        particlesInstance.pJS.fn.particlesEmpty();
                        particlesInstance.pJS.fn.particlesCreate();
                        particlesInstance.pJS.fn.particlesDraw();
                        particlesInstance.pJS.fn.canvasPaint();
                    } else {
                        clearInterval(reductionInterval);
                    }
                }, 200);

                // 确保主容器在粒子之上
                const mainContainer = document.querySelector('.main-container');
                if(mainContainer) {
                    mainContainer.style.position = 'relative';
                    mainContainer.style.zIndex = '1';
                }
            }

            // 卡片动画
            function animateCards() {
                const cards = document.querySelectorAll('.feature-card');
                if (cards && cards.length > 0) {
                    cards.forEach((card, index) => {
                        if (card && card.style) {
                            card.style.opacity = '0';
                            card.style.transform = 'translateY(30px)';
                            card.style.transition = `all 0.5s ease ${index * 0.1}s`;

                            setTimeout(() => {
                                card.style.opacity = '1';
                                card.style.transform = 'translateY(0)';
                            }, 100);
                        }
                    });
                }
            }

            // 改进的鼠标跟随效果
            function initCursor() {
                const cursor = document.createElement('div');
                cursor.id = 'custom-cursor';
                cursor.style.position = 'fixed';
                cursor.style.width = '20px';
                cursor.style.height = '20px';
                cursor.style.border = '2px solid rgba(52, 152, 219, 0.5)';
                cursor.style.borderRadius = '50%';
                cursor.style.pointerEvents = 'none';
                cursor.style.zIndex = '9999';
                cursor.style.transform = 'translate(-50%, -50%)';
                cursor.style.transition = 'all 0.01s ease, opacity 0.3s ease';
                cursor.style.opacity = '0';
                cursor.style.backgroundColor = 'transparent';
                document.body.appendChild(cursor);

                // 鼠标进入页面时显示
                document.addEventListener('mouseenter', () => {
                    cursor.style.opacity = '1';
                });

                // 鼠标离开页面时隐藏
                document.addEventListener('mouseleave', () => {
                    cursor.style.opacity = '0';
                });

                document.addEventListener('mousemove', (e) => {
                    cursor.style.left = `${e.clientX}px`;
                    cursor.style.top = `${e.clientY}px`;
                });

                const interactiveElements = document.querySelectorAll('a, button, .feature-card, .link-item');
                if (interactiveElements && interactiveElements.length > 0) {
                    interactiveElements.forEach(el => {
                        el.addEventListener('mouseenter', () => {
                            cursor.style.width = '40px';
                            cursor.style.height = '40px';
                            cursor.style.borderColor = 'rgba(155, 89, 182, 0.7)';
                            cursor.style.backgroundColor = 'rgba(155, 89, 182, 0.2)';
                        });

                        el.addEventListener('mouseleave', () => {
                            cursor.style.width = '20px';
                            cursor.style.height = '20px';
                            cursor.style.borderColor = 'rgba(52, 152, 219, 0.5)';
                            cursor.style.backgroundColor = 'transparent';
                        });
                    });
                }
            }

            // 初始化所有效果
            initParticles();
            animateCards();
            initCursor();
        });
        </script>
        <style>
        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
            background-color: #ffffff;
        }
        #custom-cursor {
            will-change: transform;
            backface-visibility: hidden;
        }
        </style>
    """)

    # 主容器
    # st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # 标题部分
    st.markdown('<p class="title">🏫华北电力大学学生管理系统</p>', unsafe_allow_html=True)

    # 副标题
    st.markdown("""
    <div class="subtitle">
        华北电力大学官方学生综合管理平台，集成学籍管理、成绩查询、选课系统、校园服务等功能，<br>
        为全校师生提供便捷、高效的一站式服务，助力智慧校园建设。
    </div>
    """, unsafe_allow_html=True)

    # 统计数据显示
    st.markdown("""
    <div class="stats-container">
        <div class="stat-item">
            <div class="stat-value">30k+</div>
            <div class="stat-label">在校学生</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">2k+</div>
            <div class="stat-label">教职工</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">100+</div>
            <div class="stat-label">客户满意度</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">24/7</div>
            <div class="stat-label">服务支持</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 使用列布局展示功能
    st.markdown("### 🚀 核心功能", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>学业发展</h3>
            <p>基于课程成绩、课堂考勤、作业提交记录和图书馆借阅数据，识别挂科风险学生，提供个性化学习方案。</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <h3>心理特质</h3>
            <p>基于SCL-90等心理测评结果，分析情绪波动热力图，识别抑郁倾向学生，评估抗压能力，提供心理预警和建议方案。</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🏆</div>
            <h3>发展潜能</h3>
            <p>分析竞赛获奖、创新创业实践、党团活动参与度，评估学生的职业适配度、深造潜力，并提供职业发展规划建议。</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <h3>行为规律</h3>
            <p>基于校园卡消费、门禁数据、作息规律，检测异常消费、成瘾行为，并生成行为预警报告。</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💬</div>
            <h3>社交网络</h3>
            <p>分析线上社交活跃度、群聊文本、舆情敏感词，识别社交孤立学生，并推荐适合的社团和活动。</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <h3>典型指标</h3>
            <p>计算学科关联度分析、学习投入度评分、领导力潜能评分、价值观偏离度评估，提供针对性的发展建议。</p>
        </div>
        """, unsafe_allow_html=True)

    # 客户评价轮播
    st.markdown("### 💬 最新通知", unsafe_allow_html=True)
    testimonial_cols = st.columns(3)

    with testimonial_cols[0]:
        st.markdown("""
        <div class="testimonial">
            <p>"2024-2025学年第二学期选课通知"\n\n</p>
            <div class="testimonial-author">
                <div class="author-avatar">教</div>
                <div>
                    <strong>教务处</strong><br>
                    <small>2025年3月25日</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with testimonial_cols[1]:
        st.markdown("""
        <div class="testimonial">
            <p>"2024届毕业生学位申请工作的通知"</p>
            <div class="testimonial-author">
                <div class="author-avatar">学</div>
                <div>
                    <strong>学位办公室</strong><br>
                    <small>2025年4月10日</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with testimonial_cols[2]:
        st.markdown("""
        <div class="testimonial">
            <p>"校园网系统升级维护通知"\n\n</p>
            <div class="testimonial-author">
                <div class="author-avatar">网</div>
                <div>
                    <strong>网络管理部</strong><br>
                    <small>2025年4月12日</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 链接部分
    st.markdown("""
    <div class="link-section">
        <h3>🔗 快速链接</h3>
        <div class="link-item">
            <span class="link-icon">🌐</span>
            <div>
                <a href="https://www.ncepu.edu.cn/" target="_blank"><strong>学校官网</strong></a>
                <p style="margin: 5px 0 0; color: #7f8c8d; font-size: 0.9rem;">了解学校详情和最新动态</p>
            </div>
        </div>
        <div class="link-item">
            <span class="link-icon">📄</span>
            <div>
                <a href="https://jwxt.ncepu.edu.cn/" target="_blank"><strong>教务系统</strong></a>
                <p style="margin: 5px 0 0; color: #7f8c8d; font-size: 0.9rem;">查看详细功能说明和使用指南</p>
            </div>
        </div>
        <div class="link-item">
            <span class="link-icon">🎥</span>
            <div>
                <a href="https://library.ncepu.edu.cn/" target="_blank"><strong>图书馆</strong></a>
                <p style="margin: 5px 0 0; color: #7f8c8d; font-size: 0.9rem;">观看系统操作演示和案例分享</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 联系信息
    st.markdown("""
    <div class="contact-section floating">
        <h3 style="color: white; margin-bottom: 1rem;">📞 技术支持</h3>
        <p style="color: rgba(255, 255, 255, 0.9); margin-bottom: 1.5rem;">有任何问题或建议？我们的团队随时为您服务</p>
        <div style="background: rgba(255, 255, 255, 0.2); display: inline-block; padding: 0.8rem 1.5rem; border-radius: 50px;">
            <a href="mailto:username@example.com" style="color: white; text-decoration: none; font-weight: 500;">
                电话: 13963347871
            </a>
        </div>
        <div style="margin-top: 1.5rem; color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">
            工作日 8:00-17:30 | 7×24小时技术支持
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # 关闭主容器
def Academic_analysis():
    # 自定义CSS样式
    st.markdown("""
        <style>
        /* 主标题样式 */
        .main-title {
            font-size: 36px !important;
            font-weight: 700 !important;
            color: #1f77b4 !important;
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 10px;
            border-bottom: 2px solid #1f77b4;
        }

        /* 分区标题样式 */
        .section-title {
            font-size: 24px !important;
            font-weight: 600 !important;
            color: #2c3e50 !important;
            margin-top: 25px;
            margin-bottom: 15px;
            padding-left: 10px;
            border-left: 4px solid #1f77b4;
        }

        /* 卡片样式 */
        .card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        /* 搜索框样式 */
        .stTextInput>div>div>input {
            border-radius: 20px !important;
            padding: 10px 15px !important;
        }

        /* 按钮样式 */
        .stButton>button {
            border-radius: 20px !important;
            padding: 8px 24px !important;
            background-color: #1f77b4 !important;
            color: white !important;
            border: none !important;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #1565c0 !important;
            transform: scale(1.05);
        }

        /* 标签样式 */
        .tag {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 600;
            margin-right: 8px;
            margin-bottom: 8px;
        }

        .tag-primary {
            background-color: #e3f2fd;
            color: #1976d2;
        }

        .tag-success {
            background-color: #e8f5e9;
            color: #388e3c;
        }

        .tag-warning {
            background-color: #fff8e1;
            color: #ffa000;
        }

        .tag-danger {
            background-color: #ffebee;
            color: #d32f2f;
        }

        /* 动画效果 */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .animate-fade {
            animation: fadeIn 0.6s ease-out forwards;
        }

        /* 首页欢迎卡片 */
        .welcome-card {
            background: linear-gradient(135deg, #1f77b4 0%, #4b9cd3 100%);
            color: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        /* 统计卡片 */
        .stats-card {
            background-color: white;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-left: 4px solid #1f77b4;
        }

        /* 功能卡片 */
        .feature-card {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
            border-top: 3px solid #1f77b4;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.12);
        }

        /* AI消息样式 */
        .ai-message {
            background-color: #f0f7ff;
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 15px;
            border-left: 4px solid #1f77b4;
        }

        .user-message {
            background-color: #e6f3ff;
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 15px;
            border-left: 4px solid #4b9cd3;
        }
        </style>
    """, unsafe_allow_html=True)

    # 初始化DeepSeek客户端
    def get_ai_client():
        return OpenAI(
            api_key="sk-24d37178569a4f9d9ee09925e6edffa5",
            base_url="https://api.deepseek.com"
        )

    # 模拟学生数据生成函数
    def generate_student_data(student_id):
        # 基础信息
        names = [
            "王思远", "李婧怡", "张子轩", "刘雨桐", "陈昊然", "杨紫彤", "赵志远", "黄梦婷", "吴梓豪", "周可欣",
            "郑一帆", "孙佳怡", "马承志", "朱宇航", "胡欣然", "郭子睿", "林雨馨", "何俊杰", "高诗涵", "罗思源",
            "宋佳琪", "谢晨曦", "唐浩然", "邓可儿", "许梓涵", "韩宇泽", "冯芷萱", "曹睿哲", "彭宸希", "萧子墨",
            "程欣妍", "尹晨雨", "陶俊熙", "袁嘉怡", "秦语嫣", "赖文博", "赖梓萱", "严浩轩", "贾婉琳", "黎思辰",
            "施凯文", "鲁子仪", "谭语嫣", "侯泽宇", "白梓萌", "丁奕辰", "康妍希", "章宇哲", "戴心怡",
            "田志伟", "石慧敏", "夏彦霏", "杜梓睿", "魏梦琪", "范奕辰", "冉梓诺", "廖俊铭",
            "裴子墨", "闫雪妍", "纪文轩", "熊雨辰", "陶思彤", "蒲晨曦", "温嘉乐", "宫子涵", "景昕怡", "梅泽铭",
            "欧阳浩然", "殷诗涵", "昌语嫣", "路宸轩", "丁心妍", "花宇杰", "边沛然", "芦梓琳",
            "晏诗琪", "裴若曦", "储子辰", "邬梦涵", "戚嘉怡", "訾皓宇", "成语彤", "昌可欣", "茅泽宇", "倪妍妍",
            "柴浩宸", "阚梓宁", "管紫嫣", "厉雨泽", "龚婧怡", "杭泽霖", "丰嘉辰", "左语嫣", "童一诺", "屈子墨",
            "庄宇萱", "边昕妍", "苗俊凯", "温佳怡", "燕泽远", "权奕辰", "党一帆", "翟宇彤", "郜梓宸",
            "滕宛妍", "米嘉昊", "郁梓轩", "焦梦妍", "严涵宇", "车思妍", "项辰曦",
            "游俊熙", "郁昕怡", "商乐怡", "臧宇航", "邝文睿", "雍芷萱", "籍紫涵",
            "隗天怡", "戎雨萌", "祖宸逸", "经乐妍", "柏志强", "燕嘉妍", "巫俊豪", "蔚子骞",
            "东语嫣", "慎晨曦", "鞠子诺",
            "墨子瑞", "南子安", "臧宇航", "索婉妍", "卞心妍", "淳嘉仪", "单梓妍",
            "胥嘉铭", "季语嫣", "岳紫彤", "权俊逸", "冷欣怡",
            "庞宇轩", "梅心怡", "禹泽宇", "苗语嫣", "赖文睿", "费文杰", "冉昕怡", "幸芷萱",
            "查语彤", "华思彤", "邸宇辰", "富梓涵", "惠雨婷", "纪一诺", "容俊豪",
            "崔奕辰",
            "米浩然", "涂雅妍", "幸俊豪"]
        majors = ["计算机科学", "软件工程", "人工智能", "数据科学", "网络安全"]
        grades = ["大一", "大二", "大三", "大四"]
        classes = ["1班", "2班", "3班", "4班"]

        # 随机生成数据
        random.seed(student_id)  # 确保相同学号生成相同数据

        student_info = {
            "学号": student_id,
            "姓名": random.choice(names),
            "性别": random.choice(["男", "女"]),
            "专业": random.choice(majors),
            "年级": random.choice(grades),
            "班级": random.choice(classes),
            "入学日期": f"20{random.randint(18, 22)}-09-01",
            "联系方式": f"1{random.randint(30, 89)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}",
            "邮箱": f"{random.choice(['student', 'learn', 'study'])}{student_id[-4:]}@university.edu.cn"
        }

        # 课程列表
        courses = {
            "计算机科学": ["程序设计", "数据结构", "算法分析", "数据库系统", "操作系统", "计算机网络", "机器学习"],
            "软件工程": ["软件工程", "系统分析与设计", "软件测试", "软件项目管理", "人机交互", "Web开发"],
            "人工智能": ["人工智能基础", "机器学习", "深度学习", "自然语言处理", "计算机视觉", "强化学习"],
            "数据科学": ["数据科学导论", "统计学", "数据挖掘", "大数据技术", "数据可视化", "数据库系统"],
            "网络安全": ["网络安全基础", "密码学", "网络攻防技术", "操作系统安全", "Web安全", "渗透测试"]
        }

        student_courses = courses[student_info["专业"]]

        # 生成成绩数据
        grades_data = {}
        for course in student_courses:
            base_score = random.randint(40, 90)
            # 添加一些波动
            grades_data[course] = max(0, min(100, base_score + random.randint(-10, 10)))

        # 考勤数据
        attendance = {
            "总课时": 32,
            "出勤": random.randint(25, 32),
            "迟到": random.randint(0, 5),
            "早退": random.randint(0, 3),
            "旷课": random.randint(0, 3)
        }

        # 作业数据
        homework = {
            "总作业数": 12,
            "按时提交": random.randint(6, 12),
            "迟交": random.randint(0, 4),
            "未交": random.randint(0, 3)
        }

        # 图书馆数据
        library = {
            "本学期借阅量": random.randint(5, 30),
            "专业相关书籍": random.randint(3, 25),
            "文学类书籍": random.randint(0, 10),
            "科技类书籍": random.randint(0, 8),
            "平均阅读时长(小时)": round(random.uniform(1.5, 5.0), 1)
        }

        # 计算学业预警指数 (0-100, 越高风险越大)
        warning_score = (
                (100 - np.mean(list(grades_data.values()))) * 0.5 +  # 成绩因素
                ((attendance["旷课"] / attendance["总课时"]) * 100) * 0.3 +  # 考勤因素
                ((homework["未交"] / homework["总作业数"]) * 100) * 0.2  # 作业因素
        )

        # 计算学习投入度评分 (0-100, 越高投入度越高)
        engagement_score = (
                (attendance["出勤"] / attendance["总课时"]) * 30 +  # 考勤占比30%
                (homework["按时提交"] / homework["总作业数"]) * 30 +  # 作业占比30%
                (min(library["本学期借阅量"], 20) / 20) * 20 +  # 借阅量占比20% (上限20本)
                (min(library["平均阅读时长(小时)"], 5) / 5) * 20  # 阅读时长占比20% (上限5小时)
        )

        # 学科关联度分析
        subjects = list(grades_data.keys())
        subject_correlation = {}
        for i in range(len(subjects)):
            for j in range(i + 1, len(subjects)):
                # 模拟相关性 (0-1之间)
                correlation = random.uniform(0.3, 0.9) if random.random() > 0.3 else random.uniform(0, 0.3)
                subject_correlation[f"{subjects[i]} & {subjects[j]}"] = correlation

        # 挂科风险预测
        fail_risk = {}
        for course, score in grades_data.items():
            if score < 60:
                risk = "高"
            elif score < 70:
                risk = "中"
            else:
                risk = "低"
            fail_risk[course] = risk

        # 个性化学习方案
        weak_subjects = [course for course, score in grades_data.items() if score < 70]
        learning_plan = []

        if len(weak_subjects) > 0:
            learning_plan.append(f"重点加强{len(weak_subjects)}门较弱学科的学习")
            for subject in weak_subjects:
                learning_plan.append(f"- {subject}: 推荐每周额外投入{random.randint(2, 5)}小时学习")
                learning_plan.append(f"  推荐资源: 《{subject}进阶教程》, 在线课程{random.choice(['A', 'B', 'C'])}")

            if attendance["旷课"] > 2:
                learning_plan.append("注意: 出勤率较低，建议提高课堂参与度")
            if homework["未交"] > 1:
                learning_plan.append("注意: 作业提交不及时，建议制定作业计划表")
            if library["本学期借阅量"] < 10:
                learning_plan.append("建议: 增加专业书籍阅读量，每月至少阅读2本相关书籍")
        else:
            learning_plan.append("学生各科表现均衡，继续保持当前学习节奏")
            learning_plan.append("建议: 可以尝试拓展学习领域，参加学术竞赛或科研项目")

        return {
            "info": student_info,
            "grades": grades_data,
            "attendance": attendance,
            "homework": homework,
            "library": library,
            "warning_score": round(warning_score, 1),
            "engagement_score": round(engagement_score, 1),
            "subject_correlation": subject_correlation,
            "fail_risk": fail_risk,
            "learning_plan": learning_plan
        }

    # 首页内容
    def show_home_page():
        st.markdown('<h1 class="main-title animate-fade">🎓 学生学业查询与分析</h1>', unsafe_allow_html=True)

        # 欢迎卡片
        st.markdown("""
            <div class="welcome-card animate-fade">
                <h2 style="color: white; margin-top: 0;">欢迎使用学生学业查询</h2>
                <p style="color: rgba(255,255,255,0.9); font-size: 16px;">
                    本界面提供全面的学生学业数据分析功能，包括成绩查询、考勤记录、作业完成情况和图书馆借阅分析等，
                    帮助教师和管理者更好地了解学生学习状况，并提供个性化的学习建议。
                </p>
            </div>
        """, unsafe_allow_html=True)

        # 系统功能简介
        st.markdown('<h2 class="section-title animate-fade">✨ 基本功能</h2>', unsafe_allow_html=True)

        cols = st.columns(3)
        with cols[0]:
            st.markdown("""
                <div class="feature-card">
                    <h3>📊 学业数据可视化</h3>
                    <p>直观展示学生各科成绩、考勤记录、作业完成情况等数据，通过图表形式呈现学业趋势。</p>
                </div>
            """, unsafe_allow_html=True)
        with cols[1]:
            st.markdown("""
                <div class="feature-card">
                    <h3>⚠️ 学业预警</h3>
                    <p>自动分析学生学业风险，识别潜在问题科目，提前预警可能的挂科风险。</p>
                </div>
            """, unsafe_allow_html=True)
        with cols[2]:
            st.markdown("""
                <div class="feature-card">
                    <h3>🤖 AI学业分析</h3>
                    <p>基于深度学习模型，提供个性化的学习建议和学业规划指导。</p>
                </div>
            """, unsafe_allow_html=True)

        # 快速查询区域
        st.markdown('<h2 class="section-title animate-fade">🔍 快速查询</h2>', unsafe_allow_html=True)

        with st.form("quick_search"):
            search_col1, search_col2 = st.columns([3, 1])
            with search_col1:
                student_id = st.text_input("输入学生学号", placeholder="例如: 202301001", key="home_search")
            with search_col2:
                st.write("")
                st.write("")
                search_clicked = st.form_submit_button("查询", use_container_width=True)

        # 统计数据展示
        st.markdown('<h2 class="section-title animate-fade">📈 学院数据概览</h2>', unsafe_allow_html=True)

        stats_cols = st.columns(4)
        with stats_cols[0]:
            st.markdown("""
                <div class="stats-card">
                    <h3 style="margin-top: 0;">学生总数</h3>
                    <h1 style="color: #1f77b4; margin-bottom: 0;">2,453</h1>
                    <p style="color: #666; font-size: 12px;">较上月 +1.2%</p>
                </div>
            """, unsafe_allow_html=True)
        with stats_cols[1]:
            st.markdown("""
                <div class="stats-card">
                    <h3 style="margin-top: 0;">平均成绩</h3>
                    <h1 style="color: #1f77b4; margin-bottom: 0;">76.5</h1>
                    <p style="color: #666; font-size: 12px;">较上学期 +2.3%</p>
                </div>
            """, unsafe_allow_html=True)
        with stats_cols[2]:
            st.markdown("""
                <div class="stats-card">
                    <h3 style="margin-top: 0;">出勤率</h3>
                    <h1 style="color: #1f77b4; margin-bottom: 0;">92.3%</h1>
                    <p style="color: #666; font-size: 12px;">较上月 +0.8%</p>
                </div>
            """, unsafe_allow_html=True)
        with stats_cols[3]:
            st.markdown("""
                <div class="stats-card">
                    <h3 style="margin-top: 0;">预警学生</h3>
                    <h1 style="color: #1f77b4; margin-bottom: 0;">127</h1>
                    <p style="color: #666; font-size: 12px;">较上月 -5.6%</p>
                </div>
            """, unsafe_allow_html=True)

        # 示例图表
        st.markdown('<h2 class="section-title animate-fade">📊 学院成绩分布</h2>', unsafe_allow_html=True)

        # 生成模拟数据
        majors = ["计算机科学", "软件工程", "人工智能", "数据科学", "网络安全"]
        data = {
            "专业": majors * 4,
            "年级": ["大一"] * 5 + ["大二"] * 5 + ["大三"] * 5 + ["大四"] * 5,
            "平均成绩": [random.randint(65, 85) for _ in range(20)]
        }
        df = pd.DataFrame(data)

        fig = px.bar(df, x="专业", y="平均成绩", color="年级", barmode="group",
                     title="各专业年级平均成绩对比", height=400)
        st.plotly_chart(fig, use_container_width=True)

        # 如果点击了查询按钮且有学号输入，则跳转到结果页面
        if search_clicked and student_id:
            # 生成学生数据并保存到session_state
            with st.spinner('正在查询学生数据...'):
                time.sleep(1.5)
                st.session_state.student_data_academic_analysis = generate_student_data(student_id)
                st.session_state.current_page_academic_analysis = "student_detail"
                st.rerun()

        return None

    # AI分析功能组件
    def show_ai_analysis(student_data):
        st.markdown('<h2 class="section-title">🤖 AI学业分析</h2>', unsafe_allow_html=True)

        # 自动生成初始分析
        if "ai_initial_analysis" not in st.session_state:
            # 准备上下文信息
            context = f"""
            学生基本信息:
            - 姓名: {student_data['info']['姓名']}
            - 专业: {student_data['info']['专业']}
            - 年级: {student_data['info']['年级']}

            学业数据:
            - 各科成绩: {student_data['grades']}
            - 出勤情况: {student_data['attendance']['出勤']}/{student_data['attendance']['总课时']} (出勤率: {round(student_data['attendance']['出勤'] / student_data['attendance']['总课时'] * 100, 1)}%)
            - 作业完成情况: {student_data['homework']['按时提交']}/{student_data['homework']['总作业数']} (按时提交率: {round(student_data['homework']['按时提交'] / student_data['homework']['总作业数'] * 100, 1)}%)
            - 图书馆借阅: 本学期共借阅{student_data['library']['本学期借阅量']}本书，其中专业相关{student_data['library']['专业相关书籍']}本

            学业分析:
            - 学业预警指数: {student_data['warning_score']}/100
            - 学习投入度: {student_data['engagement_score']}/100
            - 挂科风险科目: {[k for k, v in student_data['fail_risk'].items() if v in ['高', '中']]}
            """

            # 调用DeepSeek API生成初始分析
            try:
                client = get_ai_client()

                with st.spinner("AI正在生成分析报告..."):
                    response = client.chat.completions.create(
                        model="deepseek-chat",
                        messages=[
                            {"role": "system",
                             "content": "你是一个专业的学业分析助手，能够根据提供的学生学业数据，给出专业的分析和建议。回答要简明扼要，重点突出。"},
                            {"role": "system", "content": context},
                            {"role": "user", "content": "请分析该学生的学习情况，指出强项和弱项，并提供具体的学习建议"}
                        ],
                        stream=False
                    )

                    st.session_state.ai_initial_analysis = response.choices[0].message.content
                    st.session_state.ai_messages = [
                        {"role": "assistant",
                         "content": f"你好！我是你的学业分析助手，可以帮助你分析{student_data['info']['姓名']}同学的学习情况。"},
                        {"role": "assistant", "content": st.session_state.ai_initial_analysis}
                    ]

            except Exception as e:
                st.error(f"AI分析出错: {str(e)}")
                st.session_state.ai_initial_analysis = "抱歉，分析过程中出现了问题，请稍后再试。"
                st.session_state.ai_messages = [
                    {"role": "assistant", "content": f"你好！我是你的学业分析助手。"},
                    {"role": "assistant", "content": st.session_state.ai_initial_analysis}
                ]

        # 显示初始分析结果
        st.markdown(
            f'<div class="ai-message">🤖 <strong>AI分析报告</strong><br/>{st.session_state.ai_initial_analysis}</div>',
            unsafe_allow_html=True)

        # 显示聊天记录
        for message in st.session_state.ai_messages[2:]:  # 跳过前两条初始消息
            if message["role"] == "assistant":
                st.markdown(f'<div class="ai-message">🤖 <strong>AI助手</strong><br/>{message["content"]}</div>',
                            unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="user-message">👤 <strong>你</strong><br/>{message["content"]}</div>',
                            unsafe_allow_html=True)

        # 用户输入
        user_input = st.text_input("输入你的问题",
                                   placeholder=f"例如: 如何提高{student_data['info']['姓名']}的{list(student_data['grades'].keys())[0]}成绩?",
                                   key="ai_input", label_visibility="collapsed")

        if st.button("发送", key="ai_send") and user_input:
            # 添加用户消息到会话历史
            st.session_state.ai_messages.append({"role": "user", "content": user_input})

            # 准备上下文信息
            context = f"""
            学生基本信息:
            - 姓名: {student_data['info']['姓名']}
            - 专业: {student_data['info']['专业']}
            - 年级: {student_data['info']['年级']}

            学业数据:
            - 各科成绩: {student_data['grades']}
            - 出勤情况: {student_data['attendance']['出勤']}/{student_data['attendance']['总课时']} (出勤率: {round(student_data['attendance']['出勤'] / student_data['attendance']['总课时'] * 100, 1)}%)
            - 作业完成情况: {student_data['homework']['按时提交']}/{student_data['homework']['总作业数']} (按时提交率: {round(student_data['homework']['按时提交'] / student_data['homework']['总作业数'] * 100, 1)}%)
            - 图书馆借阅: 本学期共借阅{student_data['library']['本学期借阅量']}本书，其中专业相关{student_data['library']['专业相关书籍']}本

            学业分析:
            - 学业预警指数: {student_data['warning_score']}/100
            - 学习投入度: {student_data['engagement_score']}/100
            - 挂科风险科目: {[k for k, v in student_data['fail_risk'].items() if v in ['高', '中']]}
            """

            # 调用DeepSeek API
            try:
                client = get_ai_client()

                with st.spinner("AI正在分析中..."):
                    response = client.chat.completions.create(
                        model="deepseek-chat",
                        messages=[
                            {"role": "system",
                             "content": "你是一个专业的学业分析助手，能够根据提供的学生学业数据，给出专业的分析和建议。回答要简明扼要，重点突出。"},
                            {"role": "system", "content": context},
                            *st.session_state.ai_messages
                        ],
                        stream=False
                    )

                    ai_response = response.choices[0].message.content
                    st.session_state.ai_messages.append({"role": "assistant", "content": ai_response})

                    # 重新运行以显示新消息
                    st.rerun()

            except Exception as e:
                st.error(f"AI分析出错: {str(e)}")
                st.session_state.ai_messages.append(
                    {"role": "assistant", "content": "抱歉，分析过程中出现了问题，请稍后再试。"})
                st.rerun()

        # 提供一些建议问题
        st.markdown("""
            <div style="margin-top: 20px; color: #666; font-size: 14px;">
                <p><strong>你可以尝试问:</strong></p>
                <ul>
                    <li>如何提高某科目的成绩？</li>
                    <li>推荐适合该学生的学习资源</li>
                    <li>分析学习习惯中的问题</li>
                    <li>制定下周的学习计划</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # 学生详情页面
    def show_student_detail_page():
        student_data = st.session_state.student_data_academic_analysis

        # 显示学生基本信息
        st.markdown('<h1 class="main-title animate-fade">🎓 学生学业分析报告</h1>', unsafe_allow_html=True)

        st.markdown('<h2 class="section-title animate-fade">📋 学生基本信息</h2>', unsafe_allow_html=True)

        info_cols = st.columns(4)
        with info_cols[0]:
            st.metric("姓名", student_data["info"]["姓名"])
        with info_cols[1]:
            st.metric("专业", student_data["info"]["专业"])
        with info_cols[2]:
            st.metric("年级", student_data["info"]["年级"])
        with info_cols[3]:
            st.metric("班级", student_data["info"]["班级"])

        # 添加更多信息在可展开区域
        with st.expander("查看完整个人信息"):
            cols = st.columns(2)
            with cols[0]:
                st.write(f"**学号:** {student_data['info']['学号']}")
                st.write(f"**性别:** {student_data['info']['性别']}")
                st.write(f"**入学日期:** {student_data['info']['入学日期']}")
            with cols[1]:
                st.write(f"**联系方式:** {student_data['info']['联系方式']}")
                st.write(f"**邮箱:** {student_data['info']['邮箱']}")

        # 学业数据展示
        st.markdown('<h2 class="section-title animate-fade">📊 学业数据展示</h2>', unsafe_allow_html=True)

        # 使用选项卡组织不同类型的学业数据
        tab1, tab2, tab3, tab4 = st.tabs(["📈 课程成绩", "✅ 课堂考勤", "📝 作业提交", "📚 图书馆借阅"])

        with tab1:
            # 成绩折线图
            grades_df = pd.DataFrame(list(student_data["grades"].items()), columns=["课程", "成绩"])
            fig = px.line(grades_df, x="课程", y="成绩", title="各科成绩趋势", markers=True)
            fig.update_layout(
                yaxis_range=[0, 100],
                hovermode="x unified",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            fig.update_traces(line=dict(width=3), marker=dict(size=10))
            st.plotly_chart(fig, use_container_width=True)

            # 成绩分布雷达图
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=list(student_data["grades"].values()),
                theta=list(student_data["grades"].keys()),
                fill='toself',
                name='成绩分布'
            ))
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=False,
                title="成绩分布雷达图"
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            # 考勤数据饼图
            attendance_data = {
                "出勤": student_data["attendance"]["出勤"],
                "迟到": student_data["attendance"]["迟到"],
                "早退": student_data["attendance"]["早退"],
                "旷课": student_data["attendance"]["旷课"]
            }
            fig = px.pie(
                values=list(attendance_data.values()),
                names=list(attendance_data.keys()),
                title="课堂考勤情况",
                color=list(attendance_data.keys()),
                color_discrete_map={
                    "出勤": "#2ecc71",
                    "迟到": "#f39c12",
                    "早退": "#e74c3c",
                    "旷课": "#c0392b"
                }
            )
            st.plotly_chart(fig, use_container_width=True)

            # 考勤率指标卡
            attendance_rate = round((student_data["attendance"]["出勤"] / student_data["attendance"]["总课时"]) * 100,
                                    1)
            st.metric("出勤率", f"{attendance_rate}%")
            st.progress(attendance_rate / 100)

        with tab3:
            # 作业提交柱状图
            homework_data = {
                "按时提交": student_data["homework"]["按时提交"],
                "迟交": student_data["homework"]["迟交"],
                "未交": student_data["homework"]["未交"]
            }
            fig = px.bar(
                x=list(homework_data.keys()),
                y=list(homework_data.values()),
                title="作业提交情况",
                color=list(homework_data.keys()),
                color_discrete_sequence=["#2ecc71", "#f39c12", "#e74c3c"]
            )
            st.plotly_chart(fig, use_container_width=True)

            # 作业提交率指标卡
            submission_rate = round((student_data["homework"]["按时提交"] / student_data["homework"]["总作业数"]) * 100,
                                    1)
            st.metric("按时提交率", f"{submission_rate}%")
            st.progress(submission_rate / 100)

        with tab4:
            # 图书馆借阅数据
            library_data = {
                "专业相关": student_data["library"]["专业相关书籍"],
                "文学类": student_data["library"]["文学类书籍"],
                "科技类": student_data["library"]["科技类书籍"]
            }
            fig = px.bar(
                x=list(library_data.keys()),
                y=list(library_data.values()),
                title="图书借阅分类",
                color=list(library_data.keys()),
                color_discrete_sequence=["#3498db", "#9b59b6", "#1abc9c"]
            )
            st.plotly_chart(fig, use_container_width=True)

            # 借阅量指标卡
            cols = st.columns(2)
            with cols[0]:
                st.metric("本学期借阅量", student_data["library"]["本学期借阅量"])
            with cols[1]:
                st.metric("平均阅读时长", f"{student_data['library']['平均阅读时长(小时)']}小时")

        # 学业分析
        st.markdown('<h2 class="section-title animate-fade">🔍 学业分析</h2>', unsafe_allow_html=True)

        # 使用列布局展示分析指标
        col1, col2, col3 = st.columns(3)

        with col1:
            # 学业预警指数
            warning_level = ""
            if student_data["warning_score"] > 70:
                warning_level = "高"
                color = "red"
            elif student_data["warning_score"] > 40:
                warning_level = "中"
                color = "orange"
            else:
                warning_level = "低"
                color = "green"

            st.markdown(f"""
                <div class="card">
                    <h3>⚠️ 学业预警指数</h3>
                    <h1 style="color: {color}; text-align: center; font-size: 36px;">{student_data['warning_score']}</h1>
                    <p style="text-align: center;">风险等级: <strong>{warning_level}</strong></p>
                    <div style="height: 10px; background: #eee; border-radius: 5px; margin-top: 10px;">
                        <div style="width: {student_data['warning_score']}%; height: 100%; background: {color}; border-radius: 5px;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            # 学习投入度评分
            engagement_level = ""
            if student_data["engagement_score"] > 80:
                engagement_level = "高"
                color = "green"
            elif student_data["engagement_score"] > 60:
                engagement_level = "中"
                color = "orange"
            else:
                engagement_level = "低"
                color = "red"

            st.markdown(f"""
                <div class="card">
                    <h3>📚 学习投入度评分</h3>
                    <h1 style="color: {color}; text-align: center; font-size: 36px;">{student_data['engagement_score']}</h1>
                    <p style="text-align: center;">投入程度: <strong>{engagement_level}</strong></p>
                    <div style="height: 10px; background: #eee; border-radius: 5px; margin-top: 10px;">
                        <div style="width: {student_data['engagement_score']}%; height: 100%; background: {color}; border-radius: 5px;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            # 挂科风险科目数量
            fail_courses = [course for course, risk in student_data["fail_risk"].items() if risk in ["高", "中"]]
            num_fail_risk = len(fail_courses)

            risk_color = "red" if num_fail_risk > 2 else ("orange" if num_fail_risk > 0 else "green")
            risk_level = "高" if num_fail_risk > 2 else ("中" if num_fail_risk > 0 else "低")

            st.markdown(f"""
                <div class="card">
                    <h3>❌ 挂科风险科目</h3>
                    <h1 style="color: {risk_color}; text-align: center; font-size: 36px;">{num_fail_risk}</h1>
                    <p style="text-align: center;">风险等级: <strong>{risk_level}</strong></p>
                    <p style="text-align: center; font-size: 12px;">{', '.join(fail_courses) if fail_courses else '无高风险科目'}</p>
                </div>
            """, unsafe_allow_html=True)

        # 学科关联度分析
        st.markdown('<h3 class="section-title">🔗 学科关联度分析</h3>', unsafe_allow_html=True)

        # 创建关联度矩阵
        subjects = list(student_data["grades"].keys())
        corr_matrix = np.zeros((len(subjects), len(subjects)))

        for i in range(len(subjects)):
            for j in range(len(subjects)):
                if i == j:
                    corr_matrix[i][j] = 1.0
                elif i < j:
                    key = f"{subjects[i]} & {subjects[j]}"
                    corr_matrix[i][j] = student_data["subject_correlation"].get(key, 0.5)
                    corr_matrix[j][i] = corr_matrix[i][j]

        # 绘制热力图
        fig = px.imshow(
            corr_matrix,
            labels=dict(x="课程", y="课程", color="关联度"),
            x=subjects,
            y=subjects,
            color_continuous_scale="Blues",
            text_auto=".2f",
            aspect="auto"
        )
        fig.update_layout(title="学科关联度热力图")
        st.plotly_chart(fig, use_container_width=True)

        # 个性化学习方案
        st.markdown('<h2 class="section-title">📝 个性化学习方案</h2>', unsafe_allow_html=True)

        learning_plan_card = st.container()
        with learning_plan_card:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 🎯 学习建议")

            for item in student_data["learning_plan"]:
                if item.startswith("-"):
                    st.markdown(f'<div style="margin-left: 20px; margin-bottom: 8px;">{item}</div>',
                                unsafe_allow_html=True)
                elif item.startswith("注意:"):
                    st.markdown(f'<div style="color: #e74c3c; margin-bottom: 8px;">{item}</div>',
                                unsafe_allow_html=True)
                elif item.startswith("建议:"):
                    st.markdown(f'<div style="color: #2ecc71; margin-bottom: 8px;">{item}</div>',
                                unsafe_allow_html=True)
                else:
                    st.markdown(f'<div style="margin-bottom: 8px;"><strong>{item}</strong></div>',
                                unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

        # 显示AI分析组件
        show_ai_analysis(student_data)

        # 返回首页按钮
        if st.button("← 返回首页", key="back_to_home_bottom"):
            st.session_state.current_page_academic_analysis = "home"
            st.rerun()

    if "current_page_academic_analysis" not in st.session_state:
        st.session_state.current_page_academic_analysis = "home"

    # 处理页面导航
    if st.session_state.current_page_academic_analysis == "home":
        show_home_page()
    elif st.session_state.current_page_academic_analysis == "student_detail":
        show_student_detail_page()
def all_academics():
    # 加载动画
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_sk5h1kfn.json")

    # CSS样式
    st.markdown("""
    <style>
    /* 主容器样式 */
    .main-container {
        padding: 2rem;
        max-width: 1800px;
        margin: auto;
    }

    /* 标题样式 */
    .header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        margin-bottom: 1.5rem;
        text-align: center;
        animation: fadeIn 1.5s;
    }

    /* 卡片样式 */
    .card {
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }

    .card-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
    }

    /* 图表容器 */
    .chart-container {
        margin-top: 1rem;
    }

    /* 动画效果 */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* 指标卡片样式 */
    .metric-card {
        border-left: 5px solid #1f77b4;
        padding: 1rem;
        margin: 0.5rem;
        border-radius: 8px;
    }

    /* 风险等级标签 */
    .risk-tag {
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.8rem;
    }

    .risk-low {
        background-color: #d4edda;
        color: #155724;
    }

    .risk-medium {
        background-color: #fff3cd;
        color: #856404;
    }

    .risk-high {
        background-color: #f8d7da;
        color: #721c24;
    }

    /* 干预措施卡片 */
    .intervention-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }

    .intervention-card:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    /* 响应式布局 */
    @media (max-width: 768px) {
        .header {
            font-size: 2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # 模拟数据生成函数
    def generate_mock_data():
        # 课程成绩数据
        courses = ['高等数学', '大学物理', '数据结构', '英语', '线性代数']
        grades = ['大一', '大二', '大三', '大四']
        pass_rates = pd.DataFrame({
            '课程': np.tile(courses, len(grades)),
            '年级': np.repeat(grades, len(courses)),
            '通过率': np.random.uniform(0.7, 0.98, len(courses) * len(grades))
        })

        # 考勤数据
        classes = [f'班级{i}' for i in range(1, 11)]
        attendance = pd.DataFrame({
            '班级': classes,
            '出勤率': np.random.uniform(0.85, 0.98, len(classes)),
            '旷课率': 1 - np.random.uniform(0.85, 0.98, len(classes))
        })

        # 作业提交数据
        assignments = pd.DataFrame({
            '课程': courses,
            '提交率': np.random.uniform(0.75, 0.95, len(courses))
        })

        # 图书馆数据
        months = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
        library = pd.DataFrame({
            '月份': months,
            '借阅量': np.random.randint(500, 1500, len(months))
        })
        popular_books = pd.DataFrame({
            '书名': ['Python编程', '机器学习', '算法导论', '数据库系统', '计算机网络'],
            '借阅次数': np.random.randint(200, 500, 5)
        })

        # 学业预警数据
        # students = [f'学生{i}' for i in range(1, 501)]
        # 学生名称修改
        students = [
            "王思远", "李婧怡", "张子轩", "刘雨桐", "陈昊然", "杨紫彤", "赵志远", "黄梦婷", "吴梓豪", "周可欣",
            "郑一帆", "孙佳怡", "马承志", "朱宇航", "胡欣然", "郭子睿", "林雨馨", "何俊杰", "高诗涵", "罗思源",
            "宋佳琪", "谢晨曦", "唐浩然", "邓可儿", "许梓涵", "韩宇泽", "冯芷萱", "曹睿哲", "彭宸希", "萧子墨",
            "程欣妍", "尹晨雨", "陶俊熙", "袁嘉怡", "秦语嫣", "赖文博", "赖梓萱", "严浩轩", "贾婉琳", "黎思辰",
            "施凯文", "鲁子仪", "谭语嫣", "侯泽宇",  "白梓萌", "丁奕辰", "康妍希", "章宇哲", "戴心怡",
            "田志伟", "石慧敏", "夏彦霏", "杜梓睿", "魏梦琪", "范奕辰",  "冉梓诺", "廖俊铭",
            "裴子墨", "闫雪妍", "纪文轩", "熊雨辰", "陶思彤", "蒲晨曦", "温嘉乐", "宫子涵", "景昕怡", "梅泽铭",
            "欧阳浩然", "殷诗涵", "昌语嫣", "路宸轩", "丁心妍", "花宇杰", "边沛然", "芦梓琳",
            "晏诗琪", "裴若曦", "储子辰", "邬梦涵", "戚嘉怡", "訾皓宇", "成语彤", "昌可欣", "茅泽宇", "倪妍妍",
            "柴浩宸", "阚梓宁", "管紫嫣", "厉雨泽", "龚婧怡", "杭泽霖", "丰嘉辰", "左语嫣", "童一诺", "屈子墨",
            "庄宇萱", "边昕妍", "苗俊凯", "温佳怡", "燕泽远", "权奕辰",  "党一帆", "翟宇彤", "郜梓宸",
            "滕宛妍", "米嘉昊",  "郁梓轩", "焦梦妍", "严涵宇", "车思妍", "项辰曦",
            "游俊熙", "郁昕怡", "商乐怡", "臧宇航", "邝文睿", "雍芷萱", "籍紫涵",
            "隗天怡", "戎雨萌", "祖宸逸", "经乐妍", "柏志强",  "燕嘉妍", "巫俊豪", "蔚子骞",
            "东语嫣", "慎晨曦", "鞠子诺",
            "墨子瑞", "南子安",  "臧宇航", "索婉妍", "卞心妍",  "淳嘉仪", "单梓妍",
            "胥嘉铭",   "季语嫣", "岳紫彤","权俊逸", "冷欣怡",
            "庞宇轩",  "梅心怡", "禹泽宇", "苗语嫣", "赖文睿", "费文杰", "冉昕怡",  "幸芷萱",
             "查语彤", "华思彤", "邸宇辰",  "富梓涵", "惠雨婷", "纪一诺",  "容俊豪",
            "崔奕辰",
            "米浩然", "涂雅妍", "幸俊豪"
            # 共 500 个名字
        ]
        risk_levels = ['低风险', '中风险', '高风险']
        risk_dist = pd.DataFrame({
            '风险等级': risk_levels,
            '人数': [350, 120, 30]
        })
        at_risk_students = pd.DataFrame({
            '学号': np.random.choice(students, 50, replace=False),
            '风险等级': np.random.choice(risk_levels, 50, p=[0.5, 0.3, 0.2]),
            '挂科科目数': np.random.randint(1, 5, 50)
        })

        # 学科关联度数据
        correlation_data = pd.DataFrame({
            '数学-物理': 0.72,
            '数学-编程': 0.65,
            '英语-文学': 0.58,
            '物理-化学': 0.68,
            '编程-算法': 0.81
        }, index=[0]).T.reset_index()
        correlation_data.columns = ['课程对', '相关性']

        # 学习投入度数据
        engagement = pd.DataFrame({
            '年级': grades,
            '投入度评分': np.random.uniform(60, 90, len(grades))
        })

        return {
            'pass_rates': pass_rates,
            'attendance': attendance,
            'assignments': assignments,
            'library': library,
            'popular_books': popular_books,
            'risk_dist': risk_dist,
            'at_risk_students': at_risk_students,
            'correlation_data': correlation_data,
            'engagement': engagement
        }

    # 加载数据
    data = generate_mock_data()

    # 页面布局
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # 标题和动画
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<div class="header">全系学业数据分析仪表盘</div>', unsafe_allow_html=True)
    with col2:
        st_lottie(lottie_animation, height=100, key="header-animation")

    # 数据概览 - 指标卡片
    st.markdown('<div class="card"><div class="card-header">📊 数据概览</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("学生总数", "500人", "较上月持平")
    col2.metric("平均通过率", "89.2%", "↑2.1%")
    col3.metric("高风险学生", "30人", "↓5人")
    col4.metric("平均投入度", "78.5分", "↑1.3分")

    style_metric_cards(background_color="#f8f9fa", border_left_color="#1f77b4")

    st.markdown('</div>', unsafe_allow_html=True)

    # 学业数据分析
    st.markdown('<div class="card"><div class="card-header">📚 学业数据分析</div>', unsafe_allow_html=True)

    # 选项卡布局
    tab1, tab2, tab3, tab4 = st.tabs(["课程成绩", "课堂考勤", "作业提交", "图书馆借阅"])

    with tab1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig = px.bar(data['pass_rates'], x='课程', y='通过率', color='年级',
                     barmode='group', title='各年级课程通过率对比')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig = px.bar(data['attendance'], x='班级', y='旷课率',
                     title='各班级旷课率统计', color='旷课率',
                     color_continuous_scale='RdYlGn_r')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig = px.pie(data['assignments'], names='课程', values='提交率',
                     title='各课程作业提交率')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig = px.line(data['library'], x='月份', y='借阅量',
                      title='月度图书馆借阅趋势')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.bar(data['popular_books'].sort_values('借阅次数', ascending=False),
                     x='书名', y='借阅次数', title='热门书籍排行')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 学业预警分析
    st.markdown('<div class="card"><div class="card-header">⚠️ 学业预警分析</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(data['risk_dist'], names='风险等级', values='人数',
                     title='学业风险等级分布',
                     color='风险等级',
                     color_discrete_map={'低风险': '#28a745', '中风险': '#ffc107', '高风险': '#dc3545'})
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.bar(data['at_risk_students'].groupby('挂科科目数').size().reset_index(name='人数'),
                     x='挂科科目数', y='人数',
                     title='高风险学生挂科科目数分布',
                     color='挂科科目数',
                     color_continuous_scale='RdYlGn_r')
        st.plotly_chart(fig, use_container_width=True)

    # 高风险学生表格
    st.markdown("**高风险学生名单**")
    risk_table = data['at_risk_students'][data['at_risk_students']['风险等级'] == '高风险'].head(10)
    st.dataframe(risk_table.style.applymap(lambda x: 'background-color: #f8d7da' if x == '高风险' else '',
                                           subset=['风险等级']),
                 use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 学科关联度分析
    st.markdown('<div class="card"><div class="card-header">🔗 学科关联度分析</div>', unsafe_allow_html=True)

    fig = px.bar(data['correlation_data'].sort_values('相关性'),
                 x='相关性', y='课程对',
                 title='学科成绩相关性分析',
                 color='相关性',
                 color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
    <h4 style="margin-top: 0;">分析洞察</h4>
    <ul>
    <li>编程与算法课程相关性最高(0.81)，建议对算法学习困难的学生加强编程基础训练</li>
    <li>数学与物理相关性为0.72，数学成绩差的学生物理成绩也普遍较低</li>
    <li>英语与文学相关性为0.58，相对其他学科关联较弱</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 学习投入度分析
    st.markdown('<div class="card"><div class="card-header">📈 学习投入度分析</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(data['engagement'], x='年级', y='投入度评分',
                     title='各年级学习投入度对比',
                     color='投入度评分',
                     color_continuous_scale='Greens')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # 模拟每日投入度数据
        days = pd.date_range(start='2023-09-01', periods=30)
        daily_engagement = pd.DataFrame({
            '日期': days,
            '投入度': np.random.normal(75, 10, 30).clip(50, 100)
        })

        fig = px.line(daily_engagement, x='日期', y='投入度',
                      title='近30天学习投入度趋势',
                      markers=True)
        fig.update_traces(line_color='#2ca02c', line_width=3)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 干预措施建议
    st.markdown('<div class="card"><div class="card-header">🛠️ 干预措施建议</div>', unsafe_allow_html=True)

    interventions = [
        {
            "title": "数学基础强化计划",
            "target": "数学成绩低于60分的学生",
            "actions": ["每周额外辅导课", "配对学习伙伴", "定制练习题库"],
            "goal": "提升数学通过率15%"
        },
        {
            "title": "高风险学生导师制",
            "target": "高风险等级学生",
            "actions": ["分配专业导师", "定期学习评估", "心理辅导支持"],
            "goal": "降低高风险学生比例20%"
        },
        {
            "title": "学习习惯养成计划",
            "target": "学习投入度低于60分的学生",
            "actions": ["时间管理培训", "学习方法讲座", "自习室打卡奖励"],
            "goal": "提升投入度评分10分"
        }
    ]

    for intervention in interventions:
        st.markdown(f"""
        <div class="intervention-card">
            <h3 style="margin-top: 0; color: #1f77b4;">{intervention['title']}</h3>
            <p><strong>目标群体:</strong> {intervention['target']}</p>
            <p><strong>干预措施:</strong> {", ".join(intervention['actions'])}</p>
            <p><strong>预期目标:</strong> {intervention['goal']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 页脚
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; color: #6c757d; font-size: 0.9rem;">
        <p>数据更新时间: {}</p>
        <p>© 2023 学生管理系统 - 教务数据分析中心</p>
    </div>
    """.format(pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
def Regularity_of_behavior():
    # 初始化 DeepSeek AI 客户端
    client = OpenAI(api_key="sk-24d37178569a4f9d9ee09925e6edffa5", base_url="https://api.deepseek.com")
    def analyze_behavior(data, student_name):
        """调用 DeepSeek AI 进行行为分析"""
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个行为分析专家。"},
                {"role": "user",
                 "content": f"请分析以下学生行为数据，给出专业的行为分析和建议，学生姓名: {student_name}, 数据: {data}"},
            ],
            stream=False
        )
        return response.choices[0].message.content


    def generate_student_database():
        """生成学生数据库"""
        students = {
            "2023001": {"姓名": "许文锦", "学院": "计算机学院", "专业": "计算机科学与技术"},
            "2023002": {"姓名": "付子毅", "学院": "经济学院", "专业": "金融学"},
            "2023003": {"姓名": "王进", "学院": "文学院", "专业": "汉语言文学"},
            "2023004": {"姓名": "张铭", "学院": "理学院", "专业": "数学与应用数学"},
            "2023005": {"姓名": "田国庆", "学院": "工程学院", "专业": "机械工程"},
        }

        # 为每个学生生成行为数据
        for student_id in students:
            name = students[student_id]["姓名"]
            np.random.seed(hash(name) % 1000)
            dates = pd.date_range(start="2024-03-01", periods=7, freq='D')

            # 根据姓名生成不同特征的数据
            if "许" in name:
                late_night = np.random.randint(0, 5, size=7)
                spending = np.random.randint(30, 200, size=7)
                fitness = np.random.randint(75, 90, size=7)
            elif "付" in name:
                late_night = np.random.randint(0, 2, size=7)
                spending = np.random.randint(20, 100, size=7)
                fitness = np.random.randint(80, 95, size=7)
            elif "王" in name:
                late_night = np.random.randint(2, 7, size=7)
                spending = np.random.randint(50, 300, size=7)
                fitness = np.random.randint(70, 85, size=7)
            else:
                late_night = np.random.randint(0, 3, size=7)
                spending = np.random.randint(40, 150, size=7)
                fitness = np.random.randint(78, 92, size=7)

            students[student_id]["行为数据"] = pd.DataFrame({
                "日期": dates,
                "凌晨出入次数": late_night,
                "单日消费": spending,
                "体能评分": fitness
            })

        return students


    def display_student_info(selected_student):
        """显示学生基本信息"""
        st.subheader("👨🎓 学生基本信息")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"**姓名**: {selected_student['姓名']}")
        with col2:
            st.markdown(f"**学号**: {next(k for k, v in student_db.items() if v['姓名'] == selected_student['姓名'])}")
        with col3:
            st.markdown(f"**学院专业**: {selected_student['学院']} {selected_student['专业']}")
        st.markdown("---")


    def display_behavior_overview(df):
        """显示行为概览"""
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📅 分析周期", f"{df['日期'].min().strftime('%Y-%m-%d')} 至 {df['日期'].max().strftime('%Y-%m-%d')}")
        with col2:
            avg_spending = df["单日消费"].mean()
            st.metric("💰 平均消费", f"{avg_spending:.1f} 元", "偏高" if avg_spending > 100 else "正常")
        with col3:
            avg_late = df["凌晨出入次数"].mean()
            st.metric("🌙 平均凌晨出入", f"{avg_late:.1f} 次", "偏高" if avg_late > 2 else "正常")
        st.markdown("---")


    def display_sleep_pattern(df):
        """显示作息规律分析"""
        st.subheader("⏰ 作息规律性分析")
        st.line_chart(df, x="日期", y="凌晨出入次数", color="#FF6B6B")

        late_score = 100 - (df["凌晨出入次数"].mean() * 10)
        late_score = max(0, min(100, late_score))
        st.progress(int(late_score), text=f"作息规律性评分: {late_score:.0f}/100")
        return late_score


    def display_spending_pattern(df):
        """显示消费模式分析"""
        st.subheader("💵 消费模式分析")

        # 创建消费异常标记
        df["消费异常"] = df["单日消费"] > 100
        st.bar_chart(df, x="日期", y="单日消费", color="消费异常")

        spending_std = df["单日消费"].std()
        stability_score = max(0, 100 - spending_std)
        st.progress(int(stability_score), text=f"消费稳定性评分: {stability_score:.0f}/100")
        return stability_score


    def display_fitness_trend(df):
        """显示体能健康趋势"""
        st.subheader("🏋️ 体能健康趋势")
        st.line_chart(df, x="日期", y="体能评分", color="#4ECDC4")

        fitness_score = df["体能评分"].mean()
        st.progress(int(fitness_score), text=f"平均体能评分: {fitness_score:.0f}/100")
        return fitness_score


    def display_radar_chart(late_score, stability_score, fitness_score):
        """显示雷达图"""

        st.subheader("📊 综合行为雷达图")

        # 模拟行为评分数据
        categories = ['作息规律', '消费稳定', '体能健康']
        values = [late_score, stability_score, fitness_score]

        # 创建雷达图
        fig = px.line_polar(
            r=values + [values[0]],  # 闭合图形
            theta=categories + [categories[0]],  # 闭合图形
            line_close=True,  # 闭合
            template="plotly_dark",  # 使用暗色主题
            title="综合行为分析雷达图"  # 添加标题
        )

        # 设置填充颜色
        fig.update_traces(fill='toself', fillcolor='rgba(255, 170, 166, 0.5)', line_color='red')

        fig.update_layout(
            plot_bgcolor='white',  # 绘图区域背景色
            paper_bgcolor='white',  # 整个图表区域背景色
            title_font=dict(color='black'),  # 设置标题字体颜色
            polar=dict(bgcolor='white')  # 设置极坐标背景色为白色
        )

        # 显示图表
        st.plotly_chart(fig, use_container_width=True)


    def display_raw_data(df):
        """显示原始数据"""
        st.subheader("📝 原始数据")
        st.dataframe(df.style.background_gradient(cmap='Blues'), use_container_width=True)


    # 主程序
    def Student_behavior_analysis():
        # 页面设置
        #st.set_page_config(layout="wide", page_title="学生行为规律分析系统")
        st.title("🎯 学生行为规律分析")
        st.markdown("---")

        # 初始化学生数据库
        global student_db
        student_db = generate_student_database()

        # 学生搜索选择
        col1, col2 = st.columns([1, 3])
        with col1:
            search_type = st.radio("搜索方式", ["按学号", "按姓名"], horizontal=True)
        with col2:
            if search_type == "按学号":
                student_id = st.selectbox("选择学号", list(student_db.keys()))
                selected_student = student_db[student_id]
            else:
                student_name = st.selectbox("选择姓名", [info["姓名"] for info in student_db.values()])
                selected_student = next(v for k, v in student_db.items() if v["姓名"] == student_name)

        # 获取学生数据
        df = selected_student["行为数据"]

        # 显示学生信息
        display_student_info(selected_student)

        # 显示行为概览
        display_behavior_overview(df)

        # 图表展示
        col1, col2 = st.columns(2)

        with col1:
            late_score = display_sleep_pattern(df.copy())

        with col2:
            stability_score = display_spending_pattern(df.copy())

        st.markdown("---")

        # 第三行图表
        col1, col2 = st.columns(2)

        with col1:
            fitness_score = display_fitness_trend(df.copy())

        with col2:
            display_radar_chart(late_score, stability_score, fitness_score)

        st.markdown("---")

        # 按需AI分析
        if st.button("🔍 请求AI行为分析", type="primary"):
            with st.spinner("AI正在分析学生行为数据..."):
                analysis_result = analyze_behavior(df.to_dict(), selected_student["姓名"])
                st.success("AI分析完成！")
                st.markdown(
                    f"<div style='background-color:#f8f9fa; padding:15px; border-radius:10px;'>{analysis_result}</div>",
                    unsafe_allow_html=True)

        # 原始数据
        display_raw_data(df)

        st.markdown("---")
        st.markdown("<div style='text-align: center; color: #6c757d;'>© 2024 学生行为分析系统 | 教育大数据研究中心</div>",
                    unsafe_allow_html=True)

    Student_behavior_analysis()
def ai_psychology():
    # 初始化DeepSeek客户端
    client = OpenAI(api_key="sk-24d37178569a4f9d9ee09925e6edffa5", base_url="https://api.deepseek.com")

    # 标题和介绍
    st.title("🌱 AI心理导师")
    st.markdown("""
    <div style="background-color:#f0f2f6;padding:20px;border-radius:10px;margin-bottom:20px;">
        <h3 style="color:#2e86c1;">您好，我是您的AI心理导师</h3>
        <p>我可以帮助您：</p>
        <ul>
            <li>分析情绪困扰和压力源</li>
            <li>提供专业的心理调适建议</li>
            <li>解释常见的心理现象和机制</li>
            <li>推荐科学的心理自助方法</li>
        </ul>
        <p>请随时向我倾诉您的心理困惑或问题👇</p>
    </div>
    """, unsafe_allow_html=True)

    # 初始化对话历史
    if "messages_ai_psychology" not in st.session_state:
        st.session_state.messages_ai_psychology = []
        st.session_state.messages_ai_psychology.append({
            "role": "assistant",
            "content": "您好！我是您的AI心理导师。无论您正经历情绪困扰、压力挑战，"
                       "还是对某些心理现象感到好奇，都可以随时向我咨询。我会用专业的心理学知识"
                       "为您提供支持和指导。今天有什么想和我聊聊的吗？"
        })

    # 显示对话历史
    for message in st.session_state.messages_ai_psychology:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 用户输入
    if prompt := st.chat_input("请输入您的心理困惑或问题..."):
        st.session_state.messages_ai_psychology.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 构建专业心理咨询提示词
        system_prompt = """
        你是一位资深的心理咨询师，拥有10年临床经验，擅长认知行为疗法和正念治疗。
        请根据以下原则与用户交流：
        1. 首先共情和理解用户的感受
        2. 用专业但易懂的语言解释心理机制
        3. 提供具体可行的建议和方法
        4. 适当使用隐喻和例子帮助理解
        5. 保持温暖、支持性的语气
        6. 必要时推荐专业求助渠道

        示例：
        用户：失恋了。怎么办？
        Ai：**当爱成为一场地震：你的重建指南**

    失去深爱的人就像经历心灵的地震，那种天崩地裂般的痛楚、空荡如废墟般的心境，都
    是你真诚投入过的证明。不必指责自己“为何放不下”，也不必急于对明天做出承诺—
    —请先给自己一片停泊的空间。

    ---

    ### **第一步：与痛苦温柔相处**
    - **给情绪一个容器**  
      找一处安静角落，写下或录下所有翻涌的感受：“我好恨/好害怕...” 写完后轻轻
    把纸叠成小船放入水池，或是按下删除键。这不是告别悲伤的仪式，而是让情绪有个安
    放的空间。

    - **与身体重建联结**  
      当胃部绞痛袭来时，试试用温热毛巾敷在胸口；失眠时播放自然白噪音（雨声、篝火
    ），想象被整片森林温柔包裹。生理上的安抚会像锚点般稳住情绪的波动。

    ---

    ### **第二步：搭建临时庇护所**
    - **5分钟自救清单**  
      列出3件只需5分钟就能完成的小事（例如：给绿植擦亮叶片、用旧报纸折小动物）。
    每天任选一项进行——微光会逐渐照亮黑暗。

    - **创造安全社交模式**  
      如果倾诉吃力，可以分享：“今天看到晚霞特别美”或“突然想起那家咖啡馆换了新
    菜单”。用回忆作桥梁而非利刃，让关心你的人循着你的节奏靠近。

    ---

    ### **第三步：重新绘制自我地貌**
    - **书写平行时空日记**  
      每天记录10分钟：“今天我注意到...”（例如：咖啡杯的拉花像天鹅）。不评判好
    坏，只是练习把注意力转向世界的丰盛。

    - **设计专属治愈仪式**  
      培育豌豆苗这类生长周期短的植物，每天观察变化；或收集不同材质的纸做成拼贴画
    。亲手创造的生命力会见证重生的力量。

    ---

    ### **重要提醒**
    若出现持续性躯体化症状（心悸、社交回避）或自我否定加剧，请像对待高烧般接纳需
    要专业帮助的事实——这不是软弱，而是对自己的温柔。

    ---

    **最后想对你说：**  
    那些让你夜不能寐的思念，在某天清晨会化作回忆的晨雾。你依然记得玫瑰绽放时的美
    好与刺痛，但此刻被灼伤的地方，正在生长出更坚韧的皮肤。世界和我都在这里，等待
    你慢慢站起来。


        当前对话背景：
        """

        # 显示AI回复
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            # 流式获取响应
            for chunk in client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages_ai_psychology]
                    ],
                    stream=True,
                    temperature=0.7
            ):
                content = chunk.choices[0].delta.content or ""
                full_response += content
                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        st.session_state.messages_ai_psychology.append({"role": "assistant", "content": full_response})

    # 页脚
    st.markdown("""
    <div style="text-align:center;margin-top:30px;color:#7f8c8d;font-size:0.9em;">
        <p>💡 温馨提示：AI建议不能替代专业心理咨询</p>
        <p>如需深度帮助，请联系当地心理咨询机构</p>
    </div>
    """, unsafe_allow_html=True)
def Campus_behavior_data():
    # 初始化 DeepSeek AI 客户端
    client = OpenAI(api_key="sk-24d37178569a4f9d9ee09925e6edffa5", base_url="https://api.deepseek.com")

    # 自定义CSS样式
    def inject_custom_css():
        st.markdown("""
        <style>
            /* 主标题样式 */
            .main-title {
                font-size: 2.5rem;
                font-weight: 700;
                background: linear-gradient(90deg, #0066ff, #00ccff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-align: center;
                margin-bottom: 0.5rem;
            }

            /* 副标题样式 */
            .subheader {
                font-size: 1.2rem;
                color: #666;
                text-align: center;
                margin-bottom: 2rem;
            }

            /* 数据卡片样式 */
            .data-card {
                border-radius: 10px;
                padding: 15px;
                background-color: rgba(0, 102, 255, 0.1);
                border-left: 4px solid #0066ff;
                margin-bottom: 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            }

            /* 指标卡片样式 */
            .metric-card {
                border-radius: 10px;
                padding: 15px;
                background-color: #f8f9fa;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            }

            /* 图表容器样式 */
            .chart-container {
                border-radius: 10px;
                padding: 15px;
                background-color: white;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }

            /* 加载动画 */
            @keyframes pulse {
                0% { opacity: 0.6; }
                50% { opacity: 1; }
                100% { opacity: 0.6; }
            }
            .pulse {
                animation: pulse 1.5s infinite;
            }

            /* 网格背景 */
            .grid-bg {
                background-image: 
                    linear-gradient(rgba(0, 102, 255, 0.05) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0, 102, 255, 0.05) 1px, transparent 1px);
                background-size: 20px 20px;
            }
        </style>
        """, unsafe_allow_html=True)

    def generate_student_database():
        """生成学生数据库，包括学生基本信息和行为数据"""
        students = {
            "2023001": {"姓名": "许文锦", "学院": "计算机学院", "专业": "计算机科学与技术", "年级": "大三"},
            "2023002": {"姓名": "付子毅", "学院": "经济学院", "专业": "金融学", "年级": "大二"},
            "2023003": {"姓名": "王进", "学院": "文学院", "专业": "汉语言文学", "年级": "大一"},
            "2023004": {"姓名": "张铭", "学院": "理学院", "专业": "数学与应用数学", "年级": "大四"},
            "2023005": {"姓名": "田国庆", "学院": "工程学院", "专业": "机械工程", "年级": "大三"},
        }

        # 为每个学生生成行为数据
        for student_id in students:
            name = students[student_id]["姓名"]
            np.random.seed(hash(name) % 1000)
            dates = pd.date_range(start="2024-03-01", periods=30, freq='D')  # 生成30天数据

            if "许" in name:
                late_night = np.random.poisson(3, size=30)
                spending = np.random.normal(150, 30, size=30).clip(30, 300)
                fitness = np.random.normal(80, 5, size=30).clip(70, 95)
                library = np.random.poisson(5, size=30)
            elif "付" in name:
                late_night = np.random.poisson(1, size=30)
                spending = np.random.normal(80, 15, size=30).clip(20, 150)
                fitness = np.random.normal(90, 3, size=30).clip(80, 100)
                library = np.random.poisson(8, size=30)
            elif "王" in name:
                late_night = np.random.poisson(5, size=30)
                spending = np.random.normal(200, 50, size=30).clip(50, 400)
                fitness = np.random.normal(75, 8, size=30).clip(60, 90)
                library = np.random.poisson(2, size=30)
            else:
                late_night = np.random.poisson(2, size=30)
                spending = np.random.normal(120, 25, size=30).clip(40, 200)
                fitness = np.random.normal(85, 4, size=30).clip(75, 95)
                library = np.random.poisson(4, size=30)

            students[student_id]["行为数据"] = pd.DataFrame({
                "日期": dates,
                "凌晨出入次数": late_night,
                "单日消费(元)": spending.round(2),
                "体能评分": fitness.round(1),
                "图书馆停留(小时)": library.clip(0, 10)
            })

        return students

    def create_digital_dashboard(students_data):
        """创建数字化仪表板"""
        all_behavior_df = pd.concat([info["行为数据"].assign(学生姓名=info["姓名"])
                                     for info in students_data.values()], ignore_index=True)

        # 计算关键指标
        total_students = len(students_data)
        total_records = len(all_behavior_df)
        avg_late_night = all_behavior_df["凌晨出入次数"].mean().round(2)
        avg_spending = all_behavior_df["单日消费(元)"].mean().round(2)

        # 创建指标卡片
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>👨‍🎓 监测学生</h3>
                <h1 style="color: #0066ff;">{total_students}</h1>
                <p>人</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>📊 数据记录</h3>
                <h1 style="color: #0066ff;">{total_records}</h1>
                <p>条</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h3>🌙 平均晚归</h3>
                <h1 style="color: #0066ff;">{avg_late_night}</h1>
                <p>次/日</p>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3>💰 平均消费</h3>
                <h1 style="color: #0066ff;">{avg_spending}</h1>
                <p>元/日</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

    def create_tech_radar_chart(students_data):
        """创建科技感雷达图"""
        all_behavior_df = pd.concat([info["行为数据"].assign(学生姓名=info["姓名"])
                                     for info in students_data.values()], ignore_index=True)
        avg_scores = all_behavior_df.groupby('学生姓名').agg({
            '凌晨出入次数': 'mean',
            '单日消费(元)': 'mean',
            '体能评分': 'mean',
            '图书馆停留(小时)': 'mean'
        }).reset_index()

        # 标准化指标
        normalized = avg_scores.copy()
        normalized['作息规律'] = 10 - (normalized['凌晨出入次数'] / normalized['凌晨出入次数'].max() * 10)
        normalized['消费健康'] = 10 - (abs(normalized['单日消费(元)'] - 120) / 50 * 10).clip(0, 10)
        normalized['体能指数'] = normalized['体能评分'] / 10
        normalized['学习投入'] = normalized['图书馆停留(小时)'] / normalized['图书馆停留(小时)'].max() * 10

        # 创建雷达图
        fig = px.line_polar(
            normalized,
            r=[10, 8, 6, 4, 2, 0],  # 网格线
            theta=[''] * 6,  # 空标签
            line_close=True,
            template="plotly_dark",
            color_discrete_sequence=['rgba(0, 102, 255, 0.1)'],
            height=500
        )

        # 添加每个学生的雷达图
        for idx, row in normalized.iterrows():
            fig.add_trace(px.line_polar(
                r=[row['作息规律'], row['消费健康'], row['体能指数'], row['学习投入'], row['作息规律']],
                theta=['作息规律', '消费健康', '体能指数', '学习投入', '作息规律'],
                line_close=True
            ).data[0])

        # 更新布局
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10],
                    tickfont=dict(color='white'),
                    gridcolor='rgba(255, 255, 255, 0.2)',
                    linecolor='rgba(255, 255, 255, 0.5)'
                ),
                angularaxis=dict(
                    tickfont=dict(color='white'),
                    gridcolor='rgba(255, 255, 255, 0.2)',
                    linecolor='rgba(255, 255, 255, 0.5)'
                ),
                bgcolor='rgba(0, 0, 0, 0)'
            ),
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            font=dict(color='white'),
            title=dict(
                text='<b>学生行为多维分析雷达图</b>',
                font=dict(size=18),
                x=0.5
            ),
            margin=dict(t=50, b=30, l=30, r=30),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5
            )
        )

        # 设置轨迹样式
        for i, trace in enumerate(fig.data[1:]):  # 跳过第一个基础网格
            trace.update(
                line=dict(color=px.colors.qualitative.Plotly[i], width=2),
                fill='toself',
                fillcolor=px.colors.qualitative.Plotly[i].replace('rgb', 'rgba').replace(')', ', 0.2)'),
                name=normalized.iloc[i]['学生姓名']
            )

        return fig

    def create_network_graph(students_data):
        """创建虚拟社交网络图"""
        # 模拟社交关系
        names = [info["姓名"] for info in students_data.values()]
        connections = []

        for i, name1 in enumerate(names):
            for j, name2 in enumerate(names):
                if i < j and np.random.random() < 0.3:  # 30%概率有连接
                    weight = np.random.randint(1, 5)
                    connections.append((name1, name2, weight))

        # 创建网络图
        fig = px.scatter(
            x=[0], y=[0],  # 虚拟数据
            title="<b>学生社交网络分析</b>"
        )

        # 添加连接线
        for conn in connections:
            fig.add_shape(
                type="line",
                x0=np.random.uniform(-1, 1),
                y0=np.random.uniform(-1, 1),
                x1=np.random.uniform(-1, 1),
                y1=np.random.uniform(-1, 1),
                line=dict(
                    color=f"rgba(0, 102, 255, {conn[2] / 5})",
                    width=conn[2]
                )
            )

        # 添加节点
        for i, name in enumerate(names):
            fig.add_trace(px.scatter(
                x=[np.random.uniform(-1, 1)],
                y=[np.random.uniform(-1, 1)],
                text=[name]
            ).data[0].update(
                marker=dict(
                    size=20,
                    color="#0066ff",
                    line=dict(width=2, color="white")
                ),
                textposition="middle center",
                textfont=dict(color="white", size=12)
            ))

        # 更新布局
        fig.update_layout(
            plot_bgcolor="rgba(0, 0, 0, 0)",
            paper_bgcolor="rgba(0, 0, 0, 0)",
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            showlegend=False,
            height=400,
            margin=dict(t=50, b=30, l=30, r=30)
        )

        return fig

    def create_real_time_feed(students_data):
        """创建实时数据流（带滚屏效果）"""
        with st.expander("📡 实时行为数据流", expanded=True):
            # 创建3个空位用于显示滚屏数据
            placeholders = [st.empty() for _ in range(3)]

            # 存储最近3条消息
            messages = []

            for i in range(100):  # 总共显示100条数据
                student_id = np.random.choice(list(students_data.keys()))
                student = students_data[student_id]
                behavior = np.random.choice(["凌晨出入", "食堂消费", "图书馆签到", "体测记录"])

                if behavior == "凌晨出入":
                    timi = f"{np.random.randint(0, 6)}:{np.random.randint(0, 60):02d}"
                    text = f"{student['姓名']} 于凌晨 {timi} 进出宿舍"
                elif behavior == "食堂消费":
                    amount = np.random.randint(500, 3000) / 100
                    text = f"{student['姓名']} 在食堂消费 {amount} 元"
                elif behavior == "图书馆签到":
                    hours = np.random.uniform(10, 60) / 10
                    text = f"{student['姓名']} 在图书馆学习 {hours:.1f} 小时"
                else:
                    score = np.random.randint(60, 100)
                    text = f"{student['姓名']} 体测成绩更新: {score} 分"

                timestamp = time.strftime("%H:%M:%S", time.localtime())

                # 添加新消息到列表
                messages.append({
                    "text": text,
                    "timestamp": timestamp
                })

                # 只保留最近3条消息
                if len(messages) > 3:
                    messages = messages[-3:]

                # 更新显示
                for j, msg in enumerate(messages):
                    placeholders[j].markdown(f"""
                    <div class="data-card">
                        <div style="display: flex; justify-content: space-between;">
                            <span>{msg['text']}</span>
                            <span style="color: #666; font-size: 0.8rem;">{msg['timestamp']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                # 填充剩余空位（如果有）
                for j in range(len(messages), 3):
                    placeholders[j].markdown("")

                time.sleep(1.5)  # 刷新间隔改为1.5秒

    def analyze_behavior(data, question=None):
        """调用 DeepSeek AI 进行行为分析"""
        prompt = "你是一个大数据分析专家，请从以下学生行为数据中分析模式、异常和洞察:"
        if question:
            prompt = f"{prompt}\n用户问题: {question}\n数据: {data}"
        else:
            prompt = f"{prompt} {data}"

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个大数据分析专家，擅长从学生行为数据中发现模式、异常和洞察。"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content

    def zhongtixingweifenxi():
        """主应用"""
        inject_custom_css()

        # 添加科技感背景
        st.markdown('<div class="grid-bg">', unsafe_allow_html=True)

        # 标题区域
        st.markdown('<h1 class="main-title">智慧校园行为大数据总览</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subheader">基于多维度行为数据的实时分析与预测</p>', unsafe_allow_html=True)

        # 生成学生数据
        with st.spinner("🔄 正在加载学生行为数据..."):
            students_data = generate_student_database()
            time.sleep(1)  # 模拟加载延迟

        # 数字仪表板
        create_digital_dashboard(students_data)

        # 第一行图表
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.plotly_chart(create_tech_radar_chart(students_data), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.plotly_chart(create_network_graph(students_data), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 第二行图表
        all_behavior_df = pd.concat([info["行为数据"].assign(学生姓名=info["姓名"])
                                     for info in students_data.values()], ignore_index=True)

        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig = px.line(
            all_behavior_df,
            x="日期",
            y="单日消费(元)",
            color="学生姓名",
            title="<b>学生消费趋势分析</b>",
            line_shape="spline",
            render_mode="svg"
        )
        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(gridcolor="rgba(0, 0, 0, 0.1)"),
            yaxis=dict(gridcolor="rgba(0, 0, 0, 0.1)"),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5
            )
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # AI分析区域
        st.markdown("---")
        st.markdown('<h2 style="color: #0066ff;">🔍 AI行为分析引擎</h2>', unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["自动分析", "智能问答"])

        with tab1:
            if st.button("🚀 启动深度行为分析", type="primary"):
                with st.spinner("AI正在分析行为模式..."):
                    analysis_result = analyze_behavior(all_behavior_df.to_dict())
                    st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, rgba(0, 102, 255, 0.1), rgba(0, 204, 255, 0.1));
                        padding: 20px;
                        border-radius: 10px;
                        border-left: 4px solid #0066ff;
                        margin-top: 20px;
                    ">
                        <h4 style="color: #0066ff; margin-top: 0;">AI分析结果</h4>
                        <p>{analysis_result}</p>
                    </div>
                    """, unsafe_allow_html=True)

        with tab2:
            question = st.text_area("向AI提问关于学生行为数据的问题:", height=100,
                                    placeholder="例如: 哪些学生有异常行为模式?")
            if st.button("📩 提交问题", type="primary"):
                if question.strip():
                    with st.spinner("AI正在思考..."):
                        response = analyze_behavior(all_behavior_df.to_dict(), question)
                        st.markdown(f"""
                        <div style="
                            background: linear-gradient(135deg, rgba(0, 102, 255, 0.1), rgba(0, 204, 255, 0.1));
                            padding: 20px;
                            border-radius: 10px;
                            border-left: 4px solid #0066ff;
                            margin-top: 20px;
                        ">
                            <h4 style="color: #0066ff; margin-top: 0;">AI回答</h4>
                            <p>{response}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("请输入问题")
        # 实时数据流
        create_real_time_feed(students_data)

    zhongtixingweifenxi()
def student_social_network_page():
    @st.cache_data(ttl=3600)  # Cache data for 1 hour
    def generate_student_database():
        students = {
            "20231001": {"姓名": "王思远", "学院": "计算机学院", "专业": "计算机科学与技术"},
            "20231002": {"姓名": "李婧怡", "学院": "经济学院", "专业": "金融学"},
            "20231003": {"姓名": "张子轩", "学院": "理学院", "专业": "数学"},
            "20231004": {"姓名": "陈昊然", "学院": "文学院", "专业": "汉语言文学"},
            "20231005": {"姓名": "何俊杰", "学院": "工程学院", "专业": "机械工程"},
        }

        for student_id in students:
            name = students[student_id]["姓名"]
            np.random.seed(hash(name) % 1000)

            # Generate online activity data
            online_activity_data = {
                "平台": ["校园表白墙", "微信群聊", "在线讲座", "论坛互动"],
                "时间": [f"{random.randint(8, 22)}:{random.randint(0, 59):02d}" for _ in range(4)],
                "活跃度": [random.randint(1, 5) for _ in range(4)]
            }

            # Generate offline activity data
            offline_activity_data = {
                "活动名称": ["志愿服务", "社团活动", "校外调研", "校内讲座"],
                "时间": [f"2024-03-{random.randint(1, 7)} {random.randint(9, 18)}:{random.randint(0, 59):02d}" for _ in
                         range(4)],
                "参与度": [random.randint(1, 5) for _ in range(4)]
            }

            # Generate peer network data
            peer_network_data = {
                "学生ID": list(students.keys()),
                "互动频率": [random.randint(1, 10) for _ in students.keys()],
                "关系强度": [random.choice(["弱", "中", "强"]) for _ in students.keys()]
            }

            students[student_id]["线上社交平台活跃度"] = pd.DataFrame(online_activity_data)
            students[student_id]["线下活动参与记录"] = pd.DataFrame(offline_activity_data)
            students[student_id]["朋辈关系网络"] = pd.DataFrame(peer_network_data)

        return students
    @st.cache_resource(ttl=3600)  # Cache the client for 1 hour
    def get_openai_client():
        return OpenAI(api_key="sk-24d37178569a4f9d9ee09925e6edffa5", base_url="https://api.deepseek.com")
    def analyze_social_disorder(student):
        client = get_openai_client()
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个社交网络分析助手。"},
                {"role": "user", "content": f"请分析学生 {student['姓名']} 的社交障碍情况。"},
            ],
            stream=False
        )
        return response.choices[0].message.content
    def recommend_club(student):
        client = get_openai_client()
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个社交网络分析助手，负责推荐合适的社团活动。"},
                {"role": "user", "content": f"根据学生 {student['姓名']} 的社交行为，推荐一个适合的社团活动。"},
            ],
            stream=False
        )
        return response.choices[0].message.content
    def ask_ai_question(question, student_info):
        client = get_openai_client()
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个学生社交网络分析助手，能够根据学生的社交数据提供专业建议。"},
                {"role": "user", "content": f"学生信息: {student_info}\n\n问题: {question}"},
            ],
            stream=False
        )
        return response.choices[0].message.content
    def student_social_network_page():
        # st.set_page_config(page_title="学生社交分析", layout="wide")
        st.title("学生社交分析")
        # Custom CSS for styling
        st.markdown("""
        <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
        }
        .stDataFrame {
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stPlotlyChart {
            border-radius: 10px;
        }
        .student-selector {
            margin-bottom: 2rem;
            padding: 1rem;
            background-color: #e9f7ef;
            border-radius: 10px;
        }
        .ai-query-box {
            margin-top: 2rem;
            padding: 1.5rem;
            background-color: #f0f8ff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)

        students_data = generate_student_database()

        # Student selector in main content area
        st.markdown('<div class="student-selector">', unsafe_allow_html=True)
        student_id = st.selectbox("选择学生", list(students_data.keys()),
                                  format_func=lambda x: f"{x} - {students_data[x]['姓名']} ({students_data[x]['学院']})")
        st.markdown('</div>', unsafe_allow_html=True)

        student = students_data[student_id]

        st.header(f"👤 {student['姓名']} 同学的社交网络分析")
        st.markdown(f"**学院**: {student['学院']} | **专业**: {student['专业']}")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📱 线上社交平台活跃度")
            online_df = student["线上社交平台活跃度"]
            fig = px.bar(online_df, x="平台", y="活跃度", color="平台",
                         title="各平台活跃度对比")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(online_df.style.background_gradient(cmap="Blues"))

        with col2:
            st.subheader("🏃 线下活动参与记录")
            offline_df = student["线下活动参与记录"]
            fig = px.pie(offline_df, names="活动名称", values="参与度",
                         title="活动参与分布")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(offline_df.style.background_gradient(cmap="Greens"))

        st.subheader("🔗 朋辈关系网络")
        peer_df = student["朋辈关系网络"]
        fig = px.scatter(peer_df, x="学生ID", y="互动频率", size="互动频率",
                         color="关系强度", hover_name="学生ID",
                         title="朋辈关系网络可视化")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(peer_df.style.background_gradient(cmap="Purples"))

        st.markdown("---")
        st.subheader("🤖 AI 分析建议")

        if st.button("分析社交障碍"):
            with st.spinner("AI正在分析中..."):
                analysis = analyze_social_disorder(student)
                st.success("分析完成")
                st.markdown(f"<div style='background-color:#f0f8ff; padding:15px; border-radius:10px;'>{analysis}</div>",
                            unsafe_allow_html=True)

        if st.button("推荐适合社团"):
            with st.spinner("AI正在推荐中..."):
                recommendation = recommend_club(student)
                st.success("推荐完成")
                st.markdown(
                    f"<div style='background-color:#f0fff0; padding:15px; border-radius:10px;'>{recommendation}</div>",
                    unsafe_allow_html=True)

        # Free-form AI query section
        st.markdown("---")
        st.subheader("💬 自由咨询AI助手")

        with st.container():
            st.markdown('<div class="ai-query-box">', unsafe_allow_html=True)

            question = st.text_area("请输入您关于该学生社交情况的任何问题:",
                                    placeholder="例如: 如何帮助这位学生改善社交能力? 或者分析他的社交网络特点...",
                                    height=100)

            student_info = {
                "姓名": student["姓名"],
                "学院": student["学院"],
                "专业": student["专业"],
                "线上活跃度": student["线上社交平台活跃度"].to_dict(),
                "线下活动": student["线下活动参与记录"].to_dict(),
                "朋辈网络": student["朋辈关系网络"].to_dict()
            }

            if st.button("提交问题", key="ask_ai"):
                if question.strip():
                    with st.spinner("AI正在思考中..."):
                        answer = ask_ai_question(question, student_info)
                        st.success("AI回复:")
                        st.markdown(
                            f"<div style='background-color:#ffffff; padding:15px; border-radius:10px; margin-top:10px;'>{answer}</div>",
                            unsafe_allow_html=True)
                else:
                    st.warning("请输入问题后再提交")

            st.markdown('</div>', unsafe_allow_html=True)
    student_social_network_page()
def overall_social_network_page():
    def get_openai_client():
        return OpenAI(api_key="sk-24d37178569a4f9d9ee09925e6edffa5", base_url="https://api.deepseek.com")
    @st.cache_data(ttl=3600)  # Cache data for 1 hour
    def generate_student_database():
        students = {
            "2023001": {"姓名": "王思远", "学院": "计算机学院", "专业": "计算机科学与技术"},
            "2023002": {"姓名": "李婧怡", "学院": "商学院'", "专业": "金融学"},
            "2023003": {"姓名": "张子轩", "学院": "理学院", "专业": "数学"},
            "2023004": {"姓名": "陈昊然", "学院": "文学院", "专业": "汉语言文学"},
            "2023005": {"姓名": "何俊杰", "学院": "工程学院", "专业": "机械工程"},
        }

        for student_id in students:
            name = students[student_id]["姓名"]
            np.random.seed(hash(name) % 1000)

            # Generate online activity data
            online_activity_data = {
                "平台": ["校园表白墙", "微信群聊", "在线讲座", "论坛互动"],
                "时间": [f"{random.randint(8, 22)}:{random.randint(0, 59):02d}" for _ in range(4)],
                "活跃度": [random.randint(1, 5) for _ in range(4)]
            }

            # Generate offline activity data
            offline_activity_data = {
                "活动名称": ["志愿服务", "社团活动", "校外调研", "校内讲座"],
                "时间": [f"2024-03-{random.randint(1, 7)} {random.randint(9, 18)}:{random.randint(0, 59):02d}" for _ in
                         range(4)],
                "参与度": [random.randint(1, 5) for _ in range(4)]
            }

            # Generate peer network data
            peer_network_data = {
                "学生ID": list(students.keys()),
                "互动频率": [random.randint(1, 10) for _ in students.keys()],
                "关系强度": [random.choice(["弱", "中", "强"]) for _ in students.keys()]
            }

            students[student_id]["线上社交平台活跃度"] = pd.DataFrame(online_activity_data)
            students[student_id]["线下活动参与记录"] = pd.DataFrame(offline_activity_data)
            students[student_id]["朋辈关系网络"] = pd.DataFrame(peer_network_data)

        return students
    @st.cache_resource(ttl=3600)  # Cache the client for 1 hour
    def analyze_overall_isolation(students_data):
        client = get_openai_client()
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个社交网络分析助手。"},
                {"role": "user", "content": "请分析所有学生的整体社交孤立情况。"},
            ],
            stream=False
        )
        return response.choices[0].message.content
    def recommend_overall_improvement(students_data):
        client = get_openai_client()
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个社交网络分析助手，负责提出改善学生社交能力的策略。"},
                {"role": "user", "content": "请为所有学生推荐能够提升社交互动的整体改善策略。"},
            ],
            stream=False
        )
        return response.choices[0].message.content
    def ask_ai_question1(question):
        client = get_openai_client()
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个社交网络分析助手。"},
                {"role": "user", "content": question},
            ],
            stream=False
        )
        return response.choices[0].message.content
    def overall_social_network_page():
        #st.set_page_config(page_title="总体社交分析", layout="wide")
        st.title("总体社交分析")

        # Custom CSS for styling
        st.markdown("""
        <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
        }
        .metric-card {
            background-color: white;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

        students_data = generate_student_database()

        st.header("🌐 学生社交网络总体分析")

        activity_data = {
            "学生ID": list(students_data.keys()),
            "姓名": [students_data[id]["姓名"] for id in students_data],
            "活跃度": [random.randint(50, 100) for _ in students_data]
        }
        df_activity = pd.DataFrame(activity_data)

        # 找出活跃度最高的学生
        most_active_student = df_activity.loc[df_activity["活跃度"].idxmax()]

        # Metrics cards
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div class='metric-card'><h3>👥 学生总数</h3><h2>5</h2></div>", unsafe_allow_html=True)
        with col2:
            avg_activity = df_activity["活跃度"].mean()  # This would be calculated in a real app
            st.markdown(f"<div class='metric-card'><h3>📊 平均活跃度</h3><h2>{avg_activity}</h2></div>",
                        unsafe_allow_html=True)
        with col3:
            st.markdown(
                f"<div class='metric-card'><h3>🏆 最活跃学生</h3><h2>{most_active_student['姓名']}</h2></div>",
                unsafe_allow_html=True
            )

        # Social activity trends
        st.subheader("📈 社交活跃度趋势")

        activity_df = pd.DataFrame(activity_data)
        fig = px.bar(activity_df, x="姓名", y="活跃度", color="活跃度",
                     title="学生社交活跃度对比", color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)

        # Network visualization
        st.subheader("🕸️ 社交关系网络")
        network_data = []
        for student_id in students_data:
            for _, row in students_data[student_id]["朋辈关系网络"].iterrows():
                network_data.append({
                    "来源": students_data[student_id]["姓名"],
                    "目标": students_data[row["学生ID"]]["姓名"],
                    "强度": row["互动频率"]
                })
        network_df = pd.DataFrame(network_data)
        fig = px.scatter(network_df, x="来源", y="强度", size="强度", color="目标",
                         title="学生间互动关系", hover_name="目标")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.subheader("🤖 AI 整体分析")

        if st.button("分析社交孤立情况"):
            with st.spinner("AI正在分析中..."):
                analysis = analyze_overall_isolation(students_data)
                st.success("分析完成")
                st.markdown(f"<div style='background-color:#fff0f5; padding:15px; border-radius:10px;'>{analysis}</div>",
                            unsafe_allow_html=True)

        if st.button("推荐社交改善方案"):
            with st.spinner("AI正在推荐中..."):
                recommendation = recommend_overall_improvement(students_data)
                st.success("推荐完成")
                st.markdown(
                    f"<div style='background-color:#f0f8ff; padding:15px; border-radius:10px;'>{recommendation}</div>",
                    unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("💬 自由询问AI")

        user_question = st.text_area("请输入您关于学生社交网络的问题:", height=100)

        if st.button("提交问题"):
            if user_question.strip():
                with st.spinner("AI正在思考中..."):
                    answer = ask_ai_question1(user_question)
                    st.success("回答完成")
                    st.markdown(
                        f"<div style='background-color:#f0fff0; padding:15px; border-radius:10px;'>{answer}</div>",
                        unsafe_allow_html=True)
            else:
                st.warning("请输入有效的问题")
    overall_social_network_page()
def Student_growth():
# 模拟数据生成
# 自定义CSS样式
    st.markdown("""
    <style>
        /* 主容器样式 */
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem;
        }

        /* 标题样式 */
        .header {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1a5276;
            margin-bottom: 1.5rem;
            text-align: center;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #1a5276;
        }

        /* 卡片样式 */
        .analysis-card {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }

        .analysis-card:hover {
            box-shadow: 0 6px 16px rgba(0,0,0,0.15);
        }

        /* 指标卡片样式 */
        .metric-card {
            border-left: 4px solid #2980b9;
            padding: 1rem;
            margin: 0.5rem;
            border-radius: 8px;
            background-color: #f8f9fa;
        }

        /* 风险标签样式 */
        .risk-tag {
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.8rem;
            display: inline-block;
        }

        .risk-low {
            background-color: #d5f5e3;
            color: #27ae60;
        }

        .risk-medium {
            background-color: #fdebd0;
            color: #f39c12;
        }

        .risk-high {
            background-color: #fadbd8;
            color: #e74c3c;
        }

        /* 按钮样式 */
        .stButton>button {
            border-radius: 20px;
            padding: 8px 20px;
            background-color: #2980b9;
            color: white;
            border: none;
            transition: all 0.3s;
        }

        .stButton>button:hover {
            background-color: #2471a3;
            transform: scale(1.02);
        }

        /* 搜索框样式 */
        .stTextInput>div>div>input {
            border-radius: 20px !important;
            padding: 10px 15px !important;
        }

        /* 动画效果 */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .animate-fade {
            animation: fadeIn 0.5s ease-out forwards;
        }
    </style>
    """, unsafe_allow_html=True)

    # 模拟数据生成
    def generate_student_data():
        np.random.seed(42)

        # 基础信息
        ids = ["20231001", "20231002", "20231003", "20231004", "20231005"]
        names = ['王思远', '李婧怡', '张子轩', '陈昊然', '何俊杰']
        classes = ["计科2401", "金融2301", "数学2202", "汉语2303", "机械2401"]
        majors = ['计算机科学', '金融学', '数学', '汉语言文学', '机械工程']

        # 核心指标
        belief_scores = np.random.normal(75, 12, len(ids)).clip(40, 100)
        deviation_scores = np.random.normal(20, 8, len(ids)).clip(5, 45)
        culture_scores = np.random.normal(80, 10, len(ids)).clip(50, 100)
        activity_scores = np.random.normal(70, 15, len(ids)).clip(30, 100)

        # 风险等级计算
        risk_levels = []
        for i in range(len(ids)):
            score = (100 - belief_scores[i]) * 0.4 + deviation_scores[i] * 0.3 + (100 - culture_scores[i]) * 0.3
            if score < 30:
                risk_levels.append("低")
            elif score < 60:
                risk_levels.append("中")
            else:
                risk_levels.append("高")

        # 讨论文本关键词
        keywords = ["科技", "创新", "责任", "发展", "合作", "未来", "学习", "成长",
                    "挑战", "机遇", "团队", "进步", "知识", "探索", "实践"]

        # 创建DataFrame
        df = pd.DataFrame({
            "学号": ids,
            "姓名": names,
            "班级": classes,
            "专业": majors,
            "理想信念指数": belief_scores.round(1),
            "价值观偏离度": deviation_scores.round(1),
            "文化认同评分": culture_scores.round(1),
            "活动参与度": activity_scores.round(1),
            "风险等级": risk_levels,
            "最后活跃": pd.to_datetime(np.random.choice(pd.date_range("2023-09-01", "2023-11-30"), len(ids)))
        })

        # 为每个学生生成讨论文本
        df["讨论关键词"] = df.apply(lambda x: ", ".join(np.random.choice(keywords, 5, replace=False)), axis=1)

        return df

    # 生成词云
    def generate_wordcloud(text, title=None):
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='Blues',
            font_path="仿宋_GB2312.ttf"
        ).generate(text)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        if title:
            ax.set_title(title, fontsize=16, pad=20)
        st.pyplot(fig)

    # 首页
    def home_page():
        st.markdown('<div class="header animate-fade">学生成长分析系统</div>', unsafe_allow_html=True)

        # 顶部指标卡片
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h3>学生总数</h3>
                <h1 style="color: #2980b9;">50</h1>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h3>需关注学生</h3>
                <h1 style="color: #e74c3c;">8</h1>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="metric-card">
                <h3>平均参与度</h3>
                <h1 style="color: #27ae60;">72%</h1>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown("""
            <div class="metric-card">
                <h3>文化认同均分</h3>
                <h1 style="color: #f39c12;">82</h1>
            </div>
            """, unsafe_allow_html=True)

        # 搜索框
        st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
        st.subheader("🔍 学生搜索")
        search_col1, search_col2 = st.columns([3, 1])
        with search_col1:
            search_input = st.text_input("输入学号或姓名", placeholder="例如: 20231001 或 学生A1")
        with search_col2:
            st.write("")
            st.write("")
            if st.button("搜索"):
                if search_input:
                    st.session_state.search_query = search_input
                    st.session_state.page_Student_Growth = "student_detail"
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        # 需关注学生列表
        st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
        st.subheader("📌 需重点关注学生")
        high_risk_df = df[df["风险等级"] == "高"].sort_values("价值观偏离度", ascending=False)

        if not high_risk_df.empty:
            for _, row in high_risk_df.iterrows():
                cols = st.columns([1, 3, 1, 1])
                with cols[0]:
                    st.markdown(f"**{row['姓名']}**")
                    st.caption(f"{row['学号']} | {row['班级']}")
                with cols[1]:
                    st.progress(row["理想信念指数"] / 100, text=f"理想信念: {row['理想信念指数']}")
                    st.progress(row["价值观偏离度"] / 50, text=f"价值观偏离度: {row['价值观偏离度']}")
                with cols[2]:
                    if st.button("查看详情", key=f"detail_{row['学号']}"):
                        st.session_state.current_student = row['学号']
                        st.session_state.page = "student_detail"
                        st.rerun()
                with cols[3]:
                    st.markdown(f'<span class="risk-tag risk-high">高风险</span>', unsafe_allow_html=True)
                st.divider()
        else:
            st.success("当前没有高风险学生")
        st.markdown('</div>', unsafe_allow_html=True)

        # 全系数据分析
        st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
        st.subheader("📊 全系数据概览")
        tab1, tab2, tab3 = st.tabs(["指标分布", "活动参与", "讨论分析"])

        with tab1:
            fig = px.box(df, y=["理想信念指数", "文化认同评分"],
                         title="理想信念与文化认同分布")
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            fig = px.histogram(df, x="活动参与度", color="风险等级",
                               title="活动参与度分布", nbins=15)
            st.plotly_chart(fig, use_container_width=True)

        with tab3:
            all_keywords = ", ".join(df["讨论关键词"].tolist())
            generate_wordcloud(all_keywords, "")
        st.markdown('</div>', unsafe_allow_html=True)

    # 学生详情页
    def student_detail_page():
        student_id = st.session_state.get("current_student") or st.session_state.get("search_query")
        if not student_id:
            st.session_state.page_Student_Growth = "home"
            st.rerun()

        student_data = df[df["学号"] == student_id].iloc[0]

        st.markdown('<div class="header animate-fade">学生成长分析报告</div>', unsafe_allow_html=True)

        # 返回按钮
        if st.button("← 返回首页"):
            st.session_state.page = "home"
            st.rerun()

        # 基本信息
        st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"### {student_data['姓名']}")
            st.markdown(f"**学号:** {student_data['学号']}")
            st.markdown(f"**班级:** {student_data['班级']}")
            st.markdown(f"**专业:** {student_data['专业']}")
            st.markdown(f"**最后活跃:** {student_data['最后活跃'].strftime('%Y-%m-%d')}")

            risk_color = {
                "低": "risk-low",
                "中": "risk-medium",
                "高": "risk-high"
            }.get(student_data["风险等级"], "")

            st.markdown(f'**风险等级:** <span class="risk-tag {risk_color}">{student_data["风险等级"]}风险</span>',
                        unsafe_allow_html=True)

        with col2:
            # 雷达图展示核心指标
            categories = ['理想信念指数', '文化认同评分', '活动参与度']
            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=[student_data[c] for c in categories],
                theta=categories,
                fill='toself',
                name='个人指标'
            ))

            # 添加平均线
            avg_values = [df[c].mean() for c in categories]
            fig.add_trace(go.Scatterpolar(
                r=avg_values,
                theta=categories,
                name='全系平均',
                line=dict(color='red', dash='dot')
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=True,
                title="个人指标与全系平均对比"
            )
            st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 详细指标分析
        st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
        st.subheader("📈 详细指标分析")

        cols = st.columns(3)
        with cols[0]:
            st.markdown("""
            <div class="metric-card">
                <h3>理想信念指数</h3>
                <h1 style="color: #2980b9;">{}</h1>
                <p>全系平均: {:.1f}</p>
            </div>
            """.format(student_data["理想信念指数"], df["理想信念指数"].mean()), unsafe_allow_html=True)

            # 模拟历史趋势
            months = pd.date_range(end=datetime.today(), periods=6, freq='M')
            trend_data = {
                "月份": months,
                "指数": np.linspace(student_data["理想信念指数"] - 15, student_data["理想信念指数"], 6).clip(40, 100)
            }
            fig = px.line(trend_data, x="月份", y="指数", title="近6月趋势")
            st.plotly_chart(fig, use_container_width=True)

        with cols[1]:
            st.markdown("""
            <div class="metric-card">
                <h3>价值观偏离度</h3>
                <h1 style="color: {};">{}</h1>
                <p>全系平均: {:.1f}</p>
            </div>
            """.format("#e74c3c" if student_data["价值观偏离度"] > 30 else "#f39c12",
                       student_data["价值观偏离度"], df["价值观偏离度"].mean()), unsafe_allow_html=True)

            # 偏离度构成分析
            factors = ["网络言论", "活动参与", "社交关系", "学业表现"]
            values = np.random.dirichlet(np.ones(4), size=1)[0] * student_data["价值观偏离度"]
            fig = px.pie(names=factors, values=values, title="偏离度构成")
            st.plotly_chart(fig, use_container_width=True)

        with cols[2]:
            st.markdown("""
            <div class="metric-card">
                <h3>文化认同评分</h3>
                <h1 style="color: #27ae60;">{}</h1>
                <p>全系平均: {:.1f}</p>
            </div>
            """.format(student_data["文化认同评分"], df["文化认同评分"].mean()), unsafe_allow_html=True)

            # 文化认同细分
            aspects = ["传统", "创新", "团队", "责任"]
            scores = np.random.normal(student_data["文化认同评分"], 5, 4).clip(50, 100)
            fig = px.bar(x=aspects, y=scores, title="细分领域评分")
            st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 讨论内容分析
        st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
        st.subheader("💬 讨论内容分析")

        tab1, tab2 = st.tabs(["关键词分析", "讨论示例"])

        with tab1:
            generate_wordcloud(student_data["讨论关键词"], "")

        with tab2:
            # 模拟讨论内容
            discussions = [
                "我认为科技创新是未来发展的重要方向",
                "在团队项目中，我深刻体会到合作的重要性",
                "学习传统文化让我对历史有了更深的理解",
                "面对挑战时，我们应该保持积极的态度",
                "社会责任是每个大学生都应该重视的"
            ]

            for i, text in enumerate(discussions, 1):
                with st.container(border=True):
                    st.markdown(f"**讨论示例 {i}**")
                    st.write(text)
                    st.caption(
                        f"时间: {(datetime.now() - timedelta(days=np.random.randint(1, 30))).strftime('%Y-%m-%d')}")
        st.markdown('</div>', unsafe_allow_html=True)

        # 教育建议
        st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
        st.subheader("📚 成长建议")

        if student_data["风险等级"] == "高":
            st.warning("该学生需要重点关注，建议采取以下措施:")
            suggestions = [
                "安排导师一对一交流指导",
                "推荐参与团队建设活动",
                "提供个人发展规划咨询",
                "鼓励参与社会实践活动",
                "定期进行成长评估"
            ]
        elif student_data["风险等级"] == "中":
            st.info("该学生需要适度关注，建议采取以下措施:")
            suggestions = [
                "鼓励参与集体活动",
                "提供学习发展建议",
                "定期沟通交流",
                "推荐有益读物和资源",
                "关注社交圈层影响"
            ]
        else:
            st.success("该学生表现良好，建议采取以下措施:")
            suggestions = [
                "鼓励担任活动组织者",
                "提供更多发展机会",
                "推荐领导力培训",
                "作为榜样分享经验",
                "继续保持良好状态"
            ]

        for i, suggestion in enumerate(suggestions, 1):
            with st.container(border=True):
                st.markdown(f"**建议{i}:** {suggestion}")

        st.markdown('</div>', unsafe_allow_html=True)

    # 主程序
    if 'page_Student_Growth' not in st.session_state:
        st.session_state.page_Student_Growth = "home"

    # 加载数据
    df = generate_student_data()

    # 页面路由
    if st.session_state.page_Student_Growth == "home":
        home_page()
    elif st.session_state.page_Student_Growth == "student_detail":
        student_detail_page()
def Develop_Potential():
    # 自定义CSS样式
    st.markdown("""
    <style>
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem;
        }
        .header {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1a5276;
            margin-bottom: 1.5rem;
            text-align: center;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #1a5276;
        }
        .analysis-card {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }
        .analysis-card:hover {
            box-shadow: 0 6px 16px rgba(0,0,0,0.15);
        }
        .metric-card {
            border-left: 4px solid #2980b9;
            padding: 1rem;
            margin: 0.5rem;
            border-radius: 8px;
            background-color: #f8f9fa;
        }
        .stButton>button {
            border-radius: 20px;
            padding: 8px 20px;
            background-color: #2980b9;
            color: white;
            border: none;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #2471a3;
            transform: scale(1.02);
        }
        .stTextInput>div>div>input {
            border-radius: 20px !important;
            padding: 10px 15px !important;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade {
            animation: fadeIn 0.5s ease-out forwards;
        }
        .search-result-card {
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: #f8fafc;
        }
    </style>
    """, unsafe_allow_html=True)

    # 内置Lottie动画数据
    def get_default_lottie():
        return {
            "v": "5.5.2",
            "fr": 30,
            "ip": 0,
            "op": 60,
            "w": 500,
            "h": 500,
            "nm": "Student Avatar",
            "layers": [
                {
                    "ty": 1,
                    "sw": 500,
                    "sh": 500,
                    "sc": "#3498db",
                    "ks": {"o": {"a": 0, "k": 100}}
                },
                {
                    "ty": 4,
                    "nm": "Head",
                    "position": [250, 150],
                    "ks": {
                        "p": {"a": 0, "k": [250, 150]},
                        "s": {"a": 0, "k": [80, 80]}
                    },
                    "shapes": [{
                        "ty": "el",
                        "p": [0, 0],
                        "s": [80, 80]
                    }]
                }
            ]
        }
    # 加载动画
    def load_lottie(filepath: str) -> dict:
        if filepath == "student_avatar.json":
            return get_default_lottie()
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except:
            return get_default_lottie()
    # 生成唯一key
    def generate_key(*args) -> str:
        return hashlib.md5("_".join(str(arg) for arg in args).encode()).hexdigest()
    # 模拟学生数据库
    def generate_student_database_Dp(num: int = 50) -> pd.DataFrame:
        np.random.seed(42)
        ids = [f"2023{str(i).zfill(4)}" for i in range(1001, 1001 + num)]

        last_names = ["张", "王", "李", "赵", "刘"]
        first_names = ["伟", "芳", "娜", "秀英", "强", "洋", "明", "丽", "勇", "静", "杰", "敏"]
        names = []
        for i in range(num):
            last_name = last_names[i % len(last_names)]
            first_name = first_names[i % len(first_names)]
            names.append(f"{last_name}{first_name}")

        majors = np.random.choice(["计算机科学与技术", "电子信息工程", "机械工程", "经济管理", "外语"], num)
        grades = np.random.choice(["大一", "大二", "大三", "大四"], num)

        data = {
            "学号": ids,
            "姓名": names,
            "专业": majors,
            "年级": grades,
            "跨学科能力": np.random.normal(75, 12, num).clip(40, 100).round(1),
            "创新思维": np.random.normal(80, 10, num).clip(50, 100).round(1),
            "职业适配度": np.random.normal(70, 15, num).clip(30, 100).round(1),
            "深造潜力": np.random.normal(75, 10, num).clip(40, 100).round(1)
        }
        return pd.DataFrame(data)
    # 搜索功能
    def search_students(df: pd.DataFrame, query: str) -> Optional[pd.DataFrame]:
        if not query or not isinstance(query, str):
            return None

        query = query.strip()
        if not query:
            return None

        if query.isdigit() and len(query) == 8:
            result = df[df["学号"] == query]
            if not result.empty:
                return result

        if query.isdigit() and len(query) == 4:
            result = df[df["学号"].str.endswith(query)]
            if not result.empty:
                return result

        if query.isdigit() and len(query) == 4:
            result = df[df["学号"].str.startswith(query)]
            if not result.empty:
                return result

        name_result = df[df["姓名"].str.contains(query)]
        if not name_result.empty:
            return name_result

        major_result = df[df["专业"].str.contains(query)]
        if not major_result.empty:
            return major_result

        return None
    # 显示搜索结果
    def show_search_results(results: pd.DataFrame):
        st.success(f"🎯 找到 {len(results)} 条匹配结果")

        for _, row in results.iterrows():
            with st.container():
                avg_score = (row['跨学科能力'] + row['创新思维'] +
                             row['职业适配度'] + row['深造潜力']) / 4

                html_content = f"""
                <div class="search-result-card">
                    <div style="display:flex; align-items:center; margin-bottom:10px;">
                        <h3 style="margin:0; flex-grow:1;">{row['姓名']}</h3>
                        <span style="color:#666;">{row['学号']}</span>
                    </div>
                    <div style="display:flex; margin-bottom:8px;">
                        <span style="margin-right:15px;">📚 <strong>{row['专业']}</strong></span>
                        <span>🎓 {row['年级']}</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                        <span>🔢 综合评分: <strong>{avg_score:.1f}</strong></span>
                        <span>
                            <button style="background:#2980b9;color:white;border:none;border-radius:15px;padding:5px 12px;cursor:pointer;">
                                查看详情
                            </button>
                        </span>
                    </div>
                </div>
                """

                st.markdown(html_content, unsafe_allow_html=True)

                if st.button("查看详情", key=f"view_{row['学号']}", use_container_width=True):
                    st.session_state.current_student_development_potential = row['学号']
                    st.session_state.page_development_potential = "student_detail"
                    st.rerun()
    # 首页
    def home_page_Dp(df: pd.DataFrame):
        st.markdown('<div class="header animate-fade">学生发展潜力智能分析仪</div>', unsafe_allow_html=True)

        cols = st.columns(4)
        metrics = [
            ("学生总数", df.shape[0], "#2980b9"),
            ("高潜力学生", sum(df[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean(axis=1) > 80), "#27ae60"),
            ("平均创新思维", df["创新思维"].mean().round(1), "#f39c12"),
            ("平均深造潜力", df["深造潜力"].mean().round(1), "#9b59b6")
        ]

        for i, (title, value, color) in enumerate(metrics):
            with cols[i]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>{title}</h3>
                    <h1 style="color: {color};">{value}</h1>
                </div>
                """, unsafe_allow_html=True)

        style_metric_cards()

        # 搜索功能
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("🔍 智能搜索")

            search_input = st.text_input(
                "输入学号(支持后4位)、姓名或专业",
                placeholder="例如: 1001 或 张伟 或 计算机",
                key="search_input"
            )

            if st.button("搜索", key="search_button"):
                st.session_state.search_query_development_potential = search_input

            st.caption("💡 搜索提示: 支持完整学号(8位)、学号后4位、姓名(支持单字)、专业名称")

            if st.session_state.get("search_query_development_potential"):
                results = search_students(df, st.session_state.search_query_development_potential)
                if results is not None and not results.empty:
                    show_search_results(results)
                else:
                    st.warning("⚠️ 未找到匹配的学生，请尝试其他搜索词")

            st.markdown('</div>', unsafe_allow_html=True)

        # 高潜力学生推荐
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("🌟 高潜力学生推荐")

            df["综合评分"] = df[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean(axis=1)
            top_students = df.sort_values("综合评分", ascending=False).head(5)

            for _, row in top_students.iterrows():
                cols = st.columns([1, 3, 1])
                with cols[0]:
                    st.markdown(f"**{row['姓名']}**")
                    st.caption(f"{row['学号']} | {row['专业']}")
                with cols[1]:
                    st.progress(row["综合评分"] / 100,
                                text=f"综合评分: {row['综合评分']:.1f}")
                with cols[2]:
                    if st.button("查看详情", key=f"top_detail_{row['学号']}"):
                        st.session_state.current_student_development_potential = row['学号']
                        st.session_state.page_development_potential = "student_detail"
                        st.rerun()
                st.divider()
            st.markdown('</div>', unsafe_allow_html=True)

        # 全系能力分布
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("📊 全系能力分布")

            tab1, tab2 = st.tabs(["能力雷达图", "专业对比"])

            with tab1:
                avg_scores = df[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean().values
                labels = ["跨学科能力", "创新思维", "职业适配度", "深造潜力"]

                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=avg_scores,
                    theta=labels,
                    fill='toself',
                    name='全系平均'
                ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                    showlegend=False,
                    title="全系平均能力雷达图"
                )
                st.plotly_chart(fig, use_container_width=True)

            with tab2:
                major_avg = df.groupby("专业")[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean().reset_index()
                major_avg_long = pd.melt(
                    major_avg,
                    id_vars=["专业"],
                    value_vars=["跨学科能力", "创新思维", "职业适配度", "深造潜力"],
                    var_name="能力指标",
                    value_name="评分"
                )
                fig = px.bar(
                    major_avg_long,
                    x="专业",
                    y="评分",
                    color="能力指标",
                    barmode="group",
                    title="各专业能力对比",
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    # 学生详情页
    def student_detail_page_Dp(df: pd.DataFrame):
        student_id = st.session_state.get("current_student_development_potential")
        if not student_id:
            st.session_state.page_development_potential = "home"
            st.rerun()

        student_row = df[df["学号"] == student_id].iloc[0]
        student_data = {
            "学号": student_row["学号"],
            "姓名": student_row["姓名"],
            "专业": student_row["专业"],
            "年级": student_row["年级"],
            "跨学科能力": student_row["跨学科能力"],
            "创新思维": student_row["创新思维"],
            "职业适配度": student_row["职业适配度"],
            "深造潜力": student_row["深造潜力"]
        }

        st.markdown('<div class="header animate-fade">学生发展潜能分析报告</div>', unsafe_allow_html=True)

        if st.button("← 返回首页", key="back_button"):
            st.session_state.page_development_potential = "home"
            st.rerun()

        scores = [
            student_data["跨学科能力"],
            student_data["创新思维"],
            student_data["职业适配度"],
            student_data["深造潜力"]
        ]
        avg_score = sum(scores) / len(scores)
        overall_avg = df[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean().mean()

        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 3])

            with col1:
                st_lottie(load_lottie("student_avatar.json"),
                          height=150,
                          key=generate_key("avatar", student_id))
                st.markdown(f"**姓名:** {student_data['姓名']}")
                st.markdown(f"**学号:** {student_data['学号']}")
                st.markdown(f"**专业:** {student_data['专业']}")
                st.markdown(f"**年级:** {student_data['年级']}")
                st.metric("综合评分",
                          f"{avg_score:.1f}",
                          delta=f"{avg_score - overall_avg:+.1f} vs 平均")

            with col2:
                labels = ['跨学科能力', '创新思维', '职业适配度', '深造潜力']
                scores = [student_data[l] for l in labels]
                avg_scores = df[labels].mean().values

                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=scores,
                    theta=labels,
                    fill='toself',
                    name='个人能力'
                ))
                fig.add_trace(go.Scatterpolar(
                    r=avg_scores,
                    theta=labels,
                    name='全系平均',
                    line=dict(color='red', dash='dot')
                ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                    showlegend=True,
                    title="个人能力与全系平均对比",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 详细能力分析
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("📈 详细能力分析")

            abilities = [
                ("跨学科能力", "学生在不同领域间建立联系和应用知识的能力", "#3498db"),
                ("创新思维", "学生在解决问题时展现的创造力和原创性", "#2ecc71"),
                ("职业适配度", "学生能力与职场需求的匹配程度", "#e74c3c"),
                ("深造潜力", "学生在学术研究领域的发展可能性", "#9b59b6")
            ]

            for i in range(0, len(abilities), 2):
                cols = st.columns(2)
                for j in range(2):
                    if i + j < len(abilities):
                        ability, desc, color = abilities[i + j]
                        with cols[j]:
                            with st.container():
                                st.markdown(f"### {ability}")
                                st.metric(
                                    "评分",
                                    f"{student_data[ability]}",
                                    delta=f"{student_data[ability] - df[ability].mean():+.1f} vs 平均"
                                )
                                st.write(desc)

                                if ability == "跨学科能力":
                                    months = pd.date_range(end="2023-11-01", periods=6, freq='M')
                                    trend_data = pd.DataFrame({
                                        "月份": months.strftime("%Y-%m"),
                                        "评分": np.linspace(
                                            student_data[ability] - 15,
                                            student_data[ability], 6
                                        ).clip(40, 100)
                                    })
                                    fig = px.line(
                                        trend_data,
                                        x="月份",
                                        y="评分",
                                        title=f"{ability}趋势",
                                        color_discrete_sequence=[color]
                                    )
                                    st.plotly_chart(fig, use_container_width=True)

                                elif ability == "创新思维":
                                    aspects = ["创意表达", "问题解决", "批判思维", "好奇心"]
                                    values = np.random.dirichlet(np.ones(4)) * student_data[ability]
                                    fig = px.pie(
                                        names=aspects,
                                        values=values,
                                        title=f"{ability}构成",
                                        color_discrete_sequence=[color]
                                    )
                                    st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 发展建议
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("📚 个性化发展建议")

            if student_data['深造潜力'] > 80:
                st.success("### 🎓 深造建议")
                st.write("""
                - 🏫 推荐申请国内外顶尖研究生院
                - 🔬 参与教授的研究项目积累经验
                - 📝 发表学术论文提升研究背景
                - 🌐 参加学术会议拓展视野
                """)
            else:
                st.info("### 🎓 深造建议")
                st.write("""
                - 💼 通过实习积累实践经验
                - 📚 考虑专业认证课程提升技能
                - ⏳ 工作2-3年后再评估深造需求
                - 🗣 参加行业研讨会了解前沿动态
                """)

            if student_data['职业适配度'] > 75:
                st.success("### 💼 职业发展建议")
                st.write("""
                - 🏢 瞄准行业领先企业求职
                - 👔 申请管理培训生项目
                - 👩‍🏫 参加职业导师计划
                - 🤝 建立专业社交网络
                """)
            else:
                st.info("### 💼 职业发展建议")
                st.write("""
                - 🔍 通过实习探索职业方向
                - 🛠 参加职业技能培训
                - 📄 完善简历和面试技巧
                - 🏭 考虑中小企业积累经验
                """)

            if student_data['创新思维'] < 70:
                st.warning("### 💡 创新能力提升建议")
                st.write("""
                - 🧠 参加创新思维工作坊
                - 🚀 参与创业竞赛活动
                - ✏️ 学习设计思维方法
                - 🌈 多接触跨领域知识
                """)
            st.markdown('</div>', unsafe_allow_html=True)
    # 主程序
    def develop_potential():
        if 'page_development_potential' not in st.session_state:
            st.session_state.page_development_potential = "home"

        df = generate_student_database_Dp()

        if st.session_state.page_development_potential == "home":
            home_page_Dp(df)
        elif st.session_state.page_development_potential == "student_detail":
            student_detail_page_Dp(df)
    develop_potential()
def Psychometric_Testing():
    # 设置中文字体
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 初始化DeepSeek客户端
    client = OpenAI(api_key="sk-24d37178569a4f9d9ee09925e6edffa5", base_url="https://api.deepseek.com")

    # ------------------------- 通用工具函数 -------------------------

    # 缓存数据加载函数
    @st.cache_data
    def load_lottieurl(url: str):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return r.json()
        except:
            return None

    lottie_mental_health = load_lottieurl(
        "https://lottie.host/7b9e9b9e-9b9e-9b9e-9b9e-9b9e9b9e9b9e/9b9e9b9e-9b9e-9b9e-9b9e-9b9e9b9e9b9e.json")

    # 缓存问卷数据
    @st.cache_data
    def get_scl90_questions():
        categories = {
            "躯体化": ["1. 头痛", "4. 头晕或晕眩", "12. 胸痛", "27. 腰背酸痛", "40. 恶心或胃部不适",
                       "42. 肌肉酸痛", "48. 呼吸有困难", "49. 一阵阵发冷或发热", "52. 身体发麻或刺痛",
                       "53. 喉咙有梗塞感", "56. 感到身体的某一部分软弱无力", "58. 感到手或脚发重"],
            "强迫症状": ["3. 头脑中有不必要的想法或字句盘旋", "9. 忘性大", "10. 担心自己的衣饰整齐及仪态的端正",
                         "28. 感到难以完成任务", "38. 做事必须反复检查", "45. 难以做出决定",
                         "46. 必须反复洗手、点数目或触摸某些东西", "51. 头脑中有不必要的想法或字句盘旋",
                         "55. 不能控制地反复做某些事情", "65. 必须反复洗手、点数目或触摸某些东西"],
            "人际关系敏感": ["6. 对旁人责备求全", "21. 同异性相处时感到害羞不自在", "34. 感到别人不理解您、不同情您",
                             "36. 感到别人对您不友好、不喜欢您", "37. 做事必须做得很好以保证别人对您有好感",
                             "41. 感到有人在监视您、谈论您", "61. 感到别人想占您的便宜", "69. 感到对别人神经过敏",
                             "73. 在公共场合吃东西很不舒服"],
            "抑郁": ["5. 对异性的兴趣减退", "14. 感到自己的精力下降、活动减慢", "15. 想结束自己的生命",
                     "20. 容易哭泣", "22. 感到受骗、中了圈套或有人想抓住您", "26. 感到孤独",
                     "29. 感到苦闷", "30. 过分担忧", "31. 对事物不感兴趣", "32. 感到害怕",
                     "54. 感到前途没有希望", "71. 感到自己没有什么价值", "79. 感到任何事情都很困难"],
            "焦虑": ["2. 神经过敏、心中不踏实", "17. 发抖", "23. 无缘无故地突然感到害怕",
                     "33. 心跳得很厉害", "39. 感到害怕", "57. 感到坐立不安心神不定",
                     "72. 感到紧张或容易紧张", "78. 感到公共场合吃东西很不舒服",
                     "80. 感到熟悉的东西变成陌生或不像是真的", "86. 感到要很快把事情做完"],
            "敌对": ["11. 容易烦恼和激动", "24. 自己不能控制地大发脾气", "63. 有想打人或伤害他人的冲动",
                     "67. 有想摔坏或破坏东西的冲动", "74. 经常与人争论", "81. 大叫或摔东西"],
            "恐怖": ["13. 害怕空旷的场所或街道", "25. 怕单独出门", "47. 害怕乘坐公共汽车、地铁或火车",
                     "50. 因为感到害怕而避开某些东西、场合或活动", "70. 在商店或电影院等人多的地方感到不自在",
                     "75. 单独一人时神经很紧张", "82. 害怕会在公共场合昏倒"],
            "偏执": ["8. 责怪别人制造麻烦", "18. 感到大多数人都不可信任", "43. 感到有人在监视您、谈论您",
                     "68. 感到别人对您的成绩没有作出恰当的评价", "76. 别人对您的成绩没有作出恰当的评价",
                     "83. 感到别人想占您的便宜"],
            "精神病性": ["7. 感到别人能控制您的思想", "16. 听到旁人听不到的声音", "35. 感到别人能知道您的私下想法",
                         "62. 有一些不属于您自己的想法", "77. 感到即使有家人在身边也帮不上忙",
                         "84. 为一些有关性的想法而很苦恼", "85. 认为应该因为自己的过错而受到惩罚",
                         "87. 感到自己的身体有严重问题", "88. 从未感到和其他人很亲近",
                         "90. 感到自己的脑子有毛病"],
            "其他": ["19. 胃口不好", "44. 难以入睡", "59. 吃得太多", "60. 当别人看着您或谈论您时感到不自在",
                     "64. 醒得太早", "66. 睡得不稳不深", "89. 感到自己有罪"]
        }
        return categories

    @st.cache_data
    def get_mbti_questions():
        return [
            {"question": "1. 在聚会中，你通常", "options": ["与许多人交流，包括陌生人", "只与熟悉的人交流"]},
            {"question": "2. 你更倾向于", "options": ["现实和具体的事物", "想象和可能性"]},
            {"question": "3. 做决定时，你更注重", "options": ["逻辑和客观因素", "情感和人际关系"]},
            {"question": "4. 你更喜欢", "options": ["有计划、有组织的生活方式", "灵活、随性的生活方式"]},
            {"question": "5. 你更容易", "options": ["看到事物的细节", "看到事物的整体和大局"]},
            {"question": "6. 你认为自己更多是", "options": ["一个实际的人", "一个有想象力的人"]},
            {"question": "7. 你更倾向于", "options": ["公正，即使会伤害感情", "同情，即使逻辑上不太合理"]},
            {"question": "8. 你更喜欢", "options": ["提前安排计划", "保持选择的开放性"]},
            {"question": "9. 在社交场合，你通常", "options": ["主动与他人交谈", "等待别人来接近你"]},
            {"question": "10. 你更感兴趣于", "options": ["实际发生的事情", "可能发生的事情"]}
        ]

    @st.cache_data
    def get_depression_anxiety_questions():
        return {
            "抑郁": ["1. 我感到情绪沮丧，郁闷", "2. 我感到早晨心情最好", "3. 我要哭或想哭",
                     "4. 我夜间睡眠不好", "5. 我吃饭像平时一样多", "6. 我的性功能正常",
                     "7. 我感到体重减轻", "8. 我为便秘烦恼", "9. 我的心跳比平时快", "10. 我无故感到疲劳"],
            "焦虑": ["1. 我感到比往常更加神经过敏和焦虑", "2. 我无缘无故感到担心", "3. 我容易心烦意乱或感到恐慌",
                     "4. 我感到我可能将要发疯", "5. 我感到一切都很好，也不会发生什么不幸", "6. 我手脚发抖打颤",
                     "7. 我因为头痛、颈痛和背痛而烦恼", "8. 我感到无力且容易疲劳", "9. 我感到很平静，能安静坐下来",
                     "10. 我感到心跳很快"]
        }

    # 生成用户数据
    @st.cache_data
    def generate_user_data():
        dates = pd.date_range(start="2024-01-01", end=datetime.now().strftime("%Y-%m-%d"), freq="D")
        n = len(dates)
        data = {
            "日期": dates,
            "焦虑": np.clip(
                np.round(np.sin(np.linspace(0, 10, n)) * 3 + 3 + np.random.normal(0, 0.5, n), 1), 1, 5),
            "抑郁": np.clip(
                np.round(np.sin(np.linspace(0, 8, n)) * 2 + 2 + np.random.normal(0, 0.5, n), 1), 1, 5),
            "压力": np.clip(
                np.round(np.sin(np.linspace(0, 12, n)) * 2.5 + 2.5 + np.random.normal(0, 0.5, n), 1), 1, 5),
            "睡眠质量": np.clip(
                np.round(5 - (np.sin(np.linspace(0, 7, n)) * 1.5 - np.random.normal(0, 0.3, n)), 1), 1, 5),
            "社交意愿": np.clip(
                np.round(np.sin(np.linspace(0, 9, n)) * 2 + 3 + np.random.normal(0, 0.4, n), 1), 1, 5)
        }
        return pd.DataFrame(data)

    # 计算SCL-90得分
    def calculate_scl90_scores(answers):
        categories = get_scl90_questions()
        category_indices = {}
        idx = 0
        for category, questions in categories.items():
            category_indices[category] = list(range(idx, idx + len(questions)))
            idx += len(questions)

        scores = {}
        for category, indices in category_indices.items():
            scores[category] = np.mean([answers[i] for i in indices])

        scores["总分"] = np.mean(list(scores.values()))
        scores["阳性项目数"] = sum(1 for ans in answers if ans > 2)
        scores["阳性症状均分"] = np.mean([ans for ans in answers if ans > 2]) if scores["阳性项目数"] > 0 else 0

        return scores

    # 获取AI分析建议
    def get_ai_advice(scores):
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system",
                     "content": "你是一位专业的心理咨询师，请根据用户的SCL-90测评结果提供专业、温和且有帮助的建议。"},
                    {"role": "user", "content": f"我的SCL-90测评结果如下：{scores}。请分析我的心理状态并提供改善建议。"}
                ],
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"无法获取AI分析建议: {str(e)}。以下是一些通用建议：保持规律作息，适量运动，与亲友保持联系，必要时寻求专业帮助。"

    # 预警等级评估
    def assess_risk_level(scores):
        if scores["总分"] > 3.5 or any(
                v > 4 for v in scores.values() if isinstance(v, (int, float)) and v != scores["总分"]):
            return "red", "严重预警", "您的多项指标显示较高风险，建议立即联系心理咨询师或专业机构寻求帮助。"
        elif scores["总分"] > 2.5 or any(
                v > 3 for v in scores.values() if isinstance(v, (int, float)) and v != scores["总分"]):
            return "orange", "需关注", "您的部分指标偏高，建议关注自身情绪变化，适当调整生活方式，必要时可预约心理咨询。"
        else:
            return "green", "安全", "您的各项指标在正常范围内，继续保持健康的生活方式。"

    # ------------------------- 页面内容函数 -------------------------

    def render_home():
        st.title("🧠 心灵守护 - 大学生心理特质管理助手")

        # 欢迎区域
        col1, col2 = st.columns([3, 2])
        with col1:
            st.header("欢迎使用心灵守护助手")
            st.markdown("""
            **心灵守护**是一个专为大学生设计的心理健康管理助手，提供：

            - 📊 专业心理测评与即时分析
            - 📅 情绪波动追踪与可视化
            - 🛡️ 心理危机预警系统
            - 💡 个性化改善建议

            通过科学的方法帮助您了解自己的心理状态，提升心理健康水平。
            """)

        with col2:
            if lottie_mental_health:
                st_lottie(lottie_mental_health, height=300, key="mental_health")

        st.markdown("---")

        # 快速测评卡片
        st.subheader("快速测评")
        cols = st.columns(3)
        with cols[0]:
            with st.container(border=True):
                st.markdown("### SCL-90")
                st.markdown("**症状自评量表**")
                st.markdown("90题，约15分钟")
                if st.button("开始SCL-90测评", key="scl90_quick"):
                    st.session_state.current_page = "assessment"
                    st.session_state.test_type = "SCL-90"
                    st.session_state.answers = []
                    st.session_state.current_question_page = 0
                    st.rerun()
        with cols[1]:
            with st.container(border=True):
                st.markdown("### MBTI")
                st.markdown("**性格类型测试**")
                st.markdown("28题，约10分钟")
                if st.button("开始MBTI测评", key="mbti_quick"):
                    st.session_state.current_page = "assessment"
                    st.session_state.test_type = "MBTI"
                    st.session_state.answers = []
                    st.rerun()
        with cols[2]:
            with st.container(border=True):
                st.markdown("### 抑郁焦虑")
                st.markdown("**情绪状态评估**")
                st.markdown("20题，约5分钟")
                if st.button("开始抑郁焦虑测评", key="depression_quick"):
                    st.session_state.current_page = "assessment"
                    st.session_state.test_type = "抑郁焦虑量表"
                    st.session_state.answers = []
                    st.rerun()

        st.markdown("---")

        # 最近测评结果概览
        if "assessment_history" in st.session_state and st.session_state.assessment_history:
            latest_assessment = st.session_state.assessment_history[-1]

            if latest_assessment["type"] == "SCL-90":
                scores = latest_assessment["scores"]
                risk_color, risk_level, risk_advice = assess_risk_level(scores)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("总分", f"{scores['总分']:.1f}", "正常范围: 1.0-2.5")
                with col2:
                    st.metric("阳性项目数", scores["阳性项目数"], "正常范围: <30")
                with col3:
                    st.metric("预警等级", risk_level, help=risk_advice)

                @st.cache_data
                def create_radar_chart(scores):
                    categories = [k for k in scores.keys() if k not in ["总分", "阳性项目数", "阳性症状均分"]]
                    values = [scores[k] for k in categories]

                    fig = go.Figure()
                    fig.add_trace(go.Scatterpolar(
                        r=values + [values[0]],
                        theta=categories + [categories[0]],
                        fill='toself',
                        name='SCL-90维度得分'
                    ))
                    fig.update_layout(
                        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                        showlegend=False,
                        title="SCL-90各维度得分雷达图"
                    )
                    return fig

                st.plotly_chart(create_radar_chart(scores), use_container_width=True)

        # 情绪波动预览
        if "mood_data" in st.session_state and not st.session_state.mood_data.empty:
            st.subheader("近期情绪波动")

            @st.cache_data
            def create_line_chart(mood_data):
                fig = px.line(mood_data, x="日期", y=["焦虑", "抑郁", "压力"],
                              title="近期情绪变化趋势", markers=True)
                return fig

            st.plotly_chart(create_line_chart(st.session_state.mood_data), use_container_width=True)

    def render_assessment():
        st.title("📝 心理测评")

        # 返回按钮
        if st.button("← 返回测评选择", key="back_to_selection"):
            st.session_state.test_type = None
            st.session_state.answers = []
            if "current_question_page" in st.session_state:
                st.session_state.current_question_page = 0
            st.session_state.current_page = "home"
            st.rerun()

        # 测试类型选择
        if "test_type" not in st.session_state or not st.session_state.test_type:
            cols = st.columns(3)
            with cols[0]:
                with st.container(border=True):
                    st.markdown("### SCL-90")
                    st.markdown("**症状自评量表**")
                    st.markdown("90题，约15分钟")
                    if st.button("选择SCL-90", key="select_scl90"):
                        st.session_state.test_type = "SCL-90"
                        st.session_state.answers = []
                        st.session_state.current_question_page = 0
                        st.rerun()
            with cols[1]:
                with st.container(border=True):
                    st.markdown("### MBTI")
                    st.markdown("**性格类型测试**")
                    st.markdown("28题，约10分钟")
                    if st.button("选择MBTI", key="select_mbti"):
                        st.session_state.test_type = "MBTI"
                        st.session_state.answers = []
                        st.rerun()
            with cols[2]:
                with st.container(border=True):
                    st.markdown("### 抑郁焦虑量表")
                    st.markdown("**情绪状态评估**")
                    st.markdown("20题，约5分钟")
                    if st.button("选择抑郁焦虑量表", key="select_depression"):
                        st.session_state.test_type = "抑郁焦虑量表"
                        st.session_state.answers = []
                        st.rerun()

            st.markdown("---")
            st.info("请从上方选择您要进行的心理测评类型")
            return

        st.markdown(f"### {st.session_state.test_type}测评")

        # SCL-90测评
        if st.session_state.test_type == "SCL-90":
            categories = get_scl90_questions()
            all_questions = [q for sublist in categories.values() for q in sublist]

            if "answers" not in st.session_state or not st.session_state.answers:
                st.session_state.answers = [3] * len(all_questions)
            if "current_question_page" not in st.session_state:
                st.session_state.current_question_page = 0

            # 分页显示
            questions_per_page = 10
            total_pages = (len(all_questions) + questions_per_page - 1) // questions_per_page
            start_idx = st.session_state.current_question_page * questions_per_page
            end_idx = min((st.session_state.current_question_page + 1) * questions_per_page, len(all_questions))

            # 进度条
            progress = st.progress((st.session_state.current_question_page + 1) / total_pages)
            st.caption(
                f"进度: {start_idx + 1}-{end_idx}/{len(all_questions)}题 (第{st.session_state.current_question_page + 1}/{total_pages}页)")

            # 显示当前页的问题
            form_key = f"assessment_form_{st.session_state.current_question_page}"
            with st.form(form_key):
                for i in range(start_idx, end_idx):
                    st.session_state.answers[i] = st.slider(
                        f"问题{i + 1}: {all_questions[i]}",
                        min_value=1, max_value=5, value=st.session_state.answers[i],
                        key=f"q_{i}",
                        help="1: 无症状, 2: 轻度, 3: 中度, 4: 偏重, 5: 严重"
                    )

                col1, col2, col3 = st.columns([1, 1, 2])
                with col1:
                    if st.session_state.current_question_page > 0:
                        if st.form_submit_button("上一页"):
                            st.session_state.current_question_page -= 1
                            st.rerun()
                with col2:
                    if st.session_state.current_question_page < total_pages - 1:
                        if st.form_submit_button("下一页"):
                            st.session_state.current_question_page += 1
                            st.rerun()
                with col3:
                    if st.session_state.current_question_page == total_pages - 1:
                        if st.form_submit_button("提交测评"):
                            scores = calculate_scl90_scores(st.session_state.answers)

                            if "assessment_history" not in st.session_state:
                                st.session_state.assessment_history = []

                            st.session_state.assessment_history.append({
                                "type": "SCL-90",
                                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                                "scores": scores,
                                "answers": st.session_state.answers.copy()
                            })

                            # 更新情绪数据
                            if "mood_data" not in st.session_state:
                                st.session_state.mood_data = generate_user_data()

                            new_row = pd.DataFrame([{
                                "日期": datetime.now().strftime("%Y-%m-%d"),
                                "焦虑": scores["焦虑"],
                                "抑郁": scores["抑郁"],
                                "压力": (scores["焦虑"] + scores["抑郁"]) / 2,
                                "睡眠质量": 3 if scores["总分"] > 2.5 else 4,
                                "社交意愿": 3 if scores["人际关系敏感"] > 2.5 else 4
                            }])
                            st.session_state.mood_data = pd.concat([st.session_state.mood_data, new_row],
                                                                   ignore_index=True)

                            st.session_state.assessment_result = scores
                            st.session_state.current_page = "analysis"
                            st.rerun()

        # MBTI测评
        elif st.session_state.test_type == "MBTI":
            questions = get_mbti_questions()

            if "answers" not in st.session_state or not st.session_state.answers:
                st.session_state.answers = [0] * len(questions)

            with st.form("mbti_form"):
                for i, q in enumerate(questions):
                    st.session_state.answers[i] = st.radio(
                        q["question"],
                        options=q["options"],
                        index=st.session_state.answers[i] if st.session_state.answers[i] != 0 else None,
                        key=f"mbti_q_{i}"
                    )

                if st.form_submit_button("提交MBTI测评"):
                    # 计算MBTI类型
                    mbti_type = "".join([
                        "E" if sum(1 for i in [0, 8] if st.session_state.answers[i] == 0) > 1 else "I",
                        "S" if sum(1 for i in [1, 4, 5] if st.session_state.answers[i] == 0) > 1 else "N",
                        "T" if sum(1 for i in [2, 6] if st.session_state.answers[i] == 0) > 1 else "F",
                        "J" if sum(1 for i in [3, 7] if st.session_state.answers[i] == 0) > 1 else "P"
                    ])

                    if "assessment_history" not in st.session_state:
                        st.session_state.assessment_history = []

                    st.session_state.assessment_history.append({
                        "type": "MBTI",
                        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "result": mbti_type,
                        "answers": st.session_state.answers.copy()
                    })

                    st.session_state.assessment_result = {"MBTI类型": mbti_type}
                    st.session_state.current_page = "analysis"
                    st.rerun()

        # 抑郁焦虑测评
        elif st.session_state.test_type == "抑郁焦虑量表":
            questions = get_depression_anxiety_questions()
            all_questions = questions["抑郁"] + questions["焦虑"]

            # 答案选项配置
            ANSWER_OPTIONS = {
                "没有或很少时间": 1,
                "小部分时间": 2,
                "相当多时间": 3,
                "绝大部分或全部时间": 4
            }

            if "answers" not in st.session_state or not st.session_state.answers:
                st.session_state.answers = [1] * len(all_questions)

            with st.form("depression_anxiety_form"):
                for i, q in enumerate(all_questions):
                    # 获取当前答案对应的文本
                    current_value = st.session_state.answers[i]
                    current_text = [k for k, v in ANSWER_OPTIONS.items() if v == current_value][0]

                    # 显示单选按钮
                    selected_text = st.radio(
                        q,
                        options=list(ANSWER_OPTIONS.keys()),
                        index=current_value - 1,  # 转换为0-based索引
                        key=f"dep_anx_q_{i}"
                    )

                    # 更新答案为数值
                    st.state.answers[i] = ANSWER_OPTIONS[selected_text]

                if st.form_submit_button("提交测评"):
                    # 计算分数
                    depression_score = sum(st.session_state.answers[:10])  # 前10题是抑郁
                    anxiety_score = sum(st.session_state.answers[10:20])  # 后10题是焦虑

                    # 保存结果
                    if "assessment_history" not in st.session_state:
                        st.session_state.assessment_history = []

                    st.session_state.assessment_history.append({
                        "type": "抑郁焦虑量表",
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "scores": {
                            "抑郁": depression_score,
                            "焦虑": anxiety_score
                        },
                        "answers": st.session_state.answers.copy()
                    })

                    # 更新情绪数据
                    if "mood_data" not in st.session_state:
                        st.session_state.mood_data = generate_user_data()

                    new_row = pd.DataFrame([{
                        "日期": datetime.now().strftime("%Y-%m-%d"),
                        "焦虑": anxiety_score / 4,  # 转换为1-5范围
                        "抑郁": depression_score / 4,
                        "压力": (anxiety_score + depression_score) / 8,
                        "睡眠质量": 3 if depression_score > 15 else 4,
                        "社交意愿": 3 if depression_score > 15 else 4
                    }])
                    st.session_state.mood_data = pd.concat([st.session_state.mood_data, new_row], ignore_index=True)

                    st.session_state.assessment_result = {
                        "抑郁": depression_score,
                        "焦虑": anxiety_score
                    }
                    st.session_state.current_page = "analysis"
                    st.rerun()

    def render_analysis():
        st.title("📊 分析报告")

        if "assessment_result" not in st.session_state or "assessment_history" not in st.session_state or not st.session_state.assessment_history:
            st.warning("没有可用的测评结果，请先完成心理测评。")
            st.session_state.current_page = "assessment"
            st.rerun()

        # 返回按钮
        if st.button("← 返回首页", key="back_to_home"):
            st.session_state.current_page = "home"
            st.rerun()

        result = st.session_state.assessment_result
        last_assessment = st.session_state.assessment_history[-1]

        # SCL-90结果分析
        if last_assessment["type"] == "SCL-90":
            st.subheader("SCL-90测评结果分析")

            risk_color, risk_level, risk_advice = assess_risk_level(result)
            if risk_color == "red":
                st.error(f"⚠️ 预警等级: {risk_level} - {risk_advice}")
            elif risk_color == "orange":
                st.warning(f"⚠️ 预警等级: {risk_level} - {risk_advice}")
            else:
                st.success(f"✅ 预警等级: {risk_level} - {risk_advice}")

            st.markdown("---")

            # 各维度得分
            st.subheader("各维度得分")
            cols = st.columns(3)
            for i, (category, score) in enumerate(result.items()):
                if category not in ["总分", "阳性项目数", "阳性症状均分"]:
                    with cols[i % 3]:
                        with st.container(border=True):
                            st.markdown(f"**{category}**")
                            st.markdown(f"得分: **{score:.1f}** / 5.0")
                            if score > 3:
                                st.markdown(":warning: 偏高")
                            elif score > 2:
                                st.markdown(":large_orange_diamond: 中等")
                            else:
                                st.markdown(":green_circle: 正常")

            st.markdown("---")

            @st.cache_data
            def create_radar_chart(scores):
                categories = [k for k in scores.keys() if k not in ["总分", "阳性项目数", "阳性症状均分"]]
                values = [scores[k] for k in categories]

                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=values + [values[0]],
                    theta=categories + [categories[0]],
                    fill='toself',
                    name='SCL-90维度得分'
                ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                    showlegend=False,
                    title="SCL-90各维度得分雷达图"
                )
                return fig

            st.plotly_chart(create_radar_chart(result), use_container_width=True)

            # 总分与常模比较
            st.subheader("总分与常模比较")
            norm_data = pd.DataFrame({
                "类型": ["您的得分", "大学生常模"],
                "总分": [result["总分"], 1.8]
            })

            @st.cache_data
            def create_bar_chart(data):
                fig = px.bar(data, x="类型", y="总分", color="类型",
                             title="SCL-90总分与大学生常模比较", text="总分")
                return fig

            st.plotly_chart(create_bar_chart(norm_data), use_container_width=True)

            # AI分析建议
            st.subheader("个性化建议")
            with st.spinner("正在生成AI分析建议..."):
                advice = get_ai_advice(result)
                st.markdown(advice)

        # MBTI结果分析
        elif last_assessment["type"] == "MBTI":
            st.subheader("MBTI性格类型分析")
            mbti_type = result["MBTI类型"]

            st.markdown(f"### 您的MBTI性格类型是: **{mbti_type}**")

            mbti_descriptions = {
                "ISTJ": "检查员型 - 安静、严肃、可靠、务实，注重事实和细节",
                "ISFJ": "保护者型 - 安静、友好、负责、细心，保护他人感受",
                "INFJ": "咨询师型 - 寻求意义和联系，有洞察力，致力于价值观",
                "INTJ": "战略家型 - 有创意的战略家，对一切都有改进方案",
                "ISTP": "巧匠型 - 灵活冷静的观察者，擅长解决问题",
                "ISFP": "艺术家型 - 安静、友好、敏感、和善，享受当下",
                "INFP": "治愈者型 - 理想主义，忠于自己的价值观",
                "INTP": "建筑师型 - 逻辑、创新、理论思考者",
                "ESTP": "创业者型 - 灵活、容忍，注重实际效果",
                "ESFP": "表演者型 - 外向、友好、接受力强，热爱生活",
                "ENFP": "倡导者型 - 热情、富有想象力，视生活充满可能性",
                "ENTP": "辩论家型 - 敏捷、聪明、擅长多种事物",
                "ESTJ": "督导者型 - 务实、现实、果断，善于组织",
                "ESFJ": "供给者型 - 热心、合作、喜欢和谐，善于交际",
                "ENFJ": "教导者型 - 热情、有同情心、负责任，善交际",
                "ENTJ": "指挥官型 - 坦诚、果断，天生的领导者"
            }

            st.markdown(f"**{mbti_descriptions.get(mbti_type, '')}**")

            # MBTI雷达图
            @st.cache_data
            def create_mbti_radar(mbti_type):
                dimensions = [
                    ["外向(E)", "内向(I)"],
                    ["感觉(S)", "直觉(N)"],
                    ["思考(T)", "情感(F)"],
                    ["判断(J)", "知觉(P)"]
                ]

                fig = go.Figure()
                for i, (d1, d2) in enumerate(dimensions):
                    value = 5 if mbti_type[i] == d1[0] else 1
                    fig.add_trace(go.Scatterpolar(
                        r=[0, value, 0],
                        theta=[d1, d2, d1],
                        fill="toself",
                        name=f"{d1}/{d2}"
                    ))

                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                    showlegend=False,
                    title="MBTI性格维度分布"
                )
                return fig

            st.plotly_chart(create_mbti_radar(mbti_type), use_container_width=True)

            # 职业建议
            st.subheader("适合的职业方向")
            if mbti_type in ["ISTJ", "ESTJ", "ISFJ", "ESFJ"]:
                st.markdown("""
                - 行政管理
                - 会计/财务
                - 医疗保健
                - 教育
                - 法律
                """)
            elif mbti_type in ["ISTP", "ESTP"]:
                st.markdown("""
                - 工程技术
                - 警察/消防
                - 运动员
                - 企业家
                - 机械操作
                """)
            elif mbti_type in ["ISFP", "ESFP"]:
                st.markdown("""
                - 艺术设计
                - 护理
                - 旅游服务
                - 儿童教育
                - 客户服务
                """)
            elif mbti_type in ["INTJ", "ENTJ", "INTP", "ENTP"]:
                st.markdown("""
                - 科学研究
                - 计算机技术
                - 管理咨询
                - 战略规划
                - 创业
                """)
            elif mbti_type in ["INFJ", "ENFJ", "INFP", "ENFP"]:
                st.markdown("""
                - 心理咨询
                - 写作/创作
                - 人力资源
                - 社会工作
                - 市场营销
                """)

        # 抑郁焦虑结果分析
        elif last_assessment["type"] == "抑郁焦虑量表":
            st.subheader("抑郁焦虑测评结果分析")

            # 从session state获取分数
            depression_score = result["抑郁"]
            anxiety_score = result["焦虑"]

            col1, col2 = st.columns(2)
            with col1:
                st.metric("抑郁得分", depression_score,
                          "正常范围: 0-10" if depression_score <= 10 else "偏高: 建议关注")
            with col2:
                st.metric("焦虑得分", anxiety_score, "正常范围: 0-10" if anxiety_score <= 10 else "偏高: 建议关注")
            # 抑郁评估
            st.markdown("---")
            st.subheader("抑郁程度评估")
            if depression_score <= 10:
                st.success("您的抑郁得分在正常范围内，无明显抑郁症状")
            elif depression_score <= 16:
                st.warning("您有轻度抑郁症状，建议关注情绪变化，适当调节")
            elif depression_score <= 20:
                st.error("您有中度抑郁症状，建议寻求专业心理咨询")
            else:
                st.error("您的抑郁症状较为严重，建议立即寻求专业心理帮助")

            # 焦虑评估
            st.subheader("焦虑程度评估")
            if anxiety_score <= 10:
                st.success("您的焦虑得分在正常范围内，无明显焦虑症状")
            elif anxiety_score <= 16:
                st.warning("您有轻度焦虑症状，建议学习放松技巧")
            elif anxiety_score <= 20:
                st.error("您有中度焦虑症状，建议寻求专业心理咨询")
            else:
                st.error("您的焦虑症状较为严重，建议立即寻求专业心理帮助")

            # 改善建议
            st.subheader("改善建议")
            st.markdown("""
            - 保持规律作息，保证充足睡眠
            - 每天进行适量运动，如散步、瑜伽等
            - 练习深呼吸、冥想等放松技巧
            - 与亲友保持良好沟通
            - 减少咖啡因和酒精摄入
            - 如症状持续两周以上，建议寻求专业帮助
            """)

    def render_mood():
        st.title("📈 情绪分析")
        # 返回按钮
        if st.button("← 返回首页", key="back_to_home_mood"):
            st.session_state.current_page = "home"
            st.rerun()

        # 检查是否有情绪数据
        if "mood_data" not in st.session_state or st.session_state.mood_data.empty:
            st.warning("没有可用的情绪记录数据")
            return

        # 日期选择
        st.subheader("选择日期范围")
        mood_data = st.session_state.mood_data.copy()
        mood_data["原始日期"] = pd.to_datetime(mood_data["日期"])
        min_date = mood_data["原始日期"].min().date()
        max_date = mood_data["原始日期"].max().date()

        date_range = st.date_input(
            "选择日期范围",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            key="mood_date_range"
        )

        if isinstance(date_range, tuple) and len(date_range) == 2:
            start, end = date_range
            filtered_data = mood_data[
                (mood_data["原始日期"] >= pd.to_datetime(start)) &
                (mood_data["原始日期"] <= pd.to_datetime(end))
                ]
        else:
            filtered_data = mood_data

        # 热力图
        st.subheader("情绪波动热力图")

        @st.cache_data
        def create_heatmap(data):
            # 设置中文字体
            font_path = './仿宋_GB2312.ttf'
            font = FontProperties(fname=font_path)

            # 确保日期列是datetime类型
            data['原始日期'] = pd.to_datetime(data['原始日期'])
            heatmap_data = data.set_index("原始日期")[["焦虑", "抑郁", "压力"]]
            heatmap_data.index = heatmap_data.index.strftime("%m-%d")

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(heatmap_data.T, cmap="YlOrRd", annot=True, fmt=".1f", ax=ax, cbar_kws={'label': ''})

            # 设置所有文字元素的字体
            plt.xticks(rotation=45, fontproperties=font)
            plt.yticks(fontproperties=font)
            plt.title("情绪波动热力图", fontproperties=font)

            # 设置热力图的标签字体
            for t in ax.texts:
                t.set_fontproperties(font)

            # 设置x轴和y轴标签的字体
            ax.set_xticklabels(ax.get_xticklabels(), fontproperties=font)
            ax.set_yticklabels(ax.get_yticklabels(), fontproperties=font)

            # 设置x轴和y轴标题的字体
            ax.set_xlabel("日期", fontproperties=font)
            ax.set_ylabel("情绪指标", fontproperties=font)

            return fig

        st.pyplot(create_heatmap(filtered_data))

        # 折线图
        st.subheader("情绪变化趋势")

        @st.cache_data
        def create_line_chart(data):
            # 设置中文字体
            font_path = './仿宋_GB2312.ttf'
            font = FontProperties(fname=font_path)

            # 创建新的DataFrame
            plot_data = pd.DataFrame({
                '日期': data['原始日期'],
                '焦虑': data['焦虑'],
                '抑郁': data['抑郁'],
                '压力': data['压力']
            })

            # 转换数据格式
            plot_data = plot_data.melt(id_vars=['日期'],
                                       value_vars=['焦虑', '抑郁', '压力'],
                                       var_name='指标',
                                       value_name='得分')

            fig = px.line(plot_data, x='日期', y='得分', color='指标',
                          title='情绪指标变化趋势', markers=True)

            # 设置标题和轴标签的字体
            fig.update_layout(
                title_font=dict(family=font.get_name()),
                xaxis_title_font=dict(family=font.get_name()),
                yaxis_title_font=dict(family=font.get_name()),
                legend_title_font=dict(family=font.get_name()),
                legend_font=dict(family=font.get_name())
            )

            return fig

        st.plotly_chart(create_line_chart(filtered_data), use_container_width=True)

        # 相关性分析
        st.subheader("指标相关性分析")

        @st.cache_data
        def create_corr_heatmap(data):
            font_path = './仿宋_GB2312.ttf'
            font = FontProperties(fname=font_path)
            corr_data = data[["焦虑", "抑郁", "压力", "睡眠质量", "社交意愿"]].corr()
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(corr_data, annot=True, cmap="coolwarm", center=0, ax=ax)

            # 设置所有文字元素的字体
            plt.xticks(fontproperties=font)
            plt.yticks(fontproperties=font)
            plt.title("情绪指标相关性分析", fontproperties=font)

            # 设置热力图的标签字体
            for t in ax.texts:
                t.set_fontproperties(font)
            # 设置轴标签的字体
            ax.set_xticklabels(ax.get_xticklabels(), fontproperties=font)
            ax.set_yticklabels(ax.get_yticklabels(), fontproperties=font)

            return fig

        st.pyplot(create_corr_heatmap(filtered_data))

        # 添加今日情绪记录
        st.markdown("---")
        st.subheader("记录今日情绪")

        with st.form("daily_mood_form"):
            today = datetime.now().date()
            anxiety = st.slider("焦虑程度 (1-5分)", 1, 5, 3, key="anxiety_slider")
            depression = st.slider("抑郁程度 (1-5分)", 1, 5, 3, key="depression_slider")
            stress = st.slider("压力程度 (1-5分)", 1, 5, 3, key="stress_slider")
            sleep = st.slider("睡眠质量 (1-5分)", 1, 5, 3, key="sleep_slider")
            social = st.slider("社交意愿 (1-5分)", 1, 5, 3, key="social_slider")

            if st.form_submit_button("保存今日情绪记录"):
                new_entry = pd.DataFrame([{
                    "日期": today.strftime("%Y-%m-%d"),
                    "焦虑": anxiety,
                    "抑郁": depression,
                    "压力": stress,
                    "睡眠质量": sleep,
                    "社交意愿": social
                }])

                today_exists = pd.to_datetime(mood_data["日期"]).dt.date.eq(today).any()

                if today_exists:
                    mood_data.loc[
                        pd.to_datetime(mood_data["日期"]).dt.date == today,
                        ["焦虑", "抑郁", "压力", "睡眠质量", "社交意愿"]
                    ] = [anxiety, depression, stress, sleep, social]
                else:
                    mood_data = pd.concat([mood_data, new_entry], ignore_index=True)

                st.session_state.mood_data = mood_data

                st.success("今日情绪记录已保存!")

    def render_risk():
        st.title("⚠️ 危机预警")
        # 返回按钮
        if st.button("← 返回首页", key="back_to_home_risk"):
            st.session_state.current_page = "home"
            st.rerun()
        # 如果没有测评记录
        if "assessment_history" not in st.session_state or not st.session_state.assessment_history:
            st.warning("没有可用的测评记录，请先完成心理测评。")
            st.session_state.current_page = "assessment"
            st.rerun()

        # 获取最新SCL-90测评结果
        latest_scl90 = None
        for assessment in reversed(st.session_state.assessment_history):
            if assessment["type"] == "SCL-90":
                latest_scl90 = assessment
                break

        if not latest_scl90:
            st.warning("没有找到SCL-90测评记录，请先完成SCL-90测评。")
            st.session_state.current_page = "assessment"
            st.rerun()

        scores = latest_scl90["scores"]
        risk_color, risk_level, risk_advice = assess_risk_level(scores)

        # 预警展示
        if risk_color == "red":
            st.error(f"## 🚨 严重预警: {risk_level}")
        elif risk_color == "orange":
            st.warning(f"## ⚠️ 需关注: {risk_level}")
        else:
            st.success(f"## ✅ 安全: {risk_level}")

        st.markdown(f"**建议**: {risk_advice}")

        st.markdown("---")

        # 预警指标详情
        st.subheader("预警指标详情")

        warning_indicators = []
        for category, score in scores.items():
            if category not in ["总分", "阳性项目数", "阳性症状均分"] and score > 3:
                warning_indicators.append((category, score))

        if warning_indicators:
            st.warning("以下维度得分偏高，需特别关注:")
            for category, score in warning_indicators:
                st.markdown(f"- **{category}**: {score:.1f}分 (正常范围: <3.0)")
        else:
            st.info("各维度得分均在正常范围内，无明显预警指标。")

        st.markdown("---")

        # 抗压能力评估
        st.subheader("抗压能力评估")

        # 简单计算抗压能力 (基于SCL-90得分)
        stress_resistance = 100 - (scores["总分"] * 15 + scores["焦虑"] * 10 + scores["抑郁"] * 10)
        stress_resistance = max(0, min(100, stress_resistance))

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=stress_resistance,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "抗压能力指数"},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 40], 'color': "red"},
                    {'range': [40, 70], 'color': "orange"},
                    {'range': [70, 100], 'color': "green"}]
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

        if stress_resistance < 40:
            st.error("您的抗压能力较低，容易在压力下出现情绪困扰，建议学习压力管理技巧。")
        elif stress_resistance < 70:
            st.warning("您的抗压能力中等，能够应对一般压力，但在高强度压力下可能出现困扰。")
        else:
            st.success("您的抗压能力较强，能够较好地应对生活中的压力。")

        st.markdown("---")

        # 紧急联系方式
        st.subheader("心理援助资源")
        with st.expander("点击查看心理援助联系方式"):
            st.markdown("""
            **校内资源:**
            - 学校心理咨询中心: 010-61773111 (工作日19:00-21:00)
            - 心理危机干预热线: 2023196 (24小时)

            **校外资源:**
            - 保定市第一中心医院热线: 2023196 (24小时)
            - 保定市第一中心医院网址: http://www.bddhospital.com.cn/

            **紧急情况:**
            - 如遇紧急心理危机，请立即拨打120或前往最近医院急诊科
            """)

    def main():
        # 初始化session state（确保所有必要的状态变量都存在）
        if "current_page" not in st.session_state:
            st.session_state.current_page = "home"  # 当前页面（home/assessment/analysis/mood/risk）
        if "test_type" not in st.session_state:
            st.session_state.test_type = None  # 当前测评类型（SCL-90/MBTI/抑郁焦虑量表）
        if "answers" not in st.session_state:
            st.session_state.answers = []  # 用户答题记录
        if "assessment_history" not in st.session_state:
            st.session_state.assessment_history = []  # 历史测评记录
        if "mood_data" not in st.session_state:
            st.session_state.mood_data = generate_user_data()  # 情绪数据
        if "assessment_result" not in st.session_state:
            st.session_state.assessment_result = None  # 最近一次测评结果
        if "current_question_page" not in st.session_state:
            st.session_state.current_question_page = 0  # SCL-90当前问题页

        # 横向导航栏（使用容器实现固定位置的导航菜单）
        with st.container():
            cols = st.columns(5)
            with cols[0]:
                if st.button("🏠 心灵首页", key="nav_home"):
                    st.session_state.current_page = "home"
                    st.rerun()
            with cols[1]:
                if st.button("📝 心理测评", key="nav_assessment"):
                    st.session_state.current_page = "assessment"
                    st.rerun()
            with cols[2]:
                if st.button("📊 分析报告", key="nav_analysis"):
                    if st.session_state.assessment_history:
                        st.session_state.current_page = "analysis"
                        st.rerun()
                    else:
                        st.warning("请先完成心理测评")
            with cols[3]:
                if st.button("📅 情绪记录", key="nav_mood"):
                    st.session_state.current_page = "mood"
                    st.rerun()
            with cols[4]:
                if st.button("⚠️ 危机预警", key="nav_risk"):
                    has_scl90 = any(a["type"] == "SCL-90" for a in st.session_state.assessment_history)
                    if has_scl90:
                        st.session_state.current_page = "risk"
                        st.rerun()
                    else:
                        st.warning("请先完成SCL-90测评")

        st.markdown("---")  # 分隔线

        # 页面路由逻辑
        pages = {
            "home": render_home,
            "assessment": render_assessment,
            "analysis": render_analysis,
            "mood": render_mood,
            "risk": render_risk
        }

        # 显示当前页面（带错误处理）
        try:
            current_page = st.session_state.current_page
            if current_page in pages:
                pages[current_page]()  # 调用对应的页面渲染函数
            else:
                st.error("无效的页面路径")
                st.session_state.current_page = "home"
                pages["home"]()
        except Exception as e:
            st.error(f"页面加载错误: {str(e)}")
            st.session_state.current_page = "home"
            pages["home"]()

    main()
def Downgrade_Alerts():
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_animation = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_6wutsrox.json")

    def generate_random_student_data(num_students=10):
        # names = ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十", "郑十一", "王十二"]
        # 修改学生姓名
        names = [
            "王思远", "李婧怡", "张子轩", "刘雨桐", "陈昊然", "杨紫彤", "赵志远", "黄梦婷", "吴梓豪", "周可欣",
            "郑一帆", "孙佳怡", "马承志", "朱宇航", "胡欣然", "郭子睿", "林雨馨", "何俊杰", "高诗涵", "罗思源",
            "宋佳琪", "谢晨曦", "唐浩然", "邓可儿", "许梓涵", "韩宇泽", "冯芷萱", "曹睿哲", "彭宸希", "萧子墨",
            "程欣妍", "尹晨雨", "陶俊熙", "袁嘉怡", "秦语嫣", "赖文博", "赖梓萱", "严浩轩", "贾婉琳", "黎思辰",
            "施凯文", "鲁子仪", "谭语嫣", "侯泽宇", "白梓萌", "丁奕辰", "康妍希", "章宇哲", "戴心怡",
            "田志伟", "石慧敏", "夏彦霏", "杜梓睿", "魏梦琪", "范奕辰", "冉梓诺", "廖俊铭",
            "裴子墨", "闫雪妍", "纪文轩", "熊雨辰", "陶思彤", "蒲晨曦", "温嘉乐", "宫子涵", "景昕怡", "梅泽铭",
            "欧阳浩然", "殷诗涵", "昌语嫣", "路宸轩", "丁心妍", "花宇杰", "边沛然", "芦梓琳",
            "晏诗琪", "裴若曦", "储子辰", "邬梦涵", "戚嘉怡", "訾皓宇", "成语彤", "昌可欣", "茅泽宇", "倪妍妍",
            "柴浩宸", "阚梓宁", "管紫嫣", "厉雨泽", "龚婧怡", "杭泽霖", "丰嘉辰", "左语嫣", "童一诺", "屈子墨",
            "庄宇萱", "边昕妍", "苗俊凯", "温佳怡", "燕泽远", "权奕辰", "党一帆", "翟宇彤", "郜梓宸",
            "滕宛妍", "米嘉昊", "郁梓轩", "焦梦妍", "严涵宇", "车思妍", "项辰曦",
            "游俊熙", "郁昕怡", "商乐怡", "臧宇航", "邝文睿", "雍芷萱", "籍紫涵",
            "隗天怡", "戎雨萌", "祖宸逸", "经乐妍", "柏志强", "燕嘉妍", "巫俊豪", "蔚子骞",
            "东语嫣", "慎晨曦", "鞠子诺",
            "墨子瑞", "南子安", "臧宇航", "索婉妍", "卞心妍", "淳嘉仪", "单梓妍",
            "胥嘉铭", "季语嫣", "岳紫彤", "权俊逸", "冷欣怡",
            "庞宇轩", "梅心怡", "禹泽宇", "苗语嫣", "赖文睿", "费文杰", "冉昕怡", "幸芷萱",
            "查语彤", "华思彤", "邸宇辰", "富梓涵", "惠雨婷", "纪一诺", "容俊豪",
            "崔奕辰",
            "米浩然", "涂雅妍", "幸俊豪"]
        majors = ["计算机科学", "电子工程", "工商管理", "外国语", "数学", "物理"]
        grades = ["大一", "大二", "大三", "大四"]
        performance = ["优秀", "良好", "及格"]
        attendance = ["高", "中", "低"]

        data = {
            "姓名": np.random.choice(names, num_students, replace=False),
            "年龄": np.random.randint(18, 24, num_students),
            "在校时间": np.random.randint(1, 4, num_students),
            "专业": np.random.choice(majors, num_students),
            "年级": np.random.choice(grades, num_students),
            "GPA": np.random.uniform(2.0, 4.0, num_students).round(2),
            "学习满意度": np.random.randint(3, 10, num_students),
            "学业表现": np.random.choice(performance, num_students, p=[0.3, 0.5, 0.2]),
            "缺勤率": np.random.choice(attendance, num_students, p=[0.4, 0.4, 0.2]),
            "补考次数": np.random.randint(0, 5, num_students)
        }
        return pd.DataFrame(data)

    class StudentDB:
        def __init__(self):
            self.students = []

        def add_student(self, data):
            self.students.append(data)

        def get_student(self, name):
            for stu in self.students:
                if stu['姓名'] == name:
                    return stu
            return None

    db = StudentDB()

    def predict_dropout_risk(student_data):
        """调用 DeepSeek AI 进行降级预测"""
        client = OpenAI(api_key="sk-24d37178569a4f9d9ee09925e6edffa5", base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system",
                 "content": "你是一个专业的学业预警 AI 助手，能够准确预测学生降级风险。请分析以下学生数据并给出降级风险预测(低/中/高)，以及主要影响因素和改善建议。"},
                {"role": "user", "content": f"请分析以下学生数据并预测降级风险:\n{student_data}"},
            ],
            stream=False
        )
        return response.choices[0].message.content

    def generate_radar_chart(student_data):
        categories = ['在校时间', 'GPA', '学习满意度', '学业表现', '补考次数']

        # 将学业表现转换为数值
        perf_map = {'优秀': 9, '良好': 7, '及格': 5}
        student_data['学业表现数值'] = student_data['学业表现'].map(perf_map)

        values = [
            student_data['在校时间'].values[0] / 4 * 10,  # 归一化
            student_data['GPA'].values[0] / 4.0 * 10,
            student_data['学习满意度'].values[0],
            student_data['学业表现数值'].values[0],
            student_data['补考次数'].values[0] / 5 * 10
        ]

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='学生数据',
            line=dict(color='rgb(100, 200, 255)'),
            fillcolor='rgba(100, 200, 255, 0.5)'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=True,
            title='学生学业表现雷达图',
            template="plotly_dark",
            font=dict(
                family="Arial",
                size=12,
                color="white"
            )
        )

        return fig

    def generate_timeline_chart(student_name):
        # 模拟历史数据
        semesters = ['第一学期', '第二学期', '第三学期', '第四学期', '第五学期', '第六学期']
        satisfaction = np.random.randint(4, 9, size=6)
        performance = np.random.randint(5, 10, size=6)
        absence = np.random.randint(1, 5, size=6)

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Scatter(x=semesters, y=satisfaction, name="学习满意度", line=dict(color='#00CC96')),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=semesters, y=performance, name="学业表现", line=dict(color='#636EFA')),
            secondary_y=False,
        )

        fig.add_trace(
            go.Bar(x=semesters, y=absence, name="缺勤率", marker_color='#EF553B', opacity=0.5),
            secondary_y=True,
        )

        fig.update_layout(
            title_text=f"{student_name} 的学业历史趋势",
            template="plotly_dark",
            hovermode="x unified"
        )

        fig.update_yaxes(title_text="评分", secondary_y=False)
        fig.update_yaxes(title_text="缺勤率", secondary_y=True)

        return fig

    def generate_major_heatmap(df):
        major_data = df.groupby('专业').agg({
            '学习满意度': 'mean',
            'GPA': 'mean',
            '补考次数': 'mean'
        }).reset_index()

        fig = px.imshow(major_data.set_index('专业'),
                        color_continuous_scale='Viridis',
                        title='专业数据热力图')

        fig.update_layout(
            template="plotly_dark",
            xaxis_title="指标",
            yaxis_title="专业"
        )

        return fig

    def generate_3d_scatter(df):
        fig = px.scatter_3d(df, x='GPA', y='学习满意度', z='在校时间',
                            color='专业', size='补考次数',
                            hover_name='姓名',
                            title='学生数据3D分布',
                            opacity=0.8)

        fig.update_layout(
            scene=dict(
                xaxis_title='GPA',
                yaxis_title='学习满意度',
                zaxis_title='在校时间'
            ),
            template="plotly_dark",
            margin=dict(l=0, r=0, b=0, t=30)
        )

        return fig

    def analyze_sentiment(text):
        client = OpenAI(api_key="sk-24d37178569a4f9d9ee09925e6edffa5", base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个情绪分析AI，请分析以下文本的情绪倾向(0-10，10为最积极)"},
                {"role": "user", "content": f"分析情绪: {text}"},
            ],
            stream=False
        )
        try:
            score = int(response.choices[0].message.content)
            return min(max(score, 0), 10)
        except:
            return 5

    def dropout_projections():
        # 标题和动画
        col1, col2 = st.columns([3, 1])
        with col1:
            st.title("🚀 AI 学业预警智能分析仪")
            st.markdown("""
            <div class="neon-text">
                学业管理决策支持平台 · 预测学生降级风险 · 提供干预建议
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if lottie_animation:
                st_lottie(lottie_animation, height=150, key="dashboard")

        st.markdown("---")

        # 新增学生填写表单
        st.header("📝 添加新学生")
        with st.expander("点击填写学生信息", expanded=False):
            with st.form("student_form"):
                cols = st.columns(2)
                name = cols[0].text_input("姓名", placeholder="请输入学生姓名")
                age = cols[1].number_input("年龄", min_value=17, max_value=25, value=19)

                cols = st.columns(2)
                years_in_school = cols[0].number_input("在校时间(年)", min_value=1, max_value=4, value=1)
                gpa = cols[1].number_input("GPA", min_value=0.0, max_value=4.0, value=3.0, step=0.1)

                cols = st.columns(2)
                major = cols[0].selectbox("专业", ["计算机科学", "电子工程", "工商管理", "外国语", "数学", "物理"])
                grade = cols[1].selectbox("年级", ["大一", "大二", "大三", "大四"])

                cols = st.columns(2)
                satisfaction = cols[0].slider("学习满意度 (1-10)", 1, 10, 7)
                performance = cols[1].selectbox("学业表现", ["优秀", "良好", "及格"])

                absence = st.selectbox("缺勤率", ["高", "中", "低"])
                retakes = st.number_input("补考次数", min_value=0, max_value=10, value=0)

                submitted = st.form_submit_button("提交学生信息")

                if submitted:
                    if not name:
                        st.error("请填写学生姓名")
                    else:
                        new_student = {
                            "姓名": name,
                            "年龄": age,
                            "在校时间": years_in_school,
                            "专业": major,
                            "年级": grade,
                            "GPA": gpa,
                            "学习满意度": satisfaction,
                            "学业表现": performance,
                            "缺勤率": absence,
                            "补考次数": retakes
                        }

                        # 添加到数据框
                        if 'df_downgrade_alerts' not in st.session_state:
                            st.session_state.df_downgrade_alerts = pd.DataFrame(columns=[
                                "姓名", "年龄", "在校时间", "专业", "年级", "GPA",
                                "学习满意度", "学业表现", "缺勤率", "补考次数"
                            ])

                        new_df = pd.DataFrame([new_student])
                        st.session_state.df_downgrade_alerts = pd.concat([st.session_state.df_downgrade_alerts, new_df], ignore_index=True)
                        st.success(f"学生 {name} 信息已成功添加！")

        # 数据控制区域
        st.header("📊 数据控制中心")
        col1, col2 = st.columns(2)
        with col1:
            num_students = st.slider("选择生成学生数量", 5, 10, 10)
        with col2:
            if st.button("🎲 生成随机学生数据", use_container_width=True):
                df = generate_random_student_data(num_students)
                st.session_state.df_downgrade_alerts = df
                st.success(f"已生成 {num_students} 条随机学生数据!")

        # 初始化或获取数据
        if 'df_downgrade_alerts' not in st.session_state:
            st.session_state.df_downgrade_alerts = generate_random_student_data(num_students)
        df = st.session_state.df_downgrade_alerts

        # 数据预览
        st.header("📊 数据概览")
        with st.expander("点击查看完整数据"):
            st.dataframe(df.style.background_gradient(cmap='Blues'))

        # 整体分析
        st.header("🔍 整体分析")
        tab1, tab2, tab3 = st.tabs(["专业分布", "3D视图", "热力图"])

        with tab1:
            fig = px.pie(df, names='专业', title='学生专业分布', hole=0.4)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.plotly_chart(generate_3d_scatter(df), use_container_width=True)

        with tab3:
            st.plotly_chart(generate_major_heatmap(df), use_container_width=True)

        # 学生选择
        st.header("👤 学生分析")
        selected_student = st.selectbox("选择学生", df["姓名"].unique())
        student_data = df[df["姓名"] == selected_student].iloc[0].to_dict()

        # 学生卡片
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("学生档案")
            card = st.container(border=True)

            with card:
                cols = st.columns(2)
                cols[0].metric("姓名", student_data["姓名"])
                cols[1].metric("年龄", student_data["年龄"])

                cols = st.columns(2)
                cols[0].metric("专业", student_data["专业"])
                cols[1].metric("年级", student_data["年级"])

                cols = st.columns(2)
                cols[0].metric("在校时间", f"{student_data['在校时间']}年")
                cols[1].metric("GPA", f"{student_data['GPA']:.2f}")

                st.progress(student_data["学习满意度"] / 10, text=f"学习满意度: {student_data['学习满意度']}/10")

                # 情绪分析
                feedback = st.text_input("输入学生反馈进行情绪分析", "")
                if feedback:
                    with st.spinner("分析情绪中..."):
                        score = analyze_sentiment(feedback)
                        st.metric("情绪得分", f"{score}/10")
                        st.progress(score / 10)

        with col2:
            tab1, tab2 = st.tabs(["学业表现雷达图", "历史趋势"])

            with tab1:
                st.plotly_chart(generate_radar_chart(df[df["姓名"] == selected_student]),
                                use_container_width=True)

            with tab2:
                st.plotly_chart(generate_timeline_chart(selected_student),
                                use_container_width=True)

        # 预测分析
        st.header("🔮 降级风险预测")

        if st.button("开始预测", type="primary"):
            with st.spinner("AI正在分析..."):
                prediction = predict_dropout_risk(student_data)
                time.sleep(2)

                # 模拟风险等级
                risk_level = np.random.choice(["低", "中", "高"], p=[0.6, 0.3, 0.1])

                if risk_level == "高":
                    st.error(f"⚠️ 高风险预警: {selected_student} 的降级风险较高!")
                    st.markdown("""<div class="pulse-alert">建议立即采取干预措施</div>""",
                                unsafe_allow_html=True)
                elif risk_level == "中":
                    st.warning(f"⚠️ 中等风险: {selected_student} 的降级风险中等")
                else:
                    st.success(f"✅ 低风险: {selected_student} 的降级风险较低")

                st.markdown("---")
                st.subheader("AI分析报告")
                st.write(prediction)

                # 模拟干预建议
                st.subheader("💡 干预建议")
                suggestions = [
                    "提供学业辅导",
                    "调整学习计划",
                    "提供心理咨询",
                    "改善出勤情况",
                    "加强师生沟通"
                ]
                for i, sug in enumerate(suggestions[:3]):
                    st.checkbox(f"{i + 1}. {sug}")

        # 模拟器
        st.header("🎮 降级决策模拟器")

        col1, col2, col3 = st.columns(3)

        with col1:
            gpa_improve = st.slider("GPA提升幅度 (%)", -20, 50, 0)

        with col2:
            tutoring = st.slider("辅导时间增加", 0, 100, 50)

        with col3:
            absence_reduce = st.slider("减少缺勤 (%)", 0, 100, 0)

        if st.button("模拟降级风险变化"):
            with st.spinner("计算中..."):
                time.sleep(1)

                # 简单模拟风险变化
                base_risk = np.random.randint(20, 80)
                adjusted_risk = base_risk - gpa_improve * 0.5 - tutoring * 0.3 - absence_reduce * 0.2
                adjusted_risk = max(0, min(100, adjusted_risk))

                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=adjusted_risk,
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "模拟后降级风险"},
                    gauge={
                        'axis': {'range': [0, 100]},
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [0, 30], 'color': "green"},
                            {'range': [30, 70], 'color': "orange"},
                            {'range': [70, 100], 'color': "red"}]
                    }
                ))

                st.plotly_chart(fig, use_container_width=True)

                st.metric("风险变化",
                          f"{adjusted_risk}%",
                          delta=f"{adjusted_risk - base_risk}%")
    dropout_projections()
def Student_Counseling_Analysis():
    # 页面样式设置
    st.markdown("""
        <style>
            .stChatInput {
                bottom: 20px;
                position: fixed;
                width: 85%;
            }
            .stChatMessage {
                padding: 12px 16px;
                border-radius: 12px;
                margin-bottom: 12px;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
            }
            .stTextArea textarea {
                border-radius: 8px;
                padding: 10px;
            }
            .stFileUploader {
                margin-bottom: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    # DeepSeek API 配置
    DEEPSEEK_API_KEY = "sk-24d37178569a4f9d9ee09925e6edffa5"
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

    # 初始化消息历史
    if "messages_student_counseling_analysis" not in st.session_state:
        st.session_state["messages_student_counseling_analysis"] = [
            {"role": "assistant",
             "content": "我是学生谈心谈话分析助手，请上传谈话记录文档，我将开始分析。\n\n分析维度：\n1. 学生情绪状态评估\n2. 主要问题识别\n3. 潜在风险预警\n4. 建议干预措施\n5. 谈话技巧评价\n\n[开始分析]"}]

    # 创建标题
    colored_header(
        label="📝 学生谈心谈话记录分析",
        description="AI辅助分析学生谈话内容，识别问题并提供建议",
        color_name="blue-70",
    )

    # 显示历史消息
    for msg in st.session_state.messages_student_counseling_analysis:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # 从Word文档提取文本
    def extract_text_from_word(file):
        doc = Document(file)
        return '\n'.join(para.text for para in doc.paragraphs)

    # 上传文件区域
    with stylable_container(
            key="file_uploader",
            css_styles="""
            {
                background-color: #f0f2f6;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
            }
        """
    ):
        st.markdown("### 📤 上传谈话记录")
        doc_file = st.file_uploader("选择Word格式的谈话记录", type=["docx"], label_visibility="collapsed")

    # 文件上传处理
    if doc_file is not None:
        with st.spinner("正在分析谈话记录..."):
            text = extract_text_from_word(doc_file)
            st.success("谈话记录解析完成！")

            # 显示谈话内容
            with stylable_container(
                    key="text_area",
                    css_styles="""
                    {
                        border: 1px solid #e1e4e8;
                        border-radius: 10px;
                        padding: 15px;
                        margin-bottom: 20px;
                    }
                """
            ):
                st.markdown("### 📄 谈话内容摘要")
                st.text_area("", value=text, height=300, label_visibility="collapsed")

            # 发送分析请求
            if text:
                analysis_criteria = """
                请根据以下维度分析这份学生谈心谈话记录：
                1. 学生情绪状态评估（情绪类型、强度、稳定性）
                2. 主要问题识别（学习压力、人际关系、家庭问题等）
                3. 潜在风险预警（心理危机、行为问题等）
                4. 建议干预措施（具体可操作的建议）
                5. 谈话技巧评价（教师回应方式的有效性分析）

                请给出结构化分析报告，包含具体证据和支持点。
                """

                full_prompt = f"谈话记录内容：{text}\n\n{analysis_criteria}"

                st.session_state.messages_student_counseling_analysis.append({"role": "user", "content": "请分析这份谈话记录"})
                st.chat_message("user").write("请分析这份谈话记录")

                # 创建用于显示流式输出的容器
                response_container = st.empty()
                full_response = ""

                # 流式调用DeepSeek API
                stream = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": "你是一名专业的心理咨询师助手，擅长分析学生谈话记录"},
                        {"role": "user", "content": full_prompt}
                    ],
                    stream=True
                )

                # 逐步显示响应内容
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        chunk_content = chunk.choices[0].delta.content
                        full_response += chunk_content
                        response_container.markdown(full_response)

                # 将完整响应添加到消息历史
                st.session_state.messages_student_counseling_analysis.append({"role": "assistant", "content": full_response})

    # 用户提问处理（流式）
    if prompt := st.chat_input("关于谈话分析有什么问题..."):
        if not DEEPSEEK_API_KEY:
            st.info("请配置API密钥以继续使用。")
            st.stop()

        st.session_state.messages_student_counseling_analysis.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # 创建用于显示流式输出的容器
        response_container = st.empty()
        full_response = ""

        # 流式调用DeepSeek API
        stream = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages_student_counseling_analysis],
            stream=True
        )

        # 逐步显示响应内容
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                chunk_content = chunk.choices[0].delta.content
                full_response += chunk_content
                response_container.markdown(full_response)

        # 将完整响应添加到消息历史
        st.session_state.messages_student_counseling_analysis.append({"role": "assistant", "content": full_response})
def Student_Portraits():
    def generate_demo_data():
        # 基础信息
        employees = {
            '姓名': ['王思远', '李婧怡', '张子轩', '陈昊然', '何俊杰'],
            '学号': ['220231001', '220231002', '220231003', '220231004', '220231005'],
            '性别': ['女', '女', '男', '女', '男'],
            '年龄': [18, 19, 20, 19, 18],
            '学历': ['本科', '本科', '本科', '本科', '本科'],
            '学院': ['计算机学院', '商学院', '理学院', '文学院', '工程学院'],
            '专业': ['计算机科学', '金融学', '数学', '汉语言文学', '机械工程'],
            '入学日期': ['2022-09-01', '2021-09-01', '2020-09-01', '2021-09-01', '2022-09-01'],
            '在读状态': ['在读', '在读', '在读', '休学', '在读'],
            '联系电话': ['13800138001', '13800138002', '13800138003', '13800138004', '13800138005'],
            '学业成绩': [85, 92, 78, 88, 95],
            '年级': ['大一', '大二', '大三', '大二', '大一'],
            '专业技能': ['Python,机器学习', '金融分析,投资管理', '数学建模,统计分析', '文学创作,编辑校对',
                         '机械设计,CAD制图'],
            '项目经验': ['5个', '3个', '8个', '10个', '4个'],
            '获奖记录': ['三好学生', '优秀学生干部', '学术竞赛奖', '无', '文体活动奖'],
            '培训记录': ['领导力培训', '学术写作培训', '无', '文学创作培训', '工程实践培训'],
            '图片路径': ['OIP (3).jpeg', 'OIP (2).jpeg', 'OIP.png', '下载.jpeg',
                         'OIP (1).png']
        }

        # 行为数据
        behavior_data = {
            '姓名': ['王思远', '王思远', '李婧怡', '张子轩', '陈昊然', '何俊杰', '王思远', '李婧怡', '张子轩'],
            '类别': ['学业咨询', '导师面谈', '职业规划', '学业咨询', '导师面谈', '职业规划', '学业咨询', '导师面谈',
                     '职业规划'],
            '内容': [
                '完成课程项目A的开发任务',
                '学业表现优秀，建议申请奖学金',
                '希望向学术研究方向发展',
                '参加学术竞赛效果显著',
                '需要加强团队协作能力',
                '考虑跨专业选修课程',
                '提出创新实验方案',
                '完成学术论文写作',
                '获得专业认证'
            ],
            '地点': ['教学楼201', '导师办公室', '会议室305', '教学楼201', '导师办公室', '会议室305', '教学楼201',
                     '导师办公室', '会议室305'],
            '日期': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-12', '2023-06-18', '2023-07-22',
                     '2023-08-15', '2023-09-30'],
            '记录人': ['王老师', '李导师', '张教授', '王老师', '李导师', '张教授', '王老师', '李导师', '张教授']
        }

        # 学业数据
        performance_data = {
            '姓名': ['王思远', '王思远', '王思远', '李婧怡', '李婧怡', '李婧怡', '张子轩', '张子轩', '张子轩', '陈昊然', '陈昊然', '陈昊然',
                     '何俊杰',
                     '何俊杰'],
            '年度': [2021, 2022, 2023, 2021, 2022, 2023, 2021, 2022, 2023, 2021, 2022, 2023, 2021, 2022],
            '学业成绩': [85, 88, 90, 92, 94, 95, 78, 82, 85, 88, 90, 92, 95, 96],
            '奖学金': [5000, 5500, 6000, 6000, 6500, 7000, 4500, 5000, 5500, 5500, 6000, 6500, 7000, 7500],
            '助学金': [3000, 3150, 3300, 3300, 3450, 3600, 2850, 3000, 3150, 3150, 3300, 3450, 3600, 3750],
            '竞赛奖金': [2000, 2200, 2500, 2500, 2800, 3000, 1800, 2000, 2200, 2200, 2500, 2800, 3000, 3500]
        }

        # 项目数据
        project_data = {
            '姓名': ['王思远'] * 3 + ['李婧怡'] * 2 + ['张子轩'] * 4 + ['陈昊然'] * 3 + ['何俊杰'] * 2,
            '项目名称': ['课程项目A', '创新项目B', '科研项目C', '学术竞赛X', '商业策划Y',
                         '数学建模比赛', '数据分析项目', '算法研究', '毕业论文',
                         '文学创作计划', '编辑出版项目', '社会调研',
                         '工程实践项目', '机械设计比赛'],
            '项目角色': ['项目组长', '核心成员', '研究员', '队长', '执行人',
                         '项目总监', '数据分析师', '负责人', '主笔人',
                         '主编', '项目经理', '执行人',
                         '技术负责人', '设计组长'],
            '项目时长(月)': [6, 3, 9, 2, 4, 12, 6, 8, 10, 5, 3, 2, 1, 6],
            '项目评分': [90, 85, 95, 88, 92, 87, 93, 89, 91, 94, 86, 90, 97, 84]
        }

        return {
            'students': pd.DataFrame(employees),
            'behavior': pd.DataFrame(behavior_data),
            'performance': pd.DataFrame(performance_data),
            'projects': pd.DataFrame(project_data)
        }

    def show_personal_info(personal_info):
        """展示学生的基本信息"""
        st.header(f"👤 {personal_info['姓名']} 的学生画像")

        # 使用卡片式布局
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            with st.container(border=True):
                st.subheader("📸 照片")
                image_path = personal_info.get('图片路径', '')
                if image_path:
                    try:
                        image = Image.open(image_path)
                        st.image(image, caption=personal_info['姓名'], width=200, use_container_width=True)
                    except:
                        st.image(Image.new('RGB', (200, 200), color='gray'), caption='暂无照片', width=200)
                else:
                    st.image(Image.new('RGB', (200, 200), color='gray'), caption='暂无照片', width=200)

        with col2:
            with st.container(border=True):
                st.subheader("📋 基本信息")
                info_mapping = {
                    "学号": "🆔",
                    "性别": "👫",
                    "年龄": "🎂",
                    "学历": "🎓",
                    "学院": "🏛️",
                    "专业": "📚",
                    "入学日期": "📅",
                    "在读状态": "🟢",
                    "联系电话": "📱"
                }

                for key, emoji in info_mapping.items():
                    if key in personal_info:
                        st.markdown(f"{emoji} **{key}**: {personal_info[key]}")

        with col3:
            with st.container(border=True):
                st.subheader("🏆 学业表现")
                performance_mapping = {
                    "学业成绩": "📊",
                    "年级": "📈",
                    "专业技能": "🛠️",
                    "项目经验": "📂",
                    "获奖记录": "🏅",
                    "培训记录": "🎯"
                }

                for key, emoji in performance_mapping.items():
                    if key in personal_info:
                        value = personal_info[key] if pd.notna(personal_info[key]) else "无"
                        st.markdown(f"{emoji} **{key}**: {value}")

    def show_behavior_info(behavior_data):
        """展示学业沟通记录"""
        st.header("🗣️ 学业沟通记录")

        if behavior_data.empty:
            st.info("ℹ️ 暂无沟通记录")
            return

        # 按日期排序
        behavior_data = behavior_data.sort_values('日期', ascending=False)

        # 使用标签页分类显示
        tab1, tab2 = st.tabs(["📅 按时间排序", "🗂 按类别查看"])

        with tab1:
            for _, row in behavior_data.iterrows():
                category, content, location, date, person = row
                with st.expander(f"📌 {category} - {date}", expanded=False):
                    st.markdown(f"""
                    **📍 地点**: {location}  
                    **📝 记录人**: {person}  
                    **📄 内容**:  
                    {content}
                    """)

        with tab2:
            categories = behavior_data['类别'].unique()
            for category in categories:
                with st.expander(f"📁 {category}", expanded=False):
                    category_data = behavior_data[behavior_data['类别'] == category]
                    for _, row in category_data.iterrows():
                        _, content, location, date, person = row
                        st.markdown(f"""
                        **📅 日期**: {date}  
                        **📍 地点**: {location}  
                        **📝 记录人**: {person}  
                        **📄 内容**:  
                        {content}
                        """)
                        st.markdown("---")

    def show_personal_development(personal_info, behavior_data):
        st.header("📈 学业发展分析")

        # 使用标签页组织内容
        tab1, tab2, tab3 = st.tabs(["🏆 奖惩情况", "🌟 能力评估", "📊 发展分析"])

        with tab1:
            st.subheader("奖励记录")
            rewards = personal_info['获奖记录'].split('、') if '获奖记录' in personal_info and pd.notna(
                personal_info['获奖记录']) and personal_info['获奖记录'] != '无' else []
            if rewards:
                for i, reward in enumerate(rewards, 1):
                    st.markdown(f"{i}. 🏅 {reward}")
            else:
                st.info("暂无奖励记录")

            st.subheader("培训记录")
            trainings = personal_info['培训记录'].split('、') if '培训记录' in personal_info and pd.notna(
                personal_info['培训记录']) and personal_info['培训记录'] != '无' else []
            if trainings:
                for i, training in enumerate(trainings, 1):
                    st.markdown(f"{i}. 🎯 {training}")
            else:
                st.info("暂无培训记录")

        with tab2:
            st.subheader("能力评估雷达图")

            # 模拟能力数据
            categories = ['学术能力', '团队协作', '沟通能力', '领导力', '创新能力']
            values = [
                np.random.randint(80, 100),  # 学术能力
                np.random.randint(70, 95),  # 团队协作
                np.random.randint(75, 90),  # 沟通能力
                np.random.randint(65, 85),  # 领导力
                np.random.randint(70, 95)  # 创新能力
            ]

            # 创建雷达图
            fig = px.line_polar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                line_close=True,
                template="plotly_dark",
                title=" "
            )
            fig.update_layout(
                plot_bgcolor='white',  # 绘图区域背景色
                paper_bgcolor='white',  # 整个图表区域背景色
                title_font=dict(color='black'),  # 设置标题字体颜色
                polar=dict(bgcolor='white')  # 设置极坐标背景色为白色
            )
            fig.update_traces(fill='toself')
            st.plotly_chart(fig, use_container_width=True)

            # 能力说明
            with st.expander("📝 能力说明"):
                st.markdown("""
                - **学术能力**: 反映学生的学术知识和研究能力
                - **团队协作**: 反映学生的团队合作和协调能力
                - **沟通能力**: 反映学生的表达和沟通技巧
                - **领导力**: 反映学生的领导和管理能力
                - **创新能力**: 反映学生的创新思维和问题解决能力
                """)

        with tab3:
            st.subheader("学业发展轨迹")

            # 模拟发展数据
            progress_data = {
                '年份': [2018, 2019, 2020, 2021, 2022, 2023],
                '年级': ['高一', '高二', '高三', '大一', '大二', '大三'],
                '学业成绩': [80, 82, 85, 88, 90, 92]
            }

            # 创建折线图
            fig = px.line(
                progress_data,
                x='年份',
                y=['学业成绩'],
                title='学业发展轨迹',
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)

            # 添加发展建议
            with st.expander("💡 发展建议"):
                st.markdown("""
                1. **加强专业课程学习**，夯实学术基础
                2. **拓展跨学科知识**，提升综合素质
                3. **参与科研项目**，积累研究经验
                4. **获取专业认证**，提升专业竞争力
                5. **培养批判性思维**，提高学术水平
                """)

    def show_performance_evaluation(performance_data, selected_name):
        st.header("📊 学业考核")

        # 筛选当前学生的学业数据
        student_performance = performance_data[performance_data['姓名'] == selected_name]

        if student_performance.empty:
            st.warning("暂无学业数据")
            return

        # 使用标签页组织内容
        tab1, tab2, tab3 = st.tabs(["📈 学业趋势", "💰 奖学金分析", "📅 发展计划"])

        with tab1:
            st.subheader("年度学业成绩")

            # 创建学业成绩折线图
            fig = px.line(
                student_performance,
                x='年度',
                y='学业成绩',
                markers=True,
                title='年度学业成绩变化',
                text='学业成绩'
            )
            fig.update_traces(textposition="top center")
            fig.update_layout(
                yaxis_range=[70, 100],
                yaxis_title="学业成绩",
                xaxis_title="年度"
            )
            st.plotly_chart(fig, use_container_width=True)

            # 学业分析
            with st.expander("🔍 学业分析"):
                avg_score = student_performance['学业成绩'].mean()
                max_score = student_performance['学业成绩'].max()
                min_score = student_performance['学业成绩'].min()
                trend = "上升" if student_performance['学业成绩'].iloc[-1] > student_performance['学业成绩'].iloc[
                    0] else "下降"

                st.metric("平均成绩", f"{avg_score:.1f}")
                st.metric("最高成绩", max_score)
                st.metric("最低成绩", min_score)
                st.metric("变化趋势", trend)

        with tab2:
            st.subheader("奖学金构成分析")

            # 创建奖学金柱状图
            fig = px.bar(
                student_performance,
                x='年度',
                y=['奖学金', '助学金', '竞赛奖金'],
                barmode='group',
                title='年度奖学金构成'
            )
            st.plotly_chart(fig, use_container_width=True)

            # 奖学金增长分析
            st.subheader("奖学金增长分析")
            col1, col2, col3 = st.columns(3)

            with col1:
                scholarship_growth = (student_performance['奖学金'].iloc[-1] - student_performance['奖学金'].iloc[0]) / \
                                     student_performance['奖学金'].iloc[0] * 100
                st.metric("奖学金增长率", f"{scholarship_growth:.1f}%")

            with col2:
                grant_growth = (student_performance['助学金'].iloc[-1] - student_performance['助学金'].iloc[0]) / \
                               student_performance['助学金'].iloc[0] * 100
                st.metric("助学金增长率", f"{grant_growth:.1f}%")

            with col3:
                bonus_growth = (student_performance['竞赛奖金'].iloc[-1] - student_performance['竞赛奖金'].iloc[0]) / \
                               student_performance['竞赛奖金'].iloc[0] * 100
                st.metric("竞赛奖金增长率", f"{bonus_growth:.1f}%")

        with tab3:
            st.subheader("年度发展计划")

            # 模拟发展计划数据
            development_plans = {
                '2021': "1. 提升专业课程成绩\n2. 参加学术竞赛\n3. 参与社团活动",
                '2022': "1. 培养科研能力\n2. 主导小型研究项目\n3. 提升英语水平",
                '2023': "1. 准备研究生考试\n2. 培养学术思维\n3. 建立学术网络"
            }

            for year, plan in development_plans.items():
                with st.expander(f"📌 {year}年发展计划"):
                    st.markdown(plan)

    def show_project_data(project_data, selected_name):
        st.header("📂 项目经验分析")

        # 筛选当前学生的项目数据
        student_projects = project_data[project_data['姓名'] == selected_name]

        if student_projects.empty:
            st.warning("暂无项目数据")
            return

        # 使用标签页组织内容
        tab1, tab2 = st.tabs(["📋 项目列表", "📈 项目分析"])

        with tab1:
            st.subheader("参与项目列表")
            st.dataframe(student_projects[['项目名称', '项目角色', '项目时长(月)', '项目评分']],
                         hide_index=True,
                         column_config={
                             "项目名称": "项目名称",
                             "项目角色": "担任角色",
                             "项目时长(月)": st.column_config.NumberColumn("项目时长(月)", format="%d"),
                             "项目评分": st.column_config.NumberColumn("项目评分", format="%d")
                         })

        with tab2:
            st.subheader("项目表现分析")

            # 项目评分分析
            avg_score = student_projects['项目评分'].mean()
            max_score = student_projects['项目评分'].max()
            min_score = student_projects['项目评分'].min()

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("平均项目评分", f"{avg_score:.1f}")
            with col2:
                st.metric("最高项目评分", max_score)
            with col3:
                st.metric("最低项目评分", min_score)

            # 项目角色分布
            st.subheader("项目角色分布")
            role_counts = student_projects['项目角色'].value_counts()
            fig = px.pie(
                names=role_counts.index,
                values=role_counts.values,
                title='项目角色分布'
            )
            st.plotly_chart(fig, use_container_width=True)

            # 项目建议
            with st.expander("💡 项目发展建议"):
                st.markdown("""
                1. **参与更多跨学科项目**，拓展学术视野
                2. **尝试担任项目负责人角色**，积累管理经验
                3. **选择高质量科研项目**，提升学术能力
                4. **总结项目经验**，形成学术成果
                5. **建立项目成果档案**，展示综合能力
                """)

    def init_deepseek_client(api_key):
        return OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )

    def ask_deepseek(client, context, question, model="deepseek-chat"):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "你是一个专业的学业分析助手，能够根据提供的学生数据进行分析和建议。"},
                    {"role": "user", "content": f"上下文信息：{context}\n\n问题：{question}"}
                ],
                stream=False,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"获取AI回答时出错: {str(e)}"

    def show_ai_analysis(selected_name, personal_info, behavior_data, performance_data, project_data):
        st.header("🤖 AI智能分析")

        # 初始化DeepSeek客户端
        DEEPSEEK_API_KEY = "sk-24d37178569a4f9d9ee09925e6edffa5"  # 请替换为您的实际API密钥
        deepseek_client = init_deepseek_client(DEEPSEEK_API_KEY)

        # 准备上下文数据
        context = f"""
        学生姓名: {selected_name}
        基本信息: {personal_info.to_dict()}
        沟通记录: {behavior_data.to_dict('records') if not behavior_data.empty else '无'}
        学业数据: {performance_data[performance_data['姓名'] == selected_name].to_dict('records') if not performance_data.empty else '无'}
        项目数据: {project_data[project_data['姓名'] == selected_name].to_dict('records') if not project_data.empty else '无'}
        """

        # 使用标签页组织内容
        tab1, tab2 = st.tabs(["💬 智能问答", "📝 学生画像"])

        with tab1:
            st.subheader("关于该学生的智能问答")

            question = st.text_input("请输入您的问题",
                                     placeholder="例如: 该学生的核心优势是什么? 需要发展的方面有哪些?")

            if st.button("提交问题") and question:
                with st.spinner("AI正在思考..."):
                    response = ask_deepseek(deepseek_client, context, question)
                    st.markdown("### AI回答:")
                    st.markdown(response)

            # 预设问题
            st.subheader("常见问题")
            col1, col2 = st.columns(2)

            with col1:
                if st.button("该学生的核心优势是什么?"):
                    with st.spinner("AI正在分析..."):
                        response = ask_deepseek(deepseek_client, context, "该学生的核心优势是什么?")
                        st.markdown("### AI回答:")
                        st.markdown(response)

                if st.button("该学生适合什么发展方向?"):
                    with st.spinner("AI正在分析..."):
                        response = ask_deepseek(deepseek_client, context, "该学生适合什么发展方向?")
                        st.markdown("### AI回答:")
                        st.markdown(response)

            with col2:
                if st.button("该学生需要提升哪些能力?"):
                    with st.spinner("AI正在分析..."):
                        response = ask_deepseek(deepseek_client, context, "该学生需要提升哪些能力?")
                        st.markdown("### AI回答:")
                        st.markdown(response)

                if st.button("对该学生的培养建议?"):
                    with st.spinner("AI正在分析..."):
                        response = ask_deepseek(deepseek_client, context, "对该学生的培养建议?")
                        st.markdown("### AI回答:")
                        st.markdown(response)

        with tab2:
            st.subheader("AI生成的学生画像")

            if st.button("生成学生画像"):
                with st.spinner("AI正在生成学生画像..."):
                    prompt = f"根据以下学生数据，生成一份详细的学生画像报告，包括优势、劣势、发展建议等:\n\n{context}"
                    response = ask_deepseek(deepseek_client, context, prompt)

                    st.markdown("### AI生成的学生画像报告")
                    st.markdown(response)

                    # 保存报告
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    report_filename = f"学生画像报告_{selected_name}_{timestamp}.txt"

                    st.download_button(
                        label="下载报告",
                        data=response,
                        file_name=report_filename,
                        mime="text/plain"
                    )

    def RC():
        # 使用更美观的标题
        st.title("🎯 学生成长画像")
        st.markdown("---")  # 添加分隔线

        # 生成模拟数据
        demo_data = generate_demo_data()
        df = demo_data['students']
        behavior_df = demo_data['behavior']
        performance_df = demo_data['performance']
        project_df = demo_data['projects']

        # 添加搜索功能
        names = df['姓名'].dropna().unique().tolist()

        # 顶部搜索栏
        with st.container():
            col1, col2 = st.columns([3, 1])

            with col1:
                selected_name = st.selectbox("🔍 搜索学生姓名", names, help="从下拉列表中选择要查看的学生")

            with col2:
                st.markdown("")  # 垂直对齐
                st.markdown("")  # 垂直对齐
                if st.button("🔄 刷新数据", help="重新加载数据"):
                    st.rerun()

        st.markdown("---")

        # 导航标签页
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["👤 学生画像", "📈 学业发展", "📊 学业考核", "📂 项目经验", "🤖 AI分析"])

        # 获取当前学生数据
        personal_info = df[df['姓名'] == selected_name].iloc[0]
        behavior_data = behavior_df[behavior_df['姓名'] == selected_name][['类别', '内容', '地点', '日期', '记录人']]

        with tab1:
            show_personal_info(personal_info)
            st.markdown("---")
            show_behavior_info(behavior_data)

        with tab2:
            show_personal_development(personal_info, behavior_data)

        with tab3:
            show_performance_evaluation(performance_df, selected_name)

        with tab4:
            show_project_data(project_df, selected_name)

        with tab5:
            show_ai_analysis(selected_name, personal_info, behavior_data, performance_df, project_df)

    RC()
def Student_Deveploment_Part():
    # 自定义CSS样式
    st.markdown("""
    <style>
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem;
        }
        .header {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1a5276;
            margin-bottom: 1.5rem;
            text-align: center;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #1a5276;
        }
        .analysis-card {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }
        .analysis-card:hover {
            box-shadow: 0 6px 16px rgba(0,0,0,0.15);
        }
        .metric-card {
            border-left: 4px solid #2980b9;
            padding: 1rem;
            margin: 0.5rem;
            border-radius: 8px;
            background-color: #f8f9fa;
        }
        .stButton>button {
            border-radius: 20px;
            padding: 8px 20px;
            background-color: #2980b9;
            color: white;
            border: none;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #2471a3;
            transform: scale(1.02);
        }
        .stTextInput>div>div>input {
            border-radius: 20px !important;
            padding: 10px 15px !important;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade {
            animation: fadeIn 0.5s ease-out forwards;
        }
        .search-result-card {
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: #f8fafc;
        }
    </style>
    """, unsafe_allow_html=True)


    # 内置Lottie动画数据
    def get_default_lottie():
        return {
            "v": "5.5.2",
            "fr": 30,
            "ip": 0,
            "op": 60,
            "w": 500,
            "h": 500,
            "nm": "Student Avatar",
            "layers": [
                {
                    "ty": 1,
                    "sw": 500,
                    "sh": 500,
                    "sc": "#3498db",
                    "ks": {"o": {"a": 0, "k": 100}}
                },
                {
                    "ty": 4,
                    "nm": "Head",
                    "position": [250, 150],
                    "ks": {
                        "p": {"a": 0, "k": [250, 150]},
                        "s": {"a": 0, "k": [80, 80]}
                    },
                    "shapes": [{
                        "ty": "el",
                        "p": [0, 0],
                        "s": [80, 80]
                    }]
                }
            ]
        }


    # 加载动画
    def load_lottie(filepath: str) -> dict:
        if filepath == "student_avatar.json":
            return get_default_lottie()
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except:
            return get_default_lottie()


    # 生成唯一key
    def generate_key(*args) -> str:
        return hashlib.md5("_".join(str(arg) for arg in args).encode()).hexdigest()


    # 模拟学生数据库
    def generate_student_database(num: int = 50) -> pd.DataFrame:
        np.random.seed(42)
        ids = [f"2023{str(i).zfill(4)}" for i in range(1001, 1001 + num)]

        last_names = ["张", "王", "李", "赵", "刘"]
        first_names = ["伟", "芳", "娜", "秀英", "强", "洋", "明", "丽", "勇", "静", "杰", "敏"]
        names = []
        for i in range(num):
            last_name = last_names[i % len(last_names)]
            first_name = first_names[i % len(first_names)]
            names.append(f"{last_name}{first_name}")

        majors = np.random.choice(["计算机科学与技术", "电子信息工程", "机械工程", "经济管理", "外语"], num)
        grades = np.random.choice(["大一", "大二", "大三", "大四"], num)

        data = {
            "学号": ids,
            "姓名": names,
            "专业": majors,
            "年级": grades,
            "跨学科能力": np.random.normal(75, 12, num).clip(40, 100).round(1),
            "创新思维": np.random.normal(80, 10, num).clip(50, 100).round(1),
            "职业适配度": np.random.normal(70, 15, num).clip(30, 100).round(1),
            "深造潜力": np.random.normal(75, 10, num).clip(40, 100).round(1)
        }
        return pd.DataFrame(data)


    # 搜索功能
    def search_students(df: pd.DataFrame, query: str) -> Optional[pd.DataFrame]:
        if not query or not isinstance(query, str):
            return None

        query = query.strip()
        if not query:
            return None

        if query.isdigit() and len(query) == 8:
            result = df[df["学号"] == query]
            if not result.empty:
                return result

        if query.isdigit() and len(query) == 4:
            result = df[df["学号"].str.endswith(query)]
            if not result.empty:
                return result

        if query.isdigit() and len(query) == 4:
            result = df[df["学号"].str.startswith(query)]
            if not result.empty:
                return result

        name_result = df[df["姓名"].str.contains(query)]
        if not name_result.empty:
            return name_result

        major_result = df[df["专业"].str.contains(query)]
        if not major_result.empty:
            return major_result

        return None


    # 显示搜索结果
    def show_search_results(results: pd.DataFrame):
        st.success(f"🎯 找到 {len(results)} 条匹配结果")

        for _, row in results.iterrows():
            with st.container():
                avg_score = (row['跨学科能力'] + row['创新思维'] +
                             row['职业适配度'] + row['深造潜力']) / 4

                html_content = f"""
                <div class="search-result-card">
                    <div style="display:flex; align-items:center; margin-bottom:10px;">
                        <h3 style="margin:0; flex-grow:1;">{row['姓名']}</h3>
                        <span style="color:#666;">{row['学号']}</span>
                    </div>
                    <div style="display:flex; margin-bottom:8px;">
                        <span style="margin-right:15px;">📚 <strong>{row['专业']}</strong></span>
                        <span>🎓 {row['年级']}</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                        <span>🔢 综合评分: <strong>{avg_score:.1f}</strong></span>
                        <span>
                            <button style="background:#2980b9;color:white;border:none;border-radius:15px;padding:5px 12px;cursor:pointer;">
                                查看详情
                            </button>
                        </span>
                    </div>
                </div>
                """

                st.markdown(html_content, unsafe_allow_html=True)

                if st.button("查看详情", key=f"view_{row['学号']}", use_container_width=True):
                    st.session_state.current_student_student_development_part = row['学号']
                    st.session_state.page = "student_detail_student_development_part"
                    st.rerun()


    # 首页
    def home_page(df: pd.DataFrame):
        st.markdown('<div class="header animate-fade">学生发展潜能分析系统</div>', unsafe_allow_html=True)

        cols = st.columns(4)
        metrics = [
            ("学生总数", df.shape[0], "#2980b9"),
            ("高潜力学生", sum(df[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean(axis=1) > 80), "#27ae60"),
            ("平均创新思维", df["创新思维"].mean().round(1), "#f39c12"),
            ("平均深造潜力", df["深造潜力"].mean().round(1), "#9b59b6")
        ]

        for i, (title, value, color) in enumerate(metrics):
            with cols[i]:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>{title}</h3>
                    <h1 style="color: {color};">{value}</h1>
                </div>
                """, unsafe_allow_html=True)

        style_metric_cards()

        # 搜索功能
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("🔍 智能搜索")

            search_input = st.text_input(
                "输入学号(支持后4位)、姓名或专业",
                placeholder="例如: 1001 或 张伟 或 计算机",
                key="search_input"
            )

            if st.button("搜索", key="search_button"):
                st.session_state.search_query_student_development_part = search_input

            st.caption("💡 搜索提示: 支持完整学号(8位)、学号后4位、姓名(支持单字)、专业名称")

            if st.session_state.get("search_query_student_development_part"):
                results = search_students(df, st.session_state.search_query_student_development_part)
                if results is not None and not results.empty:
                    show_search_results(results)
                else:
                    st.warning("⚠️ 未找到匹配的学生，请尝试其他搜索词")

            st.markdown('</div>', unsafe_allow_html=True)

        # 高潜力学生推荐
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("🌟 高潜力学生推荐")

            df["综合评分"] = df[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean(axis=1)
            top_students = df.sort_values("综合评分", ascending=False).head(5)

            for _, row in top_students.iterrows():
                cols = st.columns([1, 3, 1])
                with cols[0]:
                    st.markdown(f"**{row['姓名']}**")
                    st.caption(f"{row['学号']} | {row['专业']}")
                with cols[1]:
                    st.progress(row["综合评分"] / 100,
                                text=f"综合评分: {row['综合评分']:.1f}")
                with cols[2]:
                    if st.button("查看详情", key=f"top_detail_{row['学号']}"):
                        st.session_state.current_student_student_development_part = row['学号']
                        st.session_state.page_student_development_part = "student_detail"
                        st.rerun()
                st.divider()
            st.markdown('</div>', unsafe_allow_html=True)

        # 全系能力分布
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("📊 全系能力分布")

            tab1, tab2 = st.tabs(["能力雷达图", "专业对比"])

            with tab1:
                avg_scores = df[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean().values
                labels = ["跨学科能力", "创新思维", "职业适配度", "深造潜力"]

                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=avg_scores,
                    theta=labels,
                    fill='toself',
                    name='全系平均'
                ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                    showlegend=False,
                    title="全系平均能力雷达图"
                )
                st.plotly_chart(fig, use_container_width=True)

            with tab2:
                major_avg = df.groupby("专业")[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean().reset_index()
                major_avg_long = pd.melt(
                    major_avg,
                    id_vars=["专业"],
                    value_vars=["跨学科能力", "创新思维", "职业适配度", "深造潜力"],
                    var_name="能力指标",
                    value_name="评分"
                )
                fig = px.bar(
                    major_avg_long,
                    x="专业",
                    y="评分",
                    color="能力指标",
                    barmode="group",
                    title="各专业能力对比",
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)


    # 学生详情页
    def student_detail_page(df: pd.DataFrame):
        student_id = st.session_state.get("current_student_student_development_part")
        if not student_id:
            st.session_state.page_student_development_part = "home"
            st.rerun()

        student_row = df[df["学号"] == student_id].iloc[0]
        student_data = {
            "学号": student_row["学号"],
            "姓名": student_row["姓名"],
            "专业": student_row["专业"],
            "年级": student_row["年级"],
            "跨学科能力": student_row["跨学科能力"],
            "创新思维": student_row["创新思维"],
            "职业适配度": student_row["职业适配度"],
            "深造潜力": student_row["深造潜力"]
        }

        st.markdown('<div class="header animate-fade">学生发展潜能分析报告</div>', unsafe_allow_html=True)

        if st.button("← 返回首页", key="back_button"):
            st.session_state.page_student_development_part = "home"
            st.rerun()

        scores = [
            student_data["跨学科能力"],
            student_data["创新思维"],
            student_data["职业适配度"],
            student_data["深造潜力"]
        ]
        avg_score = sum(scores) / len(scores)
        overall_avg = df[["跨学科能力", "创新思维", "职业适配度", "深造潜力"]].mean().mean()

        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 3])

            with col1:
                st_lottie(load_lottie("student_avatar.json"),
                          height=150,
                          key=generate_key("avatar", student_id))
                st.markdown(f"**姓名:** {student_data['姓名']}")
                st.markdown(f"**学号:** {student_data['学号']}")
                st.markdown(f"**专业:** {student_data['专业']}")
                st.markdown(f"**年级:** {student_data['年级']}")
                st.metric("综合评分",
                          f"{avg_score:.1f}",
                          delta=f"{avg_score - overall_avg:+.1f} vs 平均")

            with col2:
                labels = ['跨学科能力', '创新思维', '职业适配度', '深造潜力']
                scores = [student_data[l] for l in labels]
                avg_scores = df[labels].mean().values

                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=scores,
                    theta=labels,
                    fill='toself',
                    name='个人能力'
                ))
                fig.add_trace(go.Scatterpolar(
                    r=avg_scores,
                    theta=labels,
                    name='全系平均',
                    line=dict(color='red', dash='dot')
                ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                    showlegend=True,
                    title="个人能力与全系平均对比",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 详细能力分析
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("📈 详细能力分析")

            abilities = [
                ("跨学科能力", "学生在不同领域间建立联系和应用知识的能力", "#3498db"),
                ("创新思维", "学生在解决问题时展现的创造力和原创性", "#2ecc71"),
                ("职业适配度", "学生能力与职场需求的匹配程度", "#e74c3c"),
                ("深造潜力", "学生在学术研究领域的发展可能性", "#9b59b6")
            ]

            for i in range(0, len(abilities), 2):
                cols = st.columns(2)
                for j in range(2):
                    if i + j < len(abilities):
                        ability, desc, color = abilities[i + j]
                        with cols[j]:
                            with st.container():
                                st.markdown(f"### {ability}")
                                st.metric(
                                    "评分",
                                    f"{student_data[ability]}",
                                    delta=f"{student_data[ability] - df[ability].mean():+.1f} vs 平均"
                                )
                                st.write(desc)

                                if ability == "跨学科能力":
                                    months = pd.date_range(end="2023-11-01", periods=6, freq='M')
                                    trend_data = pd.DataFrame({
                                        "月份": months.strftime("%Y-%m"),
                                        "评分": np.linspace(
                                            student_data[ability] - 15,
                                            student_data[ability], 6
                                        ).clip(40, 100)
                                    })
                                    fig = px.line(
                                        trend_data,
                                        x="月份",
                                        y="评分",
                                        title=f"{ability}趋势",
                                        color_discrete_sequence=[color]
                                    )
                                    st.plotly_chart(fig, use_container_width=True)

                                elif ability == "创新思维":
                                    aspects = ["创意表达", "问题解决", "批判思维", "好奇心"]
                                    values = np.random.dirichlet(np.ones(4)) * student_data[ability]
                                    fig = px.pie(
                                        names=aspects,
                                        values=values,
                                        title=f"{ability}构成",
                                        color_discrete_sequence=[color]
                                    )
                                    st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 发展建议
        with st.container():
            st.markdown('<div class="analysis-card animate-fade">', unsafe_allow_html=True)
            st.subheader("📚 个性化发展建议")

            if student_data['深造潜力'] > 80:
                st.success("### 🎓 深造建议")
                st.write("""
                - 🏫 推荐申请国内外顶尖研究生院
                - 🔬 参与教授的研究项目积累经验
                - 📝 发表学术论文提升研究背景
                - 🌐 参加学术会议拓展视野
                """)
            else:
                st.info("### 🎓 深造建议")
                st.write("""
                - 💼 通过实习积累实践经验
                - 📚 考虑专业认证课程提升技能
                - ⏳ 工作2-3年后再评估深造需求
                - 🗣 参加行业研讨会了解前沿动态
                """)

            if student_data['职业适配度'] > 75:
                st.success("### 💼 职业发展建议")
                st.write("""
                - 🏢 瞄准行业领先企业求职
                - 👔 申请管理培训生项目
                - 👩‍🏫 参加职业导师计划
                - 🤝 建立专业社交网络
                """)
            else:
                st.info("### 💼 职业发展建议")
                st.write("""
                - 🔍 通过实习探索职业方向
                - 🛠 参加职业技能培训
                - 📄 完善简历和面试技巧
                - 🏭 考虑中小企业积累经验
                """)

            if student_data['创新思维'] < 70:
                st.warning("### 💡 创新能力提升建议")
                st.write("""
                - 🧠 参加创新思维工作坊
                - 🚀 参与创业竞赛活动
                - ✏️ 学习设计思维方法
                - 🌈 多接触跨领域知识
                """)
            st.markdown('</div>', unsafe_allow_html=True)


    # 主程序
    def Student_Development():
        if 'page_student_development_part' not in st.session_state:
            st.session_state.page_student_development_part = "home"

        df = generate_student_database()

        if st.session_state.page_student_development_part == "home":
            home_page(df)
        elif st.session_state.page_student_development_part == "student_detail":
            student_detail_page(df)

    Student_Development()




def get_ai_client():
    """Initializes and returns an OpenAI client configured for DeepSeek API."""
    return OpenAI(
        api_key="sk-24d37178569a4f9d9ee09925e6edffa5", # Replace with your actual key if different
        base_url="https://api.deepseek.com"
    )

def Chat_Box():
    st.title("职业生涯发展")

    # Initialize message history
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "您好，我是您的未来职业发展智能助手，有什么可以帮您的？"}]

    # Display message history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"], markdown=True)

    # Add selection boxes
    with st.container():
        option1 = st.selectbox('学历', ['本科生', '硕士研究生', '博士研究生'])
        option2 = st.selectbox('公司(如果没有请自行输入)',
                               ['', '国家电网', '南方电网', '国能投', '华能', '大唐', '华电', '国家电投', '三峡集团',
                                '中广核'])
        option3 = st.selectbox('地区', ['北京市', '天津市', '上海市', '重庆市', '河北省', '山西省', '辽宁省', '吉林省',
                                        '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省',
                                        '河南省', '湖北省',
                                        '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省',
                                        '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区', '西藏自治区',
                                        '宁夏回族自治区', '新疆维吾尔自治区', '香港特别行政区', '澳门特别行政区'])
        option4 = st.selectbox('发展方向', ['就业', '读研深造', '出国'])
        # Adding a text input for custom company if option2 is ''
        custom_company = ""
        if option2 == '':
             custom_company = st.text_input('请输入您希望了解的公司名称', '')


    if prompt := st.chat_input(key='chat_input_1'):
        # Construct the full query including selected options and user input
        context_prompt = f"我是一名{option1}"
        if option4 == "就业":
             company_info = custom_company if option2 == '' else option2
             location_info = f"的{option3}" if option3 != '' else ""
             if company_info or location_info:
                  context_prompt += f", 我想去{company_info}{location_info}工作。"
             else:
                  context_prompt += f", 我的发展方向是{option4}。"
        else:
             context_prompt += f", 我的发展方向是{option4}。"

        full_prompt = context_prompt + prompt

        # Add user message to chat history and display it
        st.session_state.messages.append({"role": "user", "content": full_prompt})
        st.chat_message("user").write(full_prompt, markdown=True)

        # Get the DeepSeek API client
        client = get_ai_client()

        try:
            # Use st.empty() to create a placeholder for the assistant's streaming response
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""

                # Call the DeepSeek API with stream=True
                stream = client.chat.completions.create(
                    model="deepseek-chat", # Specify the model
                    messages=[{"role": m["role"], "content": m["content"]}
                              for m in st.session_state.messages], # Send all messages
                    stream=True # Set stream to True for streaming
                )

                # Process the streaming response
                for chunk in stream:
                    # Check if there is content in the chunk
                    if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content is not None:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        # Update the placeholder with the current accumulated response
                        # We clean the <think> tag content *during* streaming to avoid displaying it
                        cleaned_response_partial = re.sub(r"<think>.*?</think>", "", full_response, flags=re.DOTALL)
                        message_placeholder.write(cleaned_response_partial, markdown=True)

                # After the stream is complete, clean the final response
                final_cleaned_response = re.sub(r"<think>.*?</think>", "", full_response, flags=re.DOTALL)

                # Append the full, cleaned response to the session state messages
                st.session_state.messages.append({"role": "assistant", "content": final_cleaned_response})

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Example of how to run the Chat_Box function in a Streamlit app:
# if __name__ == "__main__":
#     Chat_Box()

def Chat_Box1():

    FASTGPT_API_URL = 'https://s-ragflow.cpolar.top/api/v1/chats_openai/2ca243a6121611f0bd580242ac1a0006/chat/completions'
    FASTGPT_API_KEY = 'ragflow-UyNmM5NWEwMGJhZTExZjA5ZWQ5MDI0Mm'

    st.title("职业生涯发展")

    # 初始化消息历史
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "I am a smart assistant for your future,what can I help you？"}]

    # 显示消息历史
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    # 添加三个选择框
    with st.container():
        # 添加三个选择框
        option1 = st.selectbox('学历', ['本科生', '硕士研究生', '博士研究生'])
        option2 = st.selectbox('公司(如果没有请自行输入)',
                               ['', '国家电网', '南方电网', '国能投', '华能', '大唐', '华电', '国家电投', '三峡集团',
                                '中广核'])
        option3 = st.selectbox('地区', ['北京市', '天津市', '上海市', '重庆市', '河北省', '山西省', '辽宁省', '吉林省',
                                        '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省',
                                        '河南省', '湖北省',
                                        '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省',
                                        '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区', '西藏自治区',
                                        '宁夏回族自治区', '新疆维吾尔自治区', '香港特别行政区', '澳门特别行政区'])
        option4 = st.selectbox('发展方向', ['就业', '读研深造', '出国'])

    if prompt := st.chat_input(key='chat_input_1'):
        if not FASTGPT_API_KEY:
            st.info("Please add your FastGPT API key to continue.")
            st.stop()

        # 设置请求头
        headers = {
            'Authorization': f'Bearer {FASTGPT_API_KEY}',
            'Content-Type': 'application/json'
        }
        if option4=="就业":
            if option3!='':
                prompt = f"我是一名{option1},我想去{option2}的{option3}工作。"+prompt
            else:
                prompt = f"我是一名{option1},我想去{option2}。" + prompt
        else:
            prompt = f"我是一名{option1},我想{option4}。" + prompt
        # 设置请求体
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': st.session_state.messages + [{"role": "user", "content": prompt}],
            'stream': False
        }

        # 发送请求到FastGPT API
        response = requests.post(FASTGPT_API_URL, headers=headers, json=data)

        # 处理响应
        if response.status_code == 200:
            json_response = response.json()
            msg = json_response['choices'][0]['message']['content']

            # 过滤掉 <think></think> 部分的内容
            cleaned_msg = re.sub(r"<think>.*?</think>", "", msg, flags=re.DOTALL)

            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            st.session_state.messages.append({"role": "assistant", "content": cleaned_msg})
            st.chat_message("assistant").write(cleaned_msg)
        else:
            st.error(f"Error {response.status_code}: {response.text}")
def Dormitory_security():
    # 内联CSS样式
    st.markdown("""
    <style>
        /* 主容器样式 */
        .stApp {
            background-color: #f5f7fa;
            font-family: 'Arial', sans-serif;
        }

        /* 标题样式 */
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        /* 卡片样式 */
        .stMetric {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }

        .stMetric:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        /* 其他样式... */
    </style>
    """, unsafe_allow_html=True)

    # 模拟数据生成函数
    def generate_dorm_data():
        buildings = ['1号楼', '2号楼', '3号楼', '4号楼', '5号楼']
        rooms = [f"{building.split('号')[0]}-{floor}{room:02d}"
                 for building in buildings
                 for floor in range(1, 7)
                 for room in range(1, 21)]

        violations = [
            "违章电器", "夜不归宿", "抽烟", "酗酒", "大声喧哗",
            "私拉电线", "使用明火", "饲养宠物", "卫生不合格", "私自调换床位"
        ]

        electric_items = [
            "电热水壶", "电饭煲", "电磁炉", "电热毯", "电暖器",
            "洗衣机", "冰箱", "电吹风", "卷发棒", "电煮锅"
        ]

        data = []
        for room in random.sample(rooms, 50):
            record = {
                "宿舍号": room,
                "楼栋": room.split('-')[0] + "号楼",
                "人数": random.randint(4, 6),
                "最近检查日期": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'),
                "卫生评分": random.randint(60, 100),
                "违章物品": ", ".join(
                    random.sample(electric_items, random.randint(0, 3))) if random.random() > 0.7 else "无",
                "查寝违纪": ", ".join(
                    random.sample(violations, random.randint(0, 2))) if random.random() > 0.6 else "无",
                "跳闸次数": random.randint(0, 5),
                "抽烟记录": random.randint(0, 3),
                "酗酒记录": random.randint(0, 2),
                "总违纪次数": 0
            }

            # 计算总违纪次数
            record["总违纪次数"] = (
                    (1 if record["违章物品"] != "无" else 0) +
                    (1 if record["查寝违纪"] != "无" else 0) +
                    record["跳闸次数"] +
                    record["抽烟记录"] +
                    record["酗酒记录"]
            )

            data.append(record)

        return pd.DataFrame(data)

    # 加载数据
    @st.cache_data
    def load_data():
        return generate_dorm_data()

    df = load_data()

    # 页面标题和搜索栏
    st.title("🏠 宿舍安全管理平台")
    search_col, _ = st.columns([0.4, 0.6])
    with search_col:
        search_query = st.text_input("", placeholder="搜索宿舍号、楼栋或违纪类型...", key="search")

    # 筛选数据
    if search_query:
        mask = (
                df["宿舍号"].str.contains(search_query) |
                df["楼栋"].str.contains(search_query) |
                df["违章物品"].str.contains(search_query) |
                df["查寝违纪"].str.contains(search_query)
        )
        filtered_df = df[mask]
    else:
        filtered_df = df.copy()

    # KPI指标
    st.subheader("宿舍安全概览")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("严重违纪宿舍", f"{len(filtered_df[filtered_df['总违纪次数'] >= 3])}个",
                  delta=f"{len(filtered_df[filtered_df['总违纪次数'] >= 3]) - 5} 较上周" if len(
                      filtered_df) > 0 else "0")
    with col2:
        st.metric("待处理违章", f"{filtered_df['违章物品'].apply(lambda x: 0 if x == '无' else 1).sum()}项",
                  delta=f"{filtered_df['违章物品'].apply(lambda x: 0 if x == '无' else 1).sum() - 8} 较上周" if len(
                      filtered_df) > 0 else "0")
    with col3:
        st.metric("本月跳闸记录", f"{filtered_df['跳闸次数'].sum()}次",
                  delta=f"{filtered_df['跳闸次数'].sum() - 12} 较上月" if len(filtered_df) > 0 else "0")
    with col4:
        st.metric("优秀宿舍", f"{len(filtered_df[filtered_df['总违纪次数'] == 0])}个",
                  delta=f"{len(filtered_df[filtered_df['总违纪次数'] == 0]) - 15} 较上月" if len(
                      filtered_df) > 0 else "0")

    # 主内容区域
    tab1, tab2, tab3, tab4 = st.tabs(["严重违纪宿舍", "违章物品记录", "查寝违纪记录", "用电与行为记录"])

    with tab1:
        st.subheader("严重违纪宿舍列表")
        severe_df = filtered_df[filtered_df['总违纪次数'] >= 3].sort_values('总违纪次数', ascending=False)

        if not severe_df.empty:
            # 使用columns创建卡片布局
            for _, row in severe_df.iterrows():
                with st.container():
                    cols = st.columns([0.1, 0.2, 0.5, 0.2])
                    with cols[0]:
                        st.markdown(f"### {row['宿舍号']}")
                    with cols[1]:
                        st.markdown(f"**楼栋**: {row['楼栋']}")
                        st.markdown(f"**人数**: {row['人数']}人")
                    with cols[2]:
                        violations = []
                        if row['违章物品'] != '无':
                            violations.append(f"违章物品: {row['违章物品']}")
                        if row['查寝违纪'] != '无':
                            violations.append(f"查寝违纪: {row['查寝违纪']}")
                        if row['跳闸次数'] > 0:
                            violations.append(f"跳闸次数: {row['跳闸次数']}次")
                        if row['抽烟记录'] > 0:
                            violations.append(f"抽烟: {row['抽烟记录']}次")
                        if row['酗酒记录'] > 0:
                            violations.append(f"酗酒: {row['酗酒记录']}次")

                        st.markdown("**违纪记录**: " + " | ".join(violations))
                    with cols[3]:
                        st.markdown(f"**总违纪次数**: {row['总违纪次数']}")
                        st.button("处理记录", key=f"action_{row['宿舍号']}")

                    st.divider()
        else:
            st.success("当前没有严重违纪宿舍")

    with tab2:
        st.subheader("违章物品记录")
        violation_df = filtered_df[filtered_df['违章物品'] != '无']

        if not violation_df.empty:
            # 使用expandable表格
            for _, row in violation_df.iterrows():
                with st.expander(f"{row['宿舍号']} - {row['违章物品']}"):
                    cols = st.columns(3)
                    with cols[0]:
                        st.markdown(f"**楼栋**: {row['楼栋']}")
                        st.markdown(f"**人数**: {row['人数']}人")
                    with cols[1]:
                        st.markdown(f"**违章物品**: {row['违章物品']}")
                        st.markdown(f"**最近检查日期**: {row['最近检查日期']}")
                    with cols[2]:
                        st.markdown("**处理状态**: 待处理" if random.random() > 0.5 else "已处理")
                        st.button("确认处理", key=f"confirm_{row['宿舍号']}")
        else:
            st.success("当前没有违章物品记录")

    with tab3:
        st.subheader("查寝违纪记录")
        inspection_df = filtered_df[filtered_df['查寝违纪'] != '无']

        if not inspection_df.empty:
            # 使用图表和表格结合
            fig = px.bar(
                inspection_df,
                x='宿舍号',
                y=inspection_df['查寝违纪'].apply(lambda x: len(x.split(',')) if x != '无' else 0),
                color='楼栋',
                title="各宿舍查寝违纪次数"
            )
            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(
                inspection_df[['宿舍号', '楼栋', '查寝违纪', '最近检查日期']],
                column_config={
                    "宿舍号": "宿舍号",
                    "楼栋": "楼栋",
                    "查寝违纪": "违纪内容",
                    "最近检查日期": "检查日期"
                },
                hide_index=True
            )
        else:
            st.success("当前没有查寝违纪记录")

    with tab4:
        st.subheader("用电与行为记录")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 跳闸记录")
            power_df = filtered_df[filtered_df['跳闸次数'] > 0]
            if not power_df.empty:
                fig = px.pie(
                    power_df,
                    names='楼栋',
                    values='跳闸次数',
                    title="各楼栋跳闸次数分布"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("当前没有跳闸记录")

        with col2:
            st.markdown("#### 抽烟酗酒记录")
            behavior_df = filtered_df[(filtered_df['抽烟记录'] > 0) | (filtered_df['酗酒记录'] > 0)]
            if not behavior_df.empty:
                fig = px.bar(
                    behavior_df.melt(id_vars=['宿舍号', '楼栋'],
                                     value_vars=['抽烟记录', '酗酒记录'],
                                     var_name='类型',
                                     value_name='次数'),
                    x='宿舍号',
                    y='次数',
                    color='类型',
                    barmode='group',
                    title="各宿舍抽烟酗酒情况"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("当前没有抽烟酗酒记录")

    # 添加一些动画效果
    st.markdown("""
    <style>
        /* 添加一些悬停效果 */
        .stMetric {
            transition: all 0.3s ease;
        }
        .stMetric:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        /* 标签页切换动画 */
        .stTabs [role="tablist"] button [data-testid="stMarkdownContainer"] p {
            transition: all 0.3s ease;
        }
        .stTabs [role="tablist"] button:hover [data-testid="stMarkdownContainer"] p {
            color: #1e88e5;
            transform: scale(1.05);
        }

        /* 按钮悬停效果 */
        .stButton button {
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            transform: scale(1.05);
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }
    </style>
    """, unsafe_allow_html=True)
def Exception_logging():
    # 直接在代码中定义CSS样式
    def local_css():
        st.markdown("""
        <style>
        /* 主标题样式 */
        .header {
            text-align: center;
            margin-bottom: 2rem;
            padding: 1rem;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        /* 学生卡片样式 */
        .student-card {
            background-color: white;
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .student-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        .student-card h3 {
            color: #333;
            margin-top: 0;
            border-bottom: 1px solid #eee;
            padding-bottom: 0.5rem;
        }

        /* 按钮样式 */
        .stButton>button {
            border-radius: 20px;
            border: none;
            background-color: #4a6cf7;
            color: white;
            padding: 0.5rem 1rem;
            transition: all 0.3s;
        }

        .stButton>button:hover {
            background-color: #3a5bd9;
            transform: scale(1.05);
        }

        /* 搜索框样式 */
        .stTextInput>div>div>input {
            border-radius: 20px;
            padding: 0.5rem 1rem;
            border: 1px solid #ddd;
        }

        /* 分割线样式 */
        .stMarkdown hr {
            margin: 2rem 0;
            border: none;
            height: 1px;
            background: linear-gradient(to right, transparent, #6e8efb, transparent);
        }

        /* 详情展开面板样式 */
        .st-emotion-cache-1c7z2jk {
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            border: none;
            margin-bottom: 1rem;
        }

        /* 响应式调整 */
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }

            .header p {
                font-size: 1rem;
            }
        }
        </style>
        """, unsafe_allow_html=True)

    local_css()  # 应用CSS样式

    # 模拟数据
    @st.cache_data
    def load_data():
        # 当前有心理问题的学生
        current_issues = pd.DataFrame({
            '学号': ['202301001', '202301005', '202301009', '202302001', '202302007'],
            '姓名': ['隋轶楠', '杨洋', '谢洋', '彭玉龙', '刘悦'],
            '年级': ['大一', '大二', '大三', '大四', '研究生'],
            '专业': ['计算机', '心理学', '数学', '物理', '化学'],
            '问题类型': ['抑郁倾向', '焦虑症状', '睡眠障碍', '人际关系', '学业压力'],
            '严重程度': ['中度', '轻度', '重度', '中度', '轻度'],
            '最近记录日期': ['2023-05-10', '2023-05-12', '2023-05-15', '2023-05-18', '2023-05-20'],
            '辅导员': ['王老师', '李老师', '张老师', '赵老师', '钱老师']
        })

        # 可能有心理问题的学生（预警）
        potential_issues = pd.DataFrame({
            '学号': ['202302009', '202302011', '202302020', '202303002', '202303022'],
            '姓名': ['严畅', '刘风', '张明远', '李思诚', '王浩然'],
            '年级': ['大一', '大二', '大三', '大四', '研究生'],
            '专业': ['生物', '历史', '哲学', '经济', '法律'],
            '预警原因': ['近期成绩下降', '缺勤频繁', '社交减少', '情绪波动大', '家庭变故'],
            '预警等级': ['低', '中', '高', '中', '高'],
            '最近记录日期': ['2023-05-08', '2023-05-11', '2023-05-14', '2023-05-17', '2023-05-19'],
            '辅导员': ['孙老师', '周老师', '吴老师', '郑老师', '王老师']
        })

        # 去年同期有问题的学生
        last_year_issues = pd.DataFrame({
            '学号': ['202303029', '202304003', '202304009', '202304016', '202305006'],
            '姓名': ['刘雨欣', '赵雅婷', '周若曦', '吴诗涵', '李钰'],
            '年级': ['大二', '大三', '大四', '研究生', '毕业生'],
            '专业': ['医学', '艺术', '工程', '教育', '管理'],
            '去年问题类型': ['抑郁倾向', '焦虑症状', '睡眠障碍', '人际关系', '学业压力'],
            '去年严重程度': ['中度', '轻度', '重度', '中度', '轻度'],
            '去年记录日期': ['2022-05-09', '2022-05-12', '2022-05-15', '2022-05-18', '2022-05-21'],
            '辅导员': ['冯老师', '陈老师', '褚老师', '卫老师', '蒋老师']
        })

        return current_issues, potential_issues, last_year_issues

    current_issues, potential_issues, last_year_issues = load_data()

    # 主页面
    def main_page():
        st.markdown("""
        <div class='header'>
            <h1>学生心理健康预警系统</h1>
            <p>实时监控学生心理健康状况，及时发现并干预潜在问题</p>
        </div>
        """, unsafe_allow_html=True)

        # 搜索框
        search_term = st.text_input("🔍 搜索学生 (按姓名、学号或专业)", "")

        # 分割线
        st.markdown("---")

        # 当前有心理问题的学生
        st.markdown("<h2 id='current-issues'>当前有心理问题的学生</h2>", unsafe_allow_html=True)
        display_students(current_issues, search_term, "current")

        # 分割线
        st.markdown("---")

        # 可能有心理问题的学生
        st.markdown("<h2 id='potential-issues'>可能有心理问题的学生 (预警)</h2>", unsafe_allow_html=True)
        display_students(potential_issues, search_term, "potential")

        # 分割线
        st.markdown("---")

        # 去年同期有问题的学生
        st.markdown("<h2 id='last-year-issues'>去年同期有心理问题的学生</h2>", unsafe_allow_html=True)
        display_students(last_year_issues, search_term, "last_year")

        # 添加一些动画效果
        html("""
        <script>
        // 简单的滚动动画
        document.addEventListener('DOMContentLoaded', function() {
            const cards = document.querySelectorAll('.st-emotion-cache-1v0mbdj');
            cards.forEach((card, index) => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                setTimeout(() => {
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }, 100 * index);
            });
        });
        </script>
        """)

    # 显示学生数据的通用函数
    def display_students(df, search_term, issue_type):
        # 应用搜索过滤
        if search_term:
            mask = (
                    df['姓名'].str.contains(search_term) |
                    df['学号'].str.contains(search_term) |
                    df['专业'].str.contains(search_term)
            )
            df = df[mask]

        if df.empty:
            st.warning("没有找到匹配的学生记录")
            return

        # 根据问题类型显示不同的列
        if issue_type == "current":
            columns_to_display = ['姓名', '学号', '年级', '专业', '问题类型', '严重程度', '最近记录日期', '辅导员']
        elif issue_type == "potential":
            columns_to_display = ['姓名', '学号', '年级', '专业', '预警原因', '预警等级', '最近记录日期', '辅导员']
        else:  # last_year
            columns_to_display = ['姓名', '学号', '年级', '专业', '去年问题类型', '去年严重程度', '去年记录日期',
                                  '辅导员']

        # 使用卡片式布局显示学生
        cols = st.columns(3)
        for idx, row in df.iterrows():
            with cols[idx % 3]:
                # 根据问题类型设置不同的卡片颜色
                if issue_type == "current":
                    color = "#ff4b4b"  # 红色表示当前问题
                elif issue_type == "potential":
                    color = "#ffa500"  # 橙色表示潜在问题
                else:
                    color = "#6a5acd"  # 紫色表示历史问题

                with st.container():
                    st.markdown(f"""
                    <div class='student-card' style='border-left: 5px solid {color};'>
                        <h3>{row['姓名']} ({row['学号']})</h3>
                        <p><strong>年级/专业:</strong> {row['年级']} {row['专业']}</p>
                        {f"<p><strong>问题类型:</strong> {row['问题类型' if issue_type == 'current' else '预警原因' if issue_type == 'potential' else '去年问题类型']}</p>"}
                        {f"<p><strong>严重程度:</strong> {row['去年严重程度' if issue_type == 'last_year' else '严重程度' if issue_type == 'current' else '预警等级']}</p>"}
                        <p><strong>最近记录:</strong> {row['最近记录日期' if issue_type in ['current', 'potential'] else '去年记录日期']}</p>
                        <p><strong>辅导员:</strong> {row['辅导员']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    # 添加详情按钮
                    if st.button(f"查看详情", key=f"detail_{issue_type}_{idx}"):
                        show_student_detail(row, issue_type)

        # 如果没有填满一行，添加空卡片保持布局
        if len(df) % 3 != 0:
            for _ in range(3 - (len(df) % 3)):
                with cols[2 - (len(df) % 3 - 1)]:
                    st.empty()

    # 显示学生详情
    def show_student_detail(student, issue_type):
        # 使用弹出效果
        with st.expander(f"📌 {student['姓名']} 的详细信息", expanded=True):
            st.subheader("基本信息")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**学号:** {student['学号']}")
                st.write(f"**年级:** {student['年级']}")
            with col2:
                st.write(f"**专业:** {student['专业']}")
                st.write(f"**辅导员:** {student['辅导员']}")

            st.markdown("---")
            st.subheader("心理健康信息")

            if issue_type == "current":
                st.write(f"**问题类型:** {student['问题类型']}")
                st.write(f"**严重程度:** {student['严重程度']}")
                st.write(f"**最近记录日期:** {student['最近记录日期']}")

                # 添加简单的趋势图
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=70 if student['严重程度'] == '轻度' else 50 if student['严重程度'] == '中度' else 30,
                    title={'text': "心理状态评估"},
                    gauge={
                        'axis': {'range': [None, 100]},
                        'steps': [
                            {'range': [0, 40], 'color': "red"},
                            {'range': [40, 70], 'color': "orange"},
                            {'range': [70, 100], 'color': "green"}],
                        'threshold': {
                            'line': {'color': "black", 'width': 4},
                            'thickness': 0.75,
                            'value': 70 if student['严重程度'] == '轻度' else 50 if student[
                                                                                        '严重程度'] == '中度' else 30}
                    }
                ))
                st.plotly_chart(fig, use_container_width=True)


            elif issue_type == "potential":

                st.write(f"**预警原因:** {student['预警原因']}")

                st.write(f"**预警等级:** {student['预警等级']}")

                st.write(f"**最近记录日期:** {student['最近记录日期']}")

                # 预警雷达图

                categories = ['学业表现', '社交活动', '出勤率', '情绪稳定', '身体健康']

                fig = go.Figure()

                fig.add_trace(go.Scatterpolar(

                    r=[7, 5, 6, 4, 8] if student['预警等级'] == '低' else [5, 4, 3, 6, 7] if student[
                                                                                                 '预警等级'] == '中' else [
                        3, 2, 4, 5, 6],

                    theta=categories,

                    fill='toself',

                    name='各项指标'

                ))

                fig.update_layout(

                    polar=dict(

                        radialaxis=dict(

                            visible=True,

                            range=[0, 10]

                        ),

                        # 增加角标签的边距，防止文字被截断

                        angularaxis=dict(

                            tickfont=dict(size=12)  # 调整字体大小

                        ),

                        # 增加整体边距

                        bgcolor='rgba(0,0,0,0)'

                    ),

                    # 调整整体图形大小和边距

                    margin=dict(l=50, r=50, t=50, b=50),

                    height=400,  # 增加高度

                    width=500,  # 增加宽度

                    showlegend=False

                )

                st.plotly_chart(fig, use_container_width=True)


            else:  # last_year

                st.write(f"**去年问题类型:** {student['去年问题类型']}")

                st.write(f"**去年严重程度:** {student['去年严重程度']}")

                st.write(f"**去年记录日期:** {student['去年记录日期']}")

                # 为每个学生生成独特的时间线（基于学号作为随机种子）

                random_seed = int(student['学号'][-3:])  # 使用学号后三位作为随机种子

                np.random.seed(random_seed)

                # 生成随机日期序列

                base_date = pd.to_datetime(student['去年记录日期'])

                dates = [

                    base_date - pd.Timedelta(days=np.random.randint(60, 90)),  # 首次咨询

                    base_date - pd.Timedelta(days=np.random.randint(30, 60)),  # 跟进评估

                    base_date,  # 问题确认

                    base_date + pd.Timedelta(days=np.random.randint(15, 30))  # 解决

                ]

                timeline_data = pd.DataFrame({

                    '日期': [d.strftime('%Y-%m-%d') for d in dates],

                    '事件': ['首次咨询', '跟进评估', '问题确认', '解决'],

                    '状态': ['正常', '关注', '问题', '解决']

                })

                fig = px.scatter(timeline_data, x='日期', y=[1] * len(timeline_data),

                                 color='状态', size=[10] * len(timeline_data),

                                 hover_name='事件',

                                 color_discrete_map={'正常': 'green', '关注': 'orange', '问题': 'red', '解决': 'blue'})

                fig.update_layout(

                    showlegend=False,

                    yaxis={'visible': False},

                    height=200,

                    margin=dict(l=20, r=20, t=30, b=20)  # 调整边距

                )

                st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")
            st.subheader("干预措施")

            if issue_type == "current":
                st.text_area("当前干预方案", "1. 每周心理咨询\n2. 辅导员定期跟进\n3. 学业支持计划",
                             key=f"plan_{student['学号']}")
            elif issue_type == "potential":
                st.text_area("预防措施建议", "1. 关注学生日常表现\n2. 定期谈心谈话\n3. 提供必要支持",
                             key=f"suggestion_{student['学号']}")
            else:
                st.text_area("去年干预措施回顾", "1. 心理咨询6次\n2. 家长沟通3次\n3. 学业调整方案",
                             key=f"review_{student['学号']}")

            col1, col2 = st.columns(2)
            with col1:
                st.button("保存记录", key=f"save_{student['学号']}")
            with col2:
                if st.button("关闭详情", key=f"close_{student['学号']}"):
                    pass  # 会自动关闭expander

    main_page()
