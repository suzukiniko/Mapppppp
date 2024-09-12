import streamlit as st
import folium

#タイトルの設定
st.title('宮河内ハイランドハザードマップ')

#座標の設定
coordinates ={
    '立入禁止区域1':[33.187231, 131.697546],
    '立入禁止区域2':[33.188263, 131.700003],
    '遊水池':[33.190565, 131.703447],
    '立入禁止区域3':[33.190260, 131.706448],
    '立入禁止区域4':[33.193352, 131.700786],
}

#Foliumマッププロジェクトの作成
m = folium.Map(location=[33.189665, 131.703049],zoom_start=15)

#マーカーの設置
for location, coord in coordinates.items():
    folium.Marker(location=coord,popup=location).add_to(m)

#ForiumマップをHTMLとして取得
map_html = m._repr_html_()

#streamlitでマップを表示
st.components.v1.html(map_html, height=500, width=500)