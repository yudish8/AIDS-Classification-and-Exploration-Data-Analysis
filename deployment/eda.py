import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 


def run():
    st.title('AIDS Virus Infection Exploration Data Analyst(EDA)')
    st.image('https://images.theconversation.com/files/404868/original/file-20210607-28173-1rw95dw.jpg?ixlib=rb-4.1.0&q=45&auto=format&w=926&fit=clip')
    st.write('This page is made by Yudis Aditya')
    st.markdown('---')

    st.write('In this page, I want to show visualization data based on my analyst process about AIDS Infection. This EDA has information about people characteristic and people behaviour')
    st.link_button('Link dataset','https://www.kaggle.com/datasets/aadarshvelu/aids-virus-infection-prediction?select=AIDS_Classification_5000.csv')


    df = pd.read_csv('AIDS_Classification_50000.csv')

    st.write('## 1. People Characteristic')
    st.write('### 1.1 Distribution Data Age')
    # # This cell is used to create histogram column age
    data = df.groupby(['infected']).size()

    x = ["Not Infected", "Infected"]
    y = data.values
    fig = plt.figure(figsize=(15,5))
    plt.pie(y,labels=x,autopct='%1.0f%%')
    plt.title("Comparison people Not Infected and Infected By AIDS")
    plt.show()
    st.pyplot(fig)
    st.write("From Graph above we can know that in my dataset people dominant not infected by AIDS. It is indicate that people already aware about danger AIDS and try to take therapy to prevent it before it's too late.")
    
    st.write('### 1.2 Distribution data people infected and not infected based on age')
    fig = plt.figure(figsize=(15,5))
    # This cell code is used to create histogram for visualize distribution data people infected and not infected based on age
    data_0 = df[df['infected'] == 0]['age']
    data_1 = df[df['infected'] == 1]['age']

    plt.title("Distribution data people infected and not infected based on age")
    plt.hist(data_0)
    plt.hist(data_1)
    plt.show()
    st.pyplot(plt)
    st.write('From Graph above we can know distribution data people infected and not infected based on age has same pattern and dominant in range age 25 - 45. From this data, we can know people got infected AIDS or HIV when people is already teenager or adult. Goverment can make campaign for danger and anticipate HIV and AIDS around that age so the campaign can be more effective than target campaign to child or elder.')
   

    st.write('### 1.3 Percentage Homosexual and Heterosexual who have HIV')
    fig = plt.figure(figsize=(15,5))
    # This cell code is used to show pie chart percentage Homosexual and Heterosexual
    data = df.groupby('homo').size()
    label = ['Heterosexual','Homosexual']
    values = data.values

    plt.pie(values,labels=label,autopct="%.2f")
    plt.title("Percentage Homosexual and Heterosexual who have HIV")
    plt.show()
    st.pyplot(fig)
    st.write('From Graph above we can know that people total people who is homosexual that has HIV is more than Heterosexual. From my assumption this can be happened because they dont have to worry because somoene dont have to be preagnant. So with this data , i hope we can give this information to people who has homosexual activity that it has another bad impact beside that.')
    
    st.write('### 1.4 Distribution data people infected and not infected based on cd40')
    fig = plt.figure(figsize=(15,5))
    # This cell code is used to create histogram for visualize distribution data people infected and not infected based on age
    data_0 = df[df['infected'] == 0]['cd40']
    data_1 = df[df['infected'] == 1]['cd40']

    plt.title("Distribution data people infected and not infected based on cd40")
    plt.hist(data_0)
    plt.hist(data_1)
    plt.show()
    st.pyplot(fig)
    st.write('Cd40 is used as important metrix to determine people immunity who has HIV. Based graph above, we can know that people who has AIDS has the most CD40 arount 180 - 300. This can be warning area for every who has HIV to be more careful if has CD40 almost at that point. ')
    
    # This cell code is used to create histogram for visualize distribution data people infected and not infected based on age
    st.write('### 1.5 Distribution data people infected and not infected based on cd80')
    fig = plt.figure(figsize=(15,5))
    data_0 = df[df['infected'] == 0]['cd80']
    data_1 = df[df['infected'] == 1]['cd80']

    plt.title("Distribution data people infected and not infected based on cd80")
    plt.hist(data_0)
    plt.hist(data_1)
    plt.show()
    st.pyplot(fig)
    st.write('CD80 is a transmembrane protein that functions as a co-stimulatory molecule in antigen-presenting cells, such as dendritic cells, macrophages, and B cells. Based graph above, we can know that people who has AIDS has the most CD80 arount 800 - 1200. This can be warning area for every who has HIV to be more careful if has CD80 almost at that point. ')
    
    st.write('### 1.6 Percentage Race White and Non-White')
    fig = plt.figure(figsize=(15,5))
    data = df.groupby('race').size()
    label = ['White','Non-White']
    values = data.values

    plt.pie(values,labels=label,autopct="%.2f")
    plt.title("Percentage Race White and Non-White")
    plt.show()
    st.pyplot(fig)
    st.write('From Graph above we can know that total people with race white who has HIV is more than non-white. This can be happening by many factor, based on race white beahviour, tradition, believes, habit, etc. So my suggestion is to create film or another socialize method to more race white people aware about HIV and how to prevent it. ')
    
    st.write('## 2. People Behaviour')
    st.write('### 2.1 Distribution Data patient who has aids based on their treatment type')
    fig = plt.figure(figsize=(15,5))
    # This cell is used to create bar horizontal for distribution data who has AIDS based on treatment type
    data = df[df['infected'] == 1].groupby('trt').size()
    labels = ['ZDV only','ZDV + ddl','ZDV + Zal','ddl only']
    values = data.values

    plt.barh(labels,values)
    plt.title("Distribution Data patient who has aids based on their treatment type")
    plt.show()
    st.pyplot(fig)
    st.write("Based on graph above we can know the most people who has AIDS is only take ZDV treatment and ZDV + ddl is the lowest. I can assume that goverment can remove treatment for only ZDV only and increase treatment for ZDV + ddl for increase number suvivor")

    st.markdown('---')
    st.write('# Conclusion')
    st.write('From analysis and creating visualize from my dataset , This is a important point that i can share:')
    st.write("- The most effective treatment before AIDS is ZDV + ddl")
    st.write('- People who has HIV is around 25 - 45 years old. Dominant who has experience homosexual activity or white race. Has benchmark cd40 for get AIDS around 180 - 300 and cd80 around 800 - 1200.')
    
if __name__ == '__main__':
    run()
