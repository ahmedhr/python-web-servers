for i in `seq 1 2000`; 
    do 
        sleep 2
        curl --location --request GET 'http://127.0.0.1:8080/arbis' 
    done
