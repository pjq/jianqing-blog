---
title: "How to check the RSA p,q,N,phi_N,e,d"
date: 2024-11-29
author: pengjianqing
categories: ['Cryptography', 'Tech']
tags: ['Cryptography', 'Integer Factorization', 'RSA']
---

As we know the RSA certificates

- we will choose two primes p,q

- N=p*q

- phi_N = (p-1)*(q-1)

- Then choose e, e.g. 65537

- Then calculate the d, e*d % phi_N = 1

- Then we have the public key (e, N), private key (d, N)

Now we got the certificates from let's encrypt, so how can be get those values

- cert1.pem

- chain1.pem

- fullchain1.pem

- privkey1.pem

Here is one Python script that print all those details.

```
`from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def load_certificate(file_path):
    with open(file_path, 'rb') as f:
        cert_data = f.read()
    return x509.load_pem_x509_certificate(cert_data, default_backend())

def load_private_key(file_path):
    with open(file_path, 'rb') as f:
        key_data = f.read()
    return serialization.load_pem_private_key(key_data, password=None, backend=default_backend())

def display_certificate_details(cert):
    print("Issuer:", cert.issuer)
    print("Subject:", cert.subject)
    print("Serial Number:", cert.serial_number)
    print("Not Before:", cert.not_valid_before)
    print("Not After:", cert.not_valid_after)
    print("Public Key:", cert.public_key())

def display_private_key_details(key):
    print("Private Key Type:", type(key))
    print("Private Key:", key)

# Load and display details for each file
cert1 = load_certificate('cert1.pem')
chain1 = load_certificate('chain1.pem')
fullchain1 = load_certificate('fullchain1.pem')
privkey1 = load_private_key('privkey1.pem')

print("Certificate 1 Details:")
display_certificate_details(cert1)

print("\nChain 1 Details:")
display_certificate_details(chain1)

print("\nFull Chain 1 Details:")
display_certificate_details(fullchain1)

print("\nPrivate Key 1 Details:")
display_private_key_details(privkey1)

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def load_private_key(file_path):
    with open(file_path, 'rb') as f:
        key_data = f.read()
    return serialization.load_pem_private_key(key_data, password=None, backend=default_backend())

def display_rsa_parameters(key):
    if key.private_numbers():
        private_numbers = key.private_numbers()
        public_numbers = private_numbers.public_numbers

        p = private_numbers.p
        q = private_numbers.q
        d = private_numbers.d
        e = public_numbers.e
        N = public_numbers.n
        phi_N = (p - 1) * (q - 1)

        print("p:", p)
        print("q:", q)
        print("e:", e)
        print("d:", d)
        print("N:", N)
        print("phi_N:", phi_N)
    else:
        print("The key is not an RSA private key.")

# Load the private key
privkey1 = load_private_key('privkey1.pem')

# Display RSA parameters
display_rsa_parameters(privkey1)`
```

And here is the output

```
`Certificate 1 Details:
Issuer: 
Subject: 
Serial Number: 399357001611271868934008942535231577601291
/Users/i329817/SAPDevelop/workspace/SECulum-Crypto-Examples/Other/CA.py:19: CryptographyDeprecationWarning: Properties that return a naïve datetime object have been deprecated. Please switch to not_valid_before_utc.
  print("Not Before:", cert.not_valid_before)
Not Before: 2024-03-11 03:37:02
/Users/i329817/SAPDevelop/workspace/SECulum-Crypto-Examples/Other/CA.py:20: CryptographyDeprecationWarning: Properties that return a naïve datetime object have been deprecated. Please switch to not_valid_after_utc.
  print("Not After:", cert.not_valid_after)
Not After: 2024-06-09 03:37:01
Public Key: 

Chain 1 Details:
Issuer: 
Subject: 
Serial Number: 192961496339968674994309121183282847578
Not Before: 2020-09-04 00:00:00
Not After: 2025-09-15 16:00:00
Public Key: 

Full Chain 1 Details:
Issuer: 
Subject: 
Serial Number: 399357001611271868934008942535231577601291
Not Before: 2024-03-11 03:37:02
Not After: 2024-06-09 03:37:01
Public Key: 

Private Key 1 Details:
Private Key Type: 
Private Key: 
p: 132069789892654411168004522386293936563648260984708049888769058861400033840104922637240827355145535778467721990046061228393420363010924409941513508800258809981119101399937003195217979917259199066675447728576676098948661691324234988484581514373041670098119069924124636404134462689209640493314790132976282083611
q: 137105056982080406391028823084893501194543535606308088202698272087931645688882684542797221955650442538986772234601648478841035329665841202081550877179575957078786677686845060335508172755008305533505548942627696405948787947081088462002379085459968945063951380151782547161878405562777603813013479678683689059989
e: 65537
d: 756214848412734766389636904239299485009061447036919688389891952047609574545734290864923373793452280368637781527992131423339716753716888185459331923714856645280928404198259347205993579213846803666627529909232828722879650374490951581311985882248017934718743944682742282487622451272419143686155769738092352440521581984122740725976684511860250924537999931049740452351974285438729683375867711220177807812280621918795246117514339543091408571088210170010573980132856774272424920513332731618240977627013497573799860486533079269798618961305686700083116612832032852006212842303481886949894366447734991011109426370041918678153
N: 18107436068843769961592120494384716970785115109411255249546345948609495318598388096607410722799226196024630722689083053376476074858729887106484558379430237472333286381418093839181293825698895861125235085005989001100242472266354948404984880805585806133599679175254980258454991811852588023295429551087087505259481055918651153874312403039948814343657680828818579172724766105080872512340183146177770234401565111928007670988819164086328954605138596051183819569014922240750776080760982732900349444868680946505230852975887754348080529969823222341004758720100799077687160346328480228883962117022614977552611965834106892740279
phi_N: 18107436068843769961592120494384716970785115109411255249546345948609495318598388096607410722799226196024630722689083053376476074858729887106484558379430237472333286381418093839181293825698895861125235085005989001100242472266354948404984880805585806133599679175254980258454991811852588023295429551087087505259211881071776419056753369694477626905899489032227563034633298774131540832811195538997732185090769133610553176764171454379094498912461830439160755183035087473690870301674200669369623292196413441905049856304683381843183080331417898890517798120267788462525089896252573045317949248770627733246283696022446921596680`
```

I wonder if one day I will be able to see the N here being factored into p*q by a quantum computer. If it can be factored, then phi_N can be obtained, and the private key (d, N) can be derived through 65537*d % phi_N = 1. Then the RSA certificate would be doomed.