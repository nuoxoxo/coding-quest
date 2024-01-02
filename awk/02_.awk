BEGIN{set="12 48 30 95 15 55 97";split(set, a);D[3]=1;D[4]=10;D[5]=100;D[6]=1000}{w=0;for(i=1;i<=NF;i++)for(j in a)if($i==a[j])w++;r+=D[w]}END{print r}
