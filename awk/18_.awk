{D[$3]=$3 in D?D[$3]+$2:$2}END{res=1;for(key in D)res*=D[key]%100;print res}
