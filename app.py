import streamlit as st
import HelloWeb

# 设置页面标题和图标
st.set_page_config(
    page_title="EduMind",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        /* 特别为心理特质按钮设置样式 */
         .special-button0 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button0:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button0:focus {
            background-color: #e3e5e7;
        }
         .special-button1 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button1:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button1:focus {
            background-color: #e3e5e7;
        }
         .special-button2 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button2:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button2:focus {
            background-color: #e3e5e7;
        }
         .special-button3 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button3:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button3:focus {
            background-color: #e3e5e7;
        }
         .special-button4 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button4:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button4:focus {
            background-color: #e3e5e7;
        }
         .special-button5 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button5:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button5:focus {
            background-color: #e3e5e7;
        }
         .special-button6 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button6:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button6:focus {
            background-color: #e3e5e7;
        }
         .special-button7 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button7:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button7:focus {
            background-color: #e3e5e7;
        }
         .special-button8 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button8:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button8:focus {
            background-color: #e3e5e7;
        }
         .special-button9 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button9:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button9:focus {
            background-color: #e3e5e7;
        }
         .special-button10 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button10:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button10:focus {
            background-color: #e3e5e7;
        }
         .special-button11 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button11:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button11:focus {
            background-color: #e3e5e7;
        }
         .special-button12 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button12:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button12:focus {
            background-color: #e3e5e7;
        }
         .special-button13 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button13:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button13:focus {
            background-color: #e3e5e7;
        }
         .special-button14 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button14:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button14:focus {
            background-color: #e3e5e7;
        }
         .special-button15 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button15:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button15:focus {
            background-color: #e3e5e7;
        }
         .special-button16 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button16:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button16:focus {
            background-color: #e3e5e7;
        }
         .special-button17 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button17:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button17:focus {
            background-color: #e3e5e7;
        }
         .special-button18 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button18:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button18:focus {
            background-color: #e3e5e7;
        }
         .special-button19 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button19:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button19:focus {
            background-color: #e3e5e7;
        }
        .special-button20 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button20:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button20:focus {
            background-color: #e3e5e7;
        }
        .special-button21 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button21:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button21:focus {
            background-color: #e3e5e7;
        }
        .special-button22 {
            width: 100%; 
            height: 50px; 
            font-size: 20px;
            background-color: #4C9AA8;  
            font-weight: bold;  
            border-radius: 12px;  
            border: none;
        }
        .special-button22:hover {
            background-color: #e3e5e7;
            opacity: 0.85;
        }
        .special-button22:focus {
            background-color: #e3e5e7;
        }
        /* 其他普通按钮样式 */
        .stButton>button {
            background: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
            color: white;
            width:100%!important;
            height: 50px
            border-radius: 25px;
            padding: 10px 24px;
            border: none;
            font-weight: 600;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            width:100%
        }
    </style>
    """,
    unsafe_allow_html=True
)
# 初始化 session_state
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

if "show_sub_buttons1" not in st.session_state:
    st.session_state.show_sub_buttons1 = False
if "show_sub_buttons2" not in st.session_state:
    st.session_state.show_sub_buttons2 = False
if "show_sub_buttons3" not in st.session_state:
    st.session_state.show_sub_buttons3 = False
if "show_sub_buttons4" not in st.session_state:
    st.session_state.show_sub_buttons4 = False
if "show_sub_buttons5" not in st.session_state:
    st.session_state.show_sub_buttons5 = False
if "show_sub_buttons6" not in st.session_state:
    st.session_state.show_sub_buttons6 = False
if "show_sub_buttons7" not in st.session_state:
    st.session_state.show_sub_buttons7 = False

st.sidebar.image("WechatIMG52.jpg", use_container_width=True)
# 侧边栏导航
if  st.sidebar.button("🏠 Home"):
    st.session_state.page = "🏠 Home"
    st.session_state.show_sub_buttons1 = False
    st.session_state.show_sub_buttons2 = False
    st.session_state.show_sub_buttons3 = False
    st.session_state.show_sub_buttons4 = False
    st.session_state.show_sub_buttons5 = False
    st.session_state.show_sub_buttons6 = False

if st.sidebar.button("🎓 学业发展"):
    st.session_state.page = "🎓 学业发展"
    st.session_state.show_sub_buttons1 = not st.session_state.show_sub_buttons1

if st.session_state.show_sub_buttons1:
    if st.sidebar.button("🤗 学生学业",key="special_button0", help="点击查看心理评测结果", args=(), on_click=None):
        st.session_state.page = "🤗 学生学业"
    if st.sidebar.button("📄 综合学业", key="special_button1", help="点击查看谈话文本分析", args=(), on_click=None):
        st.session_state.page = "📄 综合学业"
    # if st.sidebar.button("📏 学生成长分析", key="special_button2", help="点击查看谈话文本分析", args=(), on_click=None):
    #     st.session_state.page = "📏 学生成长分析"
    if st.sidebar.button("📖 降级预警", key="special_button3", help="点击查看谈话文本分析", args=(), on_click=None):
        st.session_state.page = "📖 降级预警"

# 生成按钮并为“心理特质”按钮加上特定类
if st.sidebar.button("🧑‍💻 心理特质"):
    st.session_state.page = "🧑‍💻 心理特质"
    st.session_state.show_sub_buttons2 = not st.session_state.show_sub_buttons2
# 子按钮
if st.session_state.show_sub_buttons2:
    if st.sidebar.button("🧾 心理咨询", key="special_button4", help="点击查看心理咨询", args=(), on_click=None):
        st.session_state.page = "🧾 心理咨询"
    if st.sidebar.button("📃 心理问卷", key="special_button5", help="点击查看心理问卷", args=(), on_click=None):
        st.session_state.page = "📃 心理问卷"
    if st.sidebar.button("📱 谈话记录分析", key="special_button6", help="点击查看谈话记录分析", args=(), on_click=None):
        st.session_state.page = "📱 谈话记录分析"
    if st.sidebar.button("⚠️ 异常记录", key="special_button22", help="点击查看异常记录", args=(), on_click=None):
        st.session_state.page = "⚠️ 异常记录"

if st.sidebar.button("🏃 行为规律"):
    st.session_state.page = "🏃 行为规律"
    st.session_state.show_sub_buttons3 = not st.session_state.show_sub_buttons3

if st.session_state.show_sub_buttons3:
    if st.sidebar.button("🏫 校园行为数据", key="special_button7", help="点击查看谈话文本分析", args=(), on_click=None):
        st.session_state.page = "🏫 校园行为数据"
    if st.sidebar.button("🎯 学生行为规律分析", key="special_button8", help="点击查看谈话文本分析", args=(), on_click=None):
        st.session_state.page = "🎯 学生行为规律分析"
    if st.sidebar.button("🏥 学生画像", key="special_button9", help="点击查看谈话文本分析", args=(), on_click=None):
        st.session_state.page = "🏥 学生画像"

if st.sidebar.button("🛜 社交网络"):
    st.session_state.page = "🛜 社交网络"
    st.session_state.show_sub_buttons4 = not st.session_state.show_sub_buttons4

if st.session_state.show_sub_buttons4:
    if st.sidebar.button("🍺 学生线上活跃度", key="special_button10", help="点击查看谈话文本分析", args=(), on_click=None):
        st.session_state.page = "🍺 学生线上活跃度"
    if st.sidebar.button("📝 总体线上活跃度", key="special_button11", help="点击查看谈话文本分析", args=(), on_click=None):
        st.session_state.page = "📝 总体线上活跃度"

if st.sidebar.button("📒 价值取向"):
    st.session_state.page = "📒 价值取向"
    st.session_state.show_sub_buttons5 = not st.session_state.show_sub_buttons5

if st.sidebar.button("🔐 安全管理"):
    st.session_state.page = "🔐 安全管理"
    st.session_state.show_sub_buttons7 = not st.session_state.show_sub_buttons7
# if st.session_state.show_sub_buttons5:
#     if st.sidebar.button("🈲 舆情敏感词", key="special_button12", help="点击查看谈话文本分析", args=(), on_click=None):
#         st.session_state.page = "🈲 舆情敏感词"
#     if st.sidebar.button("🇨🇳 党团活动参与度", key="special_button13", help="点击查看谈话文本分析", args=(), on_click=None):
#         st.session_state.page = "🇨🇳  党团活动参与度"
#     if st.sidebar.button("🔥 热点事件讨论文本分析", key="special_button14", help="点击查看谈话文本分析", args=(), on_click=None):
#         st.session_state.page = "🔥 热点事件讨论文本分析"

if st.sidebar.button("📈 发展潜能"):
    st.session_state.page = "📈 发展潜能"
    st.session_state.show_sub_buttons6 = not st.session_state.show_sub_buttons6

if st.session_state.show_sub_buttons6:
    # if st.sidebar.button("🥇 竞赛获奖记录", key="special_button15", help="点击查看谈话文本分析", args=(), on_click=None):
    #     st.session_state.page = "🥇 竞赛获奖记录"
    # if st.sidebar.button("🧑‍💻 科研项目参与度", key="special_button16", help="点击查看谈话文本分析", args=(), on_click=None):
    #     st.session_state.page = "🧑‍💻 课程考情"
    if st.sidebar.button("🔬 生涯规划助手", key="special_button17", help="点击查看谈话文本分析", args=(), on_click=None):
        st.session_state.page = "🔬 生涯规划助手"
    if st.sidebar.button("💬 职业规划测评", key="special_button18", help="点击查看谈话文本分析", args=(), on_click=None):
        st.session_state.page = "💬 职业规划测评"

# 页面逻辑
if st.session_state.page == "🏠 Home":
    HelloWeb.Hello()
elif st.session_state.page == "🎓 学业发展":
    HelloWeb.Hello()
elif st.session_state.page == "📈 发展潜能":
    HelloWeb.Hello()
elif st.session_state.page == "🛜 社交网络":
    HelloWeb.Hello()
elif st.session_state.page == "🔐 安全管理":
    HelloWeb.Dormitory_security()
elif st.session_state.page == "‍🧑‍💻 心理特质":
    HelloWeb.Hello()
elif st.session_state.page == "🏃 行为规律":
    HelloWeb.Hello()
elif st.session_state.page == "🤗 学生学业":
    HelloWeb.Academic_analysis()
elif st.session_state.page == "📄 综合学业":
    HelloWeb.all_academics()
elif st.session_state.page == "🎯 学生行为规律分析":
    HelloWeb.Regularity_of_behavior()
elif st.session_state.page == "🧾 心理咨询":
    HelloWeb.ai_psychology()
elif st.session_state.page == "🏫 校园行为数据":
    HelloWeb.Campus_behavior_data()
elif st.session_state.page == "🍺 学生线上活跃度":
    HelloWeb.student_social_network_page()
elif st.session_state.page == "📝 总体线上活跃度":
    HelloWeb.overall_social_network_page()
elif st.session_state.page == "📒 价值取向":
    HelloWeb.Student_growth()
elif st.session_state.page == "💬 职业规划测评":
    HelloWeb.Develop_Potential()
elif st.session_state.page == "📃 心理问卷":
    HelloWeb.Psychometric_Testing()
elif st.session_state.page == "📖 降级预警":
    HelloWeb.Downgrade_Alerts()
elif st.session_state.page == "📱 谈话记录分析":
    HelloWeb.Student_Counseling_Analysis()
elif st.session_state.page == "🏥 学生画像":
    HelloWeb.Student_Portraits()
elif st.session_state.page == "🔬 生涯规划助手":
    HelloWeb.Chat_Box()
elif st.session_state.page == "⚠️ 异常记录":
    HelloWeb.Exception_logging()


