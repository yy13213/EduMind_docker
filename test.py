import requests
import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
from streamlit_extras.card import card
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
import plotly.graph_objects as go
from streamlit.components.v1 import html
import re

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from streamlit_extras.metric_cards import style_metric_cards
import time
import json
from datetime import datetime, timedelta

# # 页面设置
# st.set_page_config(
#     page_title="学生成长分析系统",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )


def Student_growth():
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

Student_growth()