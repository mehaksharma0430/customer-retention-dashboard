"""Streamlit host for the original interactive Customer Retention Dashboard."""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Customer Retention Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep the visual design and all JavaScript interactions from the supplied HTML.
st.markdown(
    """
    <style>
      #MainMenu, footer, header {visibility: hidden;}
      .block-container {padding: 0 0.75rem 1rem; max-width: 1200px;}
      [data-testid="stAppViewContainer"] {background: #f5f7fa;}
      iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("dashboard.html")
dashboard_html = html_path.read_text(encoding="utf-8")
components.html(dashboard_html, height=3200, scrolling=True)
