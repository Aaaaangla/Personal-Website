import streamlit as st

# ------------------------
# 页面配置
# ------------------------
st.set_page_config(
    page_title="Angela Li | Portfolio",
    page_icon="✨",
    layout="wide"
)

# ------------------------
# 默认导航初始化
# ------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ------------------------
# 顶部导航栏
# ------------------------
st.markdown(
    """
    <style>
    .nav-container {
        display: flex;
        gap: 20px;
        background-color: #f5f5f5;
        padding: 12px 25px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: 500;
    }
    .nav-item {
        cursor: pointer;
        padding: 6px 12px;
        border-radius: 6px;
    }
    .nav-item:hover {
        background-color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

nav_col = st.container()
with nav_col:
    cols = st.columns(5)
    pages = ["Home", "About Me", "Resume", "Projects", "Contact"]

    for i, name in enumerate(pages):
        if cols[i].button(name):
            st.session_state.page = name


# ------------------------
# 各页面内容函数
# ------------------------

def home_page():
    st.markdown(
        """
        <h1 style='text-align: center;'>✨ Hello，欢迎来到我的个人主页！✨</h1>
        <h2 style='text-align: center;'>我是 <span style='color:#ff4b4b;'>Angela Li</span>。</h2>
        <p style='text-align: center; font-size:18px;'>
            这是我的个人网站，你可以在这里了解我的背景、项目、简历，以及如何联系我。
        </p>
        """,
        unsafe_allow_html=True
    )


def about_me_page():
    st.header("About Me")
    st.write("这里将展示你的个人介绍、教育背景、技能等内容。")


def resume_page():
    st.header("Resume")
    st.write("这里可以放你的 CV、工作经历、教育背景等。")


def projects_page():
    st.header("Projects")
    st.write("这里展示你的项目：数据分析、可视化、AI 工具、网页系统等。")


def contact_page():
    st.header("Contact")
    st.write("这里放你的 email、LinkedIn、GitHub 链接等联系方式。")


# ------------------------
# 页面路由
# ------------------------
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "About Me":
    about_me_page()
elif st.session_state.page == "Resume":
    resume_page()
elif st.session_state.page == "Projects":
    projects_page()
elif st.session_state.page == "Contact":
    contact_page()
