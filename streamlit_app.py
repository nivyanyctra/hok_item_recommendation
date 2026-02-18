import streamlit as st
from inference_engine import forward_chaining
from knowledge_base import get_hero_list


def format_stats(stats: dict):
    items = []
    for k, v in stats.items():
        items.append(f"{k}: {v}")
    return "  |  ".join(items)


def main():
    st.set_page_config(page_title="HoK Item Recommender", layout="wide")
    st.title("HoK Item Recommender — Streamlit")

    hero_list = get_hero_list()

    col1, col2 = st.columns([2, 1])
    with col1:
        my_hero = st.selectbox("Pilih hero kamu", hero_list)
        enemy_heroes = st.multiselect("Pilih hero musuh (maks 5)", hero_list, help="Pilih hingga 5 hero musuh.")
        if len(enemy_heroes) > 5:
            st.warning("Hanya 5 hero musuh yang digunakan — sisanya akan diabaikan.")
            enemy_heroes = enemy_heroes[:5]

        if st.button("Rekomendasikan Build"):
            with st.spinner("Menghitung rekomendasi..."):
                result = forward_chaining(enemy_heroes, my_hero)

            st.subheader(f"Role terdeteksi: {result.get('my_role', 'Unknown')}")

            st.markdown("**Rekomendasi Full Build**")
            build = result.get("full_build", [])
            build_details = result.get("build_details", [])

            for name, bd in zip(build, build_details):
                with st.container():
                    cols = st.columns([1, 4])
                    # image
                    if bd.get("image_url"):
                        try:
                            cols[0].image(bd.get("image_url"), width=64)
                        except Exception:
                            pass
                    # details
                    cols[1].markdown(f"### {name}")
                    cols[1].markdown(f"**{bd.get('category','')}**")
                    if bd.get('passive'):
                        cols[1].write(bd.get('passive'))
                    stat_text = format_stats(bd.get("stats", {}))
                    if stat_text:
                        cols[1].write(stat_text)

            st.markdown("---")
            st.markdown("**Total Stats dari build**")
            st.json(result.get("total_stats", {}))

            if result.get("explanations"):
                st.markdown("**Alasan / Penjelasan**")
                for e in result.get("explanations"):
                    st.write(f"- {e}")

            with st.expander("Trace (debug / penjelasan detail)"):
                st.code(result.get("trace", ""))

    with col2:
        st.sidebar.header("Petunjuk")
        st.sidebar.markdown("Pilih hero kamu dan hero musuh lalu klik 'Rekomendasikan Build'.")
        st.sidebar.markdown("Aplikasi ini menggunakan mesin inferensi dari `inference_engine.py`.")


if __name__ == '__main__':
    main()
