import pandas as pd
import numpy as np
import pickle
import streamlit as st

st.title('Healthy Recommendation')



df_data=pickle.load(open('data1.pkl','rb'))
data=pd.DataFrame(df_data)

high_c_veg = ['beans', 'eggplant', 'yams', 'broccoli', 'spinach','bell peppers']
high_c_fru = ['oranges', 'apples','grapes', 'strawberries' ]
high_s_veg = ['broccoli','radish','bitter gourd','asparagus', 'green beans', 'squash','mushrooms']
high_s_fru = ['blackberries','strawberries','tomatoes','oranges','bananas','cherries','plums','apple','pears']
both= ['lettuce', 'tomatoes', 'cucumber', 'beans', 'broccoli', 'zucchini', 'carrots,', 'celery,' , 'bell peppers']


def reco(index):
    if data['cholesterol'].iloc[index[0]]>1 and data['gluc'].iloc[index[0]]>1:
        st.text('Hey user! Your Cholesterol and Sugar level is high')
        st.text('Vegetables and fruits suitable for you are: ')
        #st.text(both)
        for i in both:
            st.markdown('- '+i)

    elif data['cholesterol'].iloc[index[0]]>1:
        st.text('Hey user! Your Cholesterol level is high')
        st.text('Vegetables to reduce Cholesterol are: ')
        #st.text(high_c_veg)
        for i in high_c_veg:
            st.markdown('- '+i)
        st.text('Fruits to reduce Cholesterol are: ')
        #st.text(high_c_fru)
        for i in high_c_fru:
            st.markdown('- '+i)

    elif data['gluc'].iloc[index[0]]>1:
        st.text('Hey user! Your Sugar level is high')
        st.text('Vegetables to reduce sugar are: ')
        #st.text(high_s_veg)
        for i in high_s_veg:
            st.markdown('- '+i)
        st.text('Fruits to reduce sugar are: ')
        #st.text(high_s_fru)
        for i in high_s_fru:
            st.markdown('- '+i)
    else:
        st.text('Hey user! Maintain your healty diet')

selected_user_id=st.selectbox('Select your id', data['id'].values)

ind=data.index[data['id']==selected_user_id].to_list()

if st.button('Recommend'):
    reco(ind)