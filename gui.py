import time
import pandas as pd
import pickle
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

# penampung data user input
q1 = []
q2 = []
q3 = []
q4 = []
q5 = []
q6 = []
q7 = []
q8 = []
q9 = []
q10 = []
agearr = []
autismarr = []

st.title("DETEKSI AWAL AUTISME PADA ANAK") 

tab1, tab2, tab3, tab4 = st.tabs(["Dataset", "Pre-pemrosesan", "Deteksi","Grafik"])
with tab1:
    st.header('Dataset')
    data = pd.read_csv('csv_result-Autism-Child-Data.csv')
    st.dataframe(data)
with tab2:
    st.header('Pre-pemrosesan Data')
    #drop kolom
    data = data.drop(['id', 'gender', 'jundice', 'austim', 'used_app_before', 'age_desc', 'relation', 'ethnicity', 'contry_of_res'], axis=1)
    #ganti tanda tanya (?)
    data = data.replace('?', 0)
    data['age'] = data.age.astype(int)
    data['age'] = data['age'].replace(0, data['age'].mean())
    data['age'] = data.age.astype(int)
    # penggantian ke biner
    label = data['Class/ASD'].values
    le_Species = LabelEncoder()
    data['Class/ASD'] = le_Species.fit_transform(label)
    st.dataframe(data)
with tab3:
    st.header('Deteksi')

    st.write("Untuk anak umur antara 4 sampai 11 tahun")

    age = st.number_input("Umur")
    age = int(age)
    # term and condition user
    # only user age range from 4 to 11
    if age < 4 or age > 11:
        st.write("Maaf, usia anda tidak termasuk kriteria")
    else:
            autism = st.radio(
                "Riwayat Keturunan",
                ("Ya", "Tidak")
            )

            question1 = st.radio(
            "(1) Anak sering memperhatikan suara-suara kecil ketika orang lain tidak",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')
            )

            question2 = st.radio(
            "(2) Anak biasanya lebih berkonsentrasi pada keseluruhan situasi, daripada detail kecil",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')
            )

            question3 = st.radio(
            "(3) Dalam kelompok sosial, anak dapat dengan mudah mengikuti percakapan beberapa orang yang berbeda",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')
            )

            question4 = st.radio(
            "(4) Anak dengan mudah untuk melakukan aktivitas bolak-balik yang berbeda",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')
            )

            question5 = st.radio(
            "(5) Anak tidak tahu bagaimana cara mempertahankan percakapan dengan teman-temannya",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')    
            )

            question6 = st.radio(
            "(6) Anak baik dalam bersosialisi",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')    
            )

            question7 = st.radio(
            "(7) Ketika anak membaca sebuah cerita, anak merasa sulit untuk mengetahui maksud atau perasaan karakter dalam cerita.",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')    
            )

            question8 = st.radio(
            "(8) Ketika anak berada di taman kanak-kanak, anak bisa menikmati permainan yang melibatkan aktivitas bermain berpura-pura dengan anak-anak lain",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')
            )

            question9 = st.radio(
            "(9) Anak dengan mudah mengetahui apa yang dipikirkan atau dirasakan seseorang hanya dengan melihat wajahnya",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')
            )

            question10 = st.radio(
            "(10) Anak merasa sulit untuk mendapatkan teman baru",
            ('Sangat Setuju', 'Agak Setuju', 'Agak Tidak Setuju', 'Sangat Tidak Setuju')
            )

            if st.button("Submit"):

                agearr.append(age)
                agearr.append(age)

            #question 1
                if question1 == 'Sangat Setuju' or question1 == 'Agak Setuju':
                    q1.append(1)
                    q1.append(1)
                elif question1 == 'Agak Tidak Setuju' or question1 == 'Sangat Tidak Setuju':
                    q1.append(0)
                    q1.append(0)

            #question 2
                if question2 == 'Sangat Setuju' or question2 == 'Agak Setuju':
                    q2.append(0)
                    q2.append(0)
                elif question2 == 'Agak Tidak Setuju' or question2 == 'Sangat Tidak Setuju':
                    q2.append(1)
                    q2.append(1)

            #question 3
                if question3 == 'Sangat Setuju' or question3 == 'Agak Setuju':
                    q3.append(0)
                    q3.append(0)
                elif question3 == 'Agak Tidak Setuju' or question3 == 'Sangat Tidak Setuju':
                    q3.append(1)
                    q3.append(1)

            #question 4
                if question4 == 'Sangat Setuju' or question4 == 'Agak Setuju':
                    q4.append(0)
                    q4.append(0)
                elif question4 == 'Agak Tidak Setuju' or question4 == 'Sangat Tidak Setuju':
                    q4.append(1)
                    q4.append(1)

            #question 5
                if question5 == 'Sangat Setuju' or question5 == 'Agak Setuju':
                    q5.append(1)
                    q5.append(1)
                elif question5 == 'Agak Tidak Setuju' or question5 == 'Sangat Tidak Setuju':
                    q5.append(0)
                    q5.append(0)

            #question 6
                if question6 == 'Sangat Setuju' or question6 == 'Agak Setuju':
                    q6.append(0)
                    q6.append(0)
                elif question6 == 'Agak Tidak Setuju' or question6 == 'Sangat Tidak Setuju':
                    q6.append(1)
                    q6.append(1)

            #question 7
                if question7 == 'Sangat Setuju' or question7 == 'Agak Setuju':
                    q7.append(1)
                    q7.append(1)
                elif question7 == 'Agak Tidak Setuju' or question7 == 'Sangat Tidak Setuju':
                    q7.append(0)
                    q7.append(0)

            #question 8
                if question8 == 'Sangat Setuju' or question8 == 'Agak Setuju':
                    q8.append(0)
                    q8.append(0)
                elif question8 == 'Agak Tidak Setuju' or question8 == 'Sangat Tidak Setuju':
                    q8.append(1)
                    q8.append(1)   
            
            #question 9
                if question9 == 'Sangat Setuju' or question9 == 'Agak Setuju':
                    q9.append(0)
                    q9.append(0)
                elif question9 == 'Agak Tidak Setuju' or question9 == 'Sangat Tidak Setuju':
                    q9.append(1)
                    q9.append(1)

            #question 10
                if question10 == 'Sangat Setuju' or question10 == 'Agak Setuju':
                    q10.append(1)
                    q10.append(1)
                elif question10 == 'Agak Tidak Setuju' or question10 == 'Sangat Tidak Setuju':
                    q10.append(0)
                    q10.append(0)

                # riwwayat keturunan
                if autism == 'Ya':
                    st.write("Ada Riwayat Autisme Dalam Keluarga")                                                                                        
                    autismarr.append(1)
                    autismarr.append(1)
                elif autism == 'Tidak':
                    st.write("Tidak Ada Riwayat Autisme Dalam Keluarga") 
                    autismarr.append(0)
                    autismarr.append(0)

                latest_iteration = st.empty()
                bar = st.progress(0)
                for i in range(100):
                    # Update the progress bar with each iteration.
                    latest_iteration.text(f'Processing... {i+1}%')
                    bar.progress(i + 1)
                    time.sleep(0.1)

                total = q1[0] + q2[0] + q3[0] + q4[0] + q5[0] + q6[0] + q7[0] + q8[0] + q9[0] + q10[0]

                feature = {'A1_Score':q1, 'A2_Score':q2, 'A3_Score':q3, 'A4_Score':q4, 'A5_Score':q5, 'A6_Score':q6, 'A7_Score':q7, 'A8_Score':q8, 'A9_Score':q9, 'A10_Score':q10, 'age':agearr, 'result':total}
                # minus - age - austim - contry_of_res - ethnicity - gender
                label = {'Class/ASD':[0, 1]}
                labeldf = pd.DataFrame(label)
                print('featuredf: ', feature)
                featuredf = pd.DataFrame(feature)
                print('featuredf: ', featuredf)
                print('labeldf: ', labeldf)
                #Split the dataset 
                x_train , x_test , y_train , y_test = train_test_split(featuredf, labeldf, test_size=0.2, random_state = 0)

                # load the model from disk
                filename = 'finalized_model.sav'
                loaded_model = pickle.load(open(filename, 'rb'))
                result = loaded_model.score(x_test, y_test)
                nilai = loaded_model.predict(x_test)
                print("nilai: ", nilai)
            
                st.write("Score: ", total)

                if nilai == 1:
                    st.write("Terindikasi Autisme")
                else:
                    st.write("Tidak Terindikasi Autisme")
