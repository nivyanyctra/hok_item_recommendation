import streamlit as st
from inference_engine import forward_chaining
from knowledge_base import get_hero_list


CSS = r"""
/* --- Copied stylesheet from templates/index.html (abbreviated slightly) --- */
:root { --primary-gold: #d4af37; --primary-purple: #6b2fb3; --secondary-purple: #8b5cf6; --dark-bg: #0f0f1a; --card-bg: #1a1a2e; --card-bg-light: #252542; --text-light: #e4e4e7; --text-muted: #a1a1aa; --accent-green: #10b981; --accent-red: #ef4444; --accent-blue: #3b82f6; --border-color: #3f3f5a; }
*{box-sizing:border-box}
body {font-family: Poppins, Arial, sans-serif}
.hok-header{ text-align:center; padding:40px 20px; border-radius:20px; margin-bottom:30px; background:linear-gradient(135deg,var(--primary-purple) 0%, #4c1d95 50%, var(--primary-gold) 100%); color:var(--text-light)}
.form-card{ padding:30px; background: linear-gradient(145deg, var(--card-bg) 0%, var(--card-bg-light) 100%); border-radius:15px; border:1px solid var(--border-color); }
.result-card{ padding:30px; background: linear-gradient(145deg, var(--card-bg) 0%, var(--card-bg-light) 100%); border-radius:15px; border:1px solid var(--border-color); margin-top:20px }
.role-badge{ display:inline-block; background: linear-gradient(135deg, var(--primary-purple), var(--secondary-purple)); padding:8px 20px; border-radius:25px; font-weight:600; color:var(--text-light) }
.item-icon{ width:60px; height:60px; border-radius:10px; object-fit:cover; border:2px solid var(--border-color) }
.stat-box{ display:inline-block; padding:12px; background:var(--card-bg); border-radius:10px; margin:6px }
table.hok-table{ width:100%; border-collapse:collapse; margin-top:12px }
table.hok-table th{ background:linear-gradient(135deg,var(--primary-purple),#4c1d95); color:white; padding:12px; text-align:left }
table.hok-table td{ padding:12px; border-bottom:1px solid var(--border-color) }
"""


def format_stats(stats: dict):
    return ", ".join(f"{k}: {v:+}" for k, v in stats.items())


def render_result_html(result):
    if not result:
        return ""
    # Build rows for items
    rows = []
    for name, detail in zip(result.get("full_build", []), result.get("build_details", [])):
        img = detail.get("image_url", "")
        category = detail.get("category", "")
        passive = detail.get("passive", "")
        stats = "<br>".join(f"<span style='color:#a1a1aa'>{k}:</span> <strong style='color:#10b981'>+{v}</strong>" for k, v in detail.get("stats", {}).items())
        row = f"<tr><td><img class='item-icon' src='{img}'/></td><td style='color:var(--primary-gold); font-weight:600'>{name}</td><td><span class='category-tag'>{category}</span></td><td>{stats}</td><td style='font-style:italic;color:#8b5cf6'>{passive}</td></tr>"
        rows.append(row)

    table_html = """
    <table class='hok-table'>
      <thead><tr><th>Icon</th><th>Nama Item</th><th>Category</th><th>Stats Bonus</th><th>Effect/Passive</th></tr></thead>
      <tbody>
        %s
      </tbody>
    </table>
    """ % ("".join(rows))

    # total stats
    total_stats = result.get("total_stats", {})
    stat_boxes = "".join(f"<div class='stat-box'><div style='font-weight:700;color:var(--accent-green)'>+{v}</div><div style='color:#a1a1aa'>{k}</div></div>" for k, v in total_stats.items())

    explanations = result.get("explanations", [])
    expl_html = "" if not explanations else "".join(f"<li style='background:linear-gradient(135deg, rgba(212,175,55,0.1), rgba(107,47,179,0.1)); padding:12px; border-left:4px solid var(--primary-gold); margin:8px 0'>{e}</li>" for e in explanations)

    trace = (result.get("trace") or "").replace("\n", "<br>")

    html = f"""
    <div class='result-card'>
      <h2>Hasil Rekomendasi (Forward Chaining)</h2>
      <div class='role-badge'>🎯 Role: {result.get('my_role','Unknown')}</div>
      <h3>⚔️ Rekomendasi Build (6 Items):</h3>
      {table_html}
      <h3>📊 Total Stats Build:</h3>
      <div>{stat_boxes}</div>
      <h3>📝 Penjelasan (Rules Terpicu):</h3>
      <ul style='list-style:none;padding:0'>{expl_html if expl_html else '<li style="padding:12px">✨ Tidak ada counter khusus. Gunakan base build default!</li>'}</ul>
      <h3>🔍 Trace Forward Chaining:</h3>
      <div style='background:#0a0a12;padding:12px;border-radius:8px;color:var(--accent-green);font-family:monospace'>{trace}</div>
    </div>
    """
    return html


def main():
    st.set_page_config(page_title="HoK Item Recommender", layout="wide")
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

    # Header
    st.markdown("<div class='hok-header'><span style='font-size:3rem'>👑</span><h1>Sistem Pakar Rekomendasi Item Honor of Kings</h1><p>Program Studi Teknik Informatika - UCIC</p></div>", unsafe_allow_html=True)

    hero_list = [""] + get_hero_list()
    result = None

    with st.form(key='recommend_form'):
        st.markdown("<div class='form-card'>", unsafe_allow_html=True)
        my_hero = st.selectbox("Hero Kamu", hero_list, index=0)
        cols = st.columns(5)
        enemies = []
        for i in range(5):
            with cols[i]:
                e = st.selectbox(f"Musuh {i+1}", hero_list, index=0)
                enemies.append(e)

        st.markdown("</div>", unsafe_allow_html=True)
        submit = st.form_submit_button("⚡ Proses Rekomendasi")

    if submit:
        # filter empty
        enemy_list = [e for e in enemies if e]
        result = forward_chaining(enemy_list, my_hero)

    # Render result area (even if None, shows header/empty state)
    rendered = render_result_html(result)
    st.markdown(rendered, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
