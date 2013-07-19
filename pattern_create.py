#!/usr/bin/python3
#=============================================#
# Title   : Metasploit pattern_create.py      #
# Author  : Z3r0n3                            #
# Contact : z3r0n3@mail.com                   #
# Info    : This tool generates a metasploit  #
#           pattern                           #
# Usage   : Enter the size of pattern, and it #
#           will generates pattern.txt in the #
#           same path of script               #
#           max size of pattern is 20280      #
#=============================================#



def create(k1, k2, k3, c,i,j,k):
        for a in range(c):
            f.write(k1[i]+k2[j]+k3[k]);
            k+=1;
            if j==25 and k>9:
                i+=1;
                j=0;
                k=0;
            if k>9:
                k=0;
                j+=1;
        return i,j,k;


if __name__=="__main__":
    pSize=int(input("[+] Enter size of pattern (Max 20280): "));
    if pSize in range(1,20281):
            x=pSize;
            i,j,k=0,0,0;
            f=open("pattern.txt", "w");
            cyc=int(x/3);
            cyc2=x%3;
            k1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
            "S","T","U","V","W","X","Y","Z"];

            k2=[];
            for x in k1:
                k2.append(x.lower());

            k3=["0","1","2","3","4","5","6","7","8","9"];
            
            i,j,k=create(k1,k2,k3,cyc,i,j,k);
            if cyc2>1:
                f.write(k1[i]+k2[j]);
            elif cyc2==1:
                f.write(k1[i]);
            f.close();
            print("[+] %d Pattern generated"%(pSize));
    else:
            print("[!] Pattern size should be in range [1..20281]");
    

