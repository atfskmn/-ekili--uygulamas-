import random
import time

kullanıcılar = list()

def kullanıcı_ekle(x):
    
    print('-'*30)
    print("kullanıcı ekleme bölümüne hoş geldiniz...")
    ekle = input("lütfen eklemek istediğiniz kişiyi yazınız:")
    kullanıcılar.append(ekle)
    input("devam etmek için enter'a basınız...")
    
def kullanıcı_gör(x):
    say = 1
    print("-"*30)
    for i in x:
        print(str(say)+"-kullanıcı adı:",i)
        say+=1
    print("-"*30)
input("devam etmek için enter'a basınız...")

def seç(x):
    print("-"*30)
    say = 1
    kişi_seç = int(input("kaç kişi seçilsin:"))
    rastgele_seç = random.sample(x,kişi_seç)  
    
    for i in rastgele_seç:
        print(str(say)+"-kullanıcı adı:",i)
        say+=1
        print("diğer kişi sistemden çekiliyor...")
        print("-"*30)
        time.sleep(3)
    input("devam etmek için enter'a basınız...")
 
def salla(x):
    print("-"*30)
    say = 1
    random.shuffle(x)
    for i in x:
        print(str(say)+"-kullanıcı adı:",i)
    say+=1
    print("-"*30)
    input("devam etmek için enter'a basınız...")
                    
while True:
    
    seçim = int(input("1-kullanıcı ekle\n2-kullanıcı gör\n3-kullanıcıları karıştır\n4-rastgele seç\n"))
    
    if seçim ==1:
        kullanıcı_ekle(kullanıcılar)
    elif seçim ==2:
        kullanıcı_gör(kullanıcılar)
    elif seçim==3:
        salla(kullanıcılar)
    elif seçim==4:
        seç(kullanıcılar)
    else:
        print("lütfen uygun bir seçim yapınız...")        
            
    
      
        
    