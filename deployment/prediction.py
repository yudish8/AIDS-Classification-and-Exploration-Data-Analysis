import streamlit as st 
import pandas as pd 
import pickle
import json

with open('list_col_num.txt', 'r') as file_1:
  list_col_num_if = json.load(file_1)

with open('list_col_cat.txt', 'r') as file_2:
  list_col_cat_if = json.load(file_2)

with open('model_svc.pkl', 'rb') as file_3:
  model_svc = pickle.load(file_3)

def get_trt_index(trt):
    if trt == 'ZDV only':
        return 0
    elif trt == 'ZDV + ddl':
        return 1
    elif trt == 'ZDV + Zal':
        return 2
    else:
        return 3

def get_yes_no_index(yes_no):
    if yes_no == 'no':
        return 0
    else:
        return 1

def get_strat_index(strat):
    if strat == 'Antiretroviral Naive':
        return 1
    elif strat == 'Antiretroviral <= 52 weeks':
        return 2
    else:
        return 3

def get_symptom_index(symptom):
    if symptom == 'asymp':
        return 0 
    else: 
        return 1

def get_treat_index(treat):
    if treat == 'ZDV only':
        return 0 
    else:
        return 1

def get_race_index(race):
    if race == 'White':
        return 0 
    else:
        return 1

def get_gender_index(gender):
    if gender == 'Female':
        return 0 
    else:
        return 1

def get_str2_index(str2):
    if str2 == 'naive':
        return 0 
    else:
        return 1

def run():
    with st.form("prediction_form"):
        st.write('Personal Information')
        time = st.number_input('Input time to failure or censoring', value=100)
        trt = st.selectbox('Select Treatment Indicator ', {'ZDV only','ZDV + ddl','ZDV + Zal','ddl only'},index=0)
        age = st.number_input('Input age in years', value=20)
        wtkg = st.number_input('Input weight in kg', value=40.0)
        hemo = st.selectbox('Is patient has hemophilia ?', {'no','yes'},index=0)
        homo = st.selectbox('Is patient has experience do homosexuality activity ?', {'no','yes'},index=0)
        drugs = st.selectbox('Is patient has history of IV drug use ?', {'no','yes'},index=0)
        karnof = st.number_input('Input Karnofsky score (on scale 0 - 100)', value=40, min_value=0, max_value=100,step=1)
        oprior = st.selectbox('Is patient is Non-ZDV antiretroviral therapy pre-175 ?', {'no','yes'},index=0)
        z30 = st.selectbox('Is patient is ZDV in the 30 days prior to 175 ?', {'no','yes'},index=0)
        preanti = st.number_input('Input days pre-175 anti-retroviral therapy', value=40)
        race = st.selectbox('Input patient race ?', {'White','non-white'},index=0)
        gender = st.selectbox('Select gender ?', {'Female','Male'},index=0)
        str2 = st.selectbox('Input antiretroviral history', {'naive','experienced'},index=0)
        strat = st.selectbox('Input antiretroviral history stratification', {'Antiretroviral Naive','Antiretroviral <= 52 weeks','Antiretroviral > 52 weeks'},index=0)
        symptom = st.selectbox('Input symptomatic indicator', {'asymp','symp'},index=0)
        treat = st.selectbox('Input treatment indicator ', {'ZDV only','others'},index=0)
        offtrt = st.selectbox('Input indicator of off-trt before 96+/-5 weeks ', {'no','yes'},index=0)
        cd40 = st.number_input('Input CD4', value=40.0)
        cd420 = st.number_input('Input CD4 at 20+/-5 weeks', value=40.0)
        cd80 = st.number_input('Input CD8', value=40.0)
        cd820 = st.number_input('Input CD8 at 20+/-5 weeks', value=40.0)
        submitted = st.form_submit_button("Submit")
    st.write("Outside the form")

    data_inf = {
        'time': time,
        'trt' : get_trt_index(trt),
        'age': age,
        'wtkg': wtkg,
        'hemo': get_yes_no_index(hemo),
        'homo': get_yes_no_index(homo),
        'drugs': get_yes_no_index(drugs),
        'karnof': karnof,
        'oprior': get_yes_no_index(oprior),
        'z30': get_yes_no_index(z30),
        'preanti': preanti,
        'race': get_race_index(race),
        'gender': get_gender_index(gender),
        'str2': get_str2_index(str2),
        'strat': get_strat_index(strat),
        'symptom': get_symptom_index(symptom),
        'treat': get_treat_index(treat),
        'offtrt': get_yes_no_index(offtrt),
        'cd40':cd40,
        'cd420':cd420,
        'cd80':cd80,
        'cd820':cd820
    }

    if submitted:
        df = pd.DataFrame([data_inf])
        df[list_col_cat_if] = df[list_col_cat_if].astype(object)
        df = df[list_col_cat_if + list_col_num_if]

        # Do model predict from data input
        predict_result =  model_svc.predict(df)
        if predict_result[0] == 1 : 
            predic_result_value = 'yes'
        else: 
            predic_result_value = 'no'
        st.write(f'## Is patient infected AIDS: {predic_result_value}')



if __name__ == '__main__':
    run()