#!/usr/bin/env python
# coding: utf-8

# # Analysis of Pronouns

# ## Data preprocessing


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def pie_chart(df,name,ax):
    """
    Visualize pie chart 
    :param name: personality
    :param ax: ax in matplotlib
   
    """
    

    data = df.loc[name].values
    ingredients = df.loc[name].index
    wedges, texts, autotexts = ax.pie(data,autopct='%1.1f%%',
                                      textprops=dict(color="w"),pctdistance=0.6,normalize=True
                                      )
    ax.set_title(name,size=16)

        
        
def subtype_plot(df,vs_func):
    
    """
     Plot sub-personality (e.g., Feeling vs Thinking)
     :param vs_func: decide which two sub-personalities to be compared
    """
    
    pron_type = ['1st_pron','2nd_pron','3rd_pron']
    pron_name = ['1st-person pronouns', '2nd-person pronouns', '3rd-person pronouns']
    frames = []
    for i, pron in enumerate(pron_type):
        df_sub=df.groupby(df['type'].apply(vs_func))[pron+'_count'].sum()        /df.groupby(df['type'].apply(vs_func))['org_comment_count'].sum()

        df_sub = pd.DataFrame({'Personality': df_sub.index, 'Type of pronouns':pron_name[i],'Average count':df_sub.values})
        frames.append(df_sub)
    result = pd.concat(frames)
    sns.barplot(x='Type of pronouns', y='Average count', hue='Personality', data=result,palette = 'pastel')

def main():
    df = pd.read_csv('./mbti_1.csv')
    x = df.head()
    print(x)


    # Count Different types of pronouns

    first_pron_pat = r"(?i)\b(I|me|my|mine|myself|we|us|our|ours|ourselves)\b"
    first_pron_num = 10
    second_pron_pat = r"(?i)\b(you|your|yours|yourself|yourselves)\b"
    second_pron_num = 5
    third_pron_pat = r"(?i)\b(he|him|his|himself|she|her|hers|herself|they|them|their|theirs|themselves|it|its|itself)\b"
    third_pron_num = 16
    link_pat = r"http"

    df['1st_pron_count'] = df['posts'].str.count(pat=first_pron_pat)/first_pron_num
    df['2nd_pron_count'] = df['posts'].str.count(pat=second_pron_pat)/second_pron_num
    df['3rd_pron_count'] = df['posts'].str.count(pat=third_pron_pat)/third_pron_num
    df['link_count'] = df['posts'].str.count(pat=link_pat)
    df['comment_count'] = df['posts'].str.count(pat=r"\|\|\|")+1
    df['org_comment_count'] = df['comment_count'] - df['link_count']




    df_1st = df.groupby(['type'])['1st_pron_count'].sum()/df.groupby(['type'])['org_comment_count'].sum()
    df_1st = df_1st .to_frame('1st_pron_count').sort_values(by=['1st_pron_count'],ascending=False)


    # Average 1st person prounouns count


    plt.figure(figsize=(20,10))
    sns.barplot(x=df_1st.index,y=df_1st['1st_pron_count'])
    plt.ylabel('Average \n count of \n 1st-person \npronouns', fontsize=16,rotation=0,labelpad=50)
    plt.xlabel('Personality', fontsize=16)
    plt.xticks(fontsize=16, rotation=0)
    plt.yticks(fontsize=16, rotation=0)


    # Average 2nd person prounouns count



    df_2nd = df.groupby(['type'])['2nd_pron_count'].sum()/df.groupby(['type'])['org_comment_count'].sum()
    df_2nd = df_2nd.to_frame('2nd_pron_count').sort_values(by=['2nd_pron_count'],ascending=False)
    plt.figure(figsize=(20,10))
    sns.barplot(x=df_2nd.index,y=df_2nd['2nd_pron_count'])
    plt.ylabel('Average \n count of \n 2nd-person \npronouns', fontsize=16,rotation=0,labelpad=50)
    plt.xlabel('Personality', fontsize=16)
    plt.xticks(fontsize=16, rotation=0)
    plt.yticks(fontsize=16, rotation=0)
    
    # Average 3rd person prounouns count
  

    df_3rd = df.groupby(['type'])['3rd_pron_count'].sum()/df.groupby(['type'])['org_comment_count'].sum()
    df_3rd = df_3rd.to_frame('3rd_pron_count').sort_values(by=['3rd_pron_count'],ascending=False)
    plt.figure(figsize=(20,10))
    sns.barplot(x=df_3rd.index,y=df_3rd['3rd_pron_count'])
    plt.ylabel('Average \n count of \n 3rd-person \npronouns', fontsize=16,rotation=0,labelpad=50)
    plt.xlabel('Personality', fontsize=16)
    plt.xticks(fontsize=16, rotation=0)
    plt.yticks(fontsize=16, rotation=0)


    #Comparison between average pronouns count for the given pair of sub-personality

    E_vs_I = lambda x: 'Extroversion' if x[0] == 'E' else 'Introversion'
    N_vs_S = lambda x: 'Intuition' if x[1] =='N' else 'Sensing'
    T_vs_F = lambda x: 'Thinking' if x[2] == 'T' else 'Feeling'
    J_vs_P = lambda x: 'Judging' if x[3] == 'J' else 'Perceving'



    subtype_plot(df,E_vs_I)
    subtype_plot(df,N_vs_S)
    subtype_plot(df,T_vs_F)


    # "Feeling" and "Thinking" are the decision-making functions.

    # Those who prefer thinking tend to decide things from a more detached standpoint while those who prefer feeling tend to come to decisions by associating or empathizing with the situation.
    subtype_plot(df,J_vs_P)


    # Pie charts of different types of prounouns for each personality



    all_count = pd.concat([df_1st,df_2nd,df_3rd],axis=1)
    all_person_type = df.type.unique()


    # Separated



    for idx in range(16):
        fig,ax = plt.subplots(figsize=(10, 5))
        name = all_person_type[idx]
        pie_chart(all_count,name,ax)
        fig.legend(['1st_person prons','2nd_person prons','3rd_person prons'])


    # Combined


    fig,axes = plt.subplots(4,4, figsize=(18, 10))
    for i,ax in enumerate(axes.flat):
        name = all_person_type[i]
        pie_chart(all_count,name,ax)
    fig.legend(['1st_person prons','2nd_person prons','3rd_person prons'])
    fig.suptitle('Percentage of different pronouns for each personality')
if __name__ == 'main':
    main()
