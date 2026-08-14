from pathlib import Path

import streamlit.components.v1 as components


st_html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(st_html, height=1300, scrolling=True)
