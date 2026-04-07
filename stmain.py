import streamlit as st
import seaborn as sns

@st.cache_data
def load_penguins():
    return sns.load_dataset("penguins")

pg = load_penguins()

st.title(":red[:material/home:] streamlit 연습장")
st.header("연습용입니다")

st.subheader("penguins 데이터셋 예시")
st.write(pg.head())

st.subheader("penguins 데이터셋 통계")
st.write(pg.describe())

st.subheader("seaborn pairplot 예시")
#fig = sns.pairplot(pg, hue="species", diag_kind="hist", markers=["o", "s", "D"])
# seaborn.pairplot returns a PairGrid object; Streamlit renders its underlying Matplotlib figure.
st.pyplot(sns.pairplot(pg, hue="species", diag_kind="hist", markers=["o", "s", "D"])
.fig)

st.subheader("seaborn boxplot 예시")
# seaborn boxplot example
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
sns.boxplot(x="species", y="body_mass_g", data=pg, ax=ax)
st.pyplot(fig)

st.subheader("seaborn heatmap 예시")
# seaborn heatmap example   
corr = pg.corr(numeric_only=True)  # Compute correlation matrix for numeric columns
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