with tab4:
    st.header("Grafik Data")
    # Mengambil data dari file CSV
    # data = pd.read_csv('csv_result-Autism-Child-Data.csv')

    # Tampilkan data dalam bentuk tabel
    st.write(data)

    # Pilih jenis grafik
    chart_type = st.selectbox('Pilih jenis grafik', ('Bar', 'Line', 'Scatter', 'Histogram'))

    # Membuat grafik
    if chart_type == 'Bar':
        st.subheader('Grafik Batang')
        x_column = st.selectbox('Pilih kolom untuk sumbu-x', data.columns)
        y_column = st.selectbox('Pilih kolom untuk sumbu-y', data.columns)
        fig, ax = plt.subplots()
        ax.bar(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)

    elif chart_type == 'Line':
        st.subheader('Grafik Garis')
        x_column = st.selectbox('Pilih kolom untuk sumbu-x', data.columns)
        y_column = st.selectbox('Pilih kolom untuk sumbu-y', data.columns)
        fig, ax = plt.subplots()
        ax.plot(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)

    elif chart_type == 'Scatter':
        st.subheader('Grafik Sebar')
        x_column = st.selectbox('Pilih kolom untuk sumbu-x', data.columns)
        y_column = st.selectbox('Pilih kolom untuk sumbu-y', data.columns)
        fig, ax = plt.subplots()
        ax.scatter(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)

    elif chart_type == 'Histogram':
        st.subheader('Histogram')
        column = st.selectbox('Pilih kolom untuk histogram', data.columns)
        fig, ax = plt.subplots()
        ax.hist(data[column], bins='auto')
        ax.set_xlabel(column)
        ax.set_ylabel('Frekuensi')
        st.pyplot(fig)

        

    
