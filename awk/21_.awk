function h2d(h,d,c,i,r){for(i=1;i<=length(h);i++){c=substr(h,i,1);r=r*d+index("0123456789abcdef",c)-1}return r}function htd(h){return h2d(h,16)}{p=$0;c=0;c2=0;if(substr(p,1,4)!="5555")next;i=4+8+1;ship=htd(substr(p,5,i-5));i+=2;o=htd(substr(p,5,i-5));i+=2;if(i!=16+1)next;C=htd(substr(p,5,i-5));m=substr(p,i);if(length(m)!=192/4)next;dcd="";for(j=1;j<=length(m);j+=2){char=htd(substr(m,j,2));c2+=char;dcd=dcd sprintf("%c",char)}if(C%256!=c2%256)next;B[o]=dcd}END{for(o in B)res=res B[o];print "res/",res}
