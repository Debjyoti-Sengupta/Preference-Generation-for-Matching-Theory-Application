import numpy as np





v1={'pos':(5,2), 'avg_vel': 7, 'deadline':5, 'data': 200, 'pow_rating':18, 'ohm':0.2,'c':2, 'f':20}
v2={'pos':(7,3), 'avg_vel': 4, 'deadline':10, 'data': 270, 'pow_rating':25, 'ohm':0.2, 'c':3, 'f':18}
v3={'pos':(2,1), 'avg_vel': 2, 'deadline':7, 'data': 300, 'pow_rating':30, 'ohm':0.1, 'c':3, 'f':18}
v4={'pos':(2,5), 'avg_vel': 8, 'deadline':4, 'data': 250, 'pow_rating':20, 'ohm':0.4, 'c':4, 'f':25}
v5={'pos':(4,2), 'avg_vel': 10, 'deadline':4, 'data': 400, 'pow_rating':20, 'ohm':0.5, 'c':2, 'f':24}

VU_List={'v1':v1, 'v2': v2, 'v3': v3, 'v4': v4, 'v5': v5}

#VU_List=[v1,v2,v3,v4,v5]

R=50; xrsu=10; yrsu=10;

def T_Soj(veh):
    root=np.sqrt(R*R-(yrsu-veh['pos'][1])*(yrsu-veh['pos'][1]))
    pi_i=root+(xrsu-veh['pos'][0])
    Tsoj=pi_i/veh['avg_vel']
    return Tsoj

for i in VU_List.keys():
    tsoj= T_Soj(VU_List[i])
    VU_List[i]['t_soj']= tsoj



def Time_Limit(veh):
    time_limit= min(veh['deadline'], veh['t_soj'])
    return time_limit


rsucomm_bitrate={'v1':100, 'v2':70, 'v3':150, 'v4':200, 'v5':250}

m1={'ohm': 0.1, 'c': 2, 'f': 20, 'pow_rating':18}
m2={'ohm': 0.2, 'c': 2, 'f': 18, 'pow_rating':25}
m3={'ohm': 0.1, 'c': 4, 'f': 25, 'pow_rating':40}
m4={'ohm': 0.2, 'c': 3, 'f': 20, 'pow_rating':15}
m5={'ohm': 0.3, 'c': 4, 'f': 24, 'pow_rating':10}

VM_List={'m1':m1, 'm2':m2, 'm3':m3, 'm4':m4, 'm5':m5}

#VM_List=[m1,m2,m3,m4,m5]

Pv={}
Pm={}


count=0

for k in VU_List.keys():
    P={}
    for l in VM_List.keys():
        latency= 2*(VU_List[k]['data']/rsucomm_bitrate[k]) + (VM_List[l]['ohm']*VU_List[k]['data'])/(VM_List[l]['c']*VM_List[l]['f'])
        if latency<= Time_Limit(VU_List[k]):
            P[l]=latency
    Pv[k]=[i for i,v in sorted(P.items(), key=lambda item: item[1])]

for l in VM_List.keys():
    P={}
    for k in VU_List.keys():
        priority= 1/(len(Pv[k])) + (VU_List[k]['t_soj']/VU_List[k]['deadline'])
        P[k]=priority
    Pm[l]=[i for i,v in sorted(P.items(), key=lambda item: item[1], reverse=True)]

print(f'Preference List of  Vehicles:\n {Pv}')
print(f'Preference List of VMs:\n {Pm}' )

def partition(v, m):
    alpha= 1/(1+(VU_List[v]['pow_rating']/VM_List[m]['pow_rating']))
    d_local= round(alpha*VU_List[v]['data'])
    loc_latency= (VU_List[v]['ohm']*d_local)/(VU_List[v]['c']*VU_List[v]['f'])
    if loc_latency> Time_Limit(VU_List[v]):
        alpha=0
    return (alpha, 1-alpha)

