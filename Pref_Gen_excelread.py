#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
Vdeets=pd.read_excel('/Users/dsry8/Documents/PhD Docs/Research/PerCom/Input.xlsx', sheet_name='Vehicles')
display(Vdeets)

Mdeets=pd.read_excel('/Users/dsry8/Documents/PhD Docs/Research/PerCom/Input.xlsx', sheet_name='VMs')
display(Mdeets)


def T_Soj(veh):
    root=np.sqrt(Mdeets.loc[0]['R']*Mdeets.loc[0]['R']-(Mdeets.loc[0]['yrsu']-Vdeets.loc[veh]['x'])*(Mdeets.loc[0]['yrsu']-Vdeets.loc[veh]['y']))
    pi_i=root+(Mdeets.loc[0]['xrsu']-Vdeets.loc[veh]['x'])
    Tsoj=pi_i/Vdeets.loc[veh]['avg_vel']
    return Tsoj

tsoj_list=[]

for i in range(len(Vdeets.index)):
    tsoj= T_Soj(i)
    tsoj_list.append(tsoj)

Vdeets['t_soj']= tsoj_list



def Time_Limit(veh):
    time_limit= min(Vdeets.loc[veh]['deadline'], Vdeets.loc[veh]['t_soj'])
    return time_limit


Pv={}
Pm={}


for k in range(len(Vdeets.index)):
    P={}
    for l in range(len(Mdeets.index)):
        latency= 2*(Vdeets.loc[k]['data']/Vdeets.loc[k]['rsucomm_bitrate']) + (Mdeets.loc[l]['ohm']*Vdeets.loc[k]['data'])/(Mdeets.loc[l]['c']*Mdeets.loc[l]['f'])
        if latency<= Time_Limit(k):
            P[str(l)]=latency
    Pv[str(k)]=[i for i,v in sorted(P.items(), key=lambda item: item[1])]

for l in range(len(Mdeets.index)):
    P={}
    for k in range(len(Vdeets.index)):
        try:
            priority= 1/(len(Pv[str(k)])) + (Vdeets.loc[k]['t_soj']/Vdeets.loc[k]['deadline'])
            P[str(k)]=priority
        except ZeroDivisionError:
            pass
    Pm[str(l)]=[i for i,v in sorted(P.items(), key=lambda item: item[1], reverse=True)]


print(f'Preference List of  Vehicles:\n {Pv}')
print(f'Preference List of VMs:\n {Pm}' )

def partition(v, m):
    alpha= 1/(1+(Vdeets.loc[v]['pow_rating']/Mdeets.loc[m]['pow_rating']))
    d_local= round(alpha*Vdeets.loc[v]['data'])
    loc_latency= (Vdeets.loc[v]['ohm']*d_local)/(Vdeets.loc[v]['c']*VDeets.loc[v]['f'])
    if loc_latency> Time_Limit(v):
        alpha=0
    return (alpha, 1-alpha)

